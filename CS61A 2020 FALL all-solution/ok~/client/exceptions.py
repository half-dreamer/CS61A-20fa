"""Client exceptions."""

import client

import sys
import logging

log = logging.getLogger(__name__)   # Get top-level logger

class OkException(Exception):
    """Base exception class for OK."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        log.debug('Exception raised: {}'.format(type(self).__name__))
        log.debug('python version: {}'.format(sys.version_info))
        log.debug('okpy version: {}'.format(client.__version__))



class AuthenticationException(OkException):
    """Exceptions related to authentication."""


class OAuthException(AuthenticationException):
    def __init__(self, error='', error_description=''):
        super().__init__()
        self.error = error
        self.error_description = error_description


class ProtocolException(OkException):
    """Exceptions related to protocol errors."""


class EarlyExit(OkException):
    """Exceptions related to early exits that are NOT errors."""


# TODO(albert): extend from a base class designed for student bugs.
class Timeout(OkException):
    """Exception for timeouts."""
    _message = 'Evaluation timed out!'

    def __init__(self, timeout):
        """Constructor.

        PARAMTERS:
        timeout -- int; number of seconds before timeout error occurred
        """
        super().__init__()
        self.timeout = timeout
        self.message = self._message


class LoadingException(OkException):
    """Exception related to loading assignments."""

class InvalidTestInQuestionListException(LoadingException):
    def __init__(self, valid_tests, question):
        super().__init__(self.compute_message(valid_tests, question))
        self.valid_tests = valid_tests
        self.question = question

    @staticmethod
    def compute_message(valid_tests, question):
        output = []
        output += ['Test "{}" not found'.format(question)]
        output += ['Did you mean one of the following? (Names are case sensitive)']
        for test in valid_tests:
            output += ['    {}'.format(test)]
        return "\n".join(output)

class ForceDecryptionException(Exception):
    def __init__(self, keys):
        self.keys = keys


class SerializeException(LoadingException):
    """Exceptions related to de/serialization."""
