# Source Generated with Decompyle++
# File: windows_package_reporter.pyc (Python 3.11)

import time
from apex.metrics import Metric, MetricsReporter
from build_number import dropbox_version
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import WINDOWS_PACKAGE_MANAGER_EVENT
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.win32.version import WIN10, WIN10_VERSION_2109, WINDOWS_VERSION, WINDOWS_VERSION_STRING
    if WINDOWS_VERSION.version_number() >= WIN10.version_number():
        import _bowbow
    else:
        _bowbow = None
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def reduce_windows_version(windows_version_str = None):
    if windows_version_str.startswith('11 '):
        return 'Windows11'
    if None.startswith('10 '):
        return 'Windows10'


class MoreThanOnePackage(Exception):
    pass


class WindowsPackageReporter:
    
    def __init__(self = None, app = None):
        self._machine_id = str(UNSAFE_get_raw_machine_uuid())
        context = app.app_model.machine_context
        metrics_reporter = context.metrics_reporter
        self._metrics_reporter = metrics_reporter.child({ })

    
    def report(self = None):
        pass
    # WARNING: Decompyle incomplete


