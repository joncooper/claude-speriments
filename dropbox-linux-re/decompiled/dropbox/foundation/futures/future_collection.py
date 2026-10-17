# Source Generated with Decompyle++
# File: future_collection.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod
from collections import OrderedDict
from typing import Generic, List, Optional, TypeVar
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future
from dropbox.foundation.runtime import panic_with_report
from dropbox.foundation.runtime.exit_codes import ExitCode
_T = TypeVar('_T')

def FutureCollection():
    '''FutureCollection'''
    
    def __destroy__(self = None):
        self._cancel_all()

    register = (lambda self = None, future = None: self._add_to_collection(future)future.regardless(self._update_on_future_finished).ground(component = self._destroyable_component())future)()
    cancel_all = (lambda self = None: self._cancel_all())()
    in_progress_count = (lambda self = None: pass)()()
    _update_on_future_finished = (lambda self = None, future = abstractmethod: pass)()()
    _add_to_collection = (lambda self = None, future = None: pass)()
    _cancel_all = (lambda self = None: pass)()

FutureCollection = <NODE:27>(FutureCollection, 'FutureCollection', Actor, Generic[_T])

def SingleFutureCollection():
    '''SingleFutureCollection'''
    pass
# WARNING: Decompyle incomplete

SingleFutureCollection = <NODE:27>(SingleFutureCollection, 'SingleFutureCollection', FutureCollection[_T])

def CoalescingFutureCollection():
    '''CoalescingFutureCollection'''
    pass
# WARNING: Decompyle incomplete

CoalescingFutureCollection = <NODE:27>(CoalescingFutureCollection, 'CoalescingFutureCollection', FutureCollection[_T])

def MultiFutureCollection():
    '''MultiFutureCollection'''
    pass
# WARNING: Decompyle incomplete

MultiFutureCollection = <NODE:27>(MultiFutureCollection, 'MultiFutureCollection', FutureCollection[_T])
