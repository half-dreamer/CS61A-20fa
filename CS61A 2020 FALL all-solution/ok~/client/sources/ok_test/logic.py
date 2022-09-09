"""Console for interpreting Logic, a variant of the Prolog language. In
particular, this is meant to integrate with UC Berkeley CS 61A's Logic
interpreter. LogicConsole expects the an importable module called "logic" with
the following interface:

    logic.create_global_frame()
    logic.read_eval_print_loop(next_line_fn, frame, interactive)
    logic.buffer_input()
    logic.read_line(code)
    logic.process_input(exp, env)
    logic.facts
"""

from client import exceptions
from client.sources.common import interpreter
from client.sources.ok_test.scheme import SchemeConsole
from client.sources.ok_test import doctest
from client.utils import output
from client.utils import timer
import importlib
import sys
import textwrap
import traceback

class LogicConsole(interpreter.Console):
    PS1 = 'logic> '
    PS2 = '...... '

    MODULE = 'logic'
    _output_fn = str

    def load(self, code, setup='', teardown=''):
        """Prepares a set of setup, test, and teardown code to be
        run in the console.

        Loads the Logic module before loading any code.
        """
        self._import_logic()
        super().load(code, setup, teardown)
        self._frame = self.logic.create_global_frame()

    def interact(self):
        """Opens up an interactive session with the current state of
        the console.
        """
        self.logic.read_eval_print_loop(self.logic.buffer_input, self._frame,
                                         True)

    def evaluate(self, code):
        if not code.strip():
            # logic.scheme_read can't handle empty strings.
            return None, ''
        log_id = output.new_log()
        try:
            exp = self.logic.read_line(code)
            result = timer.timed(self.timeout, self.logic.scheme_eval,
                                 (exp, self._frame))
        except RuntimeError as e:
            stacktrace_length = 15
            stacktrace = traceback.format_exc().strip().split('\n')
            print('Traceback (most recent call last):\n  ...')
            print('\n'.join(stacktrace[-stacktrace_length:]))
            raise interpreter.ConsoleException(e)
        except exceptions.Timeout as e:
            print('# Error: evaluation exceeded {} seconds.'.format(e.timeout))
            raise interpreter.ConsoleException(e)
        except Exception as e:
            stacktrace = traceback.format_exc()
            token = '<module>\n'
            index = stacktrace.rfind(token) + len(token)
            stacktrace = stacktrace[index:].rstrip('\n')
            if '\n' in stacktrace:
                print('Traceback (most recent call last):')
            print(stacktrace)
            raise interpreter.ConsoleException(e)
        else:
            printed_output = ''.join(output.get_log(log_id))
            return result, printed_output
        finally:
            output.remove_log(log_id)

    def _import_logic(self):
        try:
            sys.path.insert(0, 'logic')
            self.logic = importlib.import_module(self.MODULE)
        except ImportError as e:
            raise exceptions.ProtocolException('Could not import logic')

    def _reset_logic(self):
        """The Logic interpreter needs to be reset before running a suite.
        All mutable global variables should be reset.
        """
        self.logic.facts[:] = []

    def normalize(self, response):
        return self.logic.repl_str(self.logic.read_line(response))

class LogicSuite(doctest.DoctestSuite):
    console_type = LogicConsole

    def run(self, test_name, suite_number, env=None):
        self.console._reset_logic()
        return super().run(test_name, suite_number, env)
