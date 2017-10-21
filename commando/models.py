import os
from os.path import pardir, join, abspath


def parent(path):
    """Return parent dir."""
    return abspath(join(path, pardir))


RICE_BASE = parent(parent(__file__))
RICE_BIN = join(RICE_BASE, 'commando')


class Script:

    def __init__(self, filepath):
        self.filepath = filepath

        if filepath.endswith('.py'):
            self.filetype = 'python'
        else:
            self.filetype = 'shell'

    @property
    def description(self):
        return ''

    @property
    def relpath(self):
        return os.path.relpath(self.filepath, RICE_BIN)

    def __str__(self):
        return self.relpath


class Alias:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name
