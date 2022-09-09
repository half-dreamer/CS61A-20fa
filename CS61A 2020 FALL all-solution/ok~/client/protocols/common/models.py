class Protocol(object):
    """A Protocol encapsulates a single aspect of OK functionality."""

    def __init__(self, args, assignment):
        """Constructor.

        PARAMETERS:
        args       -- Namespace; parsed command line arguments by argparse.
        assignment -- dict; general information about the assignment.
        """
        self.args = args
        self.assignment = assignment

    def run(self, messages):
        """Executes the protocol, given a dictionary of messages.

        PARAMETERS:
        messages -- dict; a structure that Protocols can use to record data
                    and/or send to a server.
        """
        raise NotImplementedError

