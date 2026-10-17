# Source Generated with Decompyle++
# File: platform.pyc (Python 3.11)

from __future__ import absolute_import
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_WINDOWS:
    from windows import MetaDirectoryWatchManager
elif IS_MAC:
    from mac import MetaDirectoryWatchManager
elif IS_LINUX:
    from linux import MetaDirectoryWatchManager
# WARNING: Decompyle incomplete
