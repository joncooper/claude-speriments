# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import
import os
from typing import Optional, Text, Union
from common import _DirectoryAbstract, _DirectoryEntryBase, DirectoryModifiedError, Path
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.repr_utils import easy_repr

class _DirectoryEntry(_DirectoryEntryBase):
    __slots__ = ('name',)
    
    def __init__(self = None, name = None):
        self.name = name

    
    def __repr__(self = None):
        return easy_repr(self, 'name')



class DirectoryPython(_DirectoryAbstract):
    __slots__ = ('ents', 'idx', 'path')
    
    def __init__(self = None, path = None, no_atime = None):
        self.path = path
        self.ents = os.listdir(path)()
        self.idx = 0

    
    def close(self = None):
        pass

    
    def reset(self = None):
        self.__init__(self.path)

    
    def readdir(self = None):
        
        try:
            toret = self.ents[self.idx]
            return toret
        except IndexError:
            return None




def Directory(path = None, no_atime = None):
    
    try:
        if IS_WINDOWS:
            windows = windows
            import 
            return windows.Directory(path, no_atime = no_atime)
        if None:
            DirectoryMac = Directory
            import mac
            return DirectoryMac(path, no_atime = no_atime)
        if None:
            posix = posix
            import 
            return posix.Directory(path, no_atime = no_atime)
        raise Exception('System not supported!')
    except ImportError:
        return 


# WARNING: Decompyle incomplete
