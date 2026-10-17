# Source Generated with Decompyle++
# File: drive_events_controller.pyc (Python 3.11)

import threading
from datetime import datetime, timezone
from typing import Optional
from apex.metrics import MetricsReporter
from build_number import is_test
from dropbox.client.features.external_drive_backup.constants import DiskArbitrationErrorOrigin, DriveArrivalCallback, DriveDepartureCallback, EDB_DA_HANDLER_TITLE, EDB_DA_RATELIMIT_PERIOD_SEC, ExternalDriveArrivalEvent
from dropbox.client.features.external_drive_backup.disk_arbitration import listen_to_external_drive_events
from dropbox.client.features.external_drive_backup.disk_arbitration.drive_events import ExternalDriveEventsProtocol
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger as Logger
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.environment import is_integration_tests
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.stormcrow.machine import MachineStormcrow
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.threadutils import StoppableThread
if IS_MAC:
    from macffi.CoreFoundation import CFRunLoopGetCurrent, CFRunLoopStop
elif IS_WINDOWS:
    import win32con
    import win32gui
    import win32process
EXTERNALDRIVEEVENTSTHREADNAME = 'EXTERNAL_DRIVE_EVENTS'

class ExternalDriveEvents(ExternalDriveEventsProtocol, StoppableThread):
    pass
# WARNING: Decompyle incomplete


class ExternalDriveEventsController(Destroyable):
    pass
# WARNING: Decompyle incomplete

