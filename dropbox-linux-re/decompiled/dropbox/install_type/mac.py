# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from  import InstallType
from dropbox.mac.helper_installer import check_helper_installer

def mac_get_dropbox_install_type():
    if check_helper_installer():
        return InstallType.MAC_NASHVILLE_WITH_HELPER
    return None.MAC_NASHVILLE_NO_HELPER

