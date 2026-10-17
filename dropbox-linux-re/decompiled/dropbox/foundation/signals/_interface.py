# Source Generated with Decompyle++
# File: _interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import abc
from typing import Callable, Generic, TypeVar
from dropbox.foundation.raii2 import Destroyable
_ArgType = TypeVar('_ArgType', covariant = True)

class SignalConnection(Destroyable):
    pass
# WARNING: Decompyle incomplete


def Signal():
    '''Signal'''
    listen = (lambda self = None, callback = None, listener_name = abc.abstractmethod: pass)()

Signal = <NODE:27>(Signal, 'Signal', Generic[_ArgType])
