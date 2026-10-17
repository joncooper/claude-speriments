# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod
from enum import Enum
from typing import NamedTuple, Optional, Text, Union
from dropbox.foundation.context import ContextInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.bridge.interface import ViewBridgeSerializable
from dropbox.foundation.html_views.common.bridge_gen.bridge_interface_view_anchor import ViewAnchorBridgeInterface
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.raii2.quick import Destroyable
CorsWhitelistEntry = NamedTuple('CorsWhitelistEntry', [
    ('sourceOrigin', Text),
    ('targetScheme', Text),
    ('targetDomain', Text)])

class StandaloneHtmlViewLocation(Enum):
    CENTER_MAIN = 0


class HtmlViewLoadErrorType(Enum):
    NO_INTERNET_CONNECTION = 0
    CONTENT_ERROR = 1
    TIMEOUT_ERROR = 2
    MISCELLANEOUS_ERROR = 3


def HtmlViewLoadingErrorData():
    '''HtmlViewLoadingErrorData'''
    pass

HtmlViewLoadingErrorData = <NODE:27>(HtmlViewLoadingErrorData, 'HtmlViewLoadingErrorData', NamedTuple('HtmlViewLoadingErrorData', [
    ('type', HtmlViewLoadErrorType),
    ('debug_message', Text),
    ('code', Optional[int])]))

class HtmlViewContentErrorType(Enum):
    UNKNOWN = 0
    CSP_VIOLATION = 1
    JAVASCRIPT_ERROR = 2
    CERTIFICATE_ERROR = 3


def HtmlViewCSPViolationErrorData():
    '''HtmlViewCSPViolationErrorData'''
    pass

HtmlViewCSPViolationErrorData = <NODE:27>(HtmlViewCSPViolationErrorData, 'HtmlViewCSPViolationErrorData', NamedTuple('HtmlViewCSPViolation', [
    ('blocked_uri', Text),
    ('violated_directive', Text),
    ('source', Text),
    ('line', int)]))

class HtmlViewJavaScriptErrorSource(Enum):
    UNKNOWN = 'unknown'
    NATIVE_EXCEPTION_HANDLER = 'native_exception_handler'
    BRIDGED_EXCEPTION_HANDLER = 'bridged_exception_handler'
    NATIVE_CONSOLE_HANDLER = 'native_console_handler'


class HtmlViewJavaScriptErrorType(Enum):
    UNKNOWN = 'unknown'
    EXCEPTION = 'exception'
    PROMISE_REJECTION = 'promise_rejection'
    BRIDGE_ERROR = 'bridge_error'
    UNRECOVERABLE_ERROR = 'unrecoverable_error'


def HtmlViewJavaScriptErrorData():
    '''HtmlViewJavaScriptErrorData'''
    pass

HtmlViewJavaScriptErrorData = <NODE:27>(HtmlViewJavaScriptErrorData, 'HtmlViewJavaScriptErrorData', NamedTuple('HtmlViewJavaScriptErrorData', [
    ('message', Text),
    ('js_stack', Text),
    ('source', HtmlViewJavaScriptErrorSource),
    ('type', HtmlViewJavaScriptErrorType)]))

def HtmlViewCertificateErrorData():
    '''HtmlViewCertificateErrorData'''
    pass

HtmlViewCertificateErrorData = <NODE:27>(HtmlViewCertificateErrorData, 'HtmlViewCertificateErrorData', NamedTuple('HtmlViewCertificateErrorData', [
    ('blocked_uri', Text),
    ('message', Text)]))
HtmlViewContentErrorData = Union[(HtmlViewCSPViolationErrorData, HtmlViewJavaScriptErrorData, HtmlViewCertificateErrorData)]

class ViewAnchorConfiguration(object):
    
    def __init__(self = None, machine_context = None, context = None, navigation_service = (None,), window_manager_delegate = ('machine_context', 'MachineContext', 'context', 'ContextInterface', 'navigation_service', 'NavigationServiceInterface', 'window_manager_delegate', 'Optional[WindowManagerDelegateInterface]', 'return', 'None')):
        self._machine_context = machine_context
        self._context = context
        self._navigation_service = navigation_service
        self._window_manager_delegate = window_manager_delegate

    machine_context = (lambda self = None: self._machine_context)()
    context = (lambda self = None: self._context)()
    navigation_service = (lambda self = None: self._navigation_service)()
    window_manager_delegate = (lambda self = None: self._window_manager_delegate)()


class ViewAnchorInterface(ViewAnchorBridgeInterface, Destroyable):
    pass
# WARNING: Decompyle incomplete


class HtmlViewAffinityGroup(Enum):
    DEFAULT = 0
    POPOVERS_AND_TRANSIENTS = 1
    TRAY = 2
    FORCE_UNIQUE = 3

