# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

from typing import Any, Callable, Dict, NamedTuple, Optional, Set, Union
from six import iteritems
from build_number.features import feature_enabled
from build_number.platform import IS_LINUX
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.home_feed.shared.util.gating import DESKTOP_TRAY_OQ_FOOTER_KILLSWITCH, OVERQUOTA_REDESIGN_STORMCROW
from dropbox.client.features.sync_error.controller.sync_error_controller import EMPTY_BREAKDOWN, SyncErrorController, VisibleErrorBreakdown
from dropbox.client.gandalf.base import Gandalf
from dropbox.client.notifications.notification_adapter import UserNotificationControllerAdapter
from dropbox.client.status.client_status import ClientStatus
from dropbox.client.status.interface import ClientStatusInterface, EngineStatus, PauseOrResume, StatusControllerInterface
from dropbox.client.status.label import StatusLabel, TRANSFER_LABELS
from dropbox.client.status.sync_engine_status import get_sync_engine_status
from dropbox.client.sync_ui_update_thread import on_sync_ui_update_thread_blocking, on_sync_ui_update_thread_returns_none, SyncUIUpdateThread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connectivity_watch.watch_interface import ConnectivityState
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.proto.nucleus.sync_failures_pb2 import GetSyncFailuresSummaryReply, GetSyncFailuresSummaryReq
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_adapter.throttled_sync_failures_api import ThrottledSyncFailuresApi
from dropbox.sync_engine_boundary.constants import SyncOperationFailureReason
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailuresSummary
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.threading import RLock
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
_StatusSnapshots = NamedTuple('_StatusSnapshots', [
    ('hash_status', Optional[TransferStatusSnapshot]),
    ('upload_status', Optional[TransferStatusSnapshot]),
    ('download_status', Optional[TransferStatusSnapshot]),
    ('percent_complete', Optional[float])])
_CombinedSnapshots = NamedTuple('_CombinedSnapshots', [
    ('combined_snapshot', _StatusSnapshots),
    ('sync_snapshot', _StatusSnapshots),
    ('backup_snapshot', _StatusSnapshots)])

class StatusController(StatusControllerInterface):
    _NO_LINKED_ACCOUNT_KEY = Account.get_dummy_account()
    
    def __repr__(self):
        return easy_repr(self, 'status_labels', 'status_callbacks', 'upload_status', 'download_status', 'hash_status')

    
    def __init__(self = None, sync_engine_adapter = None, notification_controller_adapter = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    _includes_backup = (lambda self = None: len(self._backup_instances) > 0)()
    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf

    
    def set_context(self = None, account = None, context = None):
        self._user_contexts[account] = context
        throttled_api_arc = ThrottledSyncFailuresApi.from_context(context)
        self._throttled_apis[account] = throttled_api_arc

    
    def get_context(self = None, account = None):
        return self._user_contexts.get(account, None)

    
    def release_throttled_apis(self = None):
        for _, v in self._throttled_apis.items():
            v.destroy()
        self._throttled_apis.clear()

    
    def register_backup_instance(self = None, account = None, instance = None):
        pass
    # WARNING: Decompyle incomplete

    _process_backup_sync_progress = (lambda self = None, account = None, progress = on_sync_ui_update_thread_returns_none(): pass# WARNING: Decompyle incomplete
)()
    
    def add_status_callback(self = None, callback = None):
        self.status_callbacks.add_handler(callback)

    
    def remove_status_callback(self = None, callback = None):
        self.status_callbacks.remove_handler(callback)

    
    def _run_callbacks(self = None):
        status = self.get_status()
        self.status_callbacks.run_handlers(status)

    
    def _add_account_to_map(self = None, account = None):
        self.lock
        if account in self._account_label_map:
            None(None, None)
            return None
        if None._NO_LINKED_ACCOUNT_KEY in self._account_label_map:
            self._account_label_map[account] = self._account_label_map.pop(StatusController._NO_LINKED_ACCOUNT_KEY)
        else:
            self._account_label_map[account] = { }
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def on_connectivity_changed(self = None, state = None):
        if state.state == ConnectivityState.DISCONNECTED:
            self.set_status_label_all_accounts(StatusLabel.LABEL_CONNECTING, True)
            return None
        None.set_status_label_all_accounts(StatusLabel.LABEL_CONNECTING, False)

    
    def on_account_changed(self = None, account = None, change_status = None):
        if change_status == AccountChangeType.LINK:
            if not account.is_primary:
                TRACE('StatusController: Secondary account linked!')
                self._run_callbacks()
                return None
            return None
        if None == AccountChangeType.REMOVE:
            self._account_label_map.pop(account, None)
            self._num_errors_map.pop(account, None)
            return None

    
    def _clear_labels(self = None, account = None):
        self.lock
        status_labels = self._account_label_map[account]
        for label in StatusLabel:
            status_labels[label] = False
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def _is_true_under_lock(self = None, status = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_true(self = None, status = None):
        self.lock
        None(None, None)
        return 
        with None:
            if not None, self._is_true_under_lock(status):
                pass

    
    def _pause_or_resume(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def setup_account(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    _process_sync_progress = (lambda self = None, account = None, progress = on_sync_ui_update_thread_returns_none(): pass# WARNING: Decompyle incomplete
)()
    
    def set_status_label(self = None, account = None, label = None, state = None, *, clear_previous, fail_if_set, fail_if_not_set):
        pass
    # WARNING: Decompyle incomplete

    
    def set_status_labels(self = None, account = None, labels_and_states = None, *, clear_previous, fail_if_set, fail_if_not_set):
        if not SyncUIUpdateThread.instance_stopped():
            return self._set_status_labels_on_sync_ui_thread(account, labels_and_states, clear_previous = clear_previous, fail_if_set = fail_if_set, fail_if_not_set = fail_if_not_set)
        TRACE('SyncUIUpdateThread is stopped / not started, not setting status label')
        return False

    _set_status_labels_on_sync_ui_thread = (lambda self = None, account = None, labels_and_states = None, *, clear_previous, fail_if_set, fail_if_not_set: self._set_status_labels(ac