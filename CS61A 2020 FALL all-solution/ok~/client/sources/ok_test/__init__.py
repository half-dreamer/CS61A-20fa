from client import exceptions as ex
from client.sources.common import importing
from client.sources.ok_test import concept
from client.sources.ok_test import doctest
from client.sources.ok_test import models
from client.sources.ok_test import logic
from client.sources.ok_test import scheme
from client.sources.ok_test import sqlite
from client.sources.ok_test import wwpp
import copy
import logging
import os

from client.utils import encryption

log = logging.getLogger(__name__)

SUITES = {
    'doctest': doctest.DoctestSuite,
    'concept': concept.ConceptSuite,
    'logic': logic.LogicSuite,
    'scheme': scheme.SchemeSuite,
    'sqlite': sqlite.SqliteSuite,
    'wwpp': wwpp.WwppSuite,
}

def load(file, parameter, assign):
    """Loads an OK-style test from a specified filepath.

    PARAMETERS:
    file -- str; a filepath to a Python module containing OK-style
            tests.

    RETURNS:
    Test
    """
    filename, ext = os.path.splitext(file)
    if not os.path.isfile(file) or ext != '.py':
        log.info('Cannot import {} as an OK test'.format(file))
        raise ex.LoadingException('Cannot import {} as an OK test'.format(file))

    if os.path.exists(file):
        with open(file) as f:
            data = f.read()
        if encryption.is_encrypted(data):
            decrypted, _ = assign.attempt_decryption([])
            if file not in decrypted:
                name = os.path.basename(filename)
                return {name: models.EncryptedOKTest(name=name, points=1)}

    try:
        test = importing.load_module(file).test
        test = copy.deepcopy(test)
    except Exception as e:
        raise ex.LoadingException('Error importing file {}: {}'.format(file, str(e)))

    name = os.path.basename(filename)
    try:
        return {name: models.OkTest(file, SUITES, assign.endpoint, assign,
                                    assign.cmd_args.verbose,
                                    assign.cmd_args.interactive,
                                    assign.cmd_args.timeout, **test)}
    except ex.SerializeException as e:
        raise ex.LoadingException('Cannot load OK test {}: {}'.format(file, e))
