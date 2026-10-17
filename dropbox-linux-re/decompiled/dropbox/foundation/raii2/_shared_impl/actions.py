# Source Generated with Decompyle++
# File: actions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Generic, Optional, Type, TypeVar
import six
MYPY = False
if MYPY:
    from base import SuperDestroyable as Destroyable
_T = TypeVar('_T')
_DClass = TypeVar('_DClass', bound = 'Destroyable[Any]')

def DestroyAction():
    '''DestroyAction'''
    __slots__ = ()
    _desc = (lambda self = None: pass)()
    _action = (lambda self = None, caller = None: pass)()
    
    def execute(self = None, caller = None):
        
        try:
            self._action(caller)
            return None
        except:
            caller._report_and_panic('exception during {desc} from destroy()'.format(desc = self._desc()), component = caller._destroyable_component(), use_exception = True)
            return None



DestroyAction = <NODE:27>(DestroyAction, 'DestroyAction', Generic[_DClass])()

def DestroyTarget():
    '''DestroyTarget'''
    __slots__ = ('obj', 'dst', 'cls')
    
    def __init__(self = None, obj = None, dst = None, cls = ('obj', '_T', 'dst', 'Callable[[_T], None]', 'cls', 'Optional[Type[Destroyable[_DClass]]]', 'return', 'None')):
        self.obj = obj
        self.dst = dst
        self.cls = cls

    
    def _desc(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _action(self = None, caller = None):
        self.dst(self.obj)


DestroyTarget = <NODE:27>(DestroyTarget, 'DestroyTarget', DestroyAction[_DClass], Generic[_DClass])

def DestroyCall():
    '''DestroyCall'''
    __slots__ = ('cls',)
    
    def __init__(self = None, cls = None):
        self.cls = cls

    
    def _action(self = None, caller = None):
        self.cls.__destroy__(caller)

    
    def _desc(self = None):
        return 'call to {}.__destroy__()'.format(self.cls)


DestroyCall = <NODE:27>(DestroyCall, 'DestroyCall', DestroyAction[_DClass], Generic[_DClass])
