# Source Generated with Decompyle++
# File: wrapper_future.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from concurrent.futures import Future as CFFuture
from typing import Callable, TypeVar
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.foundation.futures.basic import BaseFuture
_T = TypeVar('_T')

def WrapperFuture():
    '''WrapperFuture'''
    pass
# WARNING: Decompyle incomplete

WrapperFuture = <NODE:27>(WrapperFuture, 'WrapperFuture', BaseFuture[_T])

def create_and_wrap_future(future_thunk = None):
    
    try:
        return WrapperFuture(future_thunk())
    except Exception:
        e = None
        del e
        return None
        None = 
        del e


