# Source Generated with Decompyle++
# File: signals.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, cast, Generic, List, Optional, Tuple, TypeVar
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.signals import Signal, SignalConnection, StandardSignal
from dropbox.overrides import report_exception
from dropbox.threading import Lock
_T = TypeVar('_T')
_Inner = TypeVar('_Inner')

def ThrottledSignal():
    '''ThrottledSignal'''
    pass
# WARNING: Decompyle incomplete

ThrottledSignal = <NODE:27>(ThrottledSignal, 'ThrottledSignal', StandardSignal[_T])

def AggregatedSignal():
    '''AggregatedSignal'''
    pass
# WARNING: Decompyle incomplete

AggregatedSignal = <NODE:27>(AggregatedSignal, 'AggregatedSignal', StandardSignal[_T])

def MappedSignal():
    '''MappedSignal'''
    
    def __init__(self = None, signal = None, transform = None):
        self._signal = signal
        self._transform = transform

    
    def listen(self = None, callback = None, name = None):
        pass
    # WARNING: Decompyle incomplete


MappedSignal = <NODE:27>(MappedSignal, 'MappedSignal', Signal[_T], Generic[(_T, _Inner)])

def RepeatedEventSignalWithPayload():
    '''RepeatedEventSignalWithPayload'''
    pass
# WARNING: Decompyle incomplete

RepeatedEventSignalWithPayload = <NODE:27>(RepeatedEventSignalWithPayload, 'RepeatedEventSignalWithPayload', Destroyable, Signal[_T])
