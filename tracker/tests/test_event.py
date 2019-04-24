#!/usr/bin/env python3
#
# Author: Nordwind
# E-Mail: bm9yZHdpbmQubWVAZ21haWwuY29t
# Created  Time: 2019-04-14 20:13
# Last Modified:
# Description:
#        - Project:   Python
#        - File Name: test_event.py
#        - Test singleton instance of event.py


from event import status


class TestEvent(object):
    def test_object(self):
        assert id(status.state) == id(status.state)

    def test_state_change(self):
        status.state = False
        assert status.state is False
