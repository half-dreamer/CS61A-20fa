
import re

from doctest import OutputChecker

def remove_debug(printed_output):
    return re.sub(r'^DEBUG[: ].*\n', '', printed_output, flags=re.MULTILINE | re.IGNORECASE)

class DebugOutputChecker(OutputChecker):
    def __init__(self):
        self.output_checker = OutputChecker()

    def check_output(self, want, got, optionflags):
        return self.output_checker.check_output(want, remove_debug(got), optionflags)

    def output_difference(self, example, got, optionflags):
        return self.output_checker.output_difference(example, remove_debug(got), optionflags)
