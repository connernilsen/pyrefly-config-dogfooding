import click

from int_handler import ints
from name_handler.names import do_stuff_with_name


@click.command
@click.option("--count", default=1, help="A number")
@click.option("--name", prompt="Some name")
def get_args(count: int, name: str) -> tuple[int, str]:
    return count, name


def main():
    args = get_args()
    ints.do_stuff_with_int(args[0])
    do_stuff_with_name(args[1])


if __name__ == "__main__":
    main()
