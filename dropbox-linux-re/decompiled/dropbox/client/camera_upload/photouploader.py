# Source Generated with Decompyle++
# File: photouploader.pyc (Python 3.11)

import errno
import functools
import os
import time
from abc import abstractmethod
from threading import Event
from typing import Any, Callable, Dict, List, Optional, Text, Union
from six import itervalues
from dropbox.camera import PhotoDetails
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.camera_upload.camera_upload_metric_logger import CameraEvent, CameraExtraMetric, MetricsLogger
from dropbox.client.camera_upload.photo_constants import CU_QUOTA_UNEARNED, DEFAULT_UPLOAD_LOCATION, ENABLED_BY_ADMIN
from dropbox.client.camera_upload.photodb import PendingPhoto, PhotoDb, SYNC_STATUS_PENDING, SYNC_STATUS_REPORT_CU_HASH
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.native_event import AutoResetEvent
from dropbox.native_threading import NativeCondition
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class FreshnessTracker:
    
    def __init__(self = None):
        self._last_seen = 0

    _freshness_required = (lambda self = None: pass)()()
    _max_time_to_wait = (lambda self = None: pass)()()
    _name = (lambda self = None: pass)()()
    
    def freshen(self = None):
        self._last_seen = time.time()

    
    def is_sufficiently_fresh(self = None):
        return self._last_seen >= time.time() - self._freshness_required

    _wait_for_results = (lambda self = None, event = None, expected_completion_time = handle_exceptions: if self.is_sufficiently_fresh():
Nonetime_left = None - time.time()if time_left <= 0:
TRACE('Took longer than %r seconds before calling wait_for_results(); proceeding', self._max_time_to_wait)NoneNone.wait(timeout = time_left)if not self.is_sufficiently_fresh():
TRACE('Waited %r seconds for %r out of total execution time of %r; proceeding', time_left, self._name, self._max_time_to_wait)None)()
    demand_freshness = (lambda self = None, account = None: if self.is_sufficiently_fresh():
Noneevent = AutoResetEvent()too_late = time.time() + self._max_time_to_waitthread = db_thread(StoppableThread)(target = self._get_and_handle_data, name = self._name + '_REFRESHER', args = (account, event))thread.daemon = TrueTRACE('Starting %r thread', self._name + '_REFRESHER')thread.start()functools.partial(self._wait_for_results, event, too_late))()
    
    def demand_freshness_async(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    _get_and_handle_data = (lambda self = None, account = None, event = abstractmethod: pass)()


class CuDataFreshnessTracker(FreshnessTracker):
    pass
# WARNING: Decompyle incomplete


class CuPolicyFreshnessTracker(FreshnessTracker):
    pass
# WARNING: Decompyle incomplete


class PhotoUploader(Actor, StoppableThread):
    
    def __init__(self, app = None, path = None, account = None, sync_engine_adapter = ('app', 'DropboxApplication', 'path', 'Text', 'account', 'AccountInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'n', 'Any', 'kw', 'Any', 'return', 'None'), *n, **kw):
        kw['name'] = 'PHOTOUPLOADER'
        Actor.__init__(self)
    # WARNING: Decompyle incomplete

    
    def _destroyable_component(self = None):
        return DesktopComponent.CAMERA_UPLOAD

    
    def add_photo(self = None, details = None):
        server_path = self._sync_engine_adapter.unicode_local_to_server(self.account, Text(details.path))
    # WARNING: Decompyle incomplete

    add_seen_photos = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def report_step(self = None, step = None, **event):
        event['step'] = step
        report('photo-import', data = event, account = self.account)

    register_location_tag = (lambda self = None: if not self.location:
report_bad_assumption('Attempted to register CU folder location when no location has been set.', component = self._destroyable_component())Nonenucleus_api = None._sync_engine_adapter.nucleus_api(self.account)# WARNING: Decompyle incomplete
)()
    _setup_sync_engine_adapter = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _clear_sync_engine_callbacks(self = None):
        api = self._sync_engine_adapter.nucleus_api(self.account)
    # WARNING: Decompyle incomplete

    on_pause_resume_callback = (lambda self = None, running = GlobalPool.dispatched_as_2('PhotoUploader.on_pause_resume_callback'): if running:
self.reindex()None)()()
    
    def freshen_policy_async(self = None):
        return self._policy_tracker.demand_freshness_async(self.account) if self._policy_tracker else (lambda x: x())

    handle_cu_data = (lambda self = None, ret = None: cu_data = ret.get('cu_data')# WARNING: Decompyle incomplete
)()
    on_sync_completed_summary_callback = (lambda self = None, summary = GlobalPool.dispatched_as_2('PhotoUploader.on_sync_completed_summary_callback'): if not self.photodb.has_pending():
Nonephotos = None# WARNING: Decompyle incomplete
)()()
    complete_photos = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def reindex(self = None):
        if not self.photodb.has_pending():
            return None
        
        try:
            photos = self.photodb.pending()
            if photos:
                deleted_photos = []
                for photo in photos:
                    TRACE('Photouploader: Reindex - photo in photodb.pending: %r', photo)
                    if photo.sync_status == SYNC_STATUS_PENDING:
                        full_path = Text(self._sync_engine_adapter.server_to_local(self.account, photo.server_path))
                        os.stat(full_path)
                        
                        try:
                            continue
                            except OSError:
                                e = None
                                if e.errno == errno.ENOENT:
                                    TRACE('Photouploader: Photo %r was deleted or renamed, blocklist %s', full_path, photo.blocklist)
                                    deleted_photos.append(photo)
                                else:
                                    report_exception(component = DesktopComponent.CAMERA_UPLOAD)
                                    
                                    try:
                                        e = None
                                        del e
                                        continue
                                        e = None
                                        del e
                                        
                                        try:
                                            continue
                                            if deleted_photos:
                                                self.photodb.update_status(deleted_photos, SYNC_STATUS_REPORT_CU_HASH)
                                            self.set_wakeup_event()
                                            return None
                                            return None
                                        except Exception:
                                            report_exception(component = DesktopComponent.CAMERA_UPLOAD)
                                            return None





    
    def set_wakeup_event(self = None):
        self.wakeup_cond
        self.wakeup_cond.notify()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def run(self = None):
        if not self.stopped():
            self.wakeup_cond
            self.wakeup_cond.wait()
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        if self.photodb.has_pending():
            self.complete_photos()
    # WARNING: Decompyle incomplete


