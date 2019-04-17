import sys
import time
import threading
from functools import wraps

from menu import Menu
from update import Filer


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwage):
        if cls not in instances:
            instances[cls] = cls(*args, **kwage)
        return instances[cls]

    return getinstance


@singleton
class Event(object):
    def __init__(self):
        self._finish = False

    @property
    def state(self):
        return self._finish

    @state.setter
    def state(self, new_state):
        if isinstance(new_state, bool) and new_state is True:
            self._finish = new_state
            time.sleep(0.1)
            self._finish = False


def callback():
    event = Event()
    time.sleep(10)
    event.state = True


def spin():
    while True:
        yield from '⠹⠸⠼⠴⠦⠧⠇⠏⠋⠙'


def spin_progress():

    sp = spin()
    s = Event()
    file = Filer()
    print(f"{file.check_dirctory()}\n")
    while not s.state:
        sys.stdout.write(f"{next(sp)} Loading remote update data...")
        sys.stdout.flush()
        sys.stdout.write("\b" * 50)
        time.sleep(0.08)
    print(
        f"\033[32;1m\u2713 \033[0mUpdate remote data completed.\n\n"
        f"-- Updated: \033[32;1m2019-04-14\033[0m\n{'-'*30}")

    options = [
        'trackers_best (20 trackers)', 'trackers_best_ip (20 trackers)',
        'trackers_all (80 trackers)', 'trackers_all_ip (80 trackers)',
        'trackers_all_udp (43 trackers)', 'trackers_all_http (28 trackers)',
        'trackers_all_https (7 trackers)', 'trackers_all_ws (2 trackers)'
    ]
    m = Menu("Select trackers data options. (j/down k/up enter/select q/exit):\n", options)
    pos = m.show()
    print(f"You select \033[32;1m{options[pos]} \033[0mmodel.")


if __name__ == "__main__":
    print(
        f"BT-Trackers update tool by Nordwind. version: 0.1.2\n\nStart load remote data.\n{'-'*30}"
    )
    t1 = threading.Thread(target = spin_progress)
    t2 = threading.Thread(target = callback)

    t1.start()
    t2.start()

