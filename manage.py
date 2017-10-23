#!/usr/bin/env python3.6
import argparse
from commando.printer import print_red, Color
from commando.models import Commando


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Show all the rice commands.'
    )

    parser.add_argument(
        '--no-color',
        dest='no_color',
        action='store_true',
        default=False,
        help='Disable colors when printing',
    )

    args = parser.parse_args()
    if args.no_color:
        Color.disable = True

    for cmd in Commando.get_all():
        print_red(cmd, end=': ')
        print(cmd.doc)


if __name__ == '__main__':
    main()
