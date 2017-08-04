import re
from os.path import expanduser

ALIAS_REGEX = re.compile(r'^alias ([\w\.]+)\=.+#desc#: ?(.+)$')
FUNCTION_REGEX = re.compile(r'^(\w+) \(\) {.+#desc#: ?(.+)$')

with open(expanduser('~/.rice.bash')) as f:
    for line in f:
        match = ALIAS_REGEX.match(line)
        if match:
            print(match.groups())
            continue

        match = FUNCTION_REGEX.match(line)
        if match:
            print(match.groups())
            continue
