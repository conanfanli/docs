#!/usr/bin/env python
from jinja2 import Template

def render():

    with open(expanduser('~/rice/ansible/roles/common/files/react-container.template.tsx')) as f:
        template = Template(f.read())

    return template.render()

if __name__ == '__main__':
    print(render())

