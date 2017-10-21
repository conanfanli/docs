#!/usr/bin/env python3
import argparse
import glob
from os.path import pardir, join, abspath, relpath
from commando.get_all_aliases import get_all_aliases
from commando.printer import print_red, Color


def parent(path):
    """Return parent dir."""
    return abspath(join(path, pardir))


RICE_BASE = parent(__file__)
RICE_BIN = join(RICE_BASE, 'commando')


def get_scripts():
    generator = (
        relpath(f, RICE_BIN) for f in glob.glob('{}/*.*'.format(RICE_BIN))
    )

    rice_bin_scripts = [script for script in generator
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

    commands = get_all_aliases()
    commands.update({
        script: '' for script in get_scripts()
    })

    for name, doc in sorted(commands.items()):
        print_red(name, end=': ')
        print(doc)


if __name__ == '__main__':
    main()
