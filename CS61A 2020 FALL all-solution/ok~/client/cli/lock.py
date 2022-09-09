from client import exceptions as ex
from client.api import assignment
from client.cli.common import messages
from client.protocols import lock
import argparse
import client
import logging
import os.path

from client.utils.printer import print_error

log = logging.getLogger(__name__)

CLIENT_ROOT = os.path.dirname(client.__file__)

def parse_input():
    """Parses command line input."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-c', '--config', type=str,
                        help="Specify a configuration file")
    return parser.parse_args()

def main():
    """Run the LockingProtocol."""
    args = parse_input()
    args.lock = True
    args.question = []
    args.all = False
    args.timeout = 0
    args.verbose = False
    args.interactive = False

    try:
        assign = assignment.load_assignment(args.config, args)

        msgs = messages.Messages()

        lock.protocol(args, assign).run(msgs)
    except (ex.LoadingException, ex.SerializeException) as e:
        log.warning('Assignment could not instantiate', exc_info=True)
        print_error('Error: ' + str(e).strip())
        exit(1)
    except (KeyboardInterrupt, EOFError):
        log.info('Quitting...')
    else:
        assign.dump_tests()

if __name__ == '__main__':
    main()
