# Source Generated with Decompyle++
# File: transferable.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Generic, Optional, TypeVar
from dropbox.foundation.raii2._shared_impl.base import SuperDestroyable
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.threading import Lock
_T = TypeVar('_T', bound = SuperDestroyable)
_TFast = TypeVar('_TFast', bound = Destroyable, covariant = True)

def _SuperTransferable():
    '''_SuperTransferable'''
    pass
# WARNING: Decompyle incomplete

_SuperTransferable = <NODE:27>(_SuperTransferable, '_SuperTransferable', SuperDestroyable, Generic[_T])

def Transferable():
    '''Transferable'''
    pass

Transferable = <NODE:27>(Transferable, 'Transferable', Destroyable, _SuperTransferable[_TFast])
