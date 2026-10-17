# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum, unique
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
InstallType = <NODE:12>()

def get_dropbox_install_type():
    if IS_MAC:
        mac_get_dropbox_install_type = mac_get_dropbox_install_type
        import mac
        return mac_get_dropbox_install_type()
    if None:
        win_get_dropbox_install_type = win_get_dropbox_install_type
        import win
        return win_get_dropbox_install_type()
    if None.LINUX:
        return InstallType.LINUX
    raise None

