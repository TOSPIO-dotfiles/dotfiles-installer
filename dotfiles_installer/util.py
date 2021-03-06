import sys


def pe(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def bug(msg, *args, **kwargs):
    pe("!!! FATAL ERROR !!!")
    pe(msg.format(*args, **kwargs))
    pe("!!! Please report a bug to y-usuzumi.")
    exit(120)


def pbug(pkg, msg, *args, **kwargs):
    pe(f"! Package {pkg} is broken !")
    pe(msg.format(*args, **kwargs))
    pe("! Either you have a network issue or there is a bug in the package.")
    pe("! Please report a bug to the author of {}.".format(pkg))


def version_str_to_tuple(version):
    return tuple(int(s) for s in version.split('.'))
