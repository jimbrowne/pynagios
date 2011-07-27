"""
Contains tests to test the Plugin class.
"""

from pynagios import Plugin, Range

class TestPlugin(object):

    def test_plugin_parses_hostname(self):
        """
        Tests that plugins properly parse the hostname option.
        """
        plugin = Plugin(["-H", "foo.com"])
        assert "foo.com" == plugin.options.hostname

    def test_plugin_parses_warning_range(self):
        """
        Tests that plugins can properly parse warning ranges from
        the command line via the "-w" option.
        """
        plugin = Plugin(["-w", "10:20"])
        assert isinstance(plugin.options.warning, Range)
        assert 10.0 == plugin.options.warning.start
        assert 20.0 == plugin.options.warning.end

    def test_plugin_parses_critical_range(self):
        """
        Tests that plugins can properly parse critical ranges
        from the command line via the "-c" option.
        """
        plugin = Plugin(["-c", "10:20"])
        assert isinstance(plugin.options.critical, Range)

    def test_plugin_parses_timeout(self):
        """
        Tests that plugins can properly parse timeout
        from the command line via the "-t" option.
        """
        plugin = Plugin(["-t", "17"])
        assert 17 == plugin.options.timeout
