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

parser = argparse.ArgumentParser(
    description='Show all the rice commands.'
)

rice_bin_scripts = glob.glob('{}/*.*'.format(RICE_BIN))
assert rice_bin_scripts, 'Empty rice bin?'

parser.add_argument(
    '--no-color',
    dest='no_color',
    action='store_true',
    default=False,
    help='Disable colors when printing',
)


def main():
    args = parser.parse_args()
    if args.no_color:
        Color.disable = True

    commands = get_all_aliases()
    commands.update({
        relpath(script, RICE_BIN): '' for script in rice_bin_scripts
    })

    for name, doc in sorted(commands.items()):
        print_red(name, end=': ')
        print(doc)


if __name__ == '__main__':
    main()
