"""Case for conceptual tests.

ConceptCases are designed to be natural language tests that help
students understand high-level understanding. As such, these test cases
focus mainly on unlocking.
"""

from client import exceptions as ex
from client.sources.common import models as common_models
from client.sources.ok_test import models as ok_models
from client.sources.common import core
import textwrap
import logging

log = logging.getLogger(__name__)

class ConceptSuite(ok_models.Suite):
    scored = core.Boolean(default=False)

    def post_instantiation(self):
        for i, case in enumerate(self.cases):
            if not isinstance(case, dict):
                raise ex.SerializeException('Test cases must be dictionaries')
            self.cases[i] = ConceptCase(**case)

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
            assert success, 'Concept case should never fail while grading'
            results['passed'] += 1
        return results

class ConceptCase(common_models.Case):
    question = core.String()
    answer = core.String()
    choices = core.List(type=str, optional=True)

    def post_instantiation(self):
        self.question = textwrap.dedent(self.question).strip()
        self.answer = textwrap.dedent(self.answer).strip()

        if self.choices != core.NoValue:
            for i, choice in enumerate(self.choices):
                self.choices[i] = textwrap.dedent(choice).strip()

    def run(self):
        """Runs the conceptual test case.

        RETURNS:
        bool; True if the test case passes, False otherwise.
        """
        print('Q: ' + self.question)
        print('A: ' + self.answer)
        return True

    def lock(self, hash_fn):
        self.answer = hash_fn(self.answer)
        self.locked = True

    def unlock(self, unique_id_prefix, case_id, interact):
        """Unlocks the conceptual test case."""
        print('Q: ' + self.question)
        answer = interact(unique_id_prefix + '\n' + self.question,
                          case_id, self.question, [self.answer], self.choices)
        assert len(answer) == 1
        answer = answer[0]
        if answer != self.answer:
            # Answer was presumably unlocked
            self.locked = False
            self.answer = answer
