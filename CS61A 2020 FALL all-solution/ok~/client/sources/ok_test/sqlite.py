"""Console for interpreting sqlite."""

from client import exceptions
from client.sources.common import core, interpreter
from client.sources.ok_test import doctest
from client.utils import format
from client.utils import timer
import importlib
import io
import os
import re
import subprocess
import sys

def get_sqlite_shell():
    sqlite_shell = None
    try: import sqlite_shell
    except ImportError: pass
    return sqlite_shell

class SqliteConsole(interpreter.Console):
    PS1 = 'sqlite> '
    PS2 = '   ...> '

    VERSION = (3, 8, 3)

    ordered = False # will be set by SqliteSuite.__init__

    def load(self, code, setup='', teardown=''):
        """Prepares a set of setup, test, and teardown code to be
        run in the console.
        """
        super().load(code, setup, teardown)

    def interpret(self):
        """Interprets the code in this Console.

        If there is an executable called "sqlite3" (in the current directory is
        okay), pipe the test case into sqlite3. Otherwise, report an error.
        """
        env = dict(os.environ,
                   PATH=os.getcwd() + os.pathsep + os.environ['PATH'])
        if self._has_sqlite_cli(env):
            try:
                test, expected, actual = self._use_sqlite_cli(env)
            except interpreter.ConsoleException:
                return False
            print(format.indent(test, self.PS1))  # TODO: show test with prompt
            print(actual)
            try:
                self._diff_output(expected, actual)
                return True
            except interpreter.ConsoleException:
                return False
        else:
            print('ERROR: could not run sqlite3.')
            print('Tests will not pass, but you can still submit your assignment.')
            print('Please download the newest version of sqlite3 into this folder')
            print('to run tests.')
            return False

    def interact(self):
        """Opens up an interactive session with the current state of
        the console.
        """
        # TODO(albert)

    def _diff_output(self, expected, actual):
        """Raises an interpreter.ConsoleException if expected and actual output
        don't match.

        PARAMETERS:
        expected -- str; may be multiple lines
        actual   -- str; may be multiple lines
        """
        expected = expected.split('\n')
        actual = actual.split('\n')

        if self.ordered:
            correct = expected == actual
        else:
            correct = sorted(expected) == sorted(actual)

        if not correct:
            print()
            error_msg = '# Error: expected'
            if self.ordered:
                error_msg += ' ordered output'
            print(error_msg)
            print('\n'.join('#     {}'.format(line)
                            for line in expected))
            print('# but got')
            print('\n'.join('#     {}'.format(line)
                            for line in actual))
            raise interpreter.ConsoleException

    def _has_sqlite_cli(self, env):
        """Checks if the command "sqlite3" is executable with the given
        shell environment variables.

        PARAMETERS:
        env -- mapping; represents shell environment variables. Primarily, this
               allows modifications to PATH to check the current directory first.

        RETURNS:
        bool; True if "sqlite3" is executable and the version is at least
        self.VERSION; False otherwise.
        """
        args = ['sqlite3', '--version']
        sqlite_shell = get_sqlite_shell()
        if sqlite_shell:
            stdout = io.StringIO()
            sqlite_shell.main(*args, stdin=io.StringIO(), stdout=stdout, stderr=io.StringIO())
            version = stdout.getvalue()
        else:
            # Modify PATH in subprocess to check current directory first for sqlite3
            # executable.
            try:
                version = subprocess.check_output(args,
                                                  env=env).decode()
            except (subprocess.CalledProcessError, FileNotFoundError):
                return False
        version = version.split(' ')[0].split('.')
        version_info = tuple(int(num) for num in version)
        return version_info >= self.VERSION

    def _use_sqlite_cli(self, env):
        """Pipes the test case into the "sqlite3" executable.

        The method _has_sqlite_cli MUST be called before this method is called.

        PARAMETERS:
        env -- mapping; represents shell environment variables. Primarily, this
               allows modifications to PATH to check the current directory first.

        RETURNS:
        (test, expected, result), where
        test     -- str; test input that is piped into sqlite3
        expected -- str; the expected output, for display purposes
        result   -- str; the actual output from piping input into sqlite3
        """
        test = []
        expected = []
        for line in self._setup + self._code + self._teardown:
            if isinstance(line, interpreter.CodeAnswer):
                expected.extend(line.output)
            elif line.startswith(self.PS1):
                test.append(line[len(self.PS1):])
            elif line.startswith(self.PS2):
                test.append(line[len(self.PS2):])
        test = '\n'.join(test)
        result, error = (None, None)
        process = None
        args = ['sqlite3']
        sqlite_shell = get_sqlite_shell()
        if sqlite_shell:
            if self.timeout is None:
                (stdin, stdout, stderr) = (io.StringIO(test), io.StringIO(), io.StringIO())
                sqlite_shell.main(*args, stdin=stdin, stdout=stdout, stderr=stderr)
                result, error = (stdout.getvalue(), stderr.getvalue())
            else:
                args[:] = [sys.executable] + subprocess._args_from_interpreter_flags() + ["--", sqlite_shell.__file__] + args[1:]
        if result is None:
            process = subprocess.Popen(args,
                                        universal_newlines=True,
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        env=env)
        if process:
            try:
                result, error = process.communicate(test, timeout=self.timeout)
            except subprocess.TimeoutExpired as e:
                process.kill()
                print('# Error: evaluation exceeded {} seconds.'.format(self.timeout))
                raise interpreter.ConsoleException(exceptions.Timeout(self.timeout))
        return test, '\n'.join(expected), (error + '\n' + result).strip()

    @staticmethod
    def normalize(response):
        # no normalization for sql
        return response

class SqliteSuite(doctest.DoctestSuite):
    console_type = SqliteConsole
    # TODO: Ordered should be a property of cases, not entire suites.
    ordered = core.Boolean(default=False)

    def __init__(self, test, verbose, interactive, timeout=None, **fields):
        super().__init__(test, verbose, interactive, timeout, **fields)
        self.console.ordered = fields.get('ordered', False)
