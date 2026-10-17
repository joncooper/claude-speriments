# Source Generated with Decompyle++
# File: ids.pyc (Python 3.11)

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any

class FileID:
    __slots__ = ('_bytes',)
    
    def __init__(self = None, bs = None):
        self._bytes = bs[3:] if bs.startswith(b'id:') else bs

    from_text = (lambda text = None: FileID(text.encode('ascii')))()
    
    def to_text(self = None):
        return self._bytes.decode('ascii')

    
    def to_apiv2_text(self = None):
        return self.to_apiv2_bytes().decode('ascii')

    
    def to_bytes(self = None):
        return self._bytes

    
    def to_apiv2_bytes(self = None):
        return b'id:' + self._bytes

    
    def __eq__(self = None, other = None):
