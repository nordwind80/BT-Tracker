#!/usr/bin/env python3
#
# Author: Nordwind
# E-Mail: bm9yZHdpbmQubWVAZ21haWwuY29t
# Created  Time: 2019-04-23 17:19
# Last Modified: 
# Description:
#        - Project:   Python
#        - File Name: main.py
#        - Version: 
#        -
import argparse

from __version__ import __version__ as version


def start() -> None:
    parser = argparse.ArgumentParser(
            description = "BT Tracker updater tool of Aria2 by Nordwind.")
    parser.add_argument(
            "-v",
            "--version",
            action = "version",
            version =
            f"BT Tracker Updater tool of Aria2 by Nordwind. Version: {version}")
    arge = parser.parse_args()


if __name__ == '__main__':
    start()
