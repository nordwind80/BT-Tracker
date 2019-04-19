# /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: eagleiwngs
# E-Mail: eaglewings.yi@gmail.com
# Date: 2018-12-19 20:20:43


from BTracker.trackers.spider import Spiders


class TestSpiders(object):
    def test_datainfo(self):

        info = Spiders.create("update_info")
        assert info.get("update_info")[0] == "Updated: 2019-04-19"

        assert len(info.get("update_info")[1]) == 8

    def test_best(self):
        url = Spiders.create("best")
        assert url.get("best")[1] == 20

    def test_bestip(self):
        url = Spiders.create("best_ip")
        assert url.get("best_ip")[1] == 20

    def test_all(self):
        url = Spiders.create("all")
        assert url.get("all")[1] == 83

    def test_allip(self):
        url = Spiders.create("all_ip")
        assert url.get("all_ip")[1] == 83

    def test_udp(self):
        url = Spiders.create("all_udp")
        assert url.get("all_udp")[1] == 44

    def test_http(self):
        url = Spiders.create("all_http")
        assert url.get("all_http")[1] == 31

    def test_https(self):
        url = Spiders.create("all_https")
        assert url.get("all_https")[1] == 7

    def test_ws(self):
        url = Spiders.create("all_ws")
        assert url.get("all_ws")[1] == 1
