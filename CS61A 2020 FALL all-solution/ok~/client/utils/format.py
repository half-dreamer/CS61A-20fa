"""Formatting utilities."""

from client import exceptions
import textwrap
from contextlib import contextmanager

#############
# Whtespace #
#############

def dedent(text):
    """Dedents a string of text.

    Leading whitespace that is common to all lines in the string is
    removed. Any leading newlines and trailing whitespace is also
    removed.
    """
    return textwrap.dedent(text).lstrip('\n').rstrip()

def indent(text, indentation):
    """Indents a string of text with the given string of indentation.

    PARAMETERS:
    text        -- str
    indentation -- str; prefix of indentation to add to the front of
                   every new line.

    RETURNS:
    str; the newly indented string.
    """
    return '\n'.join([indentation + line for line in text.splitlines()])

def normalize(text):
    """Normalizes whitespace in a specified string of text."""
    return " ".join(text.strip().split())

############
# Printing #
############

def print_line(style, length=69):
    """Prints an underlined version of the given line with the
    specified underline style.

    PARAMETERS:
    style  -- str; a one-character string that denotes the line style.
    length -- int; the width of the line. The default is 69, which is the width
              for doctest lines.
    """
    print(style * length)

@contextmanager
def block(style, length=69):
    """Print a block with the specified style.
    USAGE:
    with block('-'):
        print("Hello")
    """
    print_line(style, length)
    yield
    print_line(style, length)

def print_progress_bar(header, passed, failed, locked, verbose=True):
    print_line('-')
    print(header)
    if locked > 0:
        print('    Locked: {}'.format(locked))
    if verbose:
        print('    Passed: {}'.format(passed))
        print('    Failed: {}'.format(failed))
    elif failed > 0:
        print('    {} test cases passed before encountering '
              'first failed test case'.format(passed))
        return
    else:
        print('    {} test cases passed! No cases failed.'.format(passed))
        return

    # Print [oook.....] progress bar
    total = passed + failed + locked
    print_percent(passed, total)

def print_coverage_bar(header, exec_lines, tot_lines, verbose=True):
    print_line('-')
    print(header)
    percent = round(100 * exec_lines / tot_lines, 1) if tot_lines != 0 else 0.0
    if verbose:
        print('    Lines Tested: {}'.format(exec_lines))
        print('    Total Lines: {}'.format(tot_lines))

    else:
        if percent < 80:
            print('    {}% test coverage.'.format(percent))
        else:
            print('    {}% test coverage!'.format(percent))
        return
    # Print [oook.....] progress bar
    print_percent(exec_lines, tot_lines)

def print_test_progress_bar(header, passed, failed, verbose=True):
    print_line('-')
    print(header)
    if verbose:
        print('    Passed: {}'.format(passed))
        print('    Failed: {}'.format(failed))
    elif failed > 0:
        print('    {} test examples passed before encountering '
              'first failed test example'.format(passed))
        return
    else:
        print('    {} test examples passed! No examples failed.'.format(passed))
        return

    # Print [oook.....] progress bar
    total = passed + failed
    print_percent(passed, total)
    
def print_percent(numer, denom):
    percent = round(100 * numer / denom, 1) if denom != 0 else 0.0
    print('[{}k{}] {}% passed'.format(
        'o' * int(percent // 10),
        '.' * int(10 - (percent // 10)),
        percent))

#################
# Serialization #
#################

def prettyjson(json, indentation='  '):
    """Formats a Python-object into a string in a JSON like way, but
    uses triple quotes for multiline strings.

    PARAMETERS:
    json        -- Python object that is serializable into json.
    indentation -- str; represents one level of indentation

    NOTES:
    All multiline strings are treated as raw strings.

    RETURNS:
    str; the formatted json-like string.
    """
    if isinstance(json, int) or isinstance(json, float):
        return str(json)
    elif isinstance(json, str):
        if '\n' in json:
            return 'r"""\n' + dedent(json) + '\n"""'
        return repr(json)
    elif isinstance(json, list):
        lst = [indent(prettyjson(el, indentation), indentation) for el in json]
        return '[\n' + ',\n'.join(lst) + '\n]'
    elif isinstance(json, dict):
        pairs = []
        for k, v in sorted(json.items()):
            k = prettyjson(k, indentation)
            v = prettyjson(v, indentation)
            pairs.append(indent(k + ': ' + v, indentation))
        return '{\n' + ',\n'.join(pairs) + '\n}'
    else:
        raise exceptions.SerializeException('Invalid json type: {}'.format(json))

