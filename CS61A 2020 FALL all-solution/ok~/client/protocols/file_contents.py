from client.protocols.common import models
import logging
import os

log = logging.getLogger(__name__)

class FileContentsProtocol(models.Protocol):
    """The contents of source files are sent to the server."""

    def run(self, messages):
        """Find all source files and return their complete contents.

        Source files are considered to be files listed self.assignment.src.
        If a certain source filepath is not a valid file (e.g. does not exist
        or is not a file), then the contents associated with that filepath will
        be an empty string.

        RETURNS:
        dict; a mapping of source filepath -> contents as strings.
        """
        files = {}
        # TODO(albert): move this to AnalyticsProtocol
        if self.args.submit:
            files['submit'] = True
        for file in self.assignment.src:
            if not self.is_file(file):
                # TODO(albert): add an error message
                contents = ''
                log.warning('File {} does not exist'.format(file))
            else:
                contents = self.read_file(file)
                log.info('Loaded contents of {} to send to server'.format(file))
            files[file] = contents

        messages['file_contents'] = files

    #####################
    # Mockable by tests #
    #####################

    def is_file(self, filepath):
        return os.path.isfile(filepath)

    def read_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as lines:
            return lines.read()

protocol = FileContentsProtocol
