import click.argument
import sys


if sys.platform != "abcd":
    my_str: int = "HELLO!"


def do_stuff_with_name(name: str) -> None:
    print(name)
