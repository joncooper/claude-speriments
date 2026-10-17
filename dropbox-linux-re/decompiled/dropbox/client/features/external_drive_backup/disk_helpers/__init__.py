# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from linux import is_readonly_drive, is_remote_drive
    return None
if None:
    from mac import is_readonly_drive, is_remote_drive
    return None
if None:
    from windows import is_readonly_drive, is_remote_drive
    return None
