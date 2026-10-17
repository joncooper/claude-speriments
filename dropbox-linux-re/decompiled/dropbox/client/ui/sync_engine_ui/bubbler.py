# Source Generated with Decompyle++
# File: bubbler.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from apex.metrics import Metric
from dropbox.client.ui.sync_engine_ui.notification_generator import NotificationGenerator
from dropbox.client.ui.sync_engine_ui.strategies.notification_strategy import NotificationStrategy
from dropbox.client.ui.sync_engine_ui.strategies.rosf_strategy import ROSFStrategy
from dropbox.client.ui.sync_engine_ui.sync_notification_dispatcher import SyncNotificationDispatcher
from dropbox.client.ui.sync_engine_ui.utils import SYNC_NOTIFICATION_AMP_NAMESPACE, SyncNotificationSettings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.metrics.function_usage import FuncMetricsMixin, logged_method
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, ConflictResolutionAttempt, ConflictResolutionType, MountChangeOperation
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class SyncEngineBubbler(Actor, UserSingleton, FuncMetricsMixin):
    _dropbox_app: 'DropboxApplication' = 'SyncEngineBubbler'
    
    def __init__(self = None, context = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _destroyable_component(self = None):
        return DesktopComponent.SYNC_ENGINE

    
    def __destroy__(self = None):
        pass
    # WARNING: Decompyle incomplete

    _on_sync_completed_summary = (lambda self = None, sync_completed_summary = None: pass# WARNING: Decompyle incomplete
)()
    _handle_on_conflict_resolution_attempt = (lambda self = None, attempt = None: self.on_conflict_resolution_attempt_callback(attempt))()
    _handle_on_mount_changed = (lambda self = None, mount_changed_operation = None: self.on_mount_finished_callback(mount_changed_operation))()
    _handle_on_sync_progress = (lambda self = None, sync_progress = None: self.nucleus_synced_event_callback(sync_progress))()
    register_app = (lambda cls = None, app = None: cls._dropbox_app = app)()
    
    def nucleus_synced_event_callback(self = None, sync_progress = None):
        if sync_progress.phase == SyncPhase.SYNCED:
            TRACE('bubbler nucleus_synced_event_callback synced')
            self._dispatcher.dispatch()
            return None

    on_conflict_resolution_attempt_callback = (lambda self = None, attempt = None: if not attempt.success:
Noneif None.conflict_type == ConflictResolutionType.PERMISSION:
self._rosf_strategy.aggregate_rosf_bubble(1, attempt.conflicted_copy_local_path)Noneif None.conflict_type == ConflictResolutionType.MOVE_REVERTED:
self._notif_generator.show_move_reverted_bubble(attempt.conflicted_copy_local_path)None)()
    on_mount_finished_callback = (lambda self = None, mount_changed_operation = None: self._notif_generator.on_mount_finished_callback(mount_changed_operation))()

