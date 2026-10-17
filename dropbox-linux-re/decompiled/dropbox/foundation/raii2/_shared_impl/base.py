# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import abc
import contextlib
import functools
import os
import re
import types
from typing import Any, Callable, cast, Dict, Generic, Iterator, List, Mapping, Optional, Tuple, Type, TypeVar, Union
from build_number import dropbox_version, is_frozen
from mypy_extensions import NoReturn
from actions import DestroyAction, DestroyCall, DestroyTarget
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.environment import debugging_features_are_enabled, is_profiler_running
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.runtime import Interpreter, panic_with_report
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_str
_T = TypeVar('_T')
_C = TypeVar('_C', bound = Callable)

class SuperDestroyableScope(object):
    current_scope: "Optional['SuperDestroyableScope']" = None
    
    def __init__(self = None):
        self._SuperDestroyableScope__done = False
        self._tracked = { }
        self._old_scope = SuperDestroyableScope.current_scope
        SuperDestroyableScope.current_scope = self

    
    def track_creation(self = None, obj_cls = None, obj_id = None, creation_stack = ('obj_cls', 'str', 'obj_id', 'int', 'creation_stack', 'List[str]', 'return', 'None')):
        self._tracked[obj_id] = (repr(obj_cls), creation_stack)

    
    def track_destruction(self = None, obj_id = None):
        if not self._SuperDestroyableScope__done:
            del self._tracked[obj_id]
            return None

    
    def close(self = None):
        self._SuperDestroyableScope__done = True
        SuperDestroyableScope.current_scope = self._old_scope

    
    def report(self = None):
        return self._tracked.items()()


_MClass = TypeVar('_MClass', bound = 'SuperDestroyableMeta')
_DClass = TypeVar('_DClass', bound = 'SuperDestroyable')
FINAL_INIT_WAS_CALLED_ATTR_NAME = 'SuperDestroyable: __init__ was called'

class SuperDestroyableMeta(abc.ABCMeta):
    pass
# WARNING: Decompyle incomplete


def SuperDestroyable():
    '''SuperDestroyable'''
    pass
# WARNING: Decompyle incomplete

SuperDestroyable = <NODE:27>(SuperDestroyable, 'SuperDestroyable', Generic[_DClass], metaclass = SuperDestroyableMeta)
