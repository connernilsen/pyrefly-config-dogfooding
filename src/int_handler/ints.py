import sys

from click import command


if sys.version_info == (3, 14):
    my_int: int = 1
else:
    something_else: str = 1


def do_stuff_with_int(num: int) -> None:
    print(num)

    return my_int
