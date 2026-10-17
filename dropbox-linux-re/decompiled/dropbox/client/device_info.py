# Source Generated with Decompyle++
# File: device_info.pyc (Python 3.11)

from __future__ import absolute_import, annotations, division, print_function
import hashlib
import os
import uuid
from typing import Any, Dict, Mapping, NamedTuple, Optional, Text, Tuple, Union
from uuid import getnode
import psutil
from apex._apex import lib as apex_lib
from apex.metrics import Metric, MetricsReporter
from lib.cpuid.api import processor_info
from dropbox.client.gandalf import Gandalf
from dropbox.client.util import get_sanitized_executable_path, TRACE
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.linux.client_info import MissingMachineID
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.util import safe_navigate
DeviceInfo = NamedTuple('DeviceInfo', [
    ('cpuid_process_info', Optional[Dict[(Text, Any)]]),
    ('mac_address', Optional[int]),
    ('serial_number', Text),
    ('manufacturer', Text),
    ('model', Text)])

def _parse_windows_csp_info(csp_info = None):
    serial_number = safe_navigate(csp_info, 'identifying_number')
    manufacturer = safe_navigate(csp_info, 'vendor')
    model = safe_navigate(csp_info, 'name')
    return (serial_number, manufacturer, model)


def _parse_mac_client_info(client_info = None):
    serial_number = safe_navigate(client_info, 'serial_number')
    manufacturer = safe_navigate(client_info, 'manufacturer')
    model = safe_navigate(client_info, 'model')
    return (serial_number, manufacturer, model)


def _get_mac_address():
    
    try:
        mac_address = getnode()
    except Exception:
        mac_address = None

    return mac_address


def UNSAFE_get_raw_machine_uuid():
    
    try:
        if IS_MAC:
            get_mac_client_info = get_mac_client_info
            import dropbox.mac.client_info
            return uuid.UUID(get_mac_client_info()['platform_uuid'])
        if None:
            get_machine_guid = get_machine_guid
            import dropbox.win32.win_client_info
            return get_machine_guid()
        get_machine_id = get_machine_id
        import dropbox.linux.client_info
        return get_machine_id()
    except MissingMachineID:
        report_exception(severity = Severity.TRACE, component = DesktopComponent.EVENT_REPORTING)
        return 
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.EVENT_REPORTING)
            return 



class MachineID:
    
    def __init__(self = None, hashed = None):
        self.hashed = hashed

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete



def get_machine_uuid():
    raw_uuid = UNSAFE_get_raw_machine_uuid()
    zero_id = uuid.UUID(int = 0)
    if raw_uuid == zero_id:
        return MachineID(None)
    hashed_uuid = hashlib.sha256(raw_uuid.bytes)
    return MachineID(hashed_uuid)


def get_machine_uuid_migration():
    status = apex_lib.read_machine_id_stormcrow_flag_from_cache()
    if status:
        return get_machine_uuid()
    return UNSAFE_get_raw_machine_uuid()


def set_machine_uuid_gandalf_callback(gandalf = None, metrics_reporter = None):
    pass
# WARNING: Decompyle incomplete


def get_process_start_time():
    
    try:
        running_process = psutil.Process(os.getpid())
        return running_process.create_time()
    except Exception:
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.EVENT_REPORTING)
        return 0



def get_device_info():
    if IS_WINDOWS:
        get_wmi_csp_info = get_wmi_csp_info
        import dropbox.win32.win_client_info
        (serial_number, manufacturer, model) = _parse_windows_csp_info(get_wmi_csp_info())
    elif IS_MAC:
        get_mac_client_info = get_mac_client_info
        import dropbox.mac.client_info
        (serial_number, manufacturer, model) = _parse_mac_client_info(get_mac_client_info())
    else:
        return None
    device_info = DeviceInfo(cpuid_process_info = processor_info(), mac_address = _get_mac_address(), serial_number = serial_number, manufacturer = manufacturer, model = model)
    return device_info


def report_mac_install_permission_info():
    if not IS_MAC:
        return None
    
    try:
        install_path = get_sanitized_executable_path()
        can_write_app_folder = os.access('/Applications', os.W_OK)
        can_exec_app_folder = os.access('/Applications', os.X_OK)
        report('mac-install-permissions', install_path = install_path, can_write_app_folder = can_write_app_folder, can_exec_app_folder = can_exec_app_folder)
        return None
    except Exception:
        report_exception(severity = Severity.DEBUG, component = DesktopComponent.EVENT_REPORTING)
        return None


