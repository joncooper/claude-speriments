# Source Generated with Decompyle++
# File: uuidstore.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import hmac
import struct
import uuid
from hashlib import md5
from os import makedirs as _makedirs, path as _path, remove as _remove
from typing import Dict, IO, List, Optional, Text
from uuid import UUID
from six import iteritems
from dropbox.camera.fromfiledevice import ReadFromFile
from dropbox.client.camera_upload.types import CUDeviceUID
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.fileutils import can_write_file
from dropbox.functions import make_bytes
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
MAGIC = 0xA4D7A5F1
VERSION = 1
HEADER = struct.pack('!LL', MAGIC, VERSION)
HEADERLEN = len(HEADER)
ENTRYLEN = 48
MAX_STORE_LENGTH = 1048576
HMAC_KEY = b'52\xdd\x14M\xcf.\x03\xe6\xeb\xf7D\x7fw\xfe5'
DEVICE_ID_FOLDER = 'MISC'
DEVICE_ID_PATH = '.dropbox.device'
WIN_ERROR_WRITE_PROTECT = 19
WIN_ERROR_IO_DEVICE = 1117

def user_id_to_key(user_id = None):
    return md5(make_bytes(str(user_id))).digest()


def new_uuid():
    return uuid.uuid4()

DEFAULT_USER_ID = 0

class UUIDStore(object):
    
    def __init__(self = None):
        self._uuids = { }
        self._dirty = False

    
    def _get_single_dict_value(self = None, dict = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_uuid(self = None):
        default_key = user_id_to_key(DEFAULT_USER_ID)
        if default_key in self._uuids:
            return CUDeviceUID(str(self._uuids[default_key]))
        if len(self._uuids) == 1:
            return CUDeviceUID(str(self._get_single_dict_value(self._uuids)))
        if len(self._uuids) > 1:
            result = self._get_single_dict_value(self._uuids)
            self._uuids[default_key] = result
            self._dirty = True
            return CUDeviceUID(str(result))

    
    def get_or_generate_uuid(self = None):
        device_uid = self.get_uuid()
        if device_uid:
            return device_uid
        return None.generate_uuid_and_return()

    
    def generate_uuid_and_return(self = None):
        device_uuid = new_uuid()
        self._uuids[user_id_to_key(DEFAULT_USER_ID)] = device_uuid
        self._dirty = True
        return CUDeviceUID(str(device_uuid))



def compute_hmac(payload = None, hmac_key = None):
    return hmac.new(hmac_key, payload, digestmod = md5).digest()

if IS_WINDOWS:
    from winffi.kernel32.api import FILE_ATTRIBUTE_HIDDEN, FILE_ATTRIBUTE_SYSTEM, GetFileAttributesW, SetFileAttributesW
    
    def set_hidden(path = None):
        
        try:
            attrs = GetFileAttributesW(path)
            SetFileAttributesW(path, attrs | FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM)
            return None
        except Exception:
            report_exception(component = DesktopComponent.CAMERA_UPLOAD)
            return None


    
    def clear_hidden(path = None):
        
        try:
            SetFileAttributesW(path, 0)
            return None
        except Exception:
            return None


else:
    
    def set_hidden(path = None):
        pass

    
    def clear_hidden(path = None):
        pass


class MalformedUUIDStore(Exception):
    pass


class SDCardUUIDStore(UUIDStore):
    pass
# WARNING: Decompyle incomplete


class SDCardDevice(ReadFromFile):
    pass
# WARNING: Decompyle incomplete

