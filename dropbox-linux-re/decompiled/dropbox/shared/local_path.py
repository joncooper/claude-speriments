# Source Generated with Decompyle++
# File: local_path.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Any, Text
from unicodedata import normalize
from build_number.features import feature_enabled
from fastpath import PosixPath, WinPath
from six import add_metaclass
from dropbox.assertions import assert_
from dropbox.nfcdetector import is_nfc, is_nfd

class LocalPathMeta(type):
    
    def __instancecheck__(cls = None, other = None):
        return isinstance(other, (AbstractPosixPath, WindowsPath))


LocalPath = <NODE:12>()

class AbstractLocalPath(object):
    __slots__ = ()
    
    def __setstate__(self, state):
        raise AssertionError('__setstate__ should never be called')

    
    def join_dropbox_ns_relative_path(self, ns_relative_path):
        if not is_nfc(ns_relative_path):
            raise ValueError(f'''Dropbox paths must be in NFC! {ns_relative_path!r}''')
        if ns_relative_path == '/':
            return self
    # WARNING: Decompyle incomplete

    
    def to_dropbox_ns_relative_path(self, parent_local_path):
        pass
    # WARNING: Decompyle incomplete

    
    def append(self, ext):
        return self.dirname.join(f'''{self.basename!s}{Text(ext)!s}''')

    
    def startswith(self, parent):
