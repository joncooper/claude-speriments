# Source Generated with Decompyle++
# File: ui_types.pyc (Python 3.11)

import time
from abc import ABCMeta, abstractmethod
from enum import Enum, IntEnum
from typing import Any, Callable, cast, Dict, List, NamedTuple, Optional, Text, Tuple
from six import add_metaclass
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.ui.common.strings import shorten_filename
from dropbox.i18n import trans
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.shared.local_path import LocalPath
from dropbox.shared.validated_record import Field, ValidatedRecord
from dropbox.sync_engine_boundary.infinite.recall_events import FAILURE_STATUSES, InfiniteRecallDownloadProgress, InfiniteRecallEvent, InfiniteRecallStatus

class InfiniteUIKextInstallFlowSource(Enum):
    UI_DEBUG = 0
    STARTUP = 1
    INFINITE_KEXT_NOT_APPROVED_NOTIF = 2
    INFINITE_ERROR_VIEW = 3
    INFINITE_KEXT_TRIGGER_DUE_TO_OPTIN = 4


class InfiniteUIEventType(IntEnum):
    RECALL_DELAYED = 1
    RECALL_FINISHED = 2
    RECALL_FAILED = 3
    RETRIED_RECALL_FINISHED = 4
    RECALL_FAILED_NETWORK = 5
    RECALL_FAILED_SYNC_ENGINE_PAUSED = 6
    RECALL_FAILED_NO_SPACE = 7
    RECALL_FAILED_OUTSIDE_DROPBOX = 8


class InfiniteUIStatus(IntEnum):
    ACTIVE = 1
    WAITING = 2
    CANCELLED = 3


class InfiniteRecallType(IntEnum):
    ON_DEMAND = 1
    EXTERNAL_MOVE = 2
    CLIENT_REQUEST = 3


class InfiniteUIRequest(ValidatedRecord):
    ACTION_CANCEL = 'cancel'
    account = Field.required(Account)
    local_path = Field.required(LocalPath)
    filename = Field.required(Text)
    progress = cast(Optional[Tuple[(int, int)]], Field.optional(tuple))
    request_process = Field.optional(Text)
    start_time = Field.required(float)
    start_time_utc = Field.required(float)
    status = Field.required(InfiniteUIStatus)
    notified = Field.required(bool)
    recall_id = Field.required(int)
    recall_type = Field.optional(InfiniteRecallType)
    from_recall_event = (lambda account, recall_event: ui_request = InfiniteUIRequest(account = account, local_path = recall_event.local_path, filename = recall_event.local_path.basename, progress = None, request_process = recall_event.request_process, start_time = get_monotonic_time_seconds(), start_time_utc = time.time(), status = InfiniteUIStatus.ACTIVE, notified = False, recall_id = recall_event.recall_id)ui_request.refresh_progress(recall_event.download_progress).refresh_status(recall_event.recall_status))()
    
    def refresh_progress(self = None, download_progress = None):
        progress = None
    # WARNING: Decompyle incomplete

    
    def refresh_status(self = None, recall_status = None):
        if recall_status in FAILURE_STATUSES:
            status = InfiniteUIStatus.CANCELLED
        else:
            status = InfiniteUIStatus.ACTIVE
        return self.copy(status = status)

    
    def get_state_for_view(self = None):
        shortened_filename = shorten_filename(self.filename, 20)
    # WARNING: Decompyle incomplete



class InfiniteUIAccountState(ValidatedRecord):
    account = Field.required(Account)
    requests: 'Tuple[InfiniteUIRequest, ...]' = Field.required(tuple)


class InfiniteUIState(ValidatedRecord):
    account_states: 'Tuple[InfiniteUIAccountState, ...]' = Field.required(tuple)
    
    def get_state_for_view(self = None):
        request_dicts = self.requests()
        ret = dict()
        for request_dict in request_dicts:
            request_process = request_dict['request_process']
            if request_process not in ret:
                ret[request_process] = []
            ret[request_process].append(request_dict)
            return ret

    requests = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.account_states())
)()

InfiniteUIAction = NamedTuple('InfiniteUIAction', [
    ('action_string', Text),
    ('action', Callable[([
        List[InfiniteUIRequest]], None)])])

class InfiniteUIEvent(ValidatedRecord):
    request = Field.required(InfiniteUIRequest)
    event_type = Field.required(InfiniteUIEventType)


class InfiniteUINotificationType(IntEnum):
    INFINITE_SOFT_DOWNGRADE = 1
    INFINITE_CONFIGURATION_FAILED = 2
    INFINITE_TEMPORARILY_DISABLED = 3
    INFINITE_REQUIRES_REINSTALL = 5
    INFINITE_LOW_DISK = 6
    INFINITE_KEXT_NOT_APPROVED = 7
    INFINITE_FRESH_LINK = 8
    INFINITE_KEXT_NOT_APPROVED_WEB_OPTIN = 16
    INFINITE_REQUIRES_RESTART = 17

InfiniteUIBubbleNotification = NamedTuple('InfiniteUIBubbleNotification', [
    ('account', Account),
    ('notification_type', InfiniteUINotificationType),
    ('surface_action', Optional[Callable[([], Any)]]),
    ('actions', Tuple[(Tuple[(Text, Callable[([], Any)])], ...)])])

class InfiniteUINotification(ValidatedRecord):
    account = Field.required(Account)
    notification_type = Field.required(InfiniteUINotificationType)
    actions: 'Tuple[Tuple[Text, Callable[[], None]], ...]' = Field.required(tuple)

InfiniteUIInterface = <NODE:12>()
InfiniteUIControllerInterface = <NODE:12>()
InfiniteUIDispatcherInterface = <NODE:12>()
