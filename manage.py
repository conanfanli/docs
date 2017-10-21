#!/usr/bin/env python3
import argparse
import glob
from os.path import pardir, join, abspath
from commando.get_all_aliases import get_all_aliases
from commando.printer import print_red


def parent(path):
    """Return parent dir."""
    return abspath(join(path, pardir))


RICE_BASE = parent(__file__)
RICE_BIN = join(RICE_BASE, 'commando')

print_red(RICE_BIN)

parser = argparse.ArgumentParser(
    description='Show all the rice commands.'
)

rice_bin_commands = glob.glob('{}/*'.format(RICE_BIN))


# parser.add_argument(
#     'integers',
#     metavar='N',
#     type=int,
#     nargs='+',
#     help='an integer for the accumulator',
# )
# parser.add_argument(
#     '--sum',
#     dest='accumulate',
#     action='store_const',
#     const=sum, default=max,
#     help='sum the integers (default: find the max)',
# )


def main():
    parser.parse_args()
    print_red('aliases:', get_all_aliases())
    for cmd in rice_bin_commands:
        print(cmd)


if __name__ == '__main__':
    main()
