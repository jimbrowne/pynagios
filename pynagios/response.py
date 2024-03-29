"""
Contains the class which represents a response for Nagios. This
encapsulates the response format that Nagios expects.
"""

import sys
from pynagios.perf_data import PerfData
from collections import OrderedDict as odic


class Response(object):
    """
    This class represents a response from a Nagios plugin. Nagios plugins
    must respond in a very specific format, and this plugin assists by
    providing helpers which make emitting this format simple.
    """

    def __init__(self, status=None, message=None):
        """
        Nagios responses are expected to be in a very specific format, and
        this class allows these responses to easily be built up and extracted
        in the proper format.

        This class makes it easy to set the status, message, and performance
        data for a response.

        :Parameters:
          - `status` (optional): A :py:class:`~pynagios.status.Status` object
            representing the status of the response.
          - `message` (optional): An information message to include with the
            output.
        """
        self.status = status
        self.message = message
        self.perf_data = odic({})

    def set_perf_data(self, label, value, uom=None, warn=None, crit=None,
                      minval=None, maxval=None):
        """
        Adds performance data to the response. Performance data is shown
        in the Nagios GUI and can be used by 3rd party programs to build
        graphs or other informational output. There are many options to this
        method. They are the same as the initialization parameters for a
        :py:class:`~pynagios.perf_data.PerfData` object.

        .. seealso:: :py:class:`~pynagios.perf_data.PerfData`
        """
        # Just set the perf data on the dictionary. PerfData handles
        # argument validation.
        self.perf_data[label] = PerfData(label, value, uom=uom, warn=warn,
                                         crit=crit, minval=minval,
                                         maxval=maxval)

    def exit(self):
        """
        This prints out the response to ``stdout`` and exits with the
        proper exit code.
        """
        print(str(self))
        sys.exit(self.status.exit_code)

    def __str__(self):
        """
        The string format of this object is the valid Nagios output
        format. The response format is expected to be the following:

        ::

          status: information|performance data

        An example of realistic output:

        ::

          OK: 27 users logged in|users=27;0:40;0:60;0;
        """

        result = u"%s:" % self.status.name

        if self.message is not None:
            result += " %s" % self.message

        if len(self.perf_data) > 0:
            # Attach the performance data to the result
            data = [str(val) for key, val in self.perf_data.items()]
            result += '|%s' % (' '.join(data))

        return result
