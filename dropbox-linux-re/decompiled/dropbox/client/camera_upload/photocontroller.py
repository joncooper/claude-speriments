# Source Generated with Decompyle++
# File: photocontroller.pyc (Python 3.11)

import functools
import time
from typing import Any, Callable, List, Optional, Set, Text
from dropbox.camera import Device
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.camera_upload.camera_upload_metric_logger import MetricsLogger
from dropbox.client.camera_upload.photo_constants import ACTION_DEFAULTS_SET, OLD_PHOTO_ACTION
from dropbox.client.camera_upload.photodb import PhotoDb
from dropbox.client.camera_upload.photoimporter import PhotoDetails, PhotoImporter
from dropbox.client.camera_upload.photouploader import PhotoUploader
from dropbox.client.photodownloader.base import PhotoDownloaderBase
from dropbox.client.ui.common.camera import CameraUI
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.metrics.camera_upload import CameraEvent
from dropbox.platform import IS_WINDOWS
from dropbox.preferences import OPT_PHOTO, OPT_VIDEO
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.camera_uploads import CameraUploads
    from dropbox.client.camera_upload.session_context import SessionContext
    DoneCallbackType = Optional[Callable[([
        SessionContext,
        Optional[Exception],
        Set[PhotoDetails],
        List[PhotoDetails]], None)]]
    VoidCallbackType = Callable[([
        Optional[bool]], None)]

class PhotoController(object):
    
    def __init__(self, camera_uploads = None, account = None, sync_engine_adapter = None, uploader = ('camera_uploads', 'CameraUploads', 'account', 'AccountInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'uploader', 'PhotoUploader', 'return', 'None')):
        self._camera_uploads = camera_uploads
        self._account = account
        self._sync_engine_adapter = sync_engine_adapter
        self._ui = self._camera_uploads.camera_ui
        self._uploader = uploader
        self._photodb = self._uploader.photodb
        self._importer = None

    
    def _on_change_state_done(self, session_context, importer = None, done_cb = None, never_cb = None, old_action = (None, None, None, True), highlight = ('session_context', 'SessionContext', 'importer', 'PhotoImporter', 'done_cb', 'DoneCallbackType', 'never_cb', 'Optional[Callable[[Device], None]]', 'old_action', 'Optional[str]', 'highlight', 'bool', 'return', 'None')):
        transferred_files = importer.transferred_files.get()
        failed_files = importer.remaining_files
        skipped_files = importer.skipped_files
        error = importer.error.get()
        error_class = error.__class__.__name__ if error else 'unknown'
        total_size = (lambda .0: pass# WARNING: Decompyle incomplete
)(transferred_files())
        
        try:
            transferred = transferred_files()
            failed = failed_files()
            skipped = skipped_files()
            device_uid = session_context.get_device().uid
            import_result = self._ui.done(session_context, self._photodb.get_device_last_import(device_uid), transferred, skipped, failed, error, never_cb, old_action, highlight = highlight)
            self._photodb.set_device_last_import(device_uid, import_result)
        except Exception:
            (lambda .0: pass# WARNING: Decompyle incomplete
)
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.CAMERA_UPLOAD)

        if done_cb:
            done_cb(session_context, error, failed_files, transferred_files)
            return None
        return (lambda .0: pass# WARNING: Decompyle incomplete
)

    
    def on_change_state(self, session_context, importer, new_state, always = None, done_cb = None, never_cb = None, old_action = (False, None, None, None, True), highlight = ('session_context', 'SessionContext', 'importer', 'PhotoImporter', 'new_state', 'int', 'always', 'bool', 'done_cb', 'DoneCallbackType', 'never_cb', 'Optional[Callable[[Device], None]]', 'old_action', 'Optional[str]', 'highlight', 'bool', 'return', 'None')):
        TRACE('PhotoController: on_change_state new_state[%r], importer =[%r]', str(new_state), str(importer))
        if new_state == PhotoImporter.DONE:
            self._on_change_state_done(session_context, importer, done_cb, never_cb, old_action, highlight)
            return None
        if None == PhotoImporter.STARTING:
            MetricsLogger.report_step('start', session_context, always = always)
            MetricsLogger.report_camera_metrics(CameraEvent.FLOW_STARTING_IMPORT, session_context)
            return None
        if None == PhotoImporter.SCANNING:
            self._ui.importing()
            MetricsLogger.report_camera_metrics(CameraEvent.FLOW_FILE_SCANNING, session_context)
            return None
        if None == PhotoImporter.TRANSFERRING:
            MetricsLogger.report_camera_metrics(CameraEvent.FLOW_FILE_TRANSFERING, session_context)
            return None

    
    def hook_up_ui(self, session_context, importer, done_cb = None, never_cb = None, old_action = None, highlight = (None, None, None, True, True), import_videos = ('session_context', 'SessionContext', 'importer', 'PhotoImporter', 'done_cb', 'DoneCallbackType', 'never_cb', 'Optional[Callable[[], None]]', 'old_action', 'Optional[str]', 'highlight', 'bool', 'import_videos', 'bool', 'return', 'None')):
        self._ui.set_on_cancel(importer.cancel)
        self._ui.session_context = session_context
        self._ui.set_logger(MetricsLogger.get_logger_for_session(session_context))
        self._ui.starting(session_context.get_id(), import_videos = import_videos)
        importer.total_bytes.register(self._ui.finding)
        importer.cur_bytes.register(self._ui.progress)
        importer.transferred_files.register(self._ui.file_imported)
        on_change_state = functools.partial(self.on_change_state, session_context, importer, done_cb = done_cb, never_cb = never_cb, old_action = old_action, highlight = highlight)
        importer.state.register(on_change_state)
        importer.found_files.register(self._ui.file_count)



class CameraController(PhotoController):
    pass
# WARNING: Decompyle incomplete

