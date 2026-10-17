# Source Generated with Decompyle++
# File: server.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import hashlib
import json
import logging
import os
import socket
import tempfile
import threading
import time
from typing import Any
import tornado.httpserver as tornado
import tornado.ioloop as tornado
import tornado.web as tornado
from tornado.netutil import bind_sockets
from build_number import is_frozen
from build_number.environment import is_valid_time_limited_cookie, magic_trace_key_is_set
from dropbox.client.util import get_contents_root, get_repo_root_unfrozen
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_bytes
from dropbox.trace import TRACE
from dropbox.webdebugger.handlers import webdebugger_handler_cpu, webdebugger_handler_memory, webdebugger_handler_num_fds, webdebugger_handler_threads, webdebugger_handler_version, webdebugger_handler_wid, webdebugger_handler_yappi_start, webdebugger_handler_yappi_stop
from dropbox.webdebugger.webpdb import WebPdbHandler

class WebDebuggerAPIHandler(tornado.web.RequestHandler):
    
    def initialize(self, _webdebugger_handler_func, **kwargs):
        self.func = _webdebugger_handler_func
        self._on_finish_cb = kwargs.pop('on_finish_cb', None)
        self.kwargs = kwargs

    
    def get(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def on_finish(self = None):
        if self._on_finish_cb:
            self._on_finish_cb()
            return None



class WebDebugger(object):
    pass
# WARNING: Decompyle incomplete

