# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from typing import Type, TypeVar
from _shared_impl.base import SuperDestroyable
_D = TypeVar('_D', bound = 'Destroyable')

def Destroyable():
    '''Destroyable'''
    _get_concrete_base_class = (lambda cls = None: Destroyable)()
    
    def _autodestroy(self = None, obj = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __destroy__(self = None):
        pass


Destroyable = <NODE:27>(Destroyable, 'Destroyable', SuperDestroyable['Destroyable'])
