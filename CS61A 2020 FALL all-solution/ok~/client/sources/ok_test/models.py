from client import exceptions as ex
from client.sources.common import core
from client.sources.common import models
from client.utils import format
from client.utils import output
from client.utils import storage
import os

##########
# Models #
##########
from client.utils.printer import print_error


class OkTest(models.Test):
    suites = core.List()
    description = core.String(optional=True)

    def __init__(self, file, suite_map, assign_name, assignment, verbose, interactive,
                 timeout=None, **fields):
        super().__init__(**fields)
        self.file = file
        self.suite_map = suite_map

        self.verbose = verbose
        self.interactive = interactive
        self.timeout = timeout
        self.assignment = assignment
        self.assignment_name = assign_name
        self.run_only = None

    def get_short_name(self):
        for name, value in self.assignment.test_map.items():
            if value == self:
                return name

    def post_instantiation(self):
        for i, suite in enumerate(self.suites):
            if not isinstance(suite, dict):
                raise ex.SerializeException('Test cases must be dictionaries')
            elif 'type' not in suite:
                raise ex.SerializeException('Suites must have field "type"')
            elif suite['type'] not in self.suite_map:
                raise ex.SerializeException('Invalid suite type: '
                                            '{}'.format(suite['type']))
            self.suites[i] = self.suite_map[suite['type']](
                    self, self.verbose, self.interactive, self.timeout, **suite)

    def run(self, env):
        """Runs the suites associated with this OK test.

        NOTE: env is intended only for use with the programmatic API to support
        Python OK tests. For that reason, it is only passed to DoctestSuites.

        RETURNS:
        dict; the results for this test, in the form
        {
            'passed': int,
            'failed': int,
            'locked': int,
        }
        """
        passed, failed, locked = 0, 0, 0
        for i, suite in enumerate(self.suites):
            if self.run_only and self.run_only != i + 1:
                continue

            # Env is a hack that allows programmatic API users to plumb a custom
            # environment through to Python tests.
            results = suite.run(self.name, i + 1, env)

            passed += results['passed']
            failed += results['failed']
            locked += results['locked']

            if not self.verbose and (failed > 0 or locked > 0):
                # Stop at the first failed test
                break

        if locked > 0:
            print()
            print('There are still locked tests! '
                  'Use the -u option to unlock them')

        if type(self.description) == str and self.description:
            print()
            print(self.description)
            print()
        return {
            'passed': passed,
            'failed': failed,
            'locked': locked,
        }

    def score(self, env=None):
        """Runs test cases and computes the score for this particular test.

        Scores are determined by aggregating results from suite.run() for each
        suite. A suite is considered passed only if it results in no locked
        nor failed results.

        The points available for this test are distributed evenly across
        scoreable (i.e. unlocked and 'scored' = True) suites.
        """
        passed, total = 0, 0
        for i, suite in enumerate(self.suites):
            if not suite.scored:
                continue
            total += 1

            # Env is for programmatic API users to plumb a custom environment
            results = suite.run(self.name, i + 1, env)

            if results['locked'] == 0 and results['failed'] == 0:
                passed += 1
        if total > 0:
            score = passed * self.points / total
        else:
            score = 0.0

        format.print_progress_bar(self.name, passed, total - passed, 0)
        print()
        return score

    def unlock(self, interact):
        total_cases = len([case for suite in self.suites
                           for case in suite.cases])
        for suite_num, suite in enumerate(self.suites):
            for case_num, case in enumerate(suite.cases):
                case_id = '{} > Suite {} > Case {}'.format(
                            self.name, suite_num + 1, case_num + 1)

                format.print_line('-')
                print(case_id)
                print('(cases remaining: {})'.format(total_cases))
                print()
                total_cases -= 1

                if case.locked is not True:
                    print('-- Already unlocked --')
                    print()
                    continue

                case.unlock(self.unique_id_prefix, case_id, interact)

        assert total_cases == 0, 'Number of cases is incorrect'
        format.print_line('-')
        print('OK! All cases for {} unlocked.'.format(self.name))
        print()

    def lock(self, hash_fn):
        format.print_line('-')
        print(self.name)

        for suite_num, suite in enumerate(list(self.suites)):
            for case_num, case in enumerate(list(suite.cases)):
                message = '* Suite {} > Case {}: '.format(suite_num, case_num)
                if case.hidden:
                    suite.cases.remove(case)
                    print(message + 'removing hidden case')
                elif case.locked == core.NoValue:
                    case.lock(hash_fn)
                    print(message + 'locking')
                elif case.locked is False:
                    print(message + 'leaving unlocked')
                elif case.locked is True:
                    print(message + 'already unlocked')
            if not suite.cases:
                self.suites.remove(suite)
                print('* Suite {}: removing empty suite'.format(suite_num))
        print()

    def dump(self):
        # TODO(albert): add log messages
        # TODO(albert): writing causes an error halfway, the tests
        # directory may be left in a corrupted state.
        # TODO(albert): might need to delete obsolete test files too.
        json = format.prettyjson(self.to_json())
        test_tmp = "{}.tmp".format(self.file)

        with open(test_tmp, 'w', encoding='utf-8') as f:
            f.write('test = {}\n'.format(json))

        try:
            storage.replace_transactional(test_tmp, self.file)
        except (NotImplementedError, OSError):
            # Try to use os.replace, but if on Windows manually remove then rename
            # (ref issue #339)
            if os.name == 'nt':
            # TODO(colin) Add additional error handling in case process gets killed mid remove/rename
                os.remove(self.file)
                os.rename(test_tmp, self.file)
            else:
                # Use an atomic rename operation to prevent test corruption
                os.replace(test_tmp, self.file)

    @property
    def unique_id_prefix(self):
        return self.assignment_name + '\n' + self.name

    def get_code(self):
        extracted_code = {}
        for ind, suite in enumerate(list(self.suites)):
            if suite.type != 'doctest':
                continue
            suite_code = suite.extract_code()
            if suite_code:
                # Store with 1 indexed name
                extracted_code[ind+1] = suite_code
        return extracted_code


