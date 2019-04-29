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

from functools import wraps
from typing import List, Union, NoReturn

from .event import status


# type hot
MenuOptions = List[str]
UserInput = Union[str, bytes]


UP = "k"
DOWN = "j"
EXIT = "q"
CTR_C = "\x03"
DIRECTION = "\x1b"
ENTER = "\r"


def pos_check():
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self._position %= self._total
            return

        return wrapper

    return decorator


class Menu(object):
    def __init__(self, title: str, options: MenuOptions):
        self._title = title
        self._options = options
        self._position = 0
        self._total: int = len(options)

    @staticmethod
    def _cli_input():
        user_input = sys.stdin.read(1)
        if user_input == DIRECTION:
            user_input += sys.stdin.read(2)
        return user_input

    @pos_check()
    def _move_up(self):
        self._position -= 1

    @pos_check()
    def _move_down(self):
        self._position += 1

    def _build_menu(self):
        index = 0
        s = ""
        while index < self._total:
            if index == self._position:
                temp = f"\033[32;1m \u2712  \u25CF {self._options[index]} \033[0m\n"
            else:
                temp = f"    \u25CB {self._options[index]} \033[0m\n"
            index += 1
            s += temp
        s += "\n"
        self._draw(s)

    def _draw(self, string: str):
        sys.stdout.write(string)
        sys.stdout.flush()

    def _status(self, state: bool = True):
        if state:
            self._draw(f"{self._title}\n")
        if not state:
            self._clear()
        self._build_menu()

    def _clear(self):
        self._draw(f"\033[{len(self._options) + 1}A\033[K")

    def show(self):
        self._status()

        while True:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                key = self._cli_input()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            if key == CTR_C or key == "" or key == EXIT:
                break
            elif key == ENTER:
                print(
                    f"  You chosen \033[32;1m{self._options[self._position]}\033[0m.\n  {'-'*55}"
                )
                return self._position
            elif key == UP:
                self._move_up()
            elif key == DOWN:
                self._move_down()

            self._status(False)


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
