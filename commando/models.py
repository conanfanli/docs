import typing
import os
from os.path import pardir, join, abspath
import glob

from .get_all_aliases import get_all_aliases


def parent(path):
    """Return parent dir."""
    return abspath(join(path, pardir))


RICE_BASE = parent(parent(__file__))
RICE_BIN = join(RICE_BASE, 'commando')


class Commando:
    def __init__(self, cmd_type, name, doc, filepath):
        self.cmd_type = cmd_type
        self.name = name
        self.doc = doc
        self.filepath = filepath

    @classmethod
    def from_script(cls, filepath: str):
        relpath = cls.relpath(filepath)
        return Commando(
            cmd_type='script',
            name=relpath,
            doc=None,
            filepath=filepath
        )

    @classmethod
    def from_alias(cls, name, doc):
        return Commando(
            cmd_type='alias',
            name=name,
            doc=doc,
            filepath=None,
        )

    def __str__(self):
        return self.name

    @staticmethod
    def relpath(absolute_patth):
        return os.path.relpath(absolute_patth, RICE_BIN)

    @classmethod
    def get_all(cls) -> typing.List['Commando']:
        generator = (
            f for f in glob.glob('{}/*.*'.format(RICE_BIN))
        )

        scripts = [
            Commando.from_script(script) for script in generator
            if not script.startswith('__')
        ]
        aliases = [
            Commando.from_alias(name=alias, doc=doc) for alias, doc in
            get_all_aliases().items()
        ]

        assert scripts, 'Empty rice bin?'
        return scripts + aliases
