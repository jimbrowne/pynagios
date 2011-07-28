"""
This module provides the Plugin class, which is the basic
class which encapsulates a single plugin. This is the class
which should be subclassed when creating new plugins.
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
        """
        Instantiates a plugin, setting up the options and arguments state.
        Initialization by itself shouldn't do much, since the plugin should run
        when :py:func:`check` is called.

        This init method will parse the arguments given in ``args`` and will
        set the results on the ``options`` attribute. If no ``args`` are given,
        the command line arguments given to the whole Python application will
        be used.

        All plugins parse standard command line arguments that are required
        by the Nagios developer guidelines:

          - ``hostname`` - Set via ``-H`` or ``--hostname``, this should be the
            host that this check targets, if applicable.
          - ``warning`` - Set via ``-w`` or ``--warning``, this should be a valid
            range in which the value of the plugin is considered to be a warning.
          - ``critical`` - Set via ``-c`` or ``--critical``, this should be a
            valid range in which the value is considered to be critical.
          - ``timeout`` - Set via ``-t`` or ``--timeout``, this is an int value
            for the timeout of this check.
          - ``verbosity`` - Set via ``-v``, where additional ``v`` means more
            verbosity. Example: ``-vvv`` will set ``options.verbosity`` to 3.

        Subclasses can define additional options by creating ``Option`` instances
        and assigning them to class attributes. The easiest way to make an
        ``Option`` is to use Python's built-in ``optparse`` methods. The following
        is an example plugin which adds a simple string argument:::

            class MyPlugin(Plugin):
                your_name = make_option("--your-name", dest="your_name", type="string")

        Instantiating the above plugin will result in the value of the new
        argument being available in ``options.your_name``.
        """
        # Parse the given arguments to set the options
        (self.options, self.args) = self._option_parser.parse_args(args)

    def check(self):
        """
        This method is what should be called to run this plugin and return
        a proper :py:class:`~pynagios.response.Response` object. Subclasses
        are expected to implement this.
        """
        raise NotImplementedError("This method must be implemented by the plugin.")

    def response_for_value(self, value, message=None):
        """
        This method is meant to be used by plugin implementers to return a
        valid :py:class:`~pynagios.response.Response` object for the given value.
        The status of this response is determined based on the warning and
        critical ranges given via the command line, which the plugin automatically
        parses.

        An optional ``message`` argument may be provided to set the message
        for the Response object. Note that this can easily be added later as well
        by simply setting the message attribute on the response object returned.

        Creating a response using this method from :py:func:`check` makes it
        trivial to calculate the value, grab a response, set some performance
        metrics, and return it.
        """
        status = OK
        if self.options.critical.in_range(value):
            status = CRITICAL
        elif self.options.warning.in_range(value):
            status = WARNING

        return Response(status, message=message)
