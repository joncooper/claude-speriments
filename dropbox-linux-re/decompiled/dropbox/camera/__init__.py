# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import
import datetime
import time
from contextlib import contextmanager
from typing import Any, Callable, Dict, Iterator, MutableSequence, Optional, Text, Tuple, Union
from mypy_extensions import Arg, DefaultArg, KwArg
from dropbox.client.camera_upload.types import CUDeviceUID
from dropbox.functions import split_extension
from dropbox.metrics.camera_upload import CameraEvent
from dropbox.repr_utils import easy_repr
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import ServerPath
(IMPORT_SUCCESS, IMPORT_UNKNOWN_ERROR, IMPORT_LOW_DROPBOX_SPACE, IMPORT_LOW_DISK_SPACE) = range(4)
DeviceID = Union[(str, int)]

class PhotoImportExceptionBase(Exception):
    pass


class PhotoImportCanceled(PhotoImportExceptionBase):
    pass


class PhotoImportDisconnected(PhotoImportExceptionBase):
    pass


class PhotoImportLowDropboxSpace(PhotoImportExceptionBase):
    pass


class PhotoImportDeviceLocked(PhotoImportExceptionBase):
    pass


class PhotoImportSelectiveSync(PhotoImportExceptionBase):
    pass
# WARNING: Decompyle incomplete


class PhotoImportNoConnectionError(PhotoImportExceptionBase):
    pass


class PhotoImportNotReady(PhotoImportExceptionBase):
    pass


class PhotoImportPhotoFailedToImport(PhotoImportExceptionBase):
    pass


class Device:
    PROPS: 'Tuple[str, ...]' = ('id', 'manufacturer', 'model', 'name', 'serialnum', 'uid', 'locked', 'ready', 'logger', 'needs_ptp_connect_check', 'handle_user_accept', 'skip_initial_drive_access', 'mount_path')
    
    def __init__(self = None, _id = None):
        self.id = _id
        self.manufacturer = None
        self.model = None
        self.name = None
        self.serialnum = None
        self.uid = None
        self.locked = False
        self.ready = False
        self.logger = None
        self.needs_ptp_connect_check = False
        self.handle_user_accept = None
        self.skip_initial_drive_access = False
        self.mount_path = None

    
    def __eq__(self = None, other = None):
        if not other:
            return False
        return None.id == other.id

    
    def __ne__(self = None, other = None):
        return not (self == other)

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def make_default(self = None):
        pass

    
    def release(self = None):
        pass

    
    def handle_disconnect_exceptions(self = None, e = None):
        pass

    
    def formatted_device_id(self = None):
        return str(self.id)

    
    def override_disabled(self = None):
        return False

    
    def establish_uid(self = None):
        pass

    
    def is_trackable(self = None):
        return True

    percent = (lambda self = None: 100)()
    files = (lambda self = None: pass)()
    
    def files_to_read(self = None, files_to_read = None):
        pass

    
    def did_read_file(self = None, camera_file = None):
        pass



class File:
    __slots__ = ()
    id = (lambda self = None: pass)()
    
    def name(self = None):
        pass

    
    def time(self = None):
        pass

    
    def size(self = None):
        pass

    open = (lambda self = None, fs = None, cache = contextmanager: pass)()


class PhotoDetails:
    __slots__ = ('blocklist', 'size', 'mtime', 'path', 'cu_hash_8', 'cu_hash_full', 'exif', 'f_obj', 'f_name', 'f_basename', 'f_ext', 'f_time', 'photo_name', 'photo_time', 'signature', 'mp4_creation_time')
    
    def __init__(self = None, f_obj = None):
        self.mtime = time.time()
        self.f_obj = f_obj
        self.f_time = f_obj.time()
        self.size = f_obj.size()
        self.f_name = f_obj.name()
        (self.f_basename, self.f_ext) = split_extension(self.f_name)
        self.signature = None
        self.path = None
        self.cu_hash_8 = None
        self.cu_hash_full = None
        self.exif = None
        self.photo_name = None
        self.photo_time = None
        self.blocklist = None
        self.mp4_creation_time = None

    
    def __repr__(self = None):
        return easy_repr(self, 'f_obj', 'f_time', 'size', 'f_name')


CameraSessionLogger = Callable[([
    Arg(CameraEvent, 'event'),
    DefaultArg(Optional[File], 'cu_file'),
    KwArg(Text)], None)]
CameraFileLogger = Callable[([
    Arg(CameraEvent, 'event'),
    KwArg(Text)], None)]
