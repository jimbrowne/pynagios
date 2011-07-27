"""
Contains the class which represents a response for Nagios. This
encapsulates the response format that Nagios expects.
"""

from perf_data import PerfData

class Response(object):
    """
    This class represents a response from a Nagios plugin. Nagios plugins
    must respond in a very specific format, and this plugin assists by
    providing helpers which make emitting this format simple.
    """

    def __init__(self, status=None, message=None):
        """
        Initializes a response.

        An optional `status` argument may be given which should be a
        `Status` object representing the status of the response. This
        can also be set later.

        An option `message` argument may also be given which is the
        informational text added to the Nagios output.
        """
        self.status = status
        self.message = message
        self.perf_data = {}

    def set_perf_data(self, label, value, uom=None, warn=None, crit=None,
                      minval=None, maxval=None):
        """
        Adds performance data to the response. Performance data is shown
        in the Nagios GUI and can be used by 3rd party programs to build
        graphs or other informational output. There are many options to this
        method:

        TODO
        """
        pass

    def __str__(self):
        """
        The string format of this object is the valid Nagios output
        format.
        """
        basic = "%s: %s" % (self.status.name, self.message)
        return basic
