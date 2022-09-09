import logging

log = logging.getLogger(__name__)

class Messages(dict):
    """A subclass of dictionary that prints a warning when an existing is
    overwritten.
    """
    def __setitem__(self, key, value):
        if key in self:
            log.warning('Overwriting key %s. Old: %s; New: %s', key, self[key], value)
        super().__setitem__(key, value)
