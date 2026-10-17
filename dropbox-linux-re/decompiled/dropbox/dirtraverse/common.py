# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from __future__ import absolute_import
from abc import abstractmethod
from typing import Iterator, Optional, Text, Union
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception

class DirectoryModifiedError(IOError):
    pass


class _DirectoryEntryBase(object):
    pass

Path = Union[(bytes, Text)]

def _DirectoryAbstract():
    '''_DirectoryAbstract'''
    
    def __iter__(self = None):
        return self

    
    def __next__(self = None):
        a = self.readdir()
        if not a:
            raise StopIteration
        return a

    next = __next__
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, *exc_info):
        
        try:
            self.close()
            return None
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            return None


    
    def __del__(self = None):
        
        try:
            self.close()
            return None
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            return None


    close = (lambda self = None: pass)()
    readdir = (lambda self = None: pass)()

_DirectoryAbstract = <NODE:27>(_DirectoryAbstract, '_DirectoryAbstract', Iterator[_DirectoryEntryBase])
