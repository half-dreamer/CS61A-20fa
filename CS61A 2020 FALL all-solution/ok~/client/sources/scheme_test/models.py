"""Interprets Scheme test files and compares each line of printed output from
the read-eval-print loop and from any output functions to an expected output
described in a comment.  For example,

(display (+ 2 3))
; expect 5

Differences between printed and expected outputs are printed with line numbers.

Requires the following attributes from an importable scheme module:

    scheme.create_global_frame
    scheme.Buffer
    scheme.read_eval_print_loop
    scheme.tokenize_lines
"""

from client.sources.common import models
from client.utils import format
from client.utils import output
from client.utils import timer
import importlib
import re
import sys


##########
# Models #
##########

class SchemeTest(models.Test):

    def __init__(self, file, file_contents, timeout=None, **fields):
        super().__init__(**fields)
        self.file = file
        self.file_contents = file_contents
        self.timeout = timeout

    def run(self, env):
        """Runs the suites associated with this doctest.

        NOTE: env is intended only for use with the programmatic API to support
        Python OK tests. It is not used here.

        RETURNS:
        bool; True if the doctest completely passes, False otherwise.
        """
        format.print_line('-')
        print('Scheme tests in {}'.format(self.file))
        print()

        passed, failed = self._run_tests()

        print('{} passed; {} failed'.format(passed, failed))
        if failed == 0 and passed > 0:
            print('-- OK! --')
            print()

        return {'passed': passed, 'failed': failed, 'locked': 0}

    def score(self):
        format.print_line('-')
        print('Scheme tests in {}'.format(self.file))
        print()
        _, failed = self._run_tests()
        score = 1.0 if failed == 0 else 0.0

        print('Score: {}/1'.format(score))
        print()
        return score

    def unlock(self, interact):
        """Scheme tests cannot be unlocked."""

    def lock(self, hash_fn):
        """Scheme tests cannot be locked."""

    def dump(self):
        """Scheme tests do not need to be dumped, since no state changes."""

    ###############
    # Test runner #
    ###############

    def _run_tests(self):
        """Run a read-eval loop that reads from src_file and collects outputs."""
        if not self._import_scheme():
            return 0, 0

        output.off()
        reader = None
        try:
            reader = TestReader(self.file_contents.split('\n'))
            src = self.scheme.Buffer(self.scheme.tokenize_lines(reader))
            def next_line():
                src.current()
                if reader.line_number == len(reader.lines):
                    # No more lines in file.
                    raise EOFError
                return src
            timer.timed(self.timeout, self.scheme.read_eval_print_loop,
                        (next_line, self.scheme.create_global_frame()))
        except BaseException as e:
            output.on()
            if reader:
                print("Tests terminated due to unhandled exception "
                      "after line {}:\n"
                      "{}: {}".format(reader.line_number, e.__class__.__name__, e))
        output.on()

        if reader:
            return self._summarize(reader.output, reader.expected_output)
        return 0, 0

    def _summarize(self, output, expected_output):
        """Summarize results of running tests."""
        num_failed = 0

        def failed(expected, actual, line):
            nonlocal num_failed
            num_failed += 1
            print('test failed at line', line)
            print('  expected', expected)
            print('   printed', actual)

        for (actual, (expected, line_number)) in zip(output, expected_output):
            if expected.startswith("Error"):
                if not actual.startswith("Error"):
                    failed('an error indication', actual, line_number)
            elif actual != expected:
                failed(expected, actual, line_number)

        return len(expected_output) - num_failed, num_failed

    def _import_scheme(self):
        try:
            sys.path.insert(0, 'scheme')
            self.scheme = importlib.import_module('scheme')
        except ImportError as e:
            print('Could not import scheme')
            return False
        return True

###############
# Test reader #
###############

class TestReader:
    """A TestReader is an iterable that collects test case expected results."""

    EXPECT_PATTERN = re.compile(r'\s*;\s*expect\s*(.*)', re.I)

    def __init__(self, lines):
        self.lines = lines
        self.last_out_len = 0
        self.output = []
        self.expected_output = []
        self.line_number = 0

    def __iter__(self):
        log_id = output.new_log()
        output_log = output.get_log(log_id)

        for line in self.lines:
            self.line_number += 1
            match = self.EXPECT_PATTERN.match(line)
            if match:
                expected = match.group(1).split(';')
                for exp in expected:
                    self.expected_output.append((exp.strip(), self.line_number))
                # Split output based on newlines.
                output_lines = ''.join(output_log).split('\n')
                if len(output_lines) > self.last_out_len:
                    self.output.extend(output_lines[-1-len(expected):-1])
                else:
                    self.output.extend([''] * len(expected))
                self.last_out_len = len(output_lines)
            yield line

        output.remove_log(log_id)
        raise EOFError
