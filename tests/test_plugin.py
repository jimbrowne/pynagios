"""
Contains tests to test the Plugin class.
"""

import pytest
from pynagios import Plugin, Range

class TestPlugin(object):
    Klass = Plugin

    def test_plugin_parses_hostname(self):
        """
        Tests that plugins properly parse the hostname option.
        """
        plugin = self.Klass(["-H", "foo.com"])
        assert "foo.com" == plugin.options.hostname

    def test_plugin_parses_warning_range(self):
        """
        Tests that plugins can properly parse warning ranges from
        the command line via the "-w" option.
        """
        plugin = self.Klass(["-w", "10:20"])
        assert isinstance(plugin.options.warning, Range)
        assert 10.0 == plugin.options.warning.start
        assert 20.0 == plugin.options.warning.end

    def test_plugin_parses_critical_range(self):
        """
        Tests that plugins can properly parse critical ranges
        from the command line via the "-c" option.
        """
        plugin = self.Klass(["-c", "10:20"])
        assert isinstance(plugin.options.critical, Range)

    def test_plugin_parses_timeout(self):
        """
        Tests that plugins can properly parse timeout
        from the command line via the "-t" option.
        """
        plugin = self.Klass(["-t", "17"])
        assert 17 == plugin.options.timeout

    def test_plugin_parses_verbosity(self):
        """
        Tests that plugins can properly parse verbosity.
        """
        plugin = self.Klass(["-v"])
        assert 1 == plugin.options.verbosity

        plugin = self.Klass(["-vv"])
        assert 2 == plugin.options.verbosity

        plugin = self.Klass(["-vvv"])
        assert 3 == plugin.options.verbosity

    def test_plugin_errors_on_check(self):
        """
        Tests that the base plugin throws an exception for check
        since it is not implemented.
        """
        with pytest.raises(NotImplementedError):
            Plugin([]).check()
