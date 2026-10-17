# Source Generated with Decompyle++
# File: _base.pyc (Python 3.11)

import json
from abc import abstractmethod
from collections import defaultdict, deque
from typing import Any, Callable, Deque, Dict, List, Optional, Set, Text
from _interface import ElectronIpc, ElectronIpcConnectionState, JSONDict
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.sentry import capture_raw_sentry_envelope
from dropbox.exception.severity import Severity
from dropbox.foundation.html_views.bridge.errors import message_from_js_stack, report_view_exception
from dropbox.foundation.html_views.common import HtmlViewJavaScriptErrorType
from dropbox.foundation.signals import Signal
from dropbox.foundation.signals.standard import StandardSignal
from dropbox.foundation.trace.trace_js_bridge import JavaScriptBridgeEventTracing
from dropbox.threading import Lock
from dropbox.trace import TRACE

class ElectronIpcBase(ElectronIpc):
    pass
# WARNING: Decompyle incomplete

