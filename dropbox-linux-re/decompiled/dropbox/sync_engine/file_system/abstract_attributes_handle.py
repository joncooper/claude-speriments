# Source Generated with Decompyle++
# File: abstract_attributes_handle.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Iterator
from dropbox.shared.util import Closeable
from dropbox.sync_engine_boundary.file_system_constants import DEFAULT_PRESERVED_ATTRS_NAME
MYPY = False
if MYPY:
    from abstract_file_system import AbstractFile

def AbstractAttributesHandle():
    '''AbstractAttributesHandle'''
    
    def close(self):
        raise NotImplementedError()

    closed = (lambda self: raise NotImplementedError())()
    
    def open(self, plat):
        raise NotImplementedError()

    
    def open_preserved(self = None, mode = None, name = property):
        raise NotImplementedError()

    
    def readplat(self):
        raise NotImplementedError()

    
    def remove(self, plat, key):
        raise NotImplementedError()

    
    def remove_preserved(self = None, name = None):
        raise NotImplementedError()

    
    def reset(self):
        raise NotImplementedError()

    
    def __iter__(self):
        return self

    
    def __next__(self):
        return self.next()

    
    def next(self):
        toret = self.readplat()
    # WARNING: Decompyle incomplete


AbstractAttributesHandle = <NODE:27>(AbstractAttributesHandle, 'AbstractAttributesHandle', Closeable, Iterator[str])

class AbstractPlatformHandle(Closeable):
    
    def close(self):
        raise NotImplementedError()

    closed = (lambda self: raise NotImplementedError())()
    name = (lambda self: raise NotImplementedError())()
    
    def open(self, key, mode = ('r',)):
        raise NotImplementedError()

    
    def readattr(self):
        raise NotImplementedError()

    
    def reset(self):
        raise NotImplementedError()

    
    def __iter__(self):
        return self

    
    def __next__(self):
        return self.next()

    
    def next(self):
        toret = self.readattr()
    # WARNING: Decompyle incomplete


