# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from linux import generate_icon_paths
elif IS_MAC:
    from mac import generate_icon_paths
elif IS_WINDOWS:
    from windows import generate_icon_paths
# WARNING: Decompyle incomplete
