"""
This module provides the Status class, which encapsulates
a status code for Nagios.
"""

class Status(object):
    """
    Encapsulates a Nagios status, which holds a name and
    an exit code.
    """

    def __init__(self, name, exit_code):
        """
        Creates a new status object for Nagios with the given name and
        exit code.

        **Note**: In general, this should never be called since the standard
        statuses are exported from ``pynagios``.
        """
        self.name = name
        self.exit_code = exit_code

    def __repr__(self):
        return "Status(name=%s, exit_code=%d)" % (repr(self.name), self.exit_code)
