# Source Generated with Decompyle++
# File: session_context.pyc (Python 3.11)

import datetime
import uuid
from typing import Callable, Dict, Optional, Text
from dropbox.client.authentication.account import Account
from dropbox.client.camera_upload.camera_upload_metric_logger import CameraEvent, CameraExtraMetric, MetricsLogger
from dropbox.client.camera_upload.types import CameraImportAction, CameraSplashResponse, CUDeviceUID
from dropbox.client.features.external_drive_backup.cu_edb_chooser import is_edb_preferred_device, OnboardingSuppressionReasons
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.multiaccount.role import Roles
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption
from dropbox.lock_ordering import NonRecursiveLock
from dropbox.preferences import OPT_VIDEO
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.camera import Device
    from dropbox.client.camera_upload.camera_upload_context import CameraUploadContext
    from dropbox.client.camera_upload.camera_uploads import CameraUploads
    from dropbox.client.camera_upload.configuration_manager import CameraConfigurationManager

class SessionContext:
    
    def __init__(self = None, camera_uploads = None, device = None, next_device_callback = (None,), handle_user_accept = ('camera_uploads', 'CameraUploads', 'device', 'Device', 'next_device_callback', 'Callable[[Optional[bool]], None]', 'handle_user_accept', 'Optional[Callable[[], None]]', 'return', 'None')):
        self._camera_uploads = camera_uploads
        self._device = device
        self._next_device_callback = next_device_callback
        self._user_accept_callback = handle_user_accept
        self._session_id = uuid.uuid4().hex
        self._upload_context = None
        self._splash_close_callback = None
        self._splash_opened_time = None
        self._has_started_import = False
        self._lock = NonRecursiveLock()
        device.logger = MetricsLogger.get_logger_for_session(self)

    _splash_open = (lambda self = None: self._splash_opened_time is not None)()
    _splash_open = (lambda self = None, is_open = None: self._splash_opened_time = datetime.datetime.now() if is_open else None)()
    
    def _get_config(self = None):
        return self._camera_uploads.get_config()

    
    def _get_import_video_primary(self = None):
        return self._get_config().get_primary_local_config()[OPT_VIDEO]

    
    def get_log_data(self = None):
        return dict(session_id = self._session_id, mfg = self._device.manufacturer, model = self._device.model, device_uid = self._device.uid, device_name = self._device.name, type = self._device.__class__.__name__)

    
    def get_device(self = None):
        return self._device

    
    def get_context(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_id(self = None):
        return self._session_id

    
    def get_account(self = None):
        if self._upload_context:
            return self._upload_context.get_account()

    
    def get_linked_account_count(self = None):
        account_manager = self._camera_uploads.get_app().account_manager
    # WARNING: Decompyle incomplete

    
    def matches(self = None, device = None, device_uid = None):
        if device:
            return self._device == device
        if None:
            return self._device.uid == device_uid

    
    def set_ready_device(self = None, device = None):
        pass
    # WARNING: Decompyle incomplete

    
    def ask_user(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def handle_migration(self = None):
