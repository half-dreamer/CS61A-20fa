__version__ = 'v1.18.1'

FILE_NAME = 'ok'

import os
import sys

sys.path.insert(0, '')
# Add directory in which the ok.zip is stored to sys.path.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
