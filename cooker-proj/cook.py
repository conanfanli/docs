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


def run_subcommand(subcommand, subargs):
    targets[subcommand].run_from_argv(subargs)


def main():
    parser = argparse.ArgumentParser(
        description='Start cooking'
    )

    parser.add_argument(
        'subcommand',
        type=str,
        nargs='?',
        choices=['help'] + list(targets.keys()),
        default='help',
        help='Subcommand',
    )
    parser.add_argument(
        '--no-color',
        dest='no_color',
        action='store_true',
        default=False,
        help='Disable colors when printing',
    )

    options, subargs = parser.parse_known_args()
    if options.no_color:
        Color.disable = True

    if options.subcommand == 'help':
        return help_target(len(sys.argv) >= 2 and sys.argv[2] or None)

    run_subcommand(options.subcommand, subargs)


if __name__ == "__main__":
    main()
