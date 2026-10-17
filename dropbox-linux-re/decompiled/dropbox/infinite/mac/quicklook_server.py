# Source Generated with Decompyle++
# File: quicklook_server.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import threading
from typing import Any, Callable, Optional, Text
import objc
from Foundation import NSDefaultRunLoopMode, NSMachBootstrapServer, NSMachPort, NSObject, NSRunLoop
from macinfinite.quicklook import CFRunLoopGetCurrent, CFRunLoopRunInMode, CFRunLoopStop, kCFRunLoopDefaultMode, quicklook_parse_request, QUICKLOOK_REQUEST_TYPE_CANCEL_PREVIEW, QUICKLOOK_REQUEST_TYPE_CANCEL_THUMBNAIL, QUICKLOOK_REQUEST_TYPE_PREVIEW, QUICKLOOK_REQUEST_TYPE_THUMBNAIL, quicklook_send_reply, QuickLookRequest
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client_api.thumbnailer import Thumbnailer
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.infinite.thumbnail_server import ThumbnailRequest, ThumbnailServer, ThumbnailSize
from dropbox.mac.internal import autoreleasepool
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.gandalf import Gandalf
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
QUICKLOOK_SERVER_THREAD_NAME = 'QUICKLOOK_SERVER'

class RegisterPortException(Exception):
    default_message = (lambda self = None: 'Failed to register quicklook server port, it appears someone else is using it.')()


class _QuickLookServerThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class _QuickLookServerDelegate(NSObject):
    
    def initWithServer_thread_(self = None, server = None, thread = None):
        self = objc.super(_QuickLookServerDelegate, self).init()
        self._server = server
        self._thread = thread
        return self

    handleMachMessage_ = (lambda self = None, message = objc.typedSelector(b'v@:@'): pass# WARNING: Decompyle incomplete
)()()


class QuickLookServer(ThumbnailServer):
    pass
# WARNING: Decompyle incomplete

