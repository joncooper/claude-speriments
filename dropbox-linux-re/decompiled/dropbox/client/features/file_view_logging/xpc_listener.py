# Source Generated with Decompyle++
# File: xpc_listener.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Mapping, Optional, Text
from build_number import BUILD_KEY, is_frozen
from six import add_metaclass
from dropbox.client.ui.common.harmony import log_journal_event
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
if IS_MAC:
    from Foundation import NSURL
    from macffi.xpc import XPCCallbacks, XPCClient, XPCMessage
    from dropbox.mac.internal import autoreleasepool
OCTAVE_XPC_SERVICE_NAME = f'''com.getdropbox.{BUILD_KEY.lower()}.activityprovider'''.encode('utf-8')
XPC_INTERRUPTION_MAX_RETRIES = 5

class BookmarkCreationException(Exception):
    pass

XPCClientConsuming = <NODE:12>()
ActivityProviderListener = <NODE:12>()
