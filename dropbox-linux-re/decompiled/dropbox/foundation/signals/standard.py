# Source Generated with Decompyle++
# File: standard.pyc (Python 3.11)

import contextlib
from _thread import get_ident
from typing import Callable, Iterator, Optional, Set, Tuple, TypeVar
from weakref import ref as WeakRef
from _interface import Signal, SignalConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.raii2 import Destroyable
from dropbox.threading import Lock
_ArgType = TypeVar('_ArgType')
_D = TypeVar('_D', bound = Destroyable)

def StandardSignal():
    '''StandardSignal'''
    pass
# WARNING: Decompyle incomplete

StandardSignal = <NODE:27>(StandardSignal, 'StandardSignal', Signal[_ArgType], Destroyable)
