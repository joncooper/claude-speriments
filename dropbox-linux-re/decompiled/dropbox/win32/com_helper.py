# Source Generated with Decompyle++
# File: com_helper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import functools
import threading
from contextlib import contextmanager
from typing import Optional
import comtypes
from dropbox.trace import TRACE
COINIT_APARTMENTTHREADED = comtypes.COINIT_APARTMENTTHREADED
COINIT_MULTITHREADED = comtypes.COINIT_MULTITHREADED

class COMLocalStorage(threading.local):
    com_initialized: 'Optional[bool]' = None

_LOCAL = COMLocalStorage()
initialized_com = (lambda debug_name = None, coinit = None: pass# WARNING: Decompyle incomplete
)()

def uses_com(debug_name = None, func = None, coinit = None):
    pass
# WARNING: Decompyle incomplete

