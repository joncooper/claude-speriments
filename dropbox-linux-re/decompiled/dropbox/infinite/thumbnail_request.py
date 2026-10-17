# Source Generated with Decompyle++
# File: thumbnail_request.pyc (Python 3.11)

from typing import Any
from dropbox.client_api.thumbnailer import ThumbnailSize
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.shared.local_path import LocalPath

class ThumbnailRequest:
    __slots__ = [
        'local_path',
        'size',
        'creation_time',
        'strategy',
        'mtime']
    
    def __init__(self = None, local_path = None, size = None, mtime = ('local_path', 'LocalPath', 'size', 'ThumbnailSize', 'mtime', 'float', 'return', 'None')):
        self.local_path = local_path
        self.size = size
        self.creation_time = get_monotonic_time_seconds()
        self.strategy = 'v2_request'
        self.mtime = mtime

    
    def __hash__(self = None):
        return hash((self.local_path, self.size, self.mtime))

    
    def __eq__(self = None, other = None):
        return (self.local_path, self.size, self.mtime) == (other.local_path, other.size, other.mtime)

    
    def __repr__(self):
        return 'local_path: {}, size: {}, mtime: {}'.format(self.local_path, self.size, self.mtime)


