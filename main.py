import sys
import importlib
from dotfiles_installer import error
from dotfiles_installer.util import version_str_to_tuple


def _python_dep_check(dep, pred=None, dep_spec=None):
    if dep_spec is None:
        dep_spec = dep  # dep spec name
    try:
        mod = importlib.import_module(dep)
        # If pred returns non-boolean values we're fucked up.
        # So we do strict boolean check.
        if pred and pred(mod) is False:
            error.PythonDepUnmetError.emerge(dep_spec)
    except ImportError:
        error.PythonDepUnmetError.emerge(dep_spec)


def _default_python_dep_check_pred(least_version):
    def _pred(mod):
        return (
            version_str_to_tuple(mod.__version__) >=
            version_str_to_tuple(least_version)
        )

    return _pred


def _simple_python_dep_check(dep, least_version=None, dep_name=None):
    if dep_name is None:
        dep_name = dep
    if least_version is None:
        pred = None
        dep_spec = dep_name
    else:
        pred = _default_python_dep_check_pred(least_version)
        dep_spec = '{} > {}'.format(dep_name, least_version)
    return _python_dep_check(dep, pred, dep_spec)


def check_python_version():
    python_version = sys.version_info
    if python_version < (3, 5):
        error.PythonVersionError.emerge(">= 3.5")


def check_python_deps():
    _simple_python_dep_check('pystache', least_version='0.5')


if __name__ == '__main__':
    check_python_version()
    check_python_deps()
