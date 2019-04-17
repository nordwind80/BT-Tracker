#!/usr/bin/env python3
#
# Author: Nordwind
# E-Mail: bm9yZHdpbmQubWVAZ21haWwuY29t
# Created  Time: 2019-04-14 20:14
# Last Modified: 
# Description:
#        - Project:   BT Trackers Updater
#        - File Name: event.py
#        - Version: 0.1.2
#        - singleton instance of Event


import time


class Event(object):

    def __init__(self):
        self._finish = False

    @property
    def state(self):
        return self._finish

    @state.setter
    def state(self, new_state):
        if isinstance(new_state, bool) and new_state is True:
            self._finish = new_state
            time.sleep(0.5)
            self._finish = False


event = Event()
