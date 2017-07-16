from .util import pe


# Not sure if this would be useful in the future
_errors = {}


class _ErrorMeta(type):
    def __new__(cls, name, bases, dct):
        kls = super().__new__(cls, name, bases, dct)
        if 'error_code' in dct:
            error_code = dct['error_code']
            _errors[error_code] = kls
        return kls


class Error(metaclass=_ErrorMeta):
    msg = None

    @classmethod
    def emerge(cls, *args, **kwargs):
        pe(cls.msg.format(*args, **kwargs))


class Panic(Error):
    exit_code = 123

    @classmethod
    def emerge(cls, *args, **kwargs):
        pe("!! Panic! {}".format(cls.msg.format(*args, **kwargs)))
        exit(cls.exit_code)


class PythonVersionError(Panic):
    msg = "Unmet Python version: {}"


class PythonDepUnmetError(Panic):
    msg = "Missing Python dep: {}"  # dep, version


class AttemptToRunMultipleInstancesError(Panic):
    msg = "An instance of dotfiles-installer is already running"
