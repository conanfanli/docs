#!/usr/bin/env python
import re
from os.path import expanduser

ALIAS_REGEX = re.compile(r'^alias ([\w\.]+)\=.+#desc#: ?(.+)$')
FUNCTION_REGEX = re.compile(r'^(\w+) \(\) {.+#desc#: ?(.+)$')

with open(expanduser('~/.rice.bash')) as f:
    for line in f:
        for regex in (ALIAS_REGEX, FUNCTION_REGEX):
            match = regex.match(line)
            if match:
                print(': '.join(match.groups()))
                continue
