# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import re
from typing import Optional
from dropbox.client.camera_upload.types import CUDeviceUID
from dropbox.client.photodownloader.base import PhotoDownloaderBase
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.configuration_manager import CameraConfigurationManager

def use_photouploader():
    if IS_MAC:
        return True
    if None:
        return True
    if None:
        return False
    raise 'Unknown platform'()


def create_photodownloader(camera_config = None, *n, **kw):
    pass
# WARNING: Decompyle incomplete

WIN_WDP_DEVICE_ID_PATTERN = '^(.*)\\{.*\\}$'

def parse_wpd_id(device_id = None):
