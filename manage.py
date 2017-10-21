#!/usr/bin/env python3.6
import argparse
import glob
from commando.get_all_aliases import get_all_aliases
from commando.printer import print_red, Color
from commando.models import Script, Alias, RICE_BIN


def get_scripts():
    generator = (
        f for f in glob.glob('{}/*.*'.format(RICE_BIN))
    )

    rice_bin_scripts = [Script(script) for script in generator
                        if not script.startswith('__')]

    assert rice_bin_scripts, 'Empty rice bin?'
    return rice_bin_scripts


def main():
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

    commands = [
        Alias(alias, description) for alias, description
        in get_all_aliases().items()] + get_scripts()

    for cmd in commands:
        print_red(cmd, end=': ')
        print(cmd.description)


if __name__ == '__main__':
    main()
