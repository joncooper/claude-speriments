# Source Generated with Decompyle++
# File: repr_utils.pyc (Python 3.11)

import ctypes
import threading
from typing import Any
template_repr_local = threading.local()

def _safe_repr(obj = None):
    
    try:
        return repr(obj)
    except Exception:
        e = None
        del e
        return None
        None = 
        del e



def template_repr(self = None, template = None, *fields):
    pass
# WARNING: Decompyle incomplete


def easy_repr(self = None, *fields):
    pass
# WARNING: Decompyle incomplete


def keyword_repr(self = None, *fields):
    pass
# WARNING: Decompyle incomplete


class ReprStructure(ctypes.Structure):
    
    def __repr__(self = None):
