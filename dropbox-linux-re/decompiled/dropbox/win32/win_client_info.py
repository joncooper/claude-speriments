# Source Generated with Decompyle++
# File: win_client_info.pyc (Python 3.11)

from __future__ import absolute_import, division
import copy
import ctypes
import datetime
import re
import sys
import uuid
from ctypes.wintypes import FILETIME
from types import MappingProxyType
from typing import Any, cast, Dict, List, Mapping, Optional, Text, Tuple, Type, Union
import pywintypes
from pynt.constants import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS, KEY_ALL_ACCESS, KEY_READ, KEY_WOW64_64KEY
from pynt.dlls.kernel32 import kernel32
from pynt.helpers.registry import delete_registry_value, enum_registry_values, registry_key, safe_read_registry_value
from six import string_types
from build_number import BUILD_KEY
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.functions import convert_to_twos_complement
from dropbox.win32.com_helper import uses_com

try:
    import wmi
    wmi_import_exc_info = None
except Exception:
    wmi_import_exc_info = sys.exc_info()

MYPY = False
if MYPY:
    from types import TracebackType
    ExcInfo = Tuple[(Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType])]
BIOS_ATTRIBUTES = [
    'BIOSVersion',
    'BuildNumber',
    'Caption',
    'CodeSet',
    'CurrentLanguage',
    'Description',
    'IdentificationCode',
    'InstallableLanguages',
    'InstallDate',
    'LanguageEdition',
    'ListOfLanguages',
    'Manufacturer',
    'Name',
    'OtherTargetOS',
    'PrimaryBIOS',
    'ReleaseDate',
    'SerialNumber',
    'SMBIOSBIOSVersion',
    'SMBIOSMajorVersion',
    'SMBIOSMinorVersion',
    'SMBIOSPresent',
    'SoftwareElementID',
    'SoftwareElementState',
    'Status',
    'TargetOperatingSystem',
    'Version']
CSP_ATTRIBUTES = [
    'Caption',
    'Description',
    'IdentifyingNumber',
    'Name',
    'SKUNumber',
    'UUID',
    'Vendor',
    'Version']
CS_ATTRIBUTES = [
    'Manufacturer']
CS_ATTRIBUTES_MSI = [
    'Manufacturer',
    'Model']
CPU_ATTRIBUTES = [
    'AddressWidth',
    'Architecture',
    'Description',
    'Family',
    'Name',
    'NumberOfCores']
SYSINFO_ATTRIBUTES = [
    'SystemSKU']
SYSTEM_ENCLOSURE_ATTRIBUTES = [
    'ChassisTypes',
    'InstallDate',
    'Manufacturer',
    'Model',
    'Name',
    'OtherIdentifyingInfo',
    'PartNumber',
    'SerialNumber',
    'SKU',
    'Tag',
    'TypeDescriptions',
    'Version']
OS_ATTRIBUTES = [
    'BuildNumber',
    'BuildType',
    'Caption',
    'CodeSet',
    'CountryCode',
    'CreationClassName',
    'CurrentTimeZone',
    'InstallDate',
    'LastBootUpTime',
    'LocalDateTime',
    'Locale',
    'MUILanguages',
    'NumberOfUsers',
    'OperatingSystemSKU',
    'Organization',
    'OSArchitecture',
    'OSLanguage',
    'OSProductSuite',
    'OSType',
    'ServicePackMajorVersion',
    'ServicePackMinorVersion',
    'Status',
    'SuiteMask',
    'Version']
DISK_DRIVES_ATTRIBUTES = [
    'Manufacturer',
    'Model',
    'SerialNumber']
MONITOR_ATTRIBUTES = [
    'ManufacturerName',
    'SerialNumberID']
BASE_BOARD_ATTRIBUTES = [
    'Manufacturer',
    'Product',
    'SerialNumber']
PNP_ENTITY_ATTRIBUTES = [
    'ClassGuid',
    'PNPDeviceID']
