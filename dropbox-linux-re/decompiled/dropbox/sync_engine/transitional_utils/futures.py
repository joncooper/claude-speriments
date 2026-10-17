# Source Generated with Decompyle++
# File: futures.pyc (Python 3.11)

import functools
from typing import Any, Callable, overload, TypeVar
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
_Arg0 = TypeVar('_Arg0')
_Arg1 = TypeVar('_Arg1')
_Arg2 = TypeVar('_Arg2')
_Arg3 = TypeVar('_Arg3')
_Result = TypeVar('_Result')
parasitic_future = (lambda func = None: pass)()
parasitic_future = (lambda func = None: pass)()
parasitic_future = (lambda func = None: pass)()
parasitic_future = (lambda func = None: pass)()

def parasitic_future(func = None):
    pass
# WARNING: Decompyle incomplete


def blocking_unwrap(future = None):
    future.block()
    return future.result()

