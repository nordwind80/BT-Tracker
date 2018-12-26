# /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: eagleiwngs
# E-Mail: eaglewings.yi@gmail.com
# Date: 2018-12-19 20:20:43


from ..autodate import Trackers

class TestTracker(object):

    def test_params(self):
        track = Trackers()

        index = track.start("best_ip")
        assert index == 20

        index = track.start("best_domain")
        assert index == 20

        index = track.start("all_ip")
        assert index == 63

        index = track.start("all_domain")
        assert index == 63


        index = track.start("all_udp")
        assert index == 30

        index = track.start("all_http")
        assert index == 26

        index = track.start("all_https")
        assert index == 4

        index = track.start("all_ws")
        assert index == 3

