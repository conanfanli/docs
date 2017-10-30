#!/usr/bin/env python3.6
import sys
import logging
import logging.config
import argparse
from commandos.printer import print_red, Color
from commandos.base import Commando


LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s: %(name)s %(message)s'
        },
        # You may need to specify the timezone here.
        # For example: %(asctime)s CST [%(levelname)s] %(name)s:
        # %(message)s
        'standard': {
            'format': '[%(asctime)s %(levelname)s/%(process)d] [%(module)s]: %(message)s'
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },

    'loggers': {
        'cooker': {
            'handlers': ['console'],
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'propagate': False,
        },
    },

    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


targets = {cmd.name: cmd for cmd in Commando.get_all()}


def help_target(target):
    for cmd in targets.values():
        if not target or target == cmd.name:
            print_red(cmd, end=': ')
            print(cmd.doc)


def run_target(target):
    targets[target].execute()



def main():
    print(sys.argv)
    try:
        subcommand = sys.argv[1]
    except IndexError:
        subcommand = 'help'

    if subcommand == 'help':
        help_target(len(sys.argv) >= 2 and sys.argv[2] or None)

    return
    parser = argparse.ArgumentParser(
        description='Show all the rice commands.'
    )

    parser.add_argument(
        'action',
        type=str,
        nargs='?',
        default='help',
        choices=['help', 'run'],
        help='Action to perform',
    )
    parser.add_argument(
        'target',
        type=str,
        nargs='?',
        help='Target',
    )
    parser.add_argument(
        'targs',
        type=str,
        nargs='*',
        help='target args',
    )
    parser.add_argument(
        '--no-color',
        dest='no_color',
        action='store_true',
        default=False,
        help='Disable colors when printing',
    )

    args = parser.parse_args()

    action = args.action

    if args.no_color:
        Color.disable = True

    if action == 'help':
        help_target(args.target)
    elif action == 'run':
        run_target(args.target)


if __name__ == "__main__":
    print(sys.argv)
    main()
