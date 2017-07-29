import subprocess

state = {
    "branchIsUpdated": {
        "type": "eval",
        "cmd": ["false"],
        "result": None
    }
}


def evaluate(cmd):
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError:
        return False


state["branchIsUpdated"]["result"] = evaluate(state["branchIsUpdated"]["cmd"])
print(state)
