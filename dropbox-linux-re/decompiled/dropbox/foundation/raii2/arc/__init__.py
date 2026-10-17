# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from typing import Generic, Optional, TypeVar
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.raii2._shared_impl import SuperDestroyable
from dropbox.foundation.raii2.arc._impl import ArcImpl as _ArcImpl, WeakImpl as _WeakImpl
from dropbox.foundation.raii2.arc._types import Record as _Record
from dropbox.threading import Lock
__all__ = [
    'Arc']
_Tco = TypeVar('_Tco', bound = SuperDestroyable, covariant = True)
_QD = TypeVar('_QD', bound = Destroyable)

def Arc():
    '''Arc'''
    new = (lambda cls = None, instance = None: Arc(_Record(instance = instance, count = 0, lock = Lock())))()
    
    def downgrade(self = None):
        return Weak(self._record)


Arc = <NODE:27>(Arc, 'Arc', Destroyable, _ArcImpl[_Tco], Generic[_Tco])

def Weak():
    '''Weak'''
    
    def upgrade(self = None):
        self._record.lock
    # WARNING: Decompyle incomplete


Weak = <NODE:27>(Weak, 'Weak', _WeakImpl[_Tco], Generic[_Tco])
