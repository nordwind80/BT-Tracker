# /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: eagleiwngs
# E-Mail: eaglewings.yi@gmail.com
# Date: 2018-12-18 20:11:43


import os
import re
import fileinput
import argparse
import requests


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


__version__ = "0.0.5"


class Trackers(object):
    """
        Update bt-tracker for aria2 on macOS
    """

    __headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        }

    __best_domain = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt"
    __best_ip = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt"
    __all_ip = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"
    __all_domain = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt"
    __all_udp = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt"
    __all_http = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt"
    __all_https = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt"
    __all_ws = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ws.txt"

    def __init__(self):
        self._aria2_path = "aria2.conf"
        self._trackers = ''
        self._select = {
                "best_domain": self.__best_domain,
                "best_ip": self.__best_ip,
                "all_ip": self.__all_ip,
                "all_domain": self.__all_domain,
                "all_udp": self.__all_udp,
                "all_http": self.__all_http,
                "all_https": self.__all_https,
                "all_ws": self.__all_ws
                }

    def __getResponse(self, url: str, headers: str=None, verify: bool=False, stream: bool=False) -> str:
        response = requests.get(url, headers=headers, verify=verify, stream=stream)
        if response.status_code != 200:
            print(f"Response error code: {response.status_code}")
            return
        else:
            return response.text

    def _params(self):
        urls = re.findall(f"(?P<url>[udp|http|https|wss].*?announce)", self.__getResponse(self._mode, headers=self.__headers))

        for index, url in enumerate(urls, start=1):
            self._trackers += f"{url},"

        self._trackers.strip(',')

        print(f"Params Trackers list done. Total: {index} trackers")

    def _handler(self):
        with open('text.conf', 'r+') as file:
            for index, line in enumerate(file.readlines()):
                if re.search(r'(bt-tracker=)', line):
                    os.system(f'sed -i "" "s@bt-tracker.*@bt-tracker={self._trackers}@g" {self._aria2_path} && \ ')
                    break
                else:
                    continue
            file.writelines(f"bt-tracker={self._trackers}")
        print("BT-Tracker list upgrade completed.")

    def start(self, mode: str):
        if mode:
            self._mode = self._select.get(mode)
            print(f"Select {mode} mode.")
        self._params()
        self._handler()

def arg():
    parser = argparse.ArgumentParser(description="Update BT-Trackers list for Aria2.")
    parser.add_argument("-v", "--version", action="version",
            version=f"BT-Trackers list autoupdate tool. Version: {__version__}")
    parser.add_argument("-m", "--mode", dest="mode", action="store",
            choices={
                'best_ip',
                'best_domain',
                'all_ip',
                'all_domain',
                'all_udp', 
                'all_http',
                'all_https',
                'all_ws'}, default="all_domain",
            help="Select the update mode. ep:[best_ip, best_domain, all_ip, all_domain, all_udp, all_http, all_https, all_ws]")
    arge = parser.parse_args()

    if arge.mode:
        track = Trackers()
        track.start(arge.mode)

if __name__ == "__main__":
    arg()

