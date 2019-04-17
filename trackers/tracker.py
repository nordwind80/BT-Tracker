#
# Author: Nordwind
# E-Mail: eaglewings.yi@gmail.com
# Date: 2018-12-18 20:11:43

import re
import argparse

from .menu import Menu
from .spider import SpiderFactory

__version__ = "0.1.2"


class Tracker(object):
    """
        Update bt-trackers of aria2.
    """

    def __init__(self):
        self._aria2_path = "aria2.conf"

    def update(self, check_find: bool = False) -> None:
        with open("aria2.conf", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in lines:
                if re.search(r"bt-tracker=.*", line):
                    line = line.replace(line, f"{self._trackers}\n")
                    file.write(line)
                    check_find = True
                else:
                    file.write(line)
            else:
                if check_find:
                    return
                else:
                    file.write(f"{self._trackers}\n")

    def _load_data(self):

        spider = SpiderFactory()
        update_info = spider.create("update_info")
        self._update_time, self._options = update_info.get("update_info")


    def start(self) -> None:
        menu = Menu(
            f"\nBT-Trackers update tool by Nordwind. version: {__version__}\n\n"
            f"Select tracker. (j/down k/up enter/select q/exit):",
            self.__options)
        select = menu.show()
        print(
            f"You select \033[32;1m{self.__options[select]} \033[0mmodel.\nUpdate start."
        )
        self._model = self._select.get(list(self._select.keys())[select])

        #if model:
        #    self._model = self._select.get(model)
        #    print(f"Select {model} model. Update start.")
        self._getTrackers()
        self._replace()
        print(
            f"\nBT-Trackers update \033[32;1mcompleted\033[0m, Total: \033[32;1m{self.total}\033[0m trackers.\nexit!"
        )


def arg() -> None:
    parser = argparse.ArgumentParser(
        description="BT-Trackers list update tool of Aria2 by Nordwind.")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=
        f"BT-Trackers list update tool by Nordwind. version: {__version__}")
    parser.add_argument(
        "--mode",
        dest="mode",
        action="store",
        choices={
            'best_ip', 'best_domain', 'all_ip', 'all_domain', 'all_udp',
            'all_http', 'all_https', 'all_ws'
        },
        default="all_domain",
        help=
        "Select the update mode. ep:[best_ip, best_domain, all_ip, all_domain, all_udp, all_http, all_https, all_ws]"
    )
    arge = parser.parse_args()

    if arge.mode:
        tracker = Tracker()
        tracker.update(arge.mode)


if __name__ == "__main__":
    arg()
