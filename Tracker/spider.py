#!/usr/bin/env python3
#
# Author: eaglewings
# E-Mail: ZWFnbGV3aW5ncy55aUBnbWFpbC5jb20=
# Created  Time: 11:26:58 09-04-2019
# Last Modified:
#        - Project  : BT Tracker Updater
#        - File Name: spider.py
#        - Spider Factory.


import re
from urllib import request
from urllib import error
from typing import List, Tuple, Text, NoReturn


from Tracker.event import status


# Type hint
Trackers = Tuple[str, int]
UpdateTime = Tuple[list, list]
UpdateData = Tuple[str, List[str]]

# URLS
URL = "https://github.com/ngosang/trackerslist"
URL2 = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_"


class Spider(object):
    """Spider class

    """

    def __init__(self):
        self._url = URL
        self._response = None
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }

    def _request(self) -> NoReturn:
        """
            Build response object of urllib.request.Response
        :return: NoReturn
        """
        try:
            req = request.Request(url=self._url, headers=self._headers)
            self._response = request.urlopen(req)
        except error.HTTPError as why:
            print(f"Request connect fail. code: {why.code}")
        except error.URLError as why:
            print(f"Request connect failed. reason: {why.reason}")

    @property
    def _get_html(self) -> Text:
        """
            return html of http.request.Response object.
        :return: Text
        """
        html = self._response.read().decode("utf-8")
        return html

    def _get_trackers(self) -> Trackers:
        self._request()
        trackers = re.findall(
            r"(?P<url>[udp|http|https|wss].*?announce)", self._get_html
        )
        total = len(trackers)

        url_string = ",".join(trackers)
        return url_string, total


class UpdateInfo(Spider):
    """
        Spider to get Tracker update information.
    """

    def _parse(self):
        self._request()
        html = self._get_html
        time = re.findall(r"(?P<update_time>Updated: [0-9]{4}-[0-9]{2}-[0-9]{2})", html)
        options = re.findall(r"<li>(?P<options>trackers_.*) =&gt;", html)
        return time, options

    @status.check
    def get(self):
        result = self._parse()
        return result


class BestDomain(Spider):
    """
        Tracker of Best Domain.
    """

    @status.check
    def get(self) -> Trackers:
        self._url = f"{URL2}best.txt"
        return self._get_trackers()


class BestIP(Spider):
    """
        Tracker of Best IP.
    """

    @status.check
    def get(self) -> Trackers:
        self._url = f"{URL2}best_ip.txt"
        return self._get_trackers()


class AllDomain(Spider):
    """
        Tracker of All Domain.
    """

    @status.check
    def get(self) -> Trackers:
        self._url = f"{URL2}all.txt"
        return self._get_trackers()


class AllIP(Spider):
    """
        Tracker of All IP.
    """

    @status.check
    def get(self) -> Trackers:
        self._url = f"{URL2}all_ip.txt"
        return self._get_trackers()


class AllUDP(Spider):
    """
        Tracker of UDP.
    """

    @status.check
    def get(self) -> Trackers:
        self._url = f"{URL2}all_udp.txt"
        return self._get_trackers()


class AllHTTP(Spider):
    """
        Trackers of HTTP.
    """

    @status.check
    def get(self) -> Trackers:
        self._url = f"{URL2}all_http.txt"
        return self._get_trackers()


class AllHTTPS(Spider):
    """
        Tracker of HTTPS.
    """

    @status.check
    def get(self) -> Trackers:
        self._url = f"{URL2}all_https.txt"
        return self._get_trackers()


class AllWS(Spider):
    """
        Tracker of WS.
    """

    @status.check
    def get(self) -> Trackers:
        self._url = f"{URL2}all_ws.txt"
        return self._get_trackers()


class Spiders(object):
    """
        Spider Factory
    """

    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly.")

    @staticmethod
    def create(model: str):
        options = {
            "update_info": UpdateInfo,
            "best": BestDomain,
            "best_ip": BestIP,
            "all": AllDomain,
            "all_ip": AllIP,
            "all_udp": AllUDP,
            "all_http": AllHTTP,
            "all_https": AllHTTPS,
            "all_ws": AllWS,
        }

        return options[model]()
