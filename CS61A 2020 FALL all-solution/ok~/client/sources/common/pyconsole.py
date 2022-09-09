"""Case for doctest-style Python tests."""

from client import exceptions
from client.sources.common import interpreter
from client.utils import output
from client.utils import timer
from client.utils import debug

import ast
import code
import textwrap
import traceback

class PythonConsole(interpreter.Console):
    PS1 = '>>> '
    PS2 = '... '

    def __init__(self, verbose, interactive, timeout=None):
        self._original_frame = {}
        super().__init__(verbose, interactive, timeout)

    def load(self, code, setup='', teardown=''):
        """Prepares a set of setup, test, and teardown code to be
        run in the console.

        PARAMETERS:
        code     -- list; processed lines of code. Elements in the list are
                    either strings (input) or CodeAnswer objects (output)
        setup    -- str; raw setup code
        teardown -- str; raw teardown code
        """
        super().load(code, setup, teardown)
        self._frame = self._original_frame.copy()

    def load_env(self, env):
        self._original_frame = env

    def interact(self):
        """Opens up an interactive session with the current state of
        the console.
        """
        console = code.InteractiveConsole(self._frame)
        console.interact('# Interactive console. Type exit() to quit')

    def evaluate(self, code):
        log_id = output.new_log()
        try:
            try:
                result = timer.timed(self.timeout, eval, (code, self._frame))
            except SyntaxError:
                timer.timed(self.timeout, exec, (code, self._frame))
                result = None
        except RuntimeError as e:
            stacktrace_length = 15
            stacktrace = traceback.format_exc().strip().split('\n')
            print('Traceback (most recent call last):\n  ...')
            print('\n'.join(stacktrace[-stacktrace_length:]))
            raise interpreter.ConsoleException(e)
        except exceptions.Timeout as e:
            print('# Error: evaluation exceeded {} seconds - check for infinite loops'.format(e.timeout))
            raise interpreter.ConsoleException(e)
        except Exception as e:
            stacktrace = traceback.format_exc()
            token = '<string>'
            token_start = stacktrace.rfind(token)
            index = stacktrace.find('\n', token_start) + 1
            stacktrace = stacktrace[index:].rstrip('\n')
            if '\n' in stacktrace:
                print('Traceback (most recent call last):')
            print(stacktrace)
            raise interpreter.ConsoleException(e)
        else:
            printed_output = ''.join(output.get_log(log_id))
            return result, debug.remove_debug(printed_output)
        finally:
            output.remove_log(log_id)

    @staticmethod
    def normalize(response):
        return repr(ast.literal_eval(response))
