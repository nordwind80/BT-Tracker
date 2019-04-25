#!/usr/bin/env python3
#
# Author: eaglewings
# E-Mail: ZWFnbGV3aW5ncy55aUBnbWFpbC5jb20=
# Created  Time: 2019-04-14 20:14
# Last Modified:
# Description:
#        - Project:   BT Trackers Updater
#        - File Name: event.py
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
            cls.finished = True
            time.sleep(0.1)
            cls.finished = False
            return result

        return wrapper

    @property
    def finished(self):
        return self._finish

    @finished.setter
    def finished(self, new_status: bool):
        if new_status is True:
            self._finish = new_status


status = Event()
