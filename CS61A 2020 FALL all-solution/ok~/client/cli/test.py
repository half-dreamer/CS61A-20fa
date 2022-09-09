from client import exceptions as ex
from client.cli import ok
from client.api import assignment
from client.cli.common import messages
from client.protocols import grading
from client.protocols import scoring
import argparse
import client
import logging
import os.path

from client.utils.printer import print_error

LOGGING_FORMAT = '%(levelname)s | pid %(process)d | %(filename)s:%(lineno)d | %(message)s'
logging.basicConfig(format=LOGGING_FORMAT)
log = logging.getLogger('client')   # Get top-level logger

CLIENT_ROOT = os.path.dirname(client.__file__)

def main():
    """Run GradingProtocol and ScoringProtocol."""
    args = ok.parse_input()

    log.setLevel(logging.DEBUG if args.debug else logging.ERROR)
    log.debug(args)

    try:
        assign = assignment.load_assignment(args.config, args)

        msgs = messages.Messages()

        grading.protocol(args, assign).run(msgs)
        scoring.protocol(args, assign).run(msgs)
    except (ex.LoadingException, ex.SerializeException) as e:
        log.warning('Assignment could not instantiate', exc_info=True)
        print_error('Error: ' + str(e).strip())
        exit(1)
    except (KeyboardInterrupt, EOFError):
        log.info('Quitting...')

if __name__ == '__main__':
    main()
