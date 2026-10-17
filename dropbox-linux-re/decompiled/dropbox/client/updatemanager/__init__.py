# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from build_number import is_store_managed
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from linux import UpdateManager
elif IS_MAC:
    from mac import UpdateManager
elif IS_WINDOWS:
    if is_store_managed():
        from windows_store import UpdateManager
    else:
        from windows import UpdateManager
# WARNING: Decompyle incomplete
