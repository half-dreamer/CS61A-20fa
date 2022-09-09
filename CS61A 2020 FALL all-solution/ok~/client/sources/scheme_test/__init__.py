from client import exceptions as ex
from client.sources.scheme_test import models
import os

def load(file, _, assign):
    """Loads Scheme tests from a specified filepath.

    PARAMETERS:
    file -- str; a filepath to a Scheme file.

    RETURNS:
    Test
    """
    if not os.path.isfile(file) or not file.endswith('.scm'):
        raise ex.LoadingException('Cannot run Scheme tests from {}'.format(file))

    with open(file, 'r') as f:
        file_contents = f.read()

    try:
        return {file: models.SchemeTest(file, file_contents, assign.cmd_args.timeout,
                                        name=file, points=1)}
    except ex.SerializeException:
        raise ex.LoadingException('Unable to load Scheme test '
                                  'from {}'.format(file))

