# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import socket
import struct
from ctypes import addressof, byref, c_char, c_char_p, c_uint, c_ulong, create_string_buffer, POINTER, sizeof, Structure, windll
from ctypes.wintypes import BOOL, BYTE, DWORD, ULONG
import winerror
from pynt.helpers.general import windows_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.functions import make_str
MAX_ADAPTER_DESCRIPTION_LENGTH = 128
MAX_ADAPTER_NAME_LENGTH = 256
MAX_ADAPTER_ADDRESS_LENGTH = 8

class IP_ADDR_STRING(Structure):
    pass

LP_IP_ADDR_STRING = POINTER(IP_ADDR_STRING)
IP_ADDR_STRING._fields_ = [
    ('next', LP_IP_ADDR_STRING),
    ('ipAddress', c_char * 16),
    ('ipMask', c_char * 16),
    ('context', DWORD)]

class IP_ADAPTER_INFO(Structure):
    pass

LP_IP_ADAPTER_INFO = POINTER(IP_ADAPTER_INFO)
IP_ADAPTER_INFO._fields_ = [
    ('next', LP_IP_ADAPTER_INFO),
    ('comboIndex', DWORD),
    ('adapterName', c_char * (MAX_ADAPTER_NAME_LENGTH + 4)),
    ('description', c_char * (MAX_ADAPTER_DESCRIPTION_LENGTH + 4)),
    ('addressLength', c_uint),
    ('address', BYTE * MAX_ADAPTER_ADDRESS_LENGTH),
    ('index', DWORD),
    ('type', c_uint),
    ('dhcpEnabled', c_uint),
    ('currentIpAddress', LP_IP_ADDR_STRING),
    ('ipAddressList', IP_ADDR_STRING),
    ('gatewayList', IP_ADDR_STRING),
    ('dhcpServer', IP_ADDR_STRING),
    ('haveWins', BOOL),
    ('primaryWinsServer', IP_ADDR_STRING),
    ('secondaryWinsServer', IP_ADDR_STRING),
    ('leaseObtained', c_ulong),
    ('leaseExpires', c_ulong)]
_GetAdaptersInfo = windll.iphlpapi.GetAdaptersInfo
_GetAdaptersInfo.restype = DWORD
_GetAdaptersInfo.argtypes = [
    c_char_p,
    POINTER(ULONG)]
MAX_RETRIES = 5

def GetAdaptersInfo():
    adapterInfo = create_string_buffer(sizeof(IP_ADAPTER_INFO))
    buflen = ULONG(sizeof(adapterInfo))
    result = _GetAdaptersInfo(adapterInfo, byref(buflen))
    if result not in (winerror.ERROR_SUCCESS, winerror.ERROR_BUFFER_OVERFLOW):
        raise windows_error(result)
    i = 0
# WARNING: Decompyle incomplete


def generate_adapter_info():
    pass
# WARNING: Decompyle incomplete


def generate_ipaddresses():
    pass
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    print(list(generate_ipaddresses()))
    return None
