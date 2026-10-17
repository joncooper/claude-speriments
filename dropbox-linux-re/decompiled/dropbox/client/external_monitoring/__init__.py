# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from base import MonitoringControllerBase as MonitoringController
elif IS_MAC:
    from mac import MonitoringController
elif IS_WINDOWS:
    from windows import MonitoringController
# WARNING: Decompyle incomplete
