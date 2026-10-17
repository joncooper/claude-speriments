# Source Generated with Decompyle++
# File: db_image_capture_core_factory.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Optional
from ImageCaptureCore import ICDeviceLocationTypeMaskLocal, ICDeviceTypeMaskCamera
from dropbox.client.photodownloader.mac.objc_image_capture_core import ObjCICDeviceBrowser
from dropbox.client.photodownloader.mac.stub_image_capture_core import StubICDeviceBrowser
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.photodownloader.mac.db_image_capture_core import DBICDeviceBrowser
DBICDeviceLocationTypeMaskLocal = ICDeviceLocationTypeMaskLocal
DBICDeviceTypeMaskCamera = ICDeviceTypeMaskCamera
PATRONUS_ENV_VAR_NAME = 'PATRONUS_CAMERA_UPLOAD'

def get_patronus_cu_provided_path():
    if is_patronus():
        return os.environ[PATRONUS_ENV_VAR_NAME]


def is_patronus():
    return PATRONUS_ENV_VAR_NAME in os.environ


class DBImageCaptureCoreFactory(object):
    build_device_browser = (lambda : if not is_patronus():
ObjCICDeviceBrowser()observable_path = get_patronus_cu_provided_path()TRACE('Patronus camera upload test. observable path %s', observable_path)# WARNING: Decompyle incomplete
)()

