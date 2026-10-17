# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from typing import Dict, Optional, Text
from apex.metrics import MetricsReporter
from dropbox.client.features.external_drive_backup.constants import DriveArrivalCallback, DriveDepartureCallback
from dropbox.client.features.external_drive_backup.disk_arbitration.drive_events import ExternalDriveEventsProtocol
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo

def listen_to_external_drive_events(thread = None, arrival_callback = None, departure_callback = None, metrics_reporter = (False,), include_virtual_image = ('thread', 'ExternalDriveEventsProtocol', 'arrival_callback', 'DriveArrivalCallback', 'departure_callback', 'DriveDepartureCallback', 'metrics_reporter', 'MetricsReporter', 'include_virtual_image', 'Optional[bool]', 'return', 'None')):
    pass


def debug_list_drives(metrics_reporter = None):
    return { }

