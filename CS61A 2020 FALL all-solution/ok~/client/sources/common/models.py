"""Models for serialization of tests."""

from client.sources.common import core

class Test(core.Serializable):
    name = core.String()
    points = core.Float()
    partner = core.String(optional=True)

    def run(self, env):
        """Subclasses should override this method to run tests.

        NOTE: env is intended only for use with the programmatic API for
        Python OK tests.
        """
        raise NotImplementedError

    def score(self):
        """Subclasses should override this method to score the test."""
        raise NotImplementedError

    def unlock(self, interact):
        """Subclasses should override this method to lock the test."""
        raise NotImplementedError

    def lock(self, hash_fn):
        """Subclasses should override this method to lock the test."""
        raise NotImplementedError

    def dump(self):
        """Subclasses should override this method for serialization."""
        raise NotImplementedError

class Case(core.Serializable):
    """Abstract case class."""

    hidden = core.Boolean(default=False)
    locked = core.Boolean(optional=True)

    def run(self):
        """Subclasses should override this method for running a test case.

        RETURNS:
        bool; True if the test case passes, False otherwise.
        """
        raise NotImplementedError

    def lock(self, hash_fn):
        """Subclasses should override this method for locking a test case.

        This method should mutate the object into a locked state.

        PARAMETERS:
        hash_fn -- function; computes the hash code of a given string.
        """
        raise NotImplementedError

    def unlock(self, unique_id_prefix, case_id, interact):
        """Subclasses should override this method for unlocking a test case.

        It is the responsibility of the the subclass to make any changes to the
        test case, including setting its locked field to False.

        PARAMETERS:
        unique_id_prefix -- string; an identifier for this Case, for purposes of
                            analytics.
        case_id          -- string; an identifier for this Case, for purposes of
                            analytics.
        interact         -- function; handles user interaction during the unlocking
                            phase.
        """
        raise NotImplementedError

