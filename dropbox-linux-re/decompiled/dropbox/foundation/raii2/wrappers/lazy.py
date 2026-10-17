# Source Generated with Decompyle++
# File: lazy.pyc (Python 3.11)

from typing import Callable, Generic, Optional, TypeVar
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.raii2._shared_impl import SuperDestroyable
from dropbox.threading import Lock
_T = TypeVar('_T', bound = SuperDestroyable, covariant = True)
_TFast = TypeVar('_TFast', bound = Destroyable, covariant = True)

def _SuperLazy():
    '''_SuperLazy'''
    pass
# WARNING: Decompyle incomplete

_SuperLazy = <NODE:27>(_SuperLazy, '_SuperLazy', SuperDestroyable, Generic[_T])

def Lazy():
    '''Lazy'''
    pass

Lazy = <NODE:27>(Lazy, 'Lazy', Destroyable, _SuperLazy[_TFast])
