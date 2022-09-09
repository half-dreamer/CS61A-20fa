"""Implements the HintProtocol, which generates hints for students
that are stuck on a coding question. The protocol uses analytics
to determine whether a hint should be given and then
obtains them from the hint generation server. Free response questions
may be posed before and after hints are provided.
"""
from client.sources.common import core
from client.sources.common import models as sources_models
from client.protocols.common import models as protocol_models
from client.utils import auth
from client.utils import format
from client.utils import prompt

import logging
import random
import requests

from client.utils.printer import print_error

log = logging.getLogger(__name__)

#####################
# Hinting Mechanism #
#####################

class HintingProtocol(protocol_models.Protocol):
    """A protocol that provides rubber duck debugging and hints if applicable.
    """

    HINT_SERVER = "https://hinting.cs61a.org/"
    HINT_ENDPOINT = 'api/hints'
    SMALL_EFFORT = 2
    WAIT_ATTEMPTS = 5
    SUPPORTED_ASSIGNMENTS = ['cal/cs61a/fa17/hw09', 'cal/cs61a/fa17/hw10',
            'cal/cs61a/fa17/lab10']

    def run(self, messages):
        """Determine if a student is elgible to recieve a hint. Based on their
        state, poses reflection questions.

        After more attempts, ask if students would like hints. If so, query
        the server.
        """
        if self.args.local:
            return

        # Only run hinting protocol on supported assignments.
        if self.assignment.endpoint not in self.SUPPORTED_ASSIGNMENTS:
            message = "{0} does not support hinting".format(self.assignment.endpoint)
            log.info(message)
            if self.args.hint:
                print(message)
            return

        if 'analytics' not in messages:
            log.info('Analytics Protocol is required for hint generation')
            return
        if 'file_contents' not in messages:
            log.info('File Contents needed to generate hints')
            return

        if self.args.no_experiments:
            messages['hinting'] = {'disabled': 'user'}
            return

        messages['hinting'] = {}
        history = messages['analytics'].get('history', {})
        questions = history.get('questions', [])
        current_q = history.get('question', {})
        messages['hinting']['flagged'] = self.args.hint

        for question in current_q:
            if question not in questions:
                continue
            stats = questions[question]
            is_solved = stats['solved'] == True
            messages['hinting'][question] = {'prompts': {}, 'reflection': {}}
            hint_info = messages['hinting'][question]

            # Determine a users elgibility for a prompt

            # If the user just solved this question, provide a reflection prompt
            if is_solved:
                hint_info['elgible'] = False
                hint_info['disabled'] = 'solved'
                if self.args.hint:
                    print("This question has already been solved.")
                continue
            elif stats['attempts'] < self.SMALL_EFFORT:
                log.info("Question %s is not elgible: Attempts: %s, Solved: %s",
                         question, stats['attempts'], is_solved)
                hint_info['elgible'] = False
                if self.args.hint:
                    hint_info['disabled'] = 'attempt-count'
                    print("You need to make a few more attempts before the hint system is enabled")
                    continue
            else:
                # Only prompt every WAIT_ATTEMPTS attempts to avoid annoying user
                if stats['attempts'] % self.WAIT_ATTEMPTS != 0:
                    hint_info['disabled'] = 'timer'
                    hint_info['elgible'] = False
                    log.info('Waiting for %d more attempts before prompting',
                             stats['attempts'] % self.WAIT_ATTEMPTS)
                else:
                    hint_info['elgible'] = not is_solved

            if not self.args.hint:
                if hint_info['elgible']:
                    with format.block("-"):
                        print("To get hints, try using python3 ok --hint -q {}".format(question))
                    hint_info['suggested'] = True
                continue

            hint_info['accept'] = True

            with format.block("-"):
                print(("Thinking of a hint for {}".format(question) +
                       "... (This could take up to 30 seconds)"))
                pre_hint = random.choice(PRE_HINT_MESSAGES)
                print("In the meantime, consider: \n{}".format(pre_hint))
                hint_info['pre-prompt'] = pre_hint

                log.info('Prompting for hint on %s', question)
                try:
                    response = self.query_server(messages, question)
                except (requests.exceptions.RequestException, requests.exceptions.BaseHTTPError):
                    log.debug("Network error while fetching hint", exc_info=True)
                    hint_info['fetch_error'] = True
                    print_error("\r\nNetwork Error while generating hint. Try again later")
                    response = None
                    continue

                if response:
                    hint_info['response'] = response

                    hint = response.get('message')
                    pre_prompt = response.get('pre-prompt')
                    post_prompt = response.get('post-prompt')
                    system_error = response.get('system-error')
                    log.info("Hint server response: {}".format(response))
                    if not hint:
                        if system_error:
                            print("{}".format(system_error))
                        else:
                            print("Sorry. No hints found for the current code. Try again making after some changes")
                        continue

                    # Provide padding for the the hint
                    print("\n{}".format(hint.rstrip()))

                    if post_prompt:
                        results['prompts'][query] = prompt.explanation_msg(post_prompt)

    def query_server(self, messages, test):
        user = self.assignment.get_identifier()

        data = {
            'assignment': self.assignment.endpoint,
            'test': test,
            'messages': messages,
            'user': user
        }
        address = self.HINT_SERVER + self.HINT_ENDPOINT
        log.info('Sending hint request to %s', address)

        response = requests.post(address, json=data, timeout=35)
        response.raise_for_status()
        return response.json()

SOLVE_SUCCESS_MSG = [
    "If another student had the same error on this question, what advice would you give them?",
    "What did you learn from writing this program about things that you'll continue to do in the future?",
    "What difficulties did you encounter in understanding the problem?",
    "What difficulties did you encounter in designing the program?",
]

ps_strategies_messages = ("Which of the following problem solving strategies will you attempt next?\n"
"- Manually running the code against the test cases\n"
"- Drawing out the environment diagram\n"
"- Try to solve the problem in another programming language and then translating\n"
"- Ensuring that all of the types in the input/output of the function match the specification\n"
"- Solve a few of the test cases manually and then trying to find a pattern\n"
"- Using print statements/inspecting the value of variables to debug")

PRE_HINT_MESSAGES = [
    'Could you describe what the function you are working is supposed to do at a high level?',
    'It would be helpful if you could explain the error to the computer:', # Rubber duck
    'Try to create a hypothesis for how that output was produced. This output is produced because ...',
    'What is the simplest test that exposes this error?',
    ps_strategies_messages,
    'What type of value does the code output (a list, a number etc). ',
    'What type of value (a string, a number etc) does the test indicate is outputted?',
    'Are you convinced that the test case provided is correct?',
    'Describe how exactly the program behaves incorrectly?',
    'In two sentences or less, explain how the error/output is produced by the code in the function', # Rubber Duck
    'Are there lines that you suspect could be causing the program? Why those lines?',
    'Have you tried to use print statements? On what line of the program would a print statement be useful?',
    'Where is the last place you are sure your program was correct? How do you know?',
    'What lines(s) do you think could contain the bug, and why?',
    'What additional information do you need to find the bug? How should you generate this information?',
    "Do you believe that fixing this one test case will result in the program being correct? Why or Why Not?",
    ps_strategies_messages,
]


protocol = HintingProtocol
