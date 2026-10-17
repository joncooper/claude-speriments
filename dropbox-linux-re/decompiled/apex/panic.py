# Source Generated with Decompyle++
# File: panic.pyc (Python 3.11)

import os
import sys
import threading
from typing import Any, Callable, Optional
from apex._apex import ffi

class RustPanicError(Exception):
    pass
# WARNING: Decompyle incomplete

_PANIC_LOCK = threading.Lock()
_PANIC_CALLBACK: 'Optional[Callable[[RustPanicError], None]]' = None
_IS_PANICKING = False
_WRITE_PANIC_TO_STDERR = False

def enable_print_rust_panics():
    global _WRITE_PANIC_TO_STDERR
    _WRITE_PANIC_TO_STDERR = True


def set_panic_handler(fn = None):
    global _PANIC_CALLBACK
    _PANIC_LOCK
    old, _PANIC_CALLBACK = _PANIC_CALLBACK, fn
    None(None, None)


def is_panicking():
    return _IS_PANICKING

panic_callback = (lambda msg, msg_len = None, raw_file_path = None, raw_file_path_len = ffi.def_extern(), line_no = ('msg', 'Any', 'msg_len', 'int', 'raw_file_path', 'Any', 'raw_file_path_len', 'int', 'line_no', 'int', 'return', 'None'): _IS_PANICKING = Truepanic_msg = ffi.string(msg, msg_len).decode('utf-8')file_path = ffi.string(raw_file_path, raw_file_path_len).decode('utf-8')# WARNING: Decompyle incomplete
)()
