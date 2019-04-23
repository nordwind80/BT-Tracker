# Author: Nordwind
# E-Mail: bm9yZHdpbmQubWVAZ21haWwuY29t
# Created  Time: 11:26:58 09-04-2019
# Last Modified:
#        - Project  : BT Tracker Updater
#        - File Name: spider.py
#        - Version : 0.1.2
#        - Spider Factory.


import re
import urllib.request
import urllib.error
from typing import List, Tuple, Any, Text, Union, NoReturn


from .event import status


# Type hint
Trackers = Tuple[str, int]
UpdateTime = Tuple[list, list]
UpdateData = Tuple[str, List[str]]
JSON = Union[str, Any]

# URLS
URL = "https://github.com/ngosang/trackerslist"
URL2 = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_"


class Spider(object):
    """Spider class

    """

    def __init__(self):
        self._url = URL
        self._model = ""
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }

    def _request(self) -> NoReturn:
        """
            Response object of requests.get.
        :return: NoReturn
        """
        try:
            req = urllib.request.Request(url=self._url, headers=self._headers)
            self._response = urllib.request.urlopen(req)
        except urllib.error.HTTPError as why:
            print(f"Request connect fail. code: {why.code}")
        except urllib.error.URLError as why:
            print(f"Request connect failed. reason: {why.reson}")

    @property
    def _get_text(self) -> Text:
        """
            return context of requests.Response object.
        :return: Text
        """
        return self._response.read().decode("utf-8")

    def _get_trackers(self) -> Trackers:
        self._request()
        trackers = re.findall(
            r"(?P<url>(udp|http|https|wss).*?announce)", self._get_text
        )
        total = len(trackers)

        url_string = ",".join(trackers[0])
        return url_string, total


class UpdateInfo(Spider):
    """Spider to get tracker update information.

    """

    def _parse(self) -> UpdateTime:
        self._request()
        html = self._get_text
        time = re.findall(
            r"(?P<update_time>Updated: [0-9]{4}-[0-9]{2}-[0-9]{2})", html
        )
        options = re.findall(r"<li>(?P<options>trackers_.*) =&gt;", html)
        return time, options

    @status.check
    def get(self) -> UpdateTime:
        return self._parse()


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

