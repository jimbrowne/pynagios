"""
This module provides the Plugin class, which is the basic
class which encapsulates a single plugin.
"""

import sys
from copy import copy
from optparse import Option, OptionParser, make_option
from range import Range, RangeValueError
from response import Response
from status import Status

# Status constants which contain both the status text and the
# exit status associated with them.
OK = Status("OK", 0)
WARNING = Status("WARN", 1)
CRITICAL = Status("CRIT", 2)
UNKNOWN = Status("UNKNOWN", 3)

def check_pynagios_range(option, opt, value):
    """
    This parses and returns the Nagios range value.
    """
    try:
        return Range(value)
    except RangeValueError, e:
        raise OptionValueError("options %s: %s" % (opt, e.message))

# Add the "pynagios_range" type to the global available
# options for OptionParser
Option.TYPES = Option.TYPES + ("pynagios_range",)
Option.TYPE_CHECKER["pynagios_range"] = check_pynagios_range

class PluginMeta(type):
    """
    We use a metaclass to create the plugins in order to gather and
    set up things such as command line arguments.
    """

    def __new__(cls, name, bases, attrs):
        attrs = attrs if attrs else {}

        # Set the options on the plugin by finding all the Options and
        # setting them. This also removes the original Option attributes.
        options = []

        for key,val in attrs.items():
            if isinstance(val, Option):
                options.append(val)
                del attrs[key]

        # Create the option parser
        attrs["_option_parser"] = OptionParser(option_list=options)

        # Create the class
        return super(PluginMeta, cls).__new__(cls, name, bases, attrs)

class Plugin(object):
    """
    Encapsulates a single plugin. This is able to parse the command line
    arguments, understands the range syntax, provides help output, and
    more.
    """
    __metaclass__ = PluginMeta

    hostname = make_option("-H", "--hostname", dest="hostname")
    warning = make_option("-w", "--warning", dest="warning", type="pynagios_range")
    critical = make_option("-c", "--critical", dest="critical", type="pynagios_range")
    timeout = make_option("-t", "--timeout", dest="timeout", type="int")
    verbosity = make_option("-v", "--verbose", dest="verbosity", action="count")

    # TODO: Still missing version

    def __init__(self, args=sys.argv):
        # Parse the given arguments to set the options
        (self.options, self.args) = self._option_parser.parse_args(args)

    def check(self):
        """
        This method is what should be called to run this plugin and return
        a proper Response object.
        """
        raise NotImplementedError("This method must be implemented by the plugin.")

    def response_for_value(self, value):
        """
        This method returns a new Response object for the given value. The
        Response will have a proper status depending on the range of this
        value.
        """
        status = OK
        if self.options.critical.in_range(value):
            status = CRITICAL
        elif self.options.warning.in_range(value):
            status = WARNING

        return Response(status)
