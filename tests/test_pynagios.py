"""
Tests for the pynagios package.
"""

class TestPyNagios(object):
    def test_make_option_exported(self):
        """
        Tests to make sure make_option is exported so that it is
        easy to make additional command line options.
        """
        from pynagios import make_option
