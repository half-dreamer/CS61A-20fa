"""Implements the AnalyticsProtocol, which keeps track of configuration
for the ok grading session.
"""
import logging
import os
import pickle
import re

from client.protocols.common import models
from datetime import datetime

# TODO(albert): rename this InformationProtocol
# Add all command line arguments here

log = logging.getLogger(__name__)


class AnalyticsProtocol(models.Protocol):
    """A Protocol that analyzes how much students are using the autograder."""

    ANALYTICS_FILE = ".ok_history"

    RE_DEFAULT_CODE = re.compile(r"""
    ^\"\*\*\*\sREPLACE\sTHIS\sLINE\s\*\*\*\"$
    """, re.X | re.I)

    RE_SCHEME_DEFAULT_CODE = re.compile(r"""
    ^\'REPLACE-THIS-LINE$
    """, re.X | re.I)

    RE_REPLACE_MARK = re.compile(r"""
            [\#\;][ ]Replace[ ]
            """, re.X | re.I | re.M)

    def run(self, messages):
        """Returns some analytics about this autograder run."""
        statistics = {}
        statistics['time'] = str(datetime.now())
        statistics['time-utc'] = str(datetime.utcnow())
        statistics['unlock'] = self.args.unlock

        if self.args.question:
            statistics['question'] = [t.name for t in self.assignment.specified_tests]
            statistics['requested-questions'] = self.args.question

            if self.args.suite:
                statistics['requested-suite'] = self.args.suite
            if self.args.case:
                statistics['requested-case'] = self.args.case

        messages['analytics'] = statistics
        self.log_run(messages)

    def replaced(self, contents):
        """For a question snippet containing some default code, return True if the
        default code is replaced. Default code in a snippet should have
        '\# Replace with your solution' at the end of each line.
        """
        line_num = len(contents.strip(' ').splitlines())
        replace_marks = self.RE_REPLACE_MARK.findall(contents.strip())
        if len(replace_marks) == line_num:
            return False
        return True

    @classmethod
    def read_history(cls):
        history = {'questions': {}, 'all_attempts': 0}
        try:
            with open(cls.ANALYTICS_FILE, 'rb') as fp:
                history = pickle.load(fp)
            log.info('Loaded %d history from %s',
                     len(history), cls.ANALYTICS_FILE)
        except (IOError, EOFError) as e:
            log.info('Error reading from ' + cls.ANALYTICS_FILE + \
                     ', assume no history')
        return history

    def log_run(self, messages):
        """Record this run of the autograder to a local file.

        If the student does not specify what question(s) the student is
        running ok against, assume that the student is aiming to work on
        the question with the first failed test. If a student finishes
        questions 1 - N-1, the first test to fail will be N.
        """
        # Load the contents of the local analytics file
        history = self.read_history()
        history['all_attempts'] += 1

        # List of question names that the student asked to have graded
        questions = messages['analytics'].get('question', [])
        # The output of the grading protocol
        grading = messages.get('grading')

        # Attempt to figure out what the student is currently implementing
        if not questions and grading:
            # If questions are unspecified by the user, use the first failed test
            failed = first_failed_test(self.assignment.specified_tests, grading)
            logging.info('First failed test: {}'.format(failed))
            if failed:
                questions = [failed]

            # Update question correctness status from previous attempts
            for saved_q, details in history['questions'].items():
                finished = details['solved']
                if not finished and saved_q in grading:
                    scoring = grading[saved_q]
                    details['solved'] = is_correct(scoring)

        # The question(s) that the student is testing right now.
        history['question'] = questions

        # Update attempt and correctness counts for the graded questions
        for question in questions:
            detail = history['questions']
            if grading and question in grading:
                scoring = is_correct(grading[question])
            else:
                scoring = False

            # Update attempt counts or initialize counts
            if question in history['questions']:
                q_info = detail[question]
                if grading and question in grading:
                    if q_info['solved'] != True:
                        q_info['solved'] = scoring
                    else:
                        continue  # Already solved. Do not change total
                q_info['attempts'] += 1
            else:
                detail[question] = {
                    'attempts': 1,
                    'solved': scoring
                }
            logging.info('Attempt %d for Question %s : %r',
                         history['questions'], question, scoring)

        with open(self.ANALYTICS_FILE, 'wb') as f:
            log.info('Saving history to %s', self.ANALYTICS_FILE)
            pickle.dump(history, f)
            os.fsync(f)

        messages['analytics']['history'] = history

def is_correct(grading_results):
    """The grading protocol provides grading_results, a dictionary which
    provides the count of tests passed, failed or locked for a single
    question. Return True if all tests have passed.
    """
    if grading_results['locked'] > 0:
        return False
    return sum(grading_results.values()) == grading_results['passed']

def first_failed_test(tests, scores):
    test_names = [t.name for t in tests]
    for test_name in test_names:
        scoring = scores.get(test_name, {})
        if test_name in scores and scoring.get('failed'):
            return test_name
    return None

protocol = AnalyticsProtocol
