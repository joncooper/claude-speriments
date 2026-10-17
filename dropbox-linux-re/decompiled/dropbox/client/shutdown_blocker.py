# Source Generated with Decompyle++
# File: shutdown_blocker.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import time
from abc import ABCMeta, abstractmethod
from typing import Callable, List, TypeVar
from six import with_metaclass
from dropbox.foundation.futures import Future, ResolvedFuture

def ShutdownBlockerInterface():
    '''ShutdownBlockerInterface'''
    allows_shutdown = (lambda self = None, timeout = None: pass)()
    forced_update_pending = (lambda self = None, time_until_update = None: pass)()

ShutdownBlockerInterface = <NODE:27>(ShutdownBlockerInterface, 'ShutdownBlockerInterface', with_metaclass(ABCMeta))
ArgT = TypeVar('ArgT')

def flow(future_funcs = None):
    pass
# WARNING: Decompyle incomplete


class SequentialShutdownBlocker(ShutdownBlockerInterface):
    pass
# WARNING: Decompyle incomplete

