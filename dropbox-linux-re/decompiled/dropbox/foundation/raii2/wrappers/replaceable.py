# Source Generated with Decompyle++
# File: replaceable.pyc (Python 3.11)

from typing import Generic, Optional, TypeVar
from dropbox.foundation.raii2._shared_impl.base import SuperDestroyable
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.threading import Lock
_T = TypeVar('_T', bound = Optional[SuperDestroyable])
_TFast = TypeVar('_TFast', bound = Optional[Destroyable])

def ReplaceableState():
    '''ReplaceableState'''
    
    def __init__(self = None, value = None):
        self.value = value


ReplaceableState = <NODE:27>(ReplaceableState, 'ReplaceableState', Generic[_T])

def _SuperReplaceable():
    '''_SuperReplaceable'''
    pass
# WARNING: Decompyle incomplete

_SuperReplaceable = <NODE:27>(_SuperReplaceable, '_SuperReplaceable', SuperDestroyable, Generic[_T])

def Replaceable():
    '''Replaceable'''
    pass

Replaceable = <NODE:27>(Replaceable, 'Replaceable', Destroyable, _SuperReplaceable[_TFast])
