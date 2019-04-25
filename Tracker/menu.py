#!/usr/bin/env python3
#
# Author: eaglewings
# E-Mail: ZWFnbGV3aW5ncy55aUBnbWFpbC5jb20=
# Created  Time: 22:10:27 08-04-2019
# Last Modified:
#        - Project  : BT Trackers Updater
#        - File Name: menu.py
#        - Command line interface menu.


import sys
import tty
import termios
import time
import threading

from typing import List, Union, NoReturn

from Tracker.event import status


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
                temp = f"\033[32;1m \u2712  \u25CF {self._options[index]}"
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


class ProgressThread(threading.Thread):
    """
        继承 threading.Thread 类 复写 self.run 方法。
        self.get_result 返回线程的值
    """

    def __init__(self, target, args=()):
        super(ProgressThread, self).__init__()
        self._result = None
        self._target = target
        self._args = args

    def run(self):
        self._result = self._target(*self._args)

    @property
    def get_result(self):
        return self._result


def progress(target, title, complete, arg=None):
    t1 = ProgressThread(target=target, args=arg)
    t2 = ProgressThread(target=spin_progress, args=(title,))
    threads = [t1, t2]
    for i in threads:
        i.setDaemon(True)
        i.start()
    for i in threads:
        i.join()

    print(f"\033[32;1m  \u2713 {complete}\033[0m          ")

    if t1.get_result:
        return t1.get_result
    else:
        return None


def spin_progress(title: str) -> NoReturn:
    index = 0
    while True:
        print(f"  {'⠹⠸⠼⠴⠦⠧⠇⠏⠋⠙'[index % 10]} {title}", end="\r", flush=True)
        time.sleep(0.07)
        index += 1
        if status.finished:
            break
