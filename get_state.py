import subprocess
from marshmallow import Schema, fields, pprint


class EvalCommand:

    def __init__(self, command: str, shell: bool = False) -> None:
        self.command = command
        self.shell = shell

    def to_dict(self):
        return {
            'command': self.command,
            'result': self.result
        }

    def evaluate(self):
        try:
            output = subprocess.check_output(self.command, shell=self.shell)
            self.result = True
        except subprocess.CalledProcessError:
            self.result = False
            return False


state = {
    "branchIsUpdated": EvalCommand(
        command='git remote update && git status -uno | grep up-to-date',
        shell=True
    )
}


state["branchIsUpdated"].evaluate()


def serialize(state):
    for key in state:
        value = state[key]
        if hasattr(value, 'to_dict'):
            state[key] = value.to_dict()

    return state


print(serialize(state))
