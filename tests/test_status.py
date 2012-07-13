"""
Contains tests to test the Status class, which is responsible for
storing a NAGIOS exit status and corresponding message
"""

import pytest
from pynagios.status import Status

class TestStatus(object):

    def test_status_comparison(self):
        """
        Tests __cmp__ operator of Status class
        """

        a = Status('OK',0)
        b = Status('OK',0)
        assert a == b
        assert not a is b
        assert Status('Test',0) < Status('Test',1)
        assert Status('Test',1) > Status('Test',0)
