#
# Author: Nordwind
# E-Mail: bm9yZHdpbmQubWVAZ21haWwuY29t
# Created  Time: 22:10:27 08-04-2019
# Last Modified:
#        - File Name: menu.py
#        - Command line interface menu.


import sys
import tty
import termios
import time

from typing import List, Union, NoReturn

from event import event


# type hot
MenuOptions = List[str]
UserInput = Union[str, bytes]


UP = "k"
DOWN = "j"
EXIT = "q"
CTR_C = "\x03"
DIRECTION = "\x1b"
ENTER = "\r"


class Menu(object):

    """Docstring for Menu. """

    def __init__(self, title: str, options: MenuOptions):
        """TODO: to be defined1.

        :TODO: TODO
        """
        self._title = title
        self._options = options
        self._position = 0

    def _show_choose(self) -> NoReturn:
        """TODO: Docstring for _show_choos.

        :arg1: TODO
        :returns: TODO
        """
        index = 0
        s = ""
        while index < len(self._options):
            if index == self._position:
                temp = f"\033[32;1m \u2794  \u25CF {self._options[index]} \u2713"
            else:
                temp = f"    \u25CB {self._options[index]} \033[0m"
            temp += f" \033[0m\n"
            # temp += str(self._options[index]) + '\033[0m\n'
            index += 1
            s += temp
        s += "\n"
        sys.stdout.write(s)
        sys.stdout.flush()

    def _set_menu(self, state: bool = True) -> NoReturn:
        """TODO: Docstring for _set_menu.

        :arg1: TODO
        :returns: TODO

        """
        if state:
            sys.stdout.write(self._title + "\n")
            sys.stdout.flush()
        if not state:
            self._clear_choose()
        self._show_choose()

    def show(self) -> int:
        """TODO: Docstring for _show_menu.

        :returns: TODO
        """

        self._set_menu()

        while True:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                key = self._cli_input()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            if key == CTR_C or key == "":
                break
            elif key == ENTER:
                return self._position
            elif key == UP:
                self._position -= 1
            elif key == DOWN:
                self._position += 1

            if self._position < 0:
                self._position = len(self._options) - 1
            elif self._position >= len(self._options):
                self._position = 0

            self._set_menu(False)

    def _clear_choose(self) -> NoReturn:
        """TODO: Docstring for _clear_choos.

        :arg1: TODO
        :returns: TODO
        """
        sys.stdout.write(f"\033[{len(self._options) + 1}A\033[K")
        sys.stdin.flush()

    def _cli_input(self) -> UserInput:
        """ Get command line interface input.

        :returns: input: str
        """
        user_input = sys.stdin.read(1)
        if user_input == DIRECTION:
            user_input += sys.stdin.read(2)
        return user_input


def spin_progress(title: str) -> NoReturn:
    sp = spin()
    while not event.state:
        sys.stdout.write(f"{next(sp)} {title}")
        sys.stdout.flush()
        sys.stdout.write("\b" * 50)
        time.sleep(0.08)


def spin():
    while True:
        yield from "⠹⠸⠼⠴⠦⠧⠇⠏⠋⠙"


if __name__ == "__main__":
    menu_options = [
        "trackers_best (20 trackers)",
        "trackers_best_ip (20 trackers)",
        "trackers_all (80 trackers)",
        "trackers_all_ip (80 trackers)",
        "trackers_all_udp (43 trackers)",
        "trackers_all_http (28 trackers)",
        "trackers_all_https (7 trackers)",
        "trackers_all_ws (2 trackers)",
    ]
    menu = Menu("Select tracker. j/down k/up q/exit:", menu_options)
    pos = menu.show()
    print(f"You select \033[32;1m{menu_options[pos]} \033[0mmodel.")