class EncryptedOKTest(models.Test):
    name = core.String()
    points = core.Float()
    partner = core.String(optional=True)
    def warn(self, method):
        print_error("Cannot {} {}: test is encrypted".format(method, self.name))
        keys_string = input("Please paste the key to decrypt this test: ")
        keys = keys_string.strip().split()
        if keys:
            raise ex.ForceDecryptionException(keys)

    def run(self, env):
        self.warn('run')
        return {'failed': 1, 'locked': 0, 'passed': 0}

    def score(self):
        self.warn('score')
        return 0

    def unlock(self, interact):
        self.warn('unlock')

    def lock(self, hash_fn):
        self.warn('lock')

    def dump(self):
        self.warn('save the test')


class Suite(core.Serializable):
    type = core.String()
    scored = core.Boolean(default=True)
    cases = core.List()

    def __init__(self, test, verbose, interactive, timeout=None, **fields):
        super().__init__(**fields)
        self.test = test
        self.verbose = verbose
        self.interactive = interactive
        self.timeout = timeout
        self.run_only = []

    def run(self, test_name, suite_number, env=None):
        """Subclasses should override this method to run tests.

        PARAMETERS:
        test_name    -- str; name of the parent test.
        suite_number -- int; suite number, assumed to be 1-indexed.
        env          -- dict; used by programmatic API to provide a
                        custom environment to run tests with.

        RETURNS:
        dict; results of the following form:
        {
            'passed': int,
            'failed': int,
            'locked': int,
        }
        """
        raise NotImplementedError

    def enumerate_cases(self):
        enumerated = enumerate(self.cases)
        if self.run_only:
            return [x for x in enumerated if x[0] + 1 in self.run_only]
        return enumerated

    def extract_code(self):
        """Pull out the code for any doctest cases in the suite.
        """
        data = [{'setup': c.formatted_setup(),
                 'code': c.formatted_code(),
                 'teardown': c.formatted_teardown()} for _, c in self.enumerate_cases()
                                                     if hasattr(c, 'setup')]
        return data

    def _run_case(self, test_name, suite_number, case, case_number):
        """A wrapper for case.run().

        Prints informative output and also captures output of the test case
        and returns it as a log. The output is printed only if the case fails,
        or if self.verbose is True.
        """
        output.off()    # Delay printing until case status is determined.
        log_id = output.new_log()
        format.print_line('-')
        print('{} > Suite {} > Case {}'.format(test_name, suite_number,
                                               case_number))
        print()

        success = case.run()
        if success:
            print('-- OK! --')

        output.on()
        output_log = output.get_log(log_id)
        output.remove_log(log_id)

        if not success or self.verbose:
            print(''.join(output_log))
        if not success:
            short_name = self.test.get_short_name()
            # TODO: Change when in notebook mode
            print('Run only this test case with '
                '"python3 ok -q {} --suite {} --case {}"'.format(
                    short_name, suite_number, case_number))
        return success
