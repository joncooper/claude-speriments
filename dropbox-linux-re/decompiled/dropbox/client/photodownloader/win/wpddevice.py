# Source Generated with Decompyle++
# File: wpddevice.pyc (Python 3.11)

from __future__ import absolute_import
import datetime
import functools
from contextlib import contextmanager
from ctypes import byref, cast, create_string_buffer, POINTER, sizeof
from ctypes.wintypes import LPCWSTR, LPWSTR
from typing import Any, AnyStr
from comtypes import COMError
from comtypes.automation import VARIANT
from comtypes.client import CreateObject
from comtypes.GUID import GUID
from comtypes.util import byref_at
from pynt.constants import COM_ERROR_INVALID_PARAMETER, COM_ERROR_NOT_FOUND
from pynt.dlls.ole32 import ole32
from six.moves import range
from dropbox.camera import Device, File
from dropbox.camera.filetypes import image_or_video, nonphoto_image
from dropbox.client.camera_upload.camera_handler import CameraHandler
from dropbox.client.photodownloader import parse_wpd_id
from dropbox.client.photodownloader.win.autoplay_defaults import change_autoplay_default
from dropbox.client.photodownloader.win.constants import DROPBOX_AUTOPLAY_HANDLER_NAME
from dropbox.client.photodownloader.win.helpers import DbxDeviceDisconnectedException, handle_device_disconnect_exceptions
from dropbox.client.photodownloader.win.portable_device import IPortableDevice, IPortableDevicePropVariantCollection, IPortableDeviceValues, PROPERTYKEY
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.functions import convert_to_twos_complement
from dropbox.repr_utils import easy_repr
from dropbox.trace import TRACE
from dropbox.win32.com_helper import initialized_com
WPD_OBJECT_CONTENT_TYPE = PROPERTYKEY(GUID('{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}'), 7)
WPD_OBJECT_ORIGINAL_FILE_NAME = PROPERTYKEY(GUID('{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}'), 12)
WPD_OBJECT_SIZE = PROPERTYKEY(GUID('{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}'), 11)
WPD_OBJECT_DATE_CREATED = PROPERTYKEY(GUID('{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}'), 18)
WPD_OBJECT_DATE_MODIFIED = PROPERTYKEY(GUID('{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}'), 19)
WPD_CLIENT_DESIRED_ACCESS = PROPERTYKEY(GUID('{204D9F0C-2292-4080-9F42-40664E70F859}'), 9)
WPD_RESOURCE_DEFAULT = PROPERTYKEY(GUID('{E81E79BE-34F0-41BF-B53F-F1A06AE87842}'), 0)
WPD_OBJECT_ISHIDDEN = PROPERTYKEY(GUID('{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}'), 9)
WPD_DEVICE_MANUFACTURER = PROPERTYKEY(GUID('{26D4979A-E643-4626-9E2B-736DC0C92FDC}'), 7)
WPD_DEVICE_MODEL = PROPERTYKEY(GUID('{26D4979A-E643-4626-9E2B-736DC0C92FDC}'), 8)
WPD_DEVICE_SERIAL_NUMBER = PROPERTYKEY(GUID('{26D4979A-E643-4626-9E2B-736DC0C92FDC}'), 9)
WPD_DEVICE_FRIENDLY_NAME = PROPERTYKEY(GUID('{26D4979A-E643-4626-9E2B-736DC0C92FDC}'), 12)
WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT = GUID('{99ED0160-17FF-4C44-9D98-1D7A6F941921}')
WPD_CONTENT_TYPE_FOLDER = GUID('{27e2e392-a111-48e0-ab0c-e17705a05f85}')
WPD_CONTENT_TYPE_IMAGE = GUID('{ef2107d5-a52a-4243-a26b-62d4176d7603}')
WPD_CONTENT_TYPE_VIDEO = GUID('{9261b03c-3d78-4519-85e3-02c5e1f50bb9}')
GENERIC_READ = 0x80000000
GENERIC_WRITE = 1073741824
WPD_DEVICE_OBJECT_ID = LPCWSTR('DEVICE')

class WpdFile(File):
    __slots__ = ('_id', 'resource', '_name', '_size', '_time', 'curpos', 'transfer_block_size', 'stream', '_buffer', 'opened')
    
    def __init__(self, id, resource, name, size, mtime):
        self._id = id
        self._name = name
        self._size = size
        self._time = mtime
        self.resource = resource
        self.opened = False

    id = (lambda self = None: self._id)()
    
    def name(self = None):
        return self._name

    
    def size(self = None):
        return self._size

    
    def time(self = None):
        return self._time

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    open = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def read(self, size = (-1,)):
        remaining = self._size - self.curpos
        TRACE('file_read: %s, id: %s, curpos = %d, size = %d, remaining = %d', self._name, self.id, self.curpos, size, remaining)
        if size < 0 or size > remaining:
            size = remaining
        read_size = min(self.transfer_block_size, size)
        bytes_read = self.stream.Read(self._buffer, read_size)
        TRACE('Read %d bytes from %s', bytes_read, self.name)
        return self._buffer[:bytes_read]



class WpdDevice(Device):
    pass
# WARNING: Decompyle incomplete


def _wstr_array_free(obj_ids_array, i):
    pwchar = cast(byref_at(obj_ids_array, sizeof(LPWSTR) * i), POINTER(LPWSTR)).contents
    ole32.CoTaskMemFree(pwchar)


def _get_obj_name(obj_id, obj_props):
    
    try:
        name = obj_props.GetStringValue(byref(WPD_OBJECT_ORIGINAL_FILE_NAME))
    except Exception:
        name = None

    if name == None:
        name = obj_id + '.data'
    return name


def _create_file_object(resource, obj_id, obj_props, name):
    filesize = int(obj_props.GetStringValue(byref(WPD_OBJECT_SIZE)))
    filename = name
    mtime = _get_obj_mtime(obj_props)
    TRACE('Found image file %s', filename)
    return WpdFile(id = obj_id, resource = resource, name = filename, size = filesize, mtime = mtime)


def _get_obj_mtime(obj_props):
    ret = None
    
    try:
        ctime = obj_props.GetValue(byref(WPD_OBJECT_DATE_CREATED))
        ret = ctime
    except Exception:
        pass

    
    try:
        mtime = obj_props.GetValue(byref(WPD_OBJECT_DATE_MODIFIED))
        TRACE('Returning modification time: %r', mtime)
        ret = mtime
    except Exception:
        if not ret:
            TRACE('!! No creation or modification time on this file!')
        else:
            TRACE('Returning creation time: %r', ret)

    return ret

