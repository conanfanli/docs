import subprocess
from marshmallow import Schema, fields, pprint


class EvalCommand:

    def __init__(self, command: str) -> None:
        self.command = command

    def to_dict(self):
        return {
            'command': self.command,
            'result': self.result
        }

    def evaluate(self):
        try:
            subprocess.check_output(self.command)
            self.result = True
        except subprocess.CalledProcessError:
            self.result = False
            return False


state = {
    "branchIsUpdated": EvalCommand(command='false')
}


state["branchIsUpdated"].evaluate()


def serialize(state):
    for key in state:
        value = state[key]
        if hasattr(value, 'to_dict'):
            state[key] = value.to_dict()

    return state


print(serialize(state))
