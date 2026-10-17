# Source Generated with Decompyle++
# File: _impl.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Generic, Optional, TypeVar
from _types import Record, T_co
from dropbox.foundation.raii2._shared_impl import SuperDestroyable as _SuperDestroyable
__all__ = [
    'ArcImpl',
    'WeakImpl']
_Destroyable = TypeVar('_Destroyable', bound = _SuperDestroyable)
_ArcC = TypeVar('_ArcC', bound = 'ArcImpl')

def ArcImpl():
    '''ArcImpl'''
    pass
# WARNING: Decompyle incomplete

ArcImpl = <NODE:27>(ArcImpl, 'ArcImpl', _SuperDestroyable, Generic[T_co])

def WeakImpl():
    '''WeakImpl'''
    pass
# WARNING: Decompyle incomplete

WeakImpl = <NODE:27>(WeakImpl, 'WeakImpl', Generic[T_co], object)
