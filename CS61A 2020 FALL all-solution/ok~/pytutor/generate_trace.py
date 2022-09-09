# Generates a JSON trace that is compatible with the js/pytutor.js frontend
# With customization to support extra modules. Runs within the container

import os, os.path
import sys, json
from optparse import OptionParser

from . import pg_logger

# To make regression tests work consistently across platforms,
# standardize display of floats to 3 significant figures
#
# Trick from:
# http://stackoverflow.com/questions/1447287/format-floats-with-standard-json-module
json.encoder.FLOAT_REPR = lambda f: ('%.3f' % f)
INDENT_LEVEL = 2

def json_finalizer(input_code, output_trace, modules):
    input_code.update(modules) # mutates, should be okay unless you have a module called main_code
    ret = dict(code=input_code, trace=output_trace)
    # sort_keys=True leads to printing in DETERMINISTIC order, but might
    # screw up some old tests ... however, there is STILL non-determinism
    # in Python 3.3 tests, ugh!
    json_output = json.dumps(ret, indent=INDENT_LEVEL)
    return json_output

def run_logger(source, setup, modules=None):
    modules = modules or {}
    # Add current directory to path to make sure that imports work consistently
    sys.path.append(os.getcwd() + '/')

    finalizer = lambda code,trace: json_finalizer(code, trace, modules)
    return pg_logger.exec_script_str_local(source,
                                           [], # JSON list of strings for simulated raw_
                                           True, # output cumulative trace (to display exited frames)
                                           False, # render primitives as heap objects
                                           finalizer,
                                           separate_stdout_by_module=False,
                                           disable_security_checks=True,
                                           custom_modules={'pg_setup': setup},
                                           extra_modules=modules)

