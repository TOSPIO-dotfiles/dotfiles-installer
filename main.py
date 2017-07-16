import sys
import pkg_resources
from dotfiles_installer import error
from dotfiles_installer.util import version_str_to_tuple
from dotfiles_installer.lock import global_lock


def _python_dep_check(dep, pred=None, dep_spec=None):
    if dep_spec is None:
        dep_spec = dep  # dep spec name
    try:
        pkg_version = pkg_resources.get_distribution(dep).version
        # If pred returns non-boolean values we're fucked up.
        # So we do strict boolean check.
        if pred and pred(pkg_version) is False:
            error.PythonDepUnmetError.emerge(dep_spec)
    except pkg_resources.DistributionNotFound:
        error.PythonDepUnmetError.emerge(dep_spec)


def _default_python_dep_check_pred(least_version):
    def _pred(pkg_version):
        return (
            version_str_to_tuple(pkg_version) >=
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
    _simple_python_dep_check('PyYAML', least_version='3.12')
    _simple_python_dep_check('fasteners', least_version='0.14')


if __name__ == '__main__':
    check_python_version()
    check_python_deps()
