"""
This module provides the Plugin class, which is the basic
class which encapsulates a single plugin.
"""

from copy import copy
from optparse import Option, OptionParser, make_option
from range import Range, RangeValueError

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

    def __init__(self, args):
        # Parse the given arguments to set the options
        (options, args) = self._option_parser.parse_args(args)

        self.options = options
        self.args = args
