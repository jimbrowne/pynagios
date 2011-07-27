"""
Contains tests for the pynagios.Response class.
"""

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

    def test_str_has_status_and_message(self):
        """
        Tests that without performance data, the status output
        will output the proper thing with status and a message.
        """
        instance = Response(pynagios.OK, message="Hi")
        expected = "%s: %s" % (pynagios.OK.name, "Hi")
        assert expected == str(instance)
