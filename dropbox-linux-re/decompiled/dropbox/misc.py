# Source Generated with Decompyle++
# File: misc.pyc (Python 3.11)

from __future__ import absolute_import
import functools
import os

def protect_closed(f):
    pass
# WARNING: Decompyle incomplete

READ_SIZE = 4096

class LineReaderMixin(object):
    
    def __iter__(self):
        return self

    
    def __next__(self):
        ret = self.readline()
        if not ret:
            raise StopIteration()
        return ret

    next = __next__
    
    def readline(self, size = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def readlines(self, sizehint = (None,)):
        return list(self)


