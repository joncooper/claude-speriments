# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX or IS_MAC:
    from posix import DropboxFolderPath
elif IS_WINDOWS:
    from windows import DropboxFolderPath
# WARNING: Decompyle incomplete
