import types
import typing
import os
from os.path import pardir, join, abspath
import importlib
import glob

from .get_all_aliases import get_all_aliases


def parent(path):
    """Return parent dir."""
    return abspath(join(path, pardir))


COMMANDOS_DIR = abspath(parent(__file__))


class Commando:
    def __init__(self, cmd_type, name, doc, filepath, module=None):
        self.cmd_type = cmd_type
        self.name = name
        self.doc = doc
        self.filepath = filepath
        self.module = module


    @classmethod
    def get_module(cls, full_path) -> types.ModuleType:
        relpath = cls.relpath(full_path)
        if not relpath.endswith('.py'):
            return None

        module_name = relpath.split('.py')[0]
        module = importlib.import_module(f'commandos.{module_name}')
        if not hasattr(module, 'main'):
            return None

        return module

    @classmethod
    def from_alias(cls, name, doc) -> 'Commando':
        return Commando(
            cmd_type='alias',
            name=name,
            doc=doc,
            filepath=None,
        )

    def __str__(self):
        return self.name

    @staticmethod
    def relpath(full_path):
        return os.path.relpath(full_path, COMMANDOS_DIR)

    @classmethod
    def get_all(cls) -> typing.List['Commando']:
        modules = (
            Commando.get_module(f) for f in glob.glob('{}/*.*'.format(COMMANDOS_DIR))
        )

        scripts: typing.List[Commando] = [
            PyModule(mod) for mod in modules if mod
        ]
        aliases = [
            Commando.from_alias(name=alias, doc=doc) for alias, doc in
            get_all_aliases().items()
        ]

        assert scripts, 'Empty rice bin?'
        return scripts + aliases


class PyModule(Commando):

    def __init__(self, module):
        super().__init__(
            cmd_type='PyModule',
            module=module,
            name=module.__name__,
            doc=module.__doc__,
            filepath=module.__file__
        )

    def execute(self):
        self.module.main()
