# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import
import os
from contextlib import contextmanager
from datetime import datetime
from typing import Any, Callable, IO, Iterator, List, Optional, Text
from  import Device
from filetypes import image_or_video, nonphoto_image
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.fastwalk_bridge import fastwalk_with_exception_handling
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_REGULAR
from dropbox.trace import TRACE

class OnDiskFile(object):
    __slots__ = ('id', '_name', '_size', '_time', '_path')
    
    def __init__(self, id, name = None, size = None, mtime = None, path = ('id', 'int', 'name', 'Text', 'size', 'int', 'mtime', 'Optional[datetime]', 'path', 'Text', 'return', 'None')):
        self.id = id
        self._name = name
        self._size = size
        self._time = mtime
        self._path = path

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    open = (lambda self = None, fs = None: pass# WARNING: Decompyle incomplete
)()
    
    def name(self = None):
        return self._name

    
    def size(self = None):
        return self._size

    
    def time(self = None):
        return self._time



def is_apple_device(device = None):
    pass
# WARNING: Decompyle incomplete

_NOKIA_IMAGES_PATH = os.path.join('Images', 'Camera')
_NOKIA_VIDEOS_PATH = os.path.join('Videos')

def find_dcim(srcpath = None):
    paths = []
    dcim_path = os.path.join(srcpath, 'DCIM')
    nokia_images = os.path.join(srcpath, _NOKIA_IMAGES_PATH)
    nokia_videos = os.path.join(srcpath, _NOKIA_VIDEOS_PATH)
    if os.path.isdir(nokia_images) and os.path.isdir(nokia_videos):
        TRACE('This is a suspected Symbian device')
        paths += [
            _NOKIA_IMAGES_PATH,
            _NOKIA_VIDEOS_PATH]
    if os.path.exists(dcim_path) and os.path.isdir(dcim_path):
        paths.append('DCIM')
        for path in (os.path.join('PRIVATE', 'AVCHD', 'BDMV', 'STREAM'), 'SD_VIDEO', 'VIDEO', 'MP_ROOT'):
            full_path = os.path.join(srcpath, path)
            if os.path.exists(full_path) and os.path.isdir(full_path):
                paths.append(path)
    return paths if paths else None


def get_images(root = None, paths = None, blacklist_nonphotos = None, is_path_hidden = (False, None, None), is_filename_hidden = ('return', 'Iterator[OnDiskFile]')):
    pass
# WARNING: Decompyle incomplete

