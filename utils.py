# This file contains various small helper function that hide some problems from you.
# You can ignore it.

import webbrowser
from threading import Timer
from functools import partial
import sys


# Based on https://stackoverflow.com/a/54235461/5769940
def open_browser_with_delay(url: str, delay: int = 0):
    def open_browser_now(url: str):
        webbrowser.open_new(url)

    Timer(delay, partial(open_browser_now, url=url)).start()


def modify_int_max_str_digits(max_number_of_digits: int = 0, exception_on_failure: bool = False):
    # int <-> str conversion for large numbers. Vulnerable to Denial of Service.
    # Default is 4300 digits: https://stackoverflow.com/a/73693178
    try:
        sys.set_int_max_str_digits(max_number_of_digits)
    except AttributeError:
        # This function exists only from 3.11 onwards
        # https://docs.python.org/3/library/sys.html#sys.get_int_max_str_digits
        if exception_on_failure:
            raise
