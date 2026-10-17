# Source Generated with Decompyle++
# File: tracker_linux.pyc (Python 3.11)

from __future__ import absolute_import

class IdleTracker(object):
    
    def __init__(self):
        self.trackable = False

    
    def is_trackable(self):
        return self.trackable

    
    def seconds_idle(self):
        raise AssertionError('called seconds_idle on linux')


