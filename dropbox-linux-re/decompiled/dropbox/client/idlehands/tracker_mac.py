# Source Generated with Decompyle++
# File: tracker_mac.pyc (Python 3.11)

from __future__ import absolute_import
from macffi.CoreGraphics import kCGEventTapDisabledByUserInput
from macffi.CoreGraphicsServices import CGSSecondsSinceLastInputEvent

class IdleTracker(object):
    
    def is_trackable(self):
        return True

    
    def seconds_idle(self):
        ret = CGSSecondsSinceLastInputEvent(kCGEventTapDisabledByUserInput)
        if ret > 31104000:
            return 0
        return int(ret)


