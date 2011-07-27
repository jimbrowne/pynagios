"""
This package provides all the modules for writing a Nagios plugin
with Python. The package file itself exports the constants used
throughout the library.
"""

from plugin import Plugin
from range import Range
from status import Status

__version__ = '0.1.0'

# Status constants which contain both the status text and the
# exit status associated with them.
OK = Status("OK", 0)
WARNING = Status("WARN", 1)
CRITICAL = Status("CRIT", 2)
UNKNOWN = Status("UNKNOWN", 3)
