# Source Generated with Decompyle++
# File: com.pyc (Python 3.11)

from __future__ import absolute_import
import functools
from typing import Any, Callable, Optional, Text, TypeVar
import comtypes.client as comtypes
from comtypes import COMError
from pynt.constants import COM_ERROR_DISP_E_EXCEPTION, COM_ERROR_DISP_E_UNKNOWNNAME, COM_ERROR_NO_INTERFACE, COM_ERROR_OBJECT_DELETED, COM_ERROR_OBJECT_REQUIRED, COM_ERROR_RPC_CALL_FAILED, COM_ERROR_RPC_DISCONNECTED, COM_ERROR_RPC_REJECTED, COM_ERROR_RPC_SERVER_UNAVAILABLE, COM_ERROR_RPC_SYS_CALL_FAILED
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import convert_to_twos_complement
from dropbox.repr_utils import easy_repr
from dropbox.trace import TRACE

class RPCError(Exception):
    pass
# WARNING: Decompyle incomplete


class COMAttributeError(RPCError):
    pass

COM_ERROR_RPC_S_UNKNOWN_IF = 0x800706B5
COM_ERROR_TYPE_E_REGISTRYACCESS = 0x8002801C
RPC_ERRORS = (COM_ERROR_NO_INTERFACE, COM_ERROR_RPC_S_UNKNOWN_IF, COM_ERROR_TYPE_E_REGISTRYACCESS, COM_ERROR_RPC_REJECTED, COM_ERROR_RPC_DISCONNECTED, COM_ERROR_RPC_CALL_FAILED, COM_ERROR_RPC_SERVER_UNAVAILABLE, COM_ERROR_RPC_SYS_CALL_FAILED)
RPC_ERROR_MESSAGES = {
    COM_ERROR_RPC_SYS_CALL_FAILED: 'RPC system call failed',
    COM_ERROR_RPC_SERVER_UNAVAILABLE: 'RPC server unavailable',
    COM_ERROR_RPC_DISCONNECTED: 'RPC client disconnected',
    COM_ERROR_RPC_REJECTED: 'RPC call rejected',
    COM_ERROR_RPC_CALL_FAILED: 'RPC call failed',
    COM_ERROR_TYPE_E_REGISTRYACCESS: "COM registration database couldn't be opened",
    COM_ERROR_RPC_S_UNKNOWN_IF: 'COM Interface is unknown',
    COM_ERROR_NO_INTERFACE: 'COM Interface not supported' }
INVALID_PTR_ERRORS = (COM_ERROR_DISP_E_EXCEPTION, COM_ERROR_DISP_E_UNKNOWNNAME, COM_ERROR_OBJECT_DELETED, COM_ERROR_OBJECT_REQUIRED)

class COMWrapper(object):
    
    def __init__(self, com_object):
        self.__dict__['_com_object'] = com_object

    
    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            raise AttributeError(name)
        
        try:
            value = getattr(self._com_object, name)
            if isinstance(value, (comtypes.client.dynamic._Dispatch, comtypes.client.lazybind.Dispatch)):
                value = COMWrapper(value)
            return value
        except (AttributeError, NameError, TypeError):
            raise COMAttributeError(f'''{self._com_object!r}: could not get attribute {name!s}''')


    
    def __setattr__(self, name, value):
        if name.startswith('__') and name.endswith('__'):
            raise AttributeError(name)
        
        try:
            return setattr(self._com_object, name, value)
        except (AttributeError, NameError, TypeError):
            raise COMAttributeError(f'''{self._com_object!r}: Could not set attribute {name!s} to {value!r}''')


    
    def __repr__(self):
        return '<COM Wrapper %r>' % self._com_object


_F = TypeVar('_F', bound = Callable)

def handle_rpc_errors(should_raise = None, return_value = None, invalid_pointer_handler = None):
    pass
# WARNING: Decompyle incomplete

