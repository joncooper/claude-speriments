# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from typing import Optional
from apex._apex import ffi, lib

def process_architecture():
    return str(ffi.string(lib.process_architecture()), 'utf-8')


def system_architecture():
    return str(ffi.string(lib.system_architecture()), 'utf-8')


def rust_thread_name():
    name = lib.rust_thread_name()
    return str(ffi.string(name), 'utf-8') if name else None

