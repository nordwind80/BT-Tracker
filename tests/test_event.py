#!/usr/bin/env python3
#
# Author: Nordwind
# E-Mail: bm9yZHdpbmQubWVAZ21haWwuY29t
# Created  Time: 2019-04-14 20:13
# Last Modified: 
# Description:
#        - Project:   Python
#        - File Name: test_event.py
#        - Version: 
#        - Test singleton instance of event.py


from BTracker.trackers.event import event


class TestEvent(object):

    def test_object(self):
        assert id(event.state) == id(event.state)

    def test_state_change(self):
        event.state = False
        assert event.state is False
