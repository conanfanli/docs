#!/usr/bin/env python3
"""
Create a react container.
"""
# Forcing python3 because jinja2 is likely installed with python3
# along with ansible
import sys
from os.path import expanduser

from jinja2 import Template


TEMPLATE_PATH = '~/rice/ansible/roles/common/files/react-container.template.tsx'


def render(container_name: str) -> str:
    with open(expanduser(TEMPLATE_PATH)) as f:
        template = Template(f.read())

    return template.render(container_name=container_name)


def main():
    if len(sys.argv) != 2:
        sys.stderr.write('Provide one and only 1 container name.\n')
        sys.exit(1)

    container_name = sys.argv[1]
    print(render(container_name))


if __name__ == '__main__':
    main()
