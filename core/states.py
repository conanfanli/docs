import re
import copy
import subprocess
from pprint import pformat
import logging
from typing import List
from command_streamer import stream_command

logger = logging.getLogger(__name__)


class Deferred:
    pass


class EvalCommand(Deferred):

    def __init__(self, command: List[str], print_to_console=True) -> None:
        self.command = command
        self.is_executed = False
        self._output: List = []
        self.print_to_console = print_to_console

    def on_stdout(self, output):
        output = output.decode('utf-8')
        self._output.append(output)
        if self.print_to_console:
            print(output)

    def to_dict(self):
        return {
            'command': self.command,
            'is_executed': self.is_executed
        }

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self.command))

    def evaluate(self):
        stream_command(self.command, lambda x: self.on_stdout(x))
        self.is_executed = True


class BranchStatus(EvalCommand):
    def __init__(self) -> None:
        command = ['bash', '-c', 'git remote update && git status -uno']
        super().__init__(command)

    def get_status(self):
        if not self.is_executed:
            return None

        output = ''.join(self._output)
        if re.search(r'Changes not staged', output):
            return 'AHEAD'
        if re.search(r'up-to-date', output):
            return 'UP-TO-DATE'

        return 'OUT-OF-SYNC'

    def to_dict(self):
        rv = super().to_dict()
        rv['status'] = self.get_status()
        return rv


class Package(EvalCommand):

    def __init__(self, name):
        self.name = name
        command = ['vim', '--version']
        super().__init__(command, print_to_console=False)

    def get_version(self):
        if not self.is_executed:
            return None

        first_line = self._output[0]
        match = re.search(r'Vi IMproved (\d\.\d+) \(', first_line)
        return match.groups(0)

    def evaluate(self):
        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        super().evaluate()

    def to_dict(self):
        rv = super().to_dict()
        rv['version'] = self.get_version()
        return rv


def evaluate_dict(d):
    for key in d:
        value = d[key]
        if isinstance(value, Deferred):
            value.evaluate()
        elif isinstance(value, dict):
            evaluate_dict(value)


class State(Deferred):

    def __init__(self, data: dict) -> None:
        self._data = copy.deepcopy(data)
        self._field_names = sorted(data.keys())

        for key in self._data:
            if isinstance(self._data[key], dict):
                self._data[key] = State(self._data[key])

    def __getitem__(self, key):
        return self._data[key]

    def evaluate(self):
        return evaluate_dict(self._data)
        # for attr in self._field_names:
        #     value = self._data[attr]
        #     if isinstance(value, Deferred):
        #         value.evaluate()

    def to_dict(self):
        rv = dict(self._data)
        for key in self._field_names:
            value = self._data[key]
            if hasattr(value, 'to_dict'):
                rv[key] = value.to_dict()

        return rv

    def __str__(self):
        return pformat(dict(initial_state.to_dict()))


state_definition = {
    'branchIsUpdated': BranchStatus(),
    'weapons': {
        'vim': Package('vim')
    }
}

initial_state = State(state_definition)
