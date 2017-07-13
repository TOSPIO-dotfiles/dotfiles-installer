import sys


def pe(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def bug(msg, *args, **kwargs):
    pe("!!! FATAL ERROR !!!")
    pe(msg.format(*args, **kwargs))
    pe("!!! Please report a bug to y-usuzumi.")
    exit(120)


def version_str_to_tuple(version):
    return tuple(int(s) for s in version.split('.'))
