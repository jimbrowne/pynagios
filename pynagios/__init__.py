"""
This package provides all the modules for writing a Nagios plugin
with Python. The package file itself exports the constants used
throughout the library.
"""

from optparse import make_option

from plugin import Plugin, OK, WARNING, CRITICAL, UNKNOWN
from range import Range
from response import Response
from status import Status

version = '0.1.2-dev'
"""Current version of PyNagios"""
