# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

import os
import re
import shutil
from functools import partial
from typing import Any, Callable, Dict, Mapping, Optional, Text, Tuple
import psutil
from apex.metrics import MetricsReporter
from AppKit import NSURL
from macffi.CoreFoundation import CFRunLoopRun
from pymac.helpers.disk import get_volume_desc_for_mount_point, register_arrival_callback, register_departure_callback, register_external_drive_listener_session
from dropbox.client.features.external_drive_backup.constants import DiskArbitrationErrorOrigin, DriveArrivalCallback, DriveDepartureCallback, ExternalDriveArrivalEvent
from dropbox.client.features.external_drive_backup.disk_arbitration.drive_events import ExternalDriveEventsProtocol
from dropbox.client.features.external_drive_backup.disk_helpers import is_remote_drive
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger as Logger
from dropbox.client.features.external_drive_backup.trace import EDB_WARN
from dropbox.client.features.external_drive_backup.utils import is_drive_writable
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_action_surface import EdbActionSurface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import retry, RetryException
from dropbox.mac.version import MAC_VERSION, VENTURA
from dropbox.trace import TRACE
IS_VENTURA_OR_LATER = MAC_VERSION >= VENTURA
MAX_CREATE_SESSION_RETRY = 3
compute_drive_info = (lambda volume_info = None, metrics_reporter = None: pass# WARNING: Decompyle incomplete
)()
build_drive_info = (lambda vol_mount = None, metrics_reporter = None, source = handle_exceptions: try:
volume_info = get_volume_desc_for_mount_point(vol_mount)volume_usage = shutil.disk_usage(vol_mount)volume_uuid = volume_info.get('DAVolumeUUID', None)volume_uuid_int = volume_uuid.int if volume_uuid else 0volume_name = volume_info.get('DAVolumeName', 'Unknown')volume_type = volume_info.get('DAVolumeType', 'Unknown')media_writable = volume_info.get('DAMediaWritable', None)is_writable = is_drive_writable(vol_mount, media_writable)is_remote = is_remote_drive(vol_mount)DriveInfo(id = str(volume_uuid_int), fs_type = volume_type, mount_path = vol_mount, is_writable = is_writable, is_remote = is_remote, current_usage = volume_usage.used, name = volume_name, current_capacity = str(volume_usage.total))except Exception:
exc = NoneLogger.report_event(metrics_reporter = metrics_reporter, event_name = ExternalBackupEvent.build_drive_info_fail, account = None, session_id = None, source = source, exception = repr(exc), exception_type = exc.__class__.__name__)report_exception(severity = Severity.TRACE, component = DesktopComponent.SYNC_EVERYTHING)exc = Nonedel excNoneexc = Nonedel exc)()
on_external_drive_arrival = (lambda volume_info = None, callback = None, metrics_reporter = handle_exceptions: arrival_info = compute_drive_info(volume_info, metrics_reporter)# WARNING: Decompyle incomplete
)()
on_external_drive_departure = (lambda volume_info = None, callback = None: raw_drive_path = volume_info.get('DAVolumePath', None)if not raw_drive_path:
Nonedrive_path = NSURL.URLWithString_(str(raw_drive_path)).path()callback(drive_path))()

def listen_to_external_drive_events(thread = None, arrival_callback = None, departure_callback = None, metrics_reporter = (False,), include_virtual_image = ('thread', 'ExternalDriveEventsProtocol', 'arrival_callback', 'DriveArrivalCallback', 'departure_callback', 'DriveDepartureCallback', 'metrics_reporter', 'MetricsReporter', 'include_virtual_image', 'Optional[bool]', 'return', 'None')):
    counter = 0
    session = register_arrival_callback(callback = partial(on_external_drive_arrival, callback = arrival_callback, metrics_reporter = metrics_reporter), session = None, include_virtual_image = include_virtual_image)
    register_departure_callback(callback = partial(on_external_drive_departure, callback = departure_callback), session = session)
# WARNING: Decompyle incomplete


def debug_list_drives(metrics_reporter = None):
    pass
# WARNING: Decompyle incomplete

