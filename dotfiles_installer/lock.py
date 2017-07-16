import os
import fasteners
from contextlib import contextmanager
from .error import AttemptToRunMultipleInstancesError

_lock_file_path = os.path.join(
    os.path.expanduser('~'),
    '.dotfiles-installer.lck'
)


@contextmanager
def global_lock():
    lock = fasteners.InterProcessLock(_lock_file_path)
    is_locked = lock.acquire(blocking=False)
    if is_locked:
        yield
    else:
        AttemptToRunMultipleInstancesError.emerge()
