# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from linux import get_associated_applications, get_dropbox_icon, get_dropbox_paper_icon, open_with_application
elif IS_MAC:
    from mac import get_associated_applications, get_dropbox_icon, get_dropbox_paper_icon, open_with_application
elif IS_WINDOWS:
    from windows import get_associated_applications, get_dropbox_icon, get_dropbox_paper_icon, open_with_application
# WARNING: Decompyle incomplete
