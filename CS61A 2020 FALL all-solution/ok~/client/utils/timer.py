"""Timeout mechanism."""

from client import exceptions
import threading
import traceback

def timed(timeout, fn, args=(), kargs={}):
    """For a nonzero timeout, evaluates a call expression in a separate thread.
    If the timeout is 0, the expression is evaluated in the main thread.

    PARAMETERS:
    fn      -- function; Python function to be evaluated
    args    -- tuple; positional arguments for fn
    kargs   -- dict; keyword arguments for fn
    timeout -- int; number of seconds before timer interrupt

    RETURN:
    Result of calling fn(*args, **kargs).

    RAISES:
    Timeout -- if thread takes longer than timeout to execute
    Error   -- if calling fn raises an error, raise it
    """
    if timeout == 0:
        return fn(*args, **kargs)

    submission = __ReturningThread(fn, args, kargs)
    submission.start()
    submission.join(timeout)
    if submission.is_alive():
        raise exceptions.Timeout(timeout)
    if submission.error is not None:
        raise submission.error
    return submission.result

class __ReturningThread(threading.Thread):
    """Creates a daemon Thread with a result variable."""
    def __init__(self, fn, args, kargs):
        super().__init__()
        self.daemon = True
        self.result = None
        self.error = None
        self.fn = fn
        self.args = args
        self.kargs = kargs

    def run(self):
        try:
            self.result = self.fn(*self.args, **self.kargs)
        except Exception as e:
            e._message = traceback.format_exc(limit=2)
            self.error = e

