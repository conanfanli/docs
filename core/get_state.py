import subprocess
import logging
from command_streamer import stream_command


logger = logging.getLogger(__name__)

def on_stdout(s):
    logger.info(s.decode('utf-8'))

class EvalCommand:

    def __init__(self, command: str, shell: bool = False) -> None:
        self.command = command
        # self.shell = shell

    def to_dict(self):
        return {
            'command': self.command,
            'result': self.result
        }

    def evaluate(self):
        try:
            output = subprocess.check_output(self.command)
            # rc = stream_command(self.command, on_stdout)
            # print('return code', rc)
            logger.info(output)
            self.result = True
        except subprocess.CalledProcessError:
            self.result = False
            return False


state = {
    "branchIsUpdated": EvalCommand(
        command=['bash', '-c',
                 'git remote update && git status -uno | grep up-to-date']
    )
}


def evaluate(state):
    state["branchIsUpdated"].evaluate()


def serialize(state):
    for key in state:
        value = state[key]
        if hasattr(value, 'to_dict'):
            state[key] = value.to_dict()

    return state

