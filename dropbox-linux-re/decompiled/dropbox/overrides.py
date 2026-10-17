# Source Generated with Decompyle++
# File: overrides.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import errno
import functools
import gc
import os
import sys
import threading
import traceback
import types
from typing import Any, Callable, cast, List, Optional, Text, Tuple, Union
from dropbox.components.desktop_components import DesktopComponent

def report_bad_assumption(*n, **kw):
    
    reporting
# WARNING: Decompyle incomplete


def report_exception(*n, **kw):
    
    reporting
# WARNING: Decompyle incomplete


def TRACE(*n, **kw):
    trace = trace
    import dropbox.trace
# WARNING: Decompyle incomplete


try:
    import opcode
except ImportError:
    opcode = types.ModuleType('opcode')
    opcode.__all__ = []
    opcode.reverse_engineering_note = 'Hi there!'
    sys.modules['opcode'] = opcode

import build_number
if sys.platform.startswith('darwin') and hasattr(sys, 'dropbox_target'):
    import ctypes.macholib.dyld as ctypes
    import ctypes.util as ctypes
    
    def __dyld_find_safe(name = None, *args, **kwargs):
        raise ValueError('on macos, must use the full library path')

    ctypes.macholib.dyld.dyld_find = __dyld_find_safe
    ctypes.util._dyld_find = __dyld_find_safe
if not build_number.is_frozen():
    from six.moves import builtins
    
    def dlog(*n, **kw):
        _dlog = dlog
        import dropbox.debug_tracing
        builtins.dlog = _dlog
        _dlog_first_call = _dlog
    # WARNING: Decompyle incomplete

    builtins.dlog = dlog
# WARNING: Decompyle incomplete
