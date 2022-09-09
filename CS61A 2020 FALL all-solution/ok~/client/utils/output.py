"""This module contains code related to controlling and writing to stdout."""

import io
import os
import sys

class _OutputLogger(object):
    """Custom logger for capturing and suppressing standard output."""
    # TODO(albert): logger should fully implement output stream.

    def __init__(self, stdout=sys.stdout):
        self._current_stream = self._stdout = stdout
        self._devnull = io.open(os.devnull, 'w', encoding=getattr(stdout, 'encoding', 'utf-8'))
        self._logs = {}
        self._num_logs = 0

    def on(self):
        """Allows print statements to emit to standard output."""
        self._current_stream = self._stdout

    def off(self):
        """Prevents print statements from emitting to standard out."""
        self._current_stream = self._devnull

    def new_log(self):
        """Registers a new log so that calls to write will append to the log.

        RETURN:
        int; a unique ID to reference the log.
        """
        log_id = self._num_logs
        self._logs[log_id] = []
        self._num_logs += 1
        return log_id

    def get_log(self, log_id):
        assert log_id in self._logs
        return self._logs[log_id]

    def remove_log(self, log_id):
        assert log_id in self._logs, 'Log id {} not found'.format(log_id)
        del self._logs[log_id]

    def remove_all_logs(self):
        self._logs = {}

    def is_on(self):
        return self._current_stream == self._stdout

    def write(self, msg):
        """Writes msg to the current output stream (either standard
        out or dev/null). If a log has been registered, append msg
        to the log.

        PARAMTERS:
        msg -- str
        """
        self._current_stream.write(msg)
        for log in self._logs.values():
            log.append(msg)

    def flush(self):
        self._current_stream.flush()

    # TODO(albert): rewrite this to be cleaner.
    def __getattr__(self, attr):
        return getattr(self._current_stream, attr)

_logger = sys.stdout = _OutputLogger()

def on():
    _logger.on()

def off():
    _logger.off()

def get_log(log_id):
    return _logger.get_log(log_id)

def new_log():
    return _logger.new_log()

def remove_log(log_id):
    _logger.remove_log(log_id)

def remove_all_logs():
    _logger.remove_all_logs()

class DisableLog:
    re_enable = False
    def __enter__(self):
        self.re_enable = _logger.is_on()
        off()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.re_enable:
            on()
