#!/usr/bin/env python3
#
# Author: eaglewings
# E-Mail: ZWFnbGV3aW5ncy55aUBnbWFpbC5jb20=
# Created  Time: 2019-04-14 20:13
# Description:
#        - Project:   BT Trackers Updater
#        - File Name: test_event.py
#        - Test Spiders factory.py


from ..spider import Spiders


class TestSpiders(object):
    def test_datainfo(self):

        info = Spiders.create("update_info")
        assert info.get()[0][0] == "Updated: 2019-04-23"

        assert len(info.get()[1]) == 8

    def test_best(self):
        url = Spiders.create("best")
        assert url.get()[1] == 20

    def test_bestip(self):
        url = Spiders.create("best_ip")
        assert url.get()[1] == 20

    def test_all(self):
        url = Spiders.create("all")
        assert url.get()[1] == 81

    def test_allip(self):
        url = Spiders.create("all_ip")
        assert url.get()[1] == 81

    def test_udp(self):
        url = Spiders.create("all_udp")
        assert url.get()[1] == 43

    def test_http(self):
        url = Spiders.create("all_http")
        assert url.get()[1] == 30

    def test_https(self):
        url = Spiders.create("all_https")
        assert url.get()[1] == 7

    def test_ws(self):
        url = Spiders.create("all_ws")
        assert url.get()[1] == 1
