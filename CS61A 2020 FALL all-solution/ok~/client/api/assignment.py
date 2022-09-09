import uuid

from datetime import timedelta

import requests

from client import exceptions as ex
from client.sources.common import core
from client.utils import auth, format, encryption
from client.protocols.grading import grade
from client.cli.common import messages
import client
import collections
import glob
import importlib
import json
import logging
import os
import textwrap

from client.utils.printer import print_success, print_error, print_warning

log = logging.getLogger(__name__)

CONFIG_EXTENSION = '*.ok'

def load_assignment(filepath=None, cmd_args=None):
    config = _get_config(filepath)
    if not isinstance(config, dict):
        raise ex.LoadingException('Config should be a dictionary')
    if cmd_args is None:
        cmd_args = Settings()
    return Assignment(cmd_args, **config)

def _get_config(config):
    if config is None:
        configs = glob.glob(CONFIG_EXTENSION)
        if len(configs) > 1:
            raise ex.LoadingException('\n'.join([
                'Multiple .ok files found:',
                '    ' + ' '.join(configs),
                "Please specify a particular assignment's config file with",
                '    python3 ok --config <config file>'
            ]))
        elif not configs:
            raise ex.LoadingException('No .ok configuration file found')
        config = configs[0]
    elif not os.path.isfile(config):
        raise ex.LoadingException(
                'Could not find config file: {}'.format(config))

    try:
        with open(config, 'r') as f:
            result = json.load(f, object_pairs_hook=collections.OrderedDict)
    except IOError:
        raise ex.LoadingException('Error loading config: {}'.format(config))
    except ValueError:
        raise ex.LoadingException(
            '{0} is a malformed .ok configuration file. '
            'Please re-download {0}.'.format(config))
    else:
        log.info('Loaded config from {}'.format(config))
        return result


