#!/usr/bin/env python3
#
# Author: Nordwind
# E-Mail: bm9yZHdpbmQubWVAZ21haWwuY29t
# Created  Time: 2019-04-17 15:17
# Last Modified:
# Description:
#        - Project:   BT Trackers Updater
#        - File Name: update.py
#        - Version: 0.1.2
#        - Updater


import os
from typing import NoReturn


class Filer(object):
    def __init__(self):
        self._aria2_path = "/.aria2/"
        self._file_name = "aria2.conf"
        self._file_path = f"{self._get_home}{self._aria2_path}"

    @property
    def _get_home(self) -> str:
        """
            Return User $HOME path.
        :return: str
        """
        return os.path.expanduser("~")

    @property
    def get_path(self) -> str:
        """
            Return Aria2 config file path.
        :return: str
        """
        return f"{self._file_path}{self._file_name}"

    def check_dirctory(self) -> NoReturn:
        """
            Find Aria2 directory, If not create it. If mkdir fail, raise FileExistsError error.
        :return: NoReturn
        """
        if os.path.exists(f"{self._file_path}"):
            print(f"\nFound Aria2. path: {self._file_path}{self._file_name}\n")
        else:
            try:
                print(
                    f"\nDon't find aria2, Create aria2 directory. path: {self._file_path}\n"
                )
                os.mkdir(f"{self._file_path}")
            except FileExistsError as why:
                print(f"Create directory fail. {why}")


class Updater(object):
    pass


if __name__ == "__main__":
    filer = Filer()
    print(filer.check_dirctory())
