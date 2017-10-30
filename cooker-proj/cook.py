#!/usr/bin/env python3.6
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


def main():
    parser = argparse.ArgumentParser(
        description='Show all the rice commands.'
    )

    parser.add_argument(
        'action',
        type=str,
        nargs=1,
        help='Action to perform',
    )
    parser.add_argument(
        '--no-color',
        dest='no_color',
        action='store_true',
        default=False,
        help='Disable colors when printing',
    )

    args = parser.parse_args()

    action = args.action[0]

    if args.no_color:
        Color.disable = True

    for cmd in Commando.get_all():
        if action == cmd.name:
            return cmd.execute()

        print_red(cmd, end=': ')
        print(cmd.doc)


if __name__ == "__main__":
    main()
