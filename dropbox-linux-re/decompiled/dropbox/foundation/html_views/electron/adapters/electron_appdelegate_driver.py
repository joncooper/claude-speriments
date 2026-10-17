# Source Generated with Decompyle++
# File: electron_appdelegate_driver.pyc (Python 3.11)

from apex.metrics import MetricsReporter
from AppKit import NSApplication
from dropbox.client.ui.cocoa.application_delegate import ApplicationDelegateInterface
from dropbox.client.util import hard_exit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.trace import TRACE

class ElectronAppDelegateDriver(Actor):
    pass
# WARNING: Decompyle incomplete

