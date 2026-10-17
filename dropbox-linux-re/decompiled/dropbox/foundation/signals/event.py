# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, Optional
from dropbox.foundation.raii2 import Destroyable, destroying
from dropbox.foundation.signals.standard import Signal, SignalConnection as _SigConn, StandardSignal as _StandardSignal
from dropbox.threading import Lock
__all__ = [
    'EventSignal']

class _DummyConnection(_SigConn):
    
    def __destroy__(self = None):
        pass



def EventSignal():
    '''EventSignal'''
    pass
# WARNING: Decompyle incomplete

EventSignal = <NODE:27>(EventSignal, 'EventSignal', Destroyable, Signal[None])
