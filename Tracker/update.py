#!/usr/bin/env python3
#
# Author: eaglewings
# E-Mail: ZWFnbGV3aW5ncy55aUBnbWFpbC5jb20=
# Created  Time: 2019-04-17 15:17
# Last Modified:
# Description:
#        - Project:   BT Trackers Updater
#        - File Name: update.py
#        - Trackers Updater


import os
import re
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

    def _create_dir(self) -> NoReturn:
        try:
            os.mkdir(f"{self._file_path}")
        except FileExistsError as why:
            print(f"Create directory failed. {why}")

    def check_dirctory(self) -> bool:
        """
            Find Aria2 directory, If not create it. If mkdir fail, raise FileExistsError error.
        :return: NoReturn
        """
        if os.path.exists(f"{self._file_path}"):
            return True
        else:
            self._create_dir()
            return False


class Updater(object):
    def __init__(self, path: str, trackers: str):
        self._path = path
        self._trackers = trackers

    def start(self) -> None:
        check = False
        with open(self._path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in lines:
                if re.search(r"bt-Tracker=.*", line):
                    line = line.replace(line, f"bt-Tracker={self._trackers}\n")
                    file.write(line)
                    check = True
                else:
                    file.write(line)
            else:
                if check:
                    return
                else:
                    file.write(f"bt-Tracker={self._trackers}\n")
