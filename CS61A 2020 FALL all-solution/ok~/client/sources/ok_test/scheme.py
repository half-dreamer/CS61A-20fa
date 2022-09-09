"""Console for interpreting Scheme. In particular, this is meant to integrate
with UC Berkeley CS 61A's Scheme project. SchemeConsole expects the an
importable module called "scheme" with the following interface:

    scheme.create_global_frame()
    scheme.read_eval_print_loop(next_line_fn, frame, interactive)
    scheme.buffer_input()
    scheme.read_line(code)
    scheme.scheme_eval(exp, env)
"""

from client import exceptions
from client.sources.common import interpreter
from client.sources.ok_test import doctest
from client.utils import output
from client.utils import timer
from client.utils import debug
import importlib
import sys
import textwrap
import traceback

class SchemeConsole(interpreter.Console):
    PS1 = 'scm> '
    PS2 = '.... '

    MODULE = 'scheme'
    _output_fn = str

    def load(self, code, setup='', teardown=''):
        """Prepares a set of setup, test, and teardown code to be
        run in the console.

        Loads the Scheme module before loading any code.
        """
        self._import_scheme()
        try:
            self._output_fn = self.scheme.repl_str
        except:
            pass
        super().load(code, setup, teardown)
        self._frame = self.scheme.create_global_frame()

    def interact(self):
        """Opens up an interactive session with the current state of
        the console.
        """
        self.scheme.read_eval_print_loop(self.scheme.buffer_input, self._frame,
                                         True)

    def evaluate(self, code):
        if not code.strip():
            # scheme.scheme_read can't handle empty strings.
            return None, ''
        log_id = output.new_log()
        try:
            exp = self.scheme.read_line(code)
            result = timer.timed(self.timeout, self.scheme.scheme_eval,
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
        except self.scheme.SchemeError as e:
            print('# Error: {}'.format(e))
            raise interpreter.ConsoleException(e, exception_type='SchemeError')
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
            return result, debug.remove_debug(printed_output)
        finally:
            output.remove_log(log_id)

    def _import_scheme(self):
        try:
            sys.path.insert(0, 'scheme')
            self.scheme = importlib.import_module(self.MODULE)
        except ImportError as e:
            raise exceptions.ProtocolException('Could not import scheme')

    def normalize(self, response):
        return str(self.scheme.read_line(response))

class SchemeSuite(doctest.DoctestSuite):
    console_type = SchemeConsole
