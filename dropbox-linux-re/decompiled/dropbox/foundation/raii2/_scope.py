# Source Generated with Decompyle++
# File: _scope.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Generic, TypeVar
from _shared_impl.base import SuperDestroyable
_D = TypeVar('_D', bound = SuperDestroyable)

def _Scope():
    '''_Scope'''
    
    def __init__(self = None, obj = None):
        self._obj = obj

    
    def __enter__(self = None):
        return self._obj

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('return', 'None')):
        self._obj.destroy()


_Scope = <NODE:27>(_Scope, '_Scope', Generic[_D])

def destroying(destroyable_object = None):
    return _Scope(destroyable_object)

