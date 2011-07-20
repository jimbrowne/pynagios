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
        self.name = name
        self.exit_code = exit_code

    def __repr__(self):
        return "Status(name=%s, exit_code=%d)" % (repr(self.name), self.exit_code)
