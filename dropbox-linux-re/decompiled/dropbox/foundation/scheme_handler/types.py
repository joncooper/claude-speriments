# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import urllib.parse as urllib
from enum import Enum
from typing import Callable, Dict, NamedTuple, Optional, Text
from build_number import dropbox_version
from dropbox.client_api.connection_util import ConnectionResponse
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.foundation.scheme_handler.util import get_mime_type_for_ext

class ResourceType(Enum):
    MAINFRAME = 0
    SUBFRAME = 1
    STYLESHEET = 2
    SCRIPT = 3
    IMAGE = 4
    FONTRESOURCE = 5
    SUBRESOURCE = 6
    OBJECT = 7
    MEDIA = 8
    WORKER = 9
    SHAREDWORKER = 10
    PREFETCH = 11
    FAVICON = 12
    XHR = 13
    PING = 14
    SERVICEWORKER = 15
    CSPREPORT = 16
    PLUGINRESOURCE = 17
    UNKNOWN = 255


def scheme_handler_perf_logging_percentage():
    return 0.05 if dropbox_version.is_internal_alpha() else 0.01


class CustomSchemeHandlerResultType(Enum):
    UNKNOWN = 0
    BYTES = 1
    FILE = 2


def CustomSchemeHandlerResult():
    '''CustomSchemeHandlerResult'''
    bad_request = (lambda perf_session = None, reason = None: status = 400perf_session.add_extra('status_code', str(status))CustomSchemeHandlerResult(perf_session = perf_session, on_send = (lambda : pass), type = CustomSchemeHandlerResultType.BYTES, status = status, mimetype = get_mime_type_for_ext('txt'), headers = None, bytes = bytearray(reason, encoding = 'utf-8'), filename = None)
)()
    not_found = (lambda perf_session = None: status = 404perf_session.add_extra('status_code', str(status))CustomSchemeHandlerResult(perf_session = perf_session, on_send = (lambda : pass), type = CustomSchemeHandlerResultType.BYTES, status = status, mimetype = get_mime_type_for_ext('txt'), headers = None, bytes = bytearray(), filename = None)
)()
    from_data = (lambda data, perf_session = None, mimetype = None, on_send = staticmethod, status = ((lambda : pass), None, None), headers = ('data', 'bytearray', 'perf_session', 'PerfSession', 'mimetype', 'Text', 'on_send', 'Callable[[], None]', 'status', 'Optional[int]', 'headers', 'Optional[Dict[Text, Text]]', 'return', 'CustomSchemeHandlerResult'): pass# WARNING: Decompyle incomplete
)()
    from_file = (lambda filename = None, perf_session = None, mimetype = staticmethod, status = (None, None, None), headers = ('filename', 'Text', 'perf_session', 'PerfSession', 'mimetype', 'Optional[Text]', 'status', 'Optional[int]', 'headers', 'Optional[Dict[Text, Text]]', 'return', 'CustomSchemeHandlerResult'): pass# WARNING: Decompyle incomplete
)()
    from_connection_response = (lambda response = None, perf_session = None, status = staticmethod, headers = (200, None): headers_dict = { }# WARNING: Decompyle incomplete
)()

CustomSchemeHandlerResult = <NODE:27>(CustomSchemeHandlerResult, 'CustomSchemeHandlerResult', NamedTuple('CustomSchemeHandlerResult', [
    ('perf_session', PerfSession),
    ('on_send', Callable[([], None)]),
    ('type', CustomSchemeHandlerResultType),
    ('status', int),
    ('mimetype', Optional[Text]),
    ('headers', Optional[Dict[(Text, Text)]]),
    ('bytes', Optional[bytearray]),
    ('filename', Optional[Text])]))

def CustomSchemeUrlRequest():
    '''CustomSchemeUrlRequest'''
    create = (lambda url = None, method = None: sub_group_name = None# WARNING: Decompyle incomplete
)()

CustomSchemeUrlRequest = <NODE:27>(CustomSchemeUrlRequest, 'CustomSchemeUrlRequest', NamedTuple('CustomSchemeHandlerUrlRequest', [
    ('url', Text),
    ('method', Text),
    ('perf_session', PerfSession)]))
