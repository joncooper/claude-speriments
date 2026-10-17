# Source Generated with Decompyle++
# File: connection_pool.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from threading import current_thread
from typing import Callable, List, Optional, overload, Text, TypeVar
from dropbox.db_thread import db_thread
from dropbox.foundation.futures import CancelledFuture, EasyFuture, Future
from dropbox.foundation.raii2 import Destroyable
from dropbox.native_queue import Empty, Queue
from dropbox.threading import Condition, Lock
from dropbox.threadutils import StoppableThread
_T = TypeVar('_T')

class _YetAnotherAdaptorFuture(EasyFuture):
    pass
# WARNING: Decompyle incomplete


class _YetAnotherPooledThread(StoppableThread):
    
    def set_wakeup_event(self = None):
        pass



class _YetAnotherThreadPool(Destroyable):
    pass
# WARNING: Decompyle incomplete

_THREAD_POOL: 'Optional[_YetAnotherThreadPool]' = None

def initialize_module(thread_count = None):
    pass
# WARNING: Decompyle incomplete


def make_delayed_network_call(action = None):
    pass
# WARNING: Decompyle incomplete

_Result = TypeVar('_Result')
_Arg0 = TypeVar('_Arg0')
_Arg1 = TypeVar('_Arg1')
_Arg2 = TypeVar('_Arg2')
_Arg3 = TypeVar('_Arg3')
_Arg4 = TypeVar('_Arg4')
_Arg5 = TypeVar('_Arg5')
_Arg6 = TypeVar('_Arg6')
on_network_thread = (lambda func = None: pass)()
on_network_thread = (lambda func = None: pass)()
on_network_thread = (lambda func = None: pass)()
on_network_thread = (lambda func = None: pass)()
on_network_thread = (lambda func = None: pass)()
on_network_thread = (lambda func = None: pass)()
on_network_thread = (lambda func = None: pass)()
on_network_thread = (lambda func = None: pass)()

def on_network_thread(func = None):
    pass
# WARNING: Decompyle incomplete

