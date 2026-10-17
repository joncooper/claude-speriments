# Source Generated with Decompyle++
# File: memory_placeholder.pyc (Python 3.11)

from __future__ import absolute_import
import contextlib
from typing import Iterator, Text
from file_system.indexing_attributes import IndexingAttributes
from abstract_placeholder import AbstractPlaceholder, SimpleStat
from dropbox.functions import make_unicode
from dropbox.infinite.exceptions import NotAnInfinitePlaceholderError
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import PlaceholderDetails
from dropbox.sync_engine_boundary.infinite.placeholder_context import PlaceholderContext
from dropbox.threading import Lock
MYPY = False
if MYPY:
    from file_system.memory import _MemoryFile, MemoryFS

class MemoryPlaceholderContext(PlaceholderContext):
    
    def __init__(self = None, local_path = None, memory_fs = None):
        self.local_path = local_path
        self.memory_fs = memory_fs



class MemoryPlaceholder(AbstractPlaceholder):
    
    def __init__(self = None, file_obj = None, memory_ia = None, local_path = ('file_obj', '_MemoryFile', 'memory_ia', 'IndexingAttributes', 'local_path', 'LocalPath', 'return', 'None')):
        self._file_obj = file_obj
        self._memory_ia = memory_ia
        self._local_path = local_path
        self._lock = Lock()

    open_from_context = (lambda context = None, need_write_access = staticmethod: pass# WARNING: Decompyle incomplete
)()()
    
    def read(self = None):
        return PlaceholderDetails.decode(self._memory_ia.infinite_details)

    
    def prepare_for_write(self = None, size = None):
        self._memory_ia.size = size

    
    def write(self = None, data = None, offset = None):
        self._lock.acquire()
        
        try:
            self._file_obj.seek(offset)
            self._file_obj.write(data)
            self._lock.release()
            return None
        except:
            self._lock.release()


    
    def read_data(self = None, offset = None, length = None):
        self._lock.acquire()
        
        try:
            self._file_obj.seek(offset)
            self._lock.release()
            return self._file_obj.read(length)[:self._memory_ia.size - offset]
        except:
            self._lock.release()


    
    def unset(self = None):
        self._memory_ia.infinite_details = None

    
    def reset(self = None, size = None):
        self._lock.acquire()
        
        try:
            self._file_obj.seek(0)
            self._file_obj.truncate()
            self._lock.release()
        except:
            self._lock.release()

        self._memory_ia.size = size

    
    def is_placeholder(self = None):
        return getattr(self._memory_ia, 'infinite_details', None) is not None

    
    def file_system_id(self = None):
        return 'fsid-' + make_unicode(self._local_path.db_lower())

    
    def resolve_path(self = None):
        return make_unicode(self._local_path.db_lower())

    
    def set_file_mtime(self = None, mtime = None):
        self._file_obj.metadata.mtime = mtime

    
    def simple_stat(self = None):
        return SimpleStat(volumeid = self._file_obj.metadata.volumeid, inode = self._file_obj.metadata.inode, mtime = self._file_obj.metadata.mtime, size = self._file_obj.metadata.size)


