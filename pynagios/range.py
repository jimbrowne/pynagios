"""
Contains a class to represent a range that adheres to the range
format defined by Nagios.
"""

class RangeValueError(ValueError):
    pass

class Range(object):
    """
    Encapsulates a Nagios range value. This is the value which would
    be passed to command line arguments involving ranges. Examples
    of ranges:

      10 - < 0 OR > 10
      10:20 - < 10 OR > 20
      @10:20 - >= 10 AND <= 20
      ~:10 - > 10 (~ = -inf)
      10:~ - < 10

    """

    def __init__(self, value):
        # Clean up the value by clearing whitespace. Also note that an empty
        # value is invalid.
        value = value.strip()
        if len(value) == 0: raise RangeValueError('Range must not be empty')

        # Test for the inclusivity marked by the '@' symbol at the beginning
        if value.startswith('@'):
            self.inclusive = True
            value = value[1:]
        else:
            self.inclusive = False

        # Split by the ':' character to get the start/end parts.
        parts = value.split(':')
        if len(parts) == 1: parts.insert(0, '0')

        # Parse the start value. If no ':' is included in value (e.g. '10')
        # then the start is assumed to be 0. Otherwise, it is an integer
        # value which can possibly be infinity.
        try:
            if parts[0] == '~':
                start = float("-inf")
            else:
                start = float(parts[0])
        except ValueError:
            raise RangeValueError('invalid start value: %s' % parts[0])

        # Parse the end value, which can be positive infinity.
        try:
            if parts[1] == '~':
                end = float("inf")
            else:
                end = float(parts[1])
        except ValueError:
            raise RangeValueError('invalid end value: %s' % parts[1])

        # The start must be less than the end
        if start > end: raise RangeValueError('start must be less than or equal to end')

        # Set the instance variables
        self.start = start
        self.end = end

    def in_range(self, value):
        """
        Tests whether a value is in this range.
        """
        if self.inclusive:
            return value >= self.start and value <= self.end
        else:
            return value < self.start or value > self.end
