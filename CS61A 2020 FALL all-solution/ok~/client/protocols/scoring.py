"""Implements the ScoringProtocol, which runs all specified tests
associated with an assignment.
"""

from client.sources.common import core
from client.sources.common import models as sources_models
from client.sources.ok_test import models as ok_test_models
from client.protocols.common import models as protocol_models
from client.utils import format
from collections import OrderedDict
import logging
import sys

log = logging.getLogger(__name__)

#####################
# Scoring Mechanism #
#####################

class ScoringProtocol(protocol_models.Protocol):
    """A Protocol that runs tests, formats results, and reports a student's
    score.
    """
    def run(self, messages, env=None):
        """Score tests and print results. Tests are taken from
        self.assignment.specified_tests. A score breakdown by question and the
        total score are both printed.

        ENV is used by the programatic API for Python doctests only.
        """
        if not self.args.score or self.args.testing:
            return

        format.print_line('~')
        print('Scoring tests')
        print()

        raw_scores = OrderedDict()
        for test in self.assignment.specified_tests:
            assert isinstance(test, sources_models.Test), 'ScoringProtocol received invalid test'

            log.info('Scoring test {}'.format(test.name))

            # A hack that allows programmatic API users to plumb a custom
            # environment through to Python tests.
            # Use type to ensure is an actual OkTest and not a subclass
            if type(test) == ok_test_models.OkTest:
                score = test.score(env=env)
            else:
                score = test.score()

            raw_scores[test.name] = (score, test.points)

        messages['scoring'] = display_breakdown(raw_scores, self.args.score_out)
        print()

def display_breakdown(scores, outfile=None):
    """Writes the point breakdown to `outfile` given a dictionary of scores.
    `outfile` should be a string.  If `outfile` is None, write to stdout.

    RETURNS:
    dict; 'Total' -> finalized score (float)
    """
    total = 0
    outfile = open(outfile, 'w') if outfile else sys.stdout

    format.print_line('-')
    print('Point breakdown', file=outfile)
    for name, (score, max_score) in scores.items():
        print('    {}: {}/{}'.format(name, score, max_score), file=outfile)
        total += score
    print(file=outfile)

    print('Score:', file=outfile)
    print('    Total: {}'.format(total), file=outfile)
    return {'Total': total}

protocol = ScoringProtocol
