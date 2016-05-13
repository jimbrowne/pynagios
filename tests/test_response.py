"""
Contains tests for the pynagios.Response class.
"""

from io import StringIO
from io import BytesIO
import sys
import pynagios
from pynagios import Response


class TestResponse(object):
    def test_status_gets_set_by_initializer(self):
        "Tests that the status can be set by the constructor."
        instance = Response(pynagios.OK)
        assert pynagios.OK == instance.status

    def test_message_gets_set_by_initializer(self):
        "Tests that the message can be set by the constructor."
        instance = Response(message="Hello!")
        assert "Hello!" == instance.message

    def test_str_has_blank_message(self):
        """
        Tests that a response with no message given will not include
        anything in the output.
        """
        instance = Response(pynagios.OK)
        expected = "%s:" % pynagios.OK.name
        assert expected == str(instance)

    def test_str_has_status_and_message(self):
        """
        Tests that without performance data, the status output
        will output the proper thing with status and a message.
        """
        instance = Response(pynagios.OK, message="Hi")
        expected = "%s: %s" % (pynagios.OK.name, "Hi")
        assert expected == str(instance)

    def test_str_has_performance_data(self):
        """
        Tests that with performance data, the status output
        will output the value along with the performance data.
        """
        instance = Response(pynagios.OK, message="yo")
        instance.set_perf_data("users", 20)
        instance.set_perf_data("foos", 80)
        expected = '%s: %s|users=20;;;; foos=80;;;;' % (pynagios.OK.name, "yo")
        assert expected == str(instance)

    def test_exit(self, monkeypatch):
        """
        Tests that responses exit with the proper exit code and stdout output.
        """

        def mock_exit(code):
            mock_exit.exit_status = code

        mock_exit.exit_status = None

        if sys.version_info[0] == 3:
            output = StringIO()
        else:
            output = BytesIO()
        monkeypatch.setattr(sys, 'stdout', output)
        monkeypatch.setattr(sys, 'exit', mock_exit)

        instance = Response(pynagios.OK)
        instance.exit()

        assert pynagios.OK.exit_code == mock_exit.exit_status
        assert "%s\n" % str(instance).encode() == output.getvalue()
