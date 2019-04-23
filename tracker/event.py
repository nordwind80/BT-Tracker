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
from functools import wraps


class Event(object):
    def __init__(self):
        self._finish = False

    @classmethod
    def check(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            cls.status = True
            time.sleep(0.1)
            cls.status = False
            return result

        return wrapper

    @property
    def finish(self):
        return self._finish

    @finish.setter
    def finish(self, new_status):
        self._finish = new_status


status = Event()
