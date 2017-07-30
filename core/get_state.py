from collections import namedtuple
from pprint import pprint
import subprocess
import logging
from command_streamer import stream_command


logger = logging.getLogger(__name__)


class EvalCommand:

    def __init__(self, command: str) -> None:
        self.command = command
        self.return_code = None

    def to_dict(self):
        return {
            'command': self.command,
            'return_code': self.return_code
        }

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self.command))

    def evaluate(self):
        try:
            rc = stream_command(self.command, on_stdout)
            self.return_code = True
        except subprocess.CalledProcessError:
            self.return_code = False
            return False



def on_stdout(s):
    logger.info(s.decode('utf-8'))


state_definition = {
    "branchIsUpdated": EvalCommand(
        command=['bash', '-c',
                 'git remote update && git status -uno | grep up-to-date']
    )
}

fields = sorted(state_definition.keys())


AbstractState = namedtuple('AbstractState', fields)


class State(AbstractState):

    def evaluate(self):
        pass

    def to_dict(self):
        rv = self._asdict()
        for key in self._fields:
            value = getattr(self, key)
            if hasattr(value, 'to_dict'):
                rv[key] = value.to_dict()

        return rv


initial_state = State(**state_definition)


def evaluate(state):
    state["branchIsUpdated"].evaluate()


pprint(dict(initial_state.to_dict()))
