# /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: eagleiwngs
# E-Mail: eaglewings.yi@gmail.com
# Date: 2018-12-19 20:20:43


from BTracker.trackers.spider import SpiderFactory


class TestSpiderFactory(object):
    _trackers = SpiderFactory()

    def test_datainfo(self):

        info = self._trackers.create('update_info')
        assert info.get('update_info')[0] == "Updated: 2019-04-17"

        assert len(info.get('update_info')[1]) == 8

    def test_best(self):
        url = self._trackers.create('best')
        assert url.get('best')[1] == 20

    def test_bestip(self):
        url = self._trackers.create('best_ip')
        assert url.get('best_ip')[1] == 20

    def test_all(self):
        url = self._trackers.create('all')
        assert url.get('all')[1] == 73

    def test_allip(self):
        url = self._trackers.create('all_ip')
        assert url.get('all_ip')[1] == 73

    def test_udp(self):
        url = self._trackers.create('all_udp')
        assert url.get('all_udp')[1] == 40

    def test_http(self):
        url = self._trackers.create('all_http')
        assert url.get('all_http')[1] == 25

    def test_https(self):
        url = self._trackers.create('all_https')
        assert url.get('all_https')[1] == 7

    def test_ws(self):
        url = self._trackers.create('all_ws')
        assert url.get('all_ws')[1] == 1