class Assignment(core.Serializable):
    name = core.String()
    endpoint = core.String(optional=True, default='')
    decryption_keypage = core.String(optional=True, default='')
    src = core.List(type=str, optional=True)
    tests = core.Dict(keys=str, values=str, ordered=True)
    default_tests = core.List(type=str, optional=True)
    # ignored, for backwards-compatibility only
    protocols = core.List(type=str, optional=True)

    ####################
    # Programmatic API #
    ####################

    def grade(self, question, env=None, skip_locked_cases=False):
        """Runs tests for a particular question. The setup and teardown will
        always be executed.

        question -- str; a question name (as would be entered at the command
                    line
        env      -- dict; an environment in which to execute the tests. If
                    None, uses the environment of __main__. The original
                    dictionary is never modified; each test is given a
                    duplicate of env.
        skip_locked_cases -- bool; if False, locked cases will be tested

        Returns: dict; maps question names (str) -> results (dict). The
        results dictionary contains the following fields:
        - "passed": int (number of test cases passed)
        - "failed": int (number of test cases failed)
        - "locked": int (number of test cases locked)
        """
        if env is None:
            import __main__
            env = __main__.__dict__
        messages = {}
        tests = self._resolve_specified_tests([question], all_tests=False)
        for test in tests:
            try:
                for suite in test.suites:
                    suite.skip_locked_cases = skip_locked_cases
                    suite.console.skip_locked_cases = skip_locked_cases
                    suite.console.hash_key = self.name
            except AttributeError:
                pass
        test_name = tests[0].name
        grade(tests, messages, env)
        return messages['grading'][test_name]

    ##############
    # Encryption #
    ##############

    def generate_encryption_key(self, keys_file):
        data = [(filename, encryption.generate_key()) for filename in self._get_files()]
        with open(keys_file, "w") as f:
            json.dump(data, f)

    def encrypt(self, keys_file, padding):
        """
        Encrypt each question and test, with the given keys file, which contains (file, key) pairs
        """
        with open(keys_file) as f:
            keys = dict(json.load(f))
        for file in self._get_files():
            if file in keys:
                self._encrypt_file(file, keys[file], padding)

    def decrypt(self, keys):
        decrypted_files, undecrypted_files = self.attempt_decryption(keys)
        if not undecrypted_files + decrypted_files:
            print_success("All files are decrypted")
        elif undecrypted_files:
            if keys:
                print_error("Unable to decrypt some files with the keys", ", ".join(keys))
            else:
                print_error("No keys found, could not decrypt any files")
            print_error("    Non-decrypted files:", *undecrypted_files)

    def attempt_decryption(self, keys):
        if self.decryption_keypage:
            try:
                response = requests.get(self.decryption_keypage)
                response.raise_for_status()
                keys_data = response.content.decode('utf-8')
                keys = keys + encryption.get_keys(keys_data)
            except Exception as e:
                print_error(
                    "Could not load decryption page {}: {}.".format(self.decryption_keypage, e))
                print_error("You can pass in a key directly by running python3 ok --decrypt [KEY]")

        decrypted_files = []
        undecrypted_files = []
        for file in self._get_files():
            with open(file) as f:
                if not encryption.is_encrypted(f.read()):
                    continue
            for key in keys:
                success = self._decrypt_file(file, key)
                if success:
                    decrypted_files.append(file)
                    break
            else:
                undecrypted_files.append(file)
        return decrypted_files, undecrypted_files

    def _decrypt_file(self, path, key):
        """
        Decrypt the given file in place with the given key.
        If the key does not match, do not change the file contents
        """
        success = False

        def decrypt(ciphertext):
            if not encryption.is_encrypted(ciphertext):
                return ciphertext
            try:
                plaintext = encryption.decrypt(ciphertext, key)
                nonlocal success
                success = True
                print_success("decrypted", path, "with", key)
                return plaintext
            except encryption.InvalidKeyException:
                return ciphertext

        self._in_place_edit(path, decrypt)
        return success

    def _encrypt_file(self, path, key, padding):
        """
        Encrypt the given file in place with the given key.
        This is idempotent but if you try to encrypt the same file with multiple keys it errors.
        """
        def encrypt(data):
            if encryption.is_encrypted(data):
                try:
                    data = encryption.decrypt(data, key)
                except encryption.InvalidKeyException:
                    raise ValueError("Attempt to re-encrypt file with an invalid key")
            return encryption.encrypt(data, key, padding)

        self._in_place_edit(path, encrypt)

    @staticmethod
    def _in_place_edit(path, func):
        """
        Edit the given file in place, atomically. `func` is a function that modifies the data in the file.
        """
        with open(path) as f:
            data = f.read()
        ciphertext = func(data)
        temporary_file = "." + uuid.uuid4().hex
        with open(temporary_file, "w") as f:
            f.write(ciphertext)
        # atomic rename
        os.replace(temporary_file, path)

    def _get_files(self):
        """
        Get all the test and submission source files associated with this assignment, deduplicated
        """
        tests = [file for k, v in self.tests.items() for file in glob.glob(k) if v == 'ok_test' or v == 'scheme_test']
        src = list(self.src)
        return sorted(set(tests + src))

    @property
    def server_url(self):
        scheme = 'http' if self.cmd_args.insecure else 'https'
        return '{}://{}'.format(scheme, self.cmd_args.server)

    ############
    # Internal #
    ############

    _TESTS_PACKAGE = 'client.sources'
    _PROTOCOL_PACKAGE = 'client.protocols'

    # A list of all protocols that should be loaded. Order is important.
    # Dependencies:
    # analytics     -> grading
    # autostyle     -> analytics, grading
    # backup        -> all other protocols
    # collaborate   -> file_contents, analytics
    # file_contents -> none
    # grading       -> rate_limit
    # hinting       -> file_contents, analytics
    # lock          -> none
    # rate_limit    -> none
    # scoring       -> none
    # trace         -> file_contents
    # unlock        -> none
    # testing       -> none
    _PROTOCOLS = [
        "testing",
        # "rate_limit", uncomment to turn rate limiting back on!
        "file_contents",
        "grading",
        "analytics",
        "autostyle",
        "collaborate",
        "hinting",
        "lock",
        "scoring",
        "unlock",
        "trace",
        "backup",
    ]

    def __init__(self, args, **fields):
        self.cmd_args = args
        self.test_map = collections.OrderedDict()
        self.protocol_map = collections.OrderedDict()

    def post_instantiation(self):
        self._print_header()
        self._load_tests()
        self._load_protocols()
        self.specified_tests = self._resolve_specified_tests(
            self.cmd_args.question, self.cmd_args.all)

    def set_args(self, **kwargs):
        """Set command-line arguments programmatically. For example:

            assignment.set_args(
                server='http://localhost:5000',
                no_browser=True,
                backup=True,
                timeout=60,
            )
        """
        self.cmd_args.update(**kwargs)

    def authenticate(self, force=False, inline=False, nointeract=False):
        nointeract = nointeract or self.cmd_args.nointeract
        if not inline:
            return auth.authenticate(self.cmd_args, endpoint=self.endpoint, force=force, nointeract=nointeract)
        else:
            return auth.notebook_authenticate(self.cmd_args, force=force, nointeract=nointeract)

    def get_student_email(self):
        return auth.get_student_email(self.cmd_args, endpoint=self.endpoint)

    def get_identifier(self):
        return auth.get_identifier(self.cmd_args, endpoint=self.endpoint)

    def is_empty_init(self, path):
        if os.path.basename(path) != '__init__.py':
            return False

        with open(path) as f:
            contents = f.read()

        return contents.strip() == ""

    def _load_tests(self):
        """Loads all tests specified by test_map."""
        log.info('Loading tests')
        for file_pattern, sources in self.tests.items():
            for source in sources.split(","):
                # Separate filepath and parameter
                if ':' in file_pattern:
                    file_pattern, parameter = file_pattern.split(':', 1)
                else:
                    parameter = ''

                for file in sorted(glob.glob(file_pattern)):
                    if self.is_empty_init(file):
                        continue
                    try:
                        module = importlib.import_module(self._TESTS_PACKAGE + '.' + source)
                    except ImportError:
                        raise ex.LoadingException('Invalid test source: {}'.format(source))

                    test_name = file
                    if parameter:
                        test_name += ':' + parameter

                    self.test_map.update(module.load(file, parameter, self))

                    log.info('Loaded {}'.format(test_name))

    def dump_tests(self):
        """Dumps all tests, as determined by their .dump() method.

        PARAMETERS:
        tests -- dict; file -> Test. Each Test object has a .dump method
                 that takes a filename and serializes the test object.
        """
        log.info('Dumping tests')
        for test in self.test_map.values():
            try:
                test.dump()
            except ex.SerializeException as e:
                log.warning('Unable to dump {}: {}'.format(test.name, str(e)))
            else:
                log.info('Dumped {}'.format(test.name))

    def autobackup(self, run_sync):
        backup = self._get_protocol("BackupProtocol")
        get_contents = self._get_protocol("FileContentsProtocol")
        if backup is None:
            print_error("Error: autobackup specified by backup protocol not found")
            return
        def messages_fn():
            msgs = messages.Messages()
            get_contents.run(msgs)
            return msgs
        backup.run_in_loop(messages_fn, timedelta(minutes=1), synchronous=run_sync)

    def _get_protocol(self, type_name):
        for protocol in self.protocol_map.values():
            if type(protocol).__name__ == type_name:
                return protocol
        return None

    def _resolve_specified_tests(self, questions, all_tests=False):
        """For each of the questions specified on the command line,
        find the test corresponding that question.

        Questions are preserved in the order that they are specified on the
        command line. If no questions are specified, use the entire set of
        tests.
        """
        if not questions and not all_tests \
                and self.default_tests != core.NoValue \
                and len(self.default_tests) > 0:
            log.info('Using default tests (no questions specified): '
                     '{}'.format(self.default_tests))
            bad_tests = sorted(test for test in self.default_tests if test not in self.test_map)
            if bad_tests:
                error_message = ("Required question(s) missing: {}. "
                    "This often is the result of accidentally deleting the question's doctests or the entire function.")
                raise ex.LoadingException(error_message.format(", ".join(bad_tests)))
            return [self.test_map[test] for test in self.default_tests]
        elif not questions:
            log.info('Using all tests (no questions specified and no default tests)')
            return list(self.test_map.values())
        elif not self.test_map:
            log.info('No tests loaded')
            return []

        specified_tests = []
        for question in questions:
            if question not in self.test_map:
                raise ex.InvalidTestInQuestionListException(list(self.test_map), question)

            log.info('Adding {} to specified tests'.format(question))
            if question not in specified_tests:
                specified_tests.append(self.test_map[question])
        return specified_tests

    def _load_protocols(self):
        log.info('Loading protocols')
        for proto in self._PROTOCOLS:
            module = importlib.import_module(self._PROTOCOL_PACKAGE + '.' + proto)
            self.protocol_map[proto] = module.protocol(self.cmd_args, self)
            log.info('Loaded protocol "{}"'.format(proto))

    def _print_header(self):
        if getattr(self.cmd_args, 'autobackup_actual_run_sync', False):
            return
        format.print_line('=')
        print('Assignment: {}'.format(self.name))
        print('OK, version {}'.format(client.__version__))
        format.print_line('=')
        print()

class Settings:
    """Command-line arguments that are set programmatically instead of by
    parsing the command line. For example:

        args = Settings(
            server='http://localhost:5000',
            no_browser=True,
            backup=True,
            timeout=60,
        )
        assignment = Assignment(args)
    """
    def __init__(self, **kwargs):
        from client.cli.ok import parse_input
        self.args = parse_input([])
        self.update(**kwargs)

    def __getattr__(self, attr):
        return getattr(self.args, attr)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self.args, k, v)

    def __repr__(self):
        cls = type(self).__name__
        return "{0}({1})".format(cls, vars(self.args))
