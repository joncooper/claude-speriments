# Source Generated with Decompyle++
# File: tracker_win.pyc (Python 3.11)

from __future__ import absolute_import, division
import ctypes
from ctypes import byref, c_uint, sizeof
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.repr_utils import ReprStructure

class LASTINPUTINFO(ReprStructure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint)]


class IdleTracker(object):
    
    def __init__(self):
        self.trackable = False
        
        try:
            self.lastInputInfo = LASTINPUTINFO()
            self.lastInputInfo.cbSize = sizeof(self.lastInputInfo)
            if not hasattr(ctypes.windll.user32, 'GetLastInputInfo'):
                report_bad_assumption('win32: GetLastInputInfo not available')
                return None
            self.trackable = True
            return None
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            return None


    
    def is_trackable(self):
        return self.trackable

    
    def seconds_idle(self):
        pass
    # WARNING: Decompyle incomplete


