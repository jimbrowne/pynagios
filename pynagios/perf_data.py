"""
Contains class to represent performance data for Nagios output.
"""

import re
from range import Range

class PerfData(object):
    """
    This class represents performance data for a response. Since
    performance data has a non-trivial response format, this class
    is meant to ease the formation of performance data.
    """

    def __init__(self, label, value, uom=None, warn=None, crit=None,
                 minval=None, maxval=None):
        self.label = label
        self.value = value
        self.uom = uom
        self.warn = warn
        self.crit = crit
        self.minval = minval
        self.maxval = maxval

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is None:
            raise ValueError("value must not be None")
        elif not self._is_valid_value(value):
            raise ValueError("value must be in class [-0-9.]")

        self._value = value

    @property
    def warn(self):
        return self._warn

    @warn.setter
    def warn(self, value):
        if value is not None and not isinstance(value, Range):
            value = Range(value)

        self._warn = value

    @property
    def crit(self):
        return self._crit

    @crit.setter
    def crit(self, value):
        if value is not None and not isinstance(value, Range):
            value = Range(value)

        self._crit = value

    @property
    def minval(self):
        return self._minval

    @minval.setter
    def minval(self, value):
        if not self._is_valid_value(value):
            raise ValueError("minval must be in class [-0-9.]")

        self._minval = value

    @property
    def maxval(self):
        return self._maxval

    @maxval.setter
    def maxval(self, value):
        if not self._is_valid_value(value):
            raise ValueError("maxval must be in class [-0-9.]")

        self._maxval = value

    @property
    def uom(self):
        return self._uom

    @uom.setter
    def uom(self, value):
        valids = ['', 's', '%', 'b', 'kb', 'mb', 'gb', 'tb', 'c']
        if value is not None and not str(value).lower() in valids:
            raise ValueError("uom must be in: %s" % valids)

        self._uom = value

    def __str__(self):
        """
        Returns the proper string format that should be outputted
        in the plugin response string.
        """
        # Quotify the label
        label = self._quote_if_needed(self.label)

        # Check for None in each and make it empty string if so
        uom = self.uom or ''
        warn = self.warn or ''
        crit = self.crit or ''
        minval = self.minval or ''
        maxval = self.maxval or ''

        # Create the proper format and return it
        return "%s=%s%s;%s;%s;%s;%s" % (label, self.value, uom, warn, crit, minval, maxval)

    def _is_valid_value(self, value):
        """
        Returns boolean noting whether a value is in the proper value
        format which certain values for the performance data must adhere to.
        """
        value_format = re.compile(r"[-0-9.]+$")
        return value is None or value_format.match(value)

    def _quote_if_needed(self, value):
        """
        This handles single quoting the label if necessary. The reason that
        this is not done all the time is so that characters can be saved
        since Nagios only reads 80 characters and one line of stdout.
        """
        if '=' in value or ' ' in value or "'" in value:
            # Quote the string and replace single quotes with double single
            # quotes and return that
            return "'%s'" % value.replace("'", "''")
        else:
            return value

