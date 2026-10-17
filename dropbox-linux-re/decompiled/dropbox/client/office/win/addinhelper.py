# Source Generated with Decompyle++
# File: addinhelper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import os
from typing import Any, Optional, Text
import six
from build_number import assert_full_msix_no_registry_writes
from build_number.constants import OFFICE_ADDIN_VERSION
from pynt.constants import KEY_ALL_ACCESS, REG_DWORD, REG_SZ
from pynt.helpers.registry import create_registry_key, enum_registry_values, hkey_to_str, registry_key, safe_delete_regkey, safe_read_registry_value, set_registry_value
from six.moves.winreg import HKEY_CURRENT_USER
from winrpcserver_native import ffi
from dropbox.client.background_worker import on_background_thread
from dropbox.client.office.base import BaseOfficeAddInHelper, BaseOfficeAddInHelperFactory
from dropbox.client.office.constants import CONFIG_KEY_USER_INTERACTED_WITH_ADDIN_SETTINGS, OfficeAddInMetrics, RegistryCheckValues
from dropbox.client.rpcserver.rpcserver import E_FAIL, rpc_function, S_OK
from dropbox.client.util.win import register_module, unregister_module
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.signals import SignalConnection
from dropbox.harmony.models.types import WindowFile
from dropbox.harmony.window_tracking.window_file_map import WindowFileMap
from dropbox.preferences import OPT_OFFICE_ADDIN
from dropbox.trace import TRACE
from dropbox.win32.version import OFFICE2013
OFFICE_ADDIN_VERSION_INDEPENDENT_PROG_ID = 'Dropbox.OfficeAddIn'

class WinOfficeAddInHelper(BaseOfficeAddInHelper):
    pass
# WARNING: Decompyle incomplete


class WinOfficeAddInHelperFactory(BaseOfficeAddInHelperFactory):
    _CLASS = WinOfficeAddInHelper

