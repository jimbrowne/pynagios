"""
This package provides all the modules for writing a Nagios plugin
with Python. The package file itself exports the constants used
throughout the library.
"""

import argparse

from pynagios.plugin import Plugin, OK, WARNING, CRITICAL, UNKNOWN
from pynagios.range import Range
from pynagios.response import Response
from pynagios.status import Status

version = '0.1.2-dev'
"""Current version of PyNagios"""
