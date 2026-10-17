# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from interface import UITimer
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS

class UITimerFactory(object):
    create = (lambda : if IS_MAC:
CocoaUITimer = CocoaUITimerimport cocoaCocoaUITimer()if None:
Win32UITimer = Win32UITimerimport win32Win32UITimer()if None:
LinuxUITimer = LinuxUITimerimport linuxLinuxUITimer()raise NotImplementedError())()

