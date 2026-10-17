# Source Generated with Decompyle++
# File: lifecycle.pyc (Python 3.11)

import functools
from typing import Any, Callable, cast, TypeVar
from apex.panic import is_panicking

class ApexUsedAfterCleanupException(Exception):
    pass


class CurrentlyPanickingException(Exception):
    pass

_IS_SHUTDOWN = False
F = TypeVar('F', bound = Callable)

def raise_if_shutdown(f = None):
    pass
# WARNING: Decompyle incomplete


def set_shutdown():
    global _IS_SHUTDOWN
    _IS_SHUTDOWN = True

