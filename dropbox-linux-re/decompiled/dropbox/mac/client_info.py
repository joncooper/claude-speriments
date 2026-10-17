# Source Generated with Decompyle++
# File: client_info.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import sys
from typing import Dict, Optional, Text
from pymac.constants import kIOPlatformSerialNumberKey, kIOPlatformUUIDKey, kManufacturerKey, kModelKey
from pymac.helpers.iokit import get_io_platform_expert_device_properties

def get_mac_client_info():
    client_info_dict = get_io_platform_expert_device_properties([
        kIOPlatformUUIDKey,
        kIOPlatformSerialNumberKey,
        kManufacturerKey,
        kModelKey])
    manufacturer = client_info_dict.get(kManufacturerKey)
# WARNING: Decompyle incomplete

