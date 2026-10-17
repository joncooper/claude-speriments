# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import sys
from types import TracebackType
from typing import IO, List, Optional, Tuple, Type
ExcInfo = Tuple[(Type[BaseException], BaseException, TracebackType)]
OptExcInfo = Tuple[(Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType])]

def typed_exc_info():
    (e0, e1, e2) = sys.exc_info()
# WARNING: Decompyle incomplete


def format_exc_stack(omit_frames = None):
    (_type, _value, _traceback) = typed_exc_info()
    
    try:
        import traceback
        Interpreter = Interpreter
        import runtime
        up_stack = Interpreter.current_stack()[:-omit_frames]
        down_stack = traceback.format_tb(_traceback)
        exc_itself = traceback.format_exception_only(_type, _value)
        del _traceback
        del _value
        del _type
        return up_stack + down_stack + exc_itself
    except:
        del _traceback
        del _value
        del _type



def print_exc_stack(file = None):
    for line in format_exc_stack(omit_frames = 2):
        file.write(line)
        return None

