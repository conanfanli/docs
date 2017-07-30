import re
import copy
from pprint import pformat
import subprocess
import logging
from command_streamer import stream_command


logger = logging.getLogger(__name__)


class Deferred:
    pass



class EvalCommand(Deferred):

    def __init__(self, command: str, print_to_console=True) -> None:
        self.command = command
        self.result = None
        self._output = []
        self.print_to_console = print_to_console

    def on_stdout(self, output):
        output = output.decode('utf-8')
        self._output.append(output)
        if self.print_to_console:
            print(output)


    def to_dict(self):
        return {
            'command': self.command,
            'result': self.result
        }

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self.command))

    def evaluate(self):
        try:
            rc = stream_command(self.command, lambda x: self.on_stdout(x))
            self.result = True
        except subprocess.CalledProcessError:
            self.result = False
            return False


class BranchStatus(EvalCommand):
    def __init__(self) -> None:
        command = ['bash', '-c', 'git remote update && git status -uno']
        super().__init__(command)

    def get_status(self):
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




state_definition = {
    "branchIsUpdated": BranchStatus()
}

class State:

    def __init__(self, data: dict):
        self._data = copy.deepcopy(data)
        self._field_names = sorted(data.keys())

    def evaluate(self):
        for attr in self._field_names:
            value = self._data[attr]
            if isinstance(value, Deferred):
                value.evaluate()

    def to_dict(self):
        rv = dict(self._data)
        for key in self._field_names:
            value = self._data[key]
            if hasattr(value, 'to_dict'):
                rv[key] = value.to_dict()

        return rv

    def __str__(self):
        return pformat(dict(initial_state.to_dict()))


initial_state = State(state_definition)
