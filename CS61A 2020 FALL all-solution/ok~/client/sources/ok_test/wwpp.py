"""Case for What-would-Python-print tests."""

from client import exceptions as ex
from client.sources.common import core
from client.sources.common import interpreter
from client.sources.common import pyconsole
from client.sources.ok_test import models
import logging

log = logging.getLogger(__name__)

class WwppSuite(models.Suite):
    scored = core.Boolean(default=False)

    console_type = pyconsole.PythonConsole

    def __init__(self, test, verbose, interactive, timeout=None, **fields):
        super().__init__(test, verbose, interactive, timeout, **fields)
        self.console = self.console_type(verbose, interactive, timeout)

    def post_instantiation(self):
        for i, case in enumerate(self.cases):
            if not isinstance(case, dict):
                raise ex.SerializeException('Test cases must be dictionaries')
            self.cases[i] = WwppCase(self.console, **case)

    def run(self, test_name, suite_number, env=None):
        results = {
            'passed': 0,
            'failed': 0,
            'locked': 0,
        }
        for i, case in self.enumerate_cases():
            if case.locked == True or results['locked'] > 0:
                # If a test case is locked, refuse to run any of the subsequent
                # test cases
                log.info('Case {} is locked'.format(i))
                results['locked'] += 1
                continue

            success = self._run_case(test_name, suite_number,
                                     case, i + 1)
            assert success, 'Wwpp case should never fail while grading'
            results['passed'] += 1
        return results

class WwppCase(interpreter.CodeCase):

    def run(self):
        """Runs the What-would-Python-print test case.

        RETURNS:
        bool; True if the test case passes, False otherwise.
        """
        for line in self.lines:
            if isinstance(line, str) and line:
                print(line)
            elif isinstance(line, interpreter.CodeAnswer):
                assert not line.locked, 'WwppCase should be unlocked in run'
                print('\n'.join(line.output))
        return True

    def unlock(self, unique_id_prefix, case_id, interact):
        print('What would Python display? If you get stuck, try it out in the '
              'Python\ninterpreter!')
        super().unlock(unique_id_prefix, case_id, interact)
