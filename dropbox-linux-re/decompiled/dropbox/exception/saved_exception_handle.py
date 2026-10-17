# Source Generated with Decompyle++
# File: saved_exception_handle.pyc (Python 3.11)

from typing_extensions import Protocol
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_WINDOWS:
    from dropbox.exception.win import SavedExceptionHandle as SavedExceptionHandleImpl
elif IS_MAC:
    from dropbox.exception.mac import SavedExceptionHandle as SavedExceptionHandleImpl
elif IS_LINUX:
    from dropbox.exception.linux import SavedExceptionHandle as SavedExceptionHandleImpl
# WARNING: Decompyle incomplete
