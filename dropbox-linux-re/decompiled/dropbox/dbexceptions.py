# Source Generated with Decompyle++
# File: dbexceptions.pyc (Python 3.11)

from __future__ import absolute_import, division
import errno
from dropbox.exception.severity import Severity

class TimeoutError(Exception):
    pass


class InterruptError(Exception):
    pass


class LowDiskSpaceError(IOError):
    _severity_class = Severity.DEBUG
    
    def __init__(self = None, free_space = None, min_space = None):
        IOError.__init__(self, (errno.ENOSPC, 'Available space %.2fMB < %.2fMB requested' % (free_space / 1.04858e+06, min_space / 1.04858e+06)))


