# Source Generated with Decompyle++
# File: error_reporting.pyc (Python 3.11)

from typing import Optional, Set, Text
from errors import message_from_js_stack, report_view_exception
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineStormcrow
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.exception_info.bridge_gen.bridge_interface_error_reporter import ErrorReporterBridgeInterface
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.common import HtmlViewJavaScriptErrorSource, HtmlViewJavaScriptErrorType, HtmlViewLoggerEvent, HtmlViewStateMachine
from dropbox.foundation.runtime import ExitCode, panic_with_report
from dropbox.trace import TRACE

class ErrorReporter(ErrorReporterBridgeInterface, Actor):
    pass
# WARNING: Decompyle incomplete

