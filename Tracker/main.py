#!/usr/bin/env python3
#
# Author: eaglewings
# E-Mail: ZWFnbGV3aW5ncy55aUBnbWFpbC5jb20=
# Created  Time: 2019-04-23 17:19
# Last Modified:
# Description:
#        - Project:   BT Trackers Updater
#        - File Name: main.py
#        - main

import re
import argparse

from Tracker.update import Filer, Updater
from Tracker.menu import progress, Menu
from Tracker.spider import Spiders
from Tracker.__version__ import __version__ as version


def start() -> None:
    parser = argparse.ArgumentParser(
        description="BT Trackers Updater of Aria2 by Eaglewings."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"BT Trackers Updater of Aria2 by Eaglewings. Version: {version}",
    )
    parser.parse_args()

    print(
        f"  BT Trackers Updater of Aria2 by Nordwind. \n\n  Version: {version}\n\n  - Initialization:\n  {'-'*55}"
    )
    filer = Filer()
    info = Spiders.create("update_info")

    if filer.check_dirctory():
        print(f"\033[32;1m  \u2713 Found Aria2 directory.\033[0m")
    else:
        print(
            f"\033[32;1m  \u2713 Can't find directory of Aria2, Create a new directory.\033[0m"
        )

    update_info = progress(
        info.get,
        "Loading remote update data.",
        "Load remote update data completed.",
        "",
    )
    print(f"  - {update_info[0][0]}\n  {'-'*55}")

    menu = Menu(
        f"  - Sclect the item you want update. [J/DOWN K/UP ENTER/Select Q/EXIT]:\n",
        update_info[1],
    )
    select = menu.show()
    print(f"  You chosen \033[32;1m{update_info[1][select]} \033[0mmodel.\n  {'-'*55}")

    option = re.findall(r"^trackers_(.+) \(", update_info[1][select])[0]
    tracker = Spiders.create(option)

    trackers = progress(tracker.get, "Start update.", "Trackers update completed.", "")

    update = Updater(filer.get_path, trackers[0])
    update.start()
    print(
        f"  {'-'*55}\n  Updated \033[32;1m{trackers[1]}\033[0m tracker in \033[32;1m{filer.get_path}\033[0m.\n\n  "
        f"Updater exit! "
    )


if __name__ == "__main__":
    start()
