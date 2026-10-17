# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import ctypes
import os
from typing import Any, Dict, Optional, Text, Tuple
import pywintypes
import win32api
import win32evtlog
import win32service
import winerror
from pynt.helpers.registry import registry_key, safe_read_registry_value
from win32api import RegOpenKeyEx, RegQueryValueEx
from win32con import HKEY_LOCAL_MACHINE, KEY_READ, KEY_WOW64_64KEY
from dropbox.trace import TRACE
DRIVER_NAME = 'dbx'
SERVICE_NAME = 'DbxSvc'
VERSION_REG_VALUE_NAME = 'Version'

def _get_version_from_key(key_name = None):
    version = None
    key = registry_key(HKEY_LOCAL_MACHINE, key_name)
    if key:
        version = safe_read_registry_value(key, VERSION_REG_VALUE_NAME)
    None(None, None)


def get_running_version():
    version = _get_version_from_key('System\\CurrentControlSet\\services\\' + DRIVER_NAME + '\\Volatile')
    return version


def is_driver_running():
    return get_running_version() is not None


def is_service_checking_client_signature():
