# Source Generated with Decompyle++
# File: _types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Generic, Optional, TypeVar
from dropbox.foundation.raii2._shared_impl import SuperDestroyable as _SuperDestroyable
from dropbox.threading import Lock
T_co = TypeVar('T_co', bound = _SuperDestroyable, covariant = True)

def Record():
    '''Record'''
    __slots__ = ('instance', 'count', 'lock')
    
    def __init__(self = None, instance = None, count = None, lock = ('instance', 'T_co', 'count', 'int', 'lock', 'Lock', 'return', 'None')):
        self.instance = instance
        self.count = count
        self.lock = lock


Record = <NODE:27>(Record, 'Record', Generic[T_co])
