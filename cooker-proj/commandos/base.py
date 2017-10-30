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


class BaseCommando:
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
        if not hasattr(module, 'Commando'):
            return None

        return module

    @classmethod
    def from_alias(cls, name, doc) -> 'BaseCommando':
        return BaseCommando(
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
    def get_all(cls) -> typing.List['BaseCommando']:
        modules = (
            BaseCommando.get_module(f) for f in glob.glob('{}/*.*'.format(COMMANDOS_DIR))
        )

        scripts: typing.List[BaseCommando] = [
            getattr(mod, 'Commando')(mod) for mod in modules if mod
        ]
        aliases = [
            BaseCommando.from_alias(name=alias, doc=doc) for alias, doc in
            get_all_aliases().items()
        ]

        assert scripts, 'Empty rice bin?'
        return scripts + aliases

    def run_from_argv(self, argv):
        raise NotImplementedError(f'run_from_argv is not implemented for {self}')


class PyModule(BaseCommando):
    parser: typing.ClassVar = None

    def __init__(self, module):
        super().__init__(
            cmd_type='PyModule',
            module=module,
            name=module.__name__,
            doc=module.__doc__,
            filepath=module.__file__
        )

    def run_from_argv(self, argv):
        return self.module.run_from_argv(argv)

    def print_help(self):
        if self.parser:
            self.parser.print_help()
        elif self.doc:
            print(self.doc)
        else:
            raise NotImplementedError('Must implement print help')
