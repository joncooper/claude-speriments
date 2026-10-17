# Source Generated with Decompyle++
# File: bridge_interface_external_drive_backup_permissions_view_model.pyc (Python 3.11)

from abc import ABC, abstractmethod
from dropbox.foundation.futures import Future
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent

class ExternalDriveBackupPermissionsViewModelBridgeInterface(ABC):
    cancel_setup = (lambda self = None, drive_info = None, session_logging_id = abstractmethod, source = ('drive_info', 'DriveInfo', 'session_logging_id', 'str', 'source', 'EdbSource', 'return', 'Future[None]'): pass)()
    retry_backup = (lambda self = None, drive_info = None, session_logging_id = abstractmethod, source = ('drive_info', 'DriveInfo', 'session_logging_id', 'str', 'source', 'EdbSource', 'return', 'Future[None]'): pass)()
    log_event = (lambda self, drive_info = None, event_name = None, session_logging_id = abstractmethod, source = ('drive_info', 'DriveInfo', 'event_name', 'ExternalBackupEvent', 'session_logging_id', 'str', 'source', 'EdbSource', 'return', 'Future[None]'): pass)()