MSI_PNP_HID_CLASS_GUID = '{745a17a0-74d3-11d0-b6fe-00a0c90f57da}'
MSI_PNP_GRAPHICS_CARD_CLASS_GUIDE = '{4d36e968-e325-11ce-bfc1-08002be10318}'
MSI_PNP_HID_VID = '0DB0'
MSI_PNP_GRAPHICS_CARD_VEN_NVIDIA = '10DE'
MSI_PNP_GRAPHICS_CARD_VEN_AMD = '1002'
MSI_PNP_GRAPHICS_CARD_SUBSYS = '1462'
REGISTRY_KEYS = dict(ua_key = (HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\5.0\\User Agent\\Post Platform', KEY_READ | KEY_WOW64_64KEY, None), ua64_key = (HKEY_LOCAL_MACHINE, 'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\5.0\\User Agent\\Post Platform', KEY_READ, None), lenovo_mfgdate = (HKEY_LOCAL_MACHINE, 'SOFTWARE\\Lenovo\\ExperienceImprovement', KEY_READ | KEY_WOW64_64KEY, 'MFGDate'))

def _convert_from_camel_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', '\\1_\\2', name)
    return re.sub('([a-z0-9])([A-Z])', '\\1_\\2', s1).lower()


def _get_info_from_wmi_class(obj_list, attributes):
    return _get_single_from_wmi_class(obj_list[0], attributes)


def _get_list_info_from_wmi_class(obj_list, attributes):
    class_info = []
    for obj in obj_list:
        class_info.append(_get_single_from_wmi_class(obj, attributes))
        return class_info


def _get_single_from_wmi_class(obj, attributes):
    class_info = { }
    for attr in attributes:
        key = _convert_from_camel_case(attr)
        val = getattr(obj, attr)
        if isinstance(val, tuple):
            val = bytes(val).decode('ascii').strip('\x00')
        
    if isinstance(val, string_types):
        val = val.strip()
    class_info[key] = val
    continue
    return class_info


def _is_msi_pnp_peripheral(wmi_entity = None, expected_class_guid = None, expected_ven = None, expected_vid = (None, None, None), expected_subsys_end = ('wmi_entity', 'Any', 'expected_class_guid', 'str', 'expected_ven', 'Union[Optional[str], Optional[List[str]]]', 'expected_vid', 'Optional[str]', 'expected_subsys_end', 'Optional[str]', 'return', 'bool')):
    pass
# WARNING: Decompyle incomplete

_SILENT_WMI_EXCEPTION_CODES = set([
    0x80041002,
    0x80080005,
    0x80070005,
    0x80041013])

def _maybe_report_wmi_exception(exc_info = None):
    if not exc_info[1]:
        report_exception(severity = Severity.DEBUG, exc_type = exc_info[0], exc_val = exc_info[1], exc_traceback = exc_info[2], component = DesktopComponent.UNKNOWN)
        return None
    exc = None[1]
    has_error_code = getattr(exc, 'hresult', None) is not None
    if not has_error_code:
        report_exception(severity = Severity.DEBUG, exc_type = exc_info[0], exc_val = exc_info[1], exc_traceback = exc_info[2], component = DesktopComponent.UNKNOWN)
        return None
    
    try:
        hresult = convert_to_twos_complement(cast(pywintypes.com_error, exc).hresult)
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
        return None

    if hresult in _SILENT_WMI_EXCEPTION_CODES:
        report_exception(severity = Severity.TRACE, exc_type = exc_info[0], exc_val = exc_info[1], exc_traceback = exc_info[2], component = DesktopComponent.UNKNOWN)
        return None
    report_exception(severity = Severity.DEBUG, exc_type = exc_info[0], exc_val = exc_info[1], exc_traceback = exc_info[2], component = DesktopComponent.UNKNOWN)

_wmi_info_cache: 'Dict[str, Dict[str, Any]]' = { }
_wmi_csp_info_cache: 'Dict[str, Any]' = { }
_get_wmi_csp_info_fetch = (lambda wmi_inst = None: if wmi_import_exc_info:
_maybe_report_wmi_exception(wmi_import_exc_info){ }report_app_framework_event('get_wmi_csp_info_triggered')if not wmi_inst:
try:
wmi_inst = wmi.WMI()except Exception:
report_app_framework_event('get_wmi_csp_info_failed', reason = 'wmi_creation')try:
_get_info_from_wmi_class(wmi_inst.Win32_ComputerSystemProduct(), CSP_ATTRIBUTES)except Exception:
report_app_framework_event('get_wmi_csp_info_failed', reason = 'csp_attributes'){ })()

def _get_wmi_csp_info_cached(wmi_inst = None):
    global _wmi_csp_info_cache
    if _wmi_csp_info_cache:
        return _wmi_csp_info_cache
    _wmi_csp_info_cache = _get_wmi_csp_info_fetch(wmi_inst)
    return _wmi_csp_info_cache


def get_wmi_csp_info(wmi_inst = None):
    return MappingProxyType(_get_wmi_csp_info_cached(wmi_inst))

_get_wmi_info = (lambda gandalf = None, dealcode = None: 