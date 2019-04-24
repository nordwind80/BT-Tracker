#!/usr/bin/env python3
#
# Author: eaglewings
# E-Mail: ZWFnbGV3aW5ncy55aUBnbWFpbC5jb20=
# Created  Time: 2019-04-14 20:13
# Last Modified:
# Description:
#        - Project:   BT Trackers Updater
#        - File Name: test_event.py
#        - Test singleton instance of event.py


from event import status


class TestEvent(object):
    def test_object(self):
        assert id(status.state) == id(status.state)

    def test_state_change(self):
        status.state = False
        assert status.state is False
