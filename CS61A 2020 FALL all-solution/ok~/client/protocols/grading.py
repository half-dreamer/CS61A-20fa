"""Implements the GradingProtocol, which runs all specified tests
associated with an assignment.

The GradedTestCase interface should be implemented by TestCases that
are compatible with the GradingProtocol.
"""

from client.protocols.common import models
from client.utils import format
from client.utils import storage
import logging
import sys

log = logging.getLogger(__name__)

#####################
# Testing Mechanism #
#####################

class GradingProtocol(models.Protocol):
    """A Protocol that runs tests, formats results, and sends results
    to the server.
    """
    def run(self, messages, env=None):
        """Run gradeable tests and print results and return analytics.

        RETURNS:
        dict; a mapping of test name -> JSON-serializable object. It is up to
        each test to determine what kind of data it wants to return as
        significant for analytics. However, all tests must include the number
        passed, the number of locked tests and the number of failed tests.
        """
        if self.args.score or self.args.unlock or self.args.testing:
            return
        tests = self.assignment.specified_tests
        for test in tests:
            if self.args.suite and hasattr(test, 'suites'):
                test.run_only = int(self.args.suite)
                try:
                    suite = test.suites[int(self.args.suite) - 1]
                except IndexError as e:
                    sys.exit(('python3 ok: error: '
                        'Suite number must be valid.({})'.format(len(test.suites))))
                if self.args.case:
                    suite.run_only = [int(c) for c in self.args.case]
        grade(tests, messages, env, verbose=self.args.verbose)


def grade(questions, messages, env=None, verbose=True):
    format.print_line('~')
    print('Running tests')
    print()
    passed = 0
    failed = 0
    locked = 0

    analytics = {}

    # The environment in which to run the tests.
    for test in questions:
        log.info('Running tests for {}'.format(test.name))
        results = test.run(env)

        # if correct once, set persistent flag
        if results['failed'] == 0 and results['locked'] == 0:
            storage.store(test.name, 'correct', True)

        passed += results['passed']
        failed += results['failed']
        locked += results['locked']
        analytics[test.name] = results

        if not verbose and (failed > 0 or locked > 0):
            # Stop at the first failed test
            break

    format.print_progress_bar('Test summary', passed, failed, locked,
                              verbose=verbose)
    print()

    messages['grading'] = analytics

protocol = GradingProtocol
