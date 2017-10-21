#!/usr/bin/env python3
import re
from os.path import expanduser

ALIAS_REGEX = re.compile(r'^alias ([\w\.]+)\=.+# ?(.+)$')
FUNCTION_REGEX = re.compile(r'^(\w+) ?\(\) {.+# ?(.+)$')


def get_all_aliases() -> dict:
    aliases = {}
    with open(expanduser('~/.rice.bash')) as f:
        for line in f:
            for regex in (ALIAS_REGEX, FUNCTION_REGEX):
                match = regex.match(line)
                if match:
                    name, doc = match.groups()
                    aliases[name] = doc
                    continue

    return aliases


if __name__ == '__main__':
    for name, value in get_all_aliases().items():
        print('{}: {}'.format(name, value))
