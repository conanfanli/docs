import io


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    # RED = '\033[1;31m'
    RED = '\u001b[31m'
    NO_COLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


_print = print


def print_red(*args, **kwargs):
    f = io.StringIO()
    # Set end to '' so we don't get two newlines
    _print(*args, file=f, **kwargs)
    return _print(Color.RED + f.getvalue() + Color.NO_COLOR, end='')
