from client.protocols.common import models
from client.exceptions import EarlyExit
from client.utils.storage import contains, get, store
import time
import textwrap

class Hint:
    def __init__(self, text='', cooldown=0):
        self.text = text
        self.cooldown = cooldown

Hint.NONE = Hint()

EXAMPLES = \
"""Try explaining the problem, its domain (inputs), range (outputs),
and behavior in your own words. Come up with a few example inputs
and outputs.
"""

PROCESS = \
"""Try identifying where you are in the problem-solving process

    https://cs61a.org/articles/studying.html#solving-problems
"""

TEST = \
"""Try testing a few of your own examples in the interpreter:

    python3 -i {files}

You can also run the doctests:

    python3 -m doctest {files}
"""

PYTHON_TUTOR = \
"""Try plugging the code along with an example into Python Tutor
to visualize Python's process with

    http://tutor.cs61a.org
"""

DIAGRAM = \
"""Try walking through your approach with a friend and
diagramming your solution. Verify that each step matches with
the implementation by working through smaller examples in the
interpreter or with your friend.
"""

HINTS = (
        Hint.NONE, Hint.NONE, Hint.NONE,
        Hint(EXAMPLES, 30),
        Hint.NONE, Hint.NONE, Hint.NONE,
        Hint(PROCESS, 45),
        Hint.NONE, Hint.NONE, Hint.NONE,
        Hint(TEST, 60),
        Hint.NONE, Hint.NONE, Hint.NONE,
        Hint(PYTHON_TUTOR, 75),
        Hint.NONE, Hint.NONE, Hint.NONE,
        Hint(DIAGRAM, 90),
        )


COOLDOWN_MSG = \
"""Woah, you're working really fast!
Spend a minute or two applying this hint before trying again.

"""

RETRY_MSG = \
"""
If you're convinced you've fixed the problem, spend some time
reflecting on the solution process and how you implemented
any fixes along the way.
"""

RETRY_THRESHOLD = 0.5 # How long into the cooldown until we switch to RETRY_MSG


###########################
# Rate Limiting Mechanism #
###########################

class RateLimitProtocol(models.Protocol):
    """A Protocol that keeps track of rate limiting for specific questions.
    """
    def __init__(self, args, assignment, hints=HINTS):
        self.hints = hints
        super().__init__(args, assignment)

    def run(self, messages):
        if self.args.score or self.args.unlock or self.args.testing:
            return
        analytics = {}
        tests = self.assignment.specified_tests
        for test in tests:
            if get(test.name, 'correct', default=False):
                continue # suppress rate limiting if question is correct
            last_attempt, attempts = self.check_attempt(test)
            analytics[test.name] = {
                'attempts': store(test.name, 'attempts', attempts),
                'last_attempt': store(test.name, 'last_attempt', last_attempt),
                }

        messages['rate_limit'] = analytics

    def check_attempt(self, test):
        now = int(time.time())
        last_attempt = get(test.name, 'last_attempt', now)
        attempts = get(test.name, 'attempts', 0)
        elapsed = now - last_attempt
        hint = self.hints[attempts % len(self.hints)]
        if attempts and hint.cooldown > elapsed:
            files = ' '.join(self.assignment.src)
            if elapsed <= RETRY_THRESHOLD * hint.cooldown:
                raise EarlyExit(COOLDOWN_MSG + hint.text.format(files=files))
            else:
                raise EarlyExit(hint.text.format(files=files) + RETRY_MSG)
        return now, attempts + 1

protocol = RateLimitProtocol
