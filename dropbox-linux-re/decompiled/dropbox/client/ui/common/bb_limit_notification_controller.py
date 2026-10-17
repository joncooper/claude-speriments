# Source Generated with Decompyle++
# File: bb_limit_notification_controller.pyc (Python 3.11)

import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable, Mapping, Optional, Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.features.business_basic.constants import STORMCROW_VARIANT_BB_MONTHLY_UPLOAD_LIMIT_RESULT_ENABLED
from dropbox.client.features.business_basic.notification_state import BB_MODAL_TYPES, BBLimitNotificationVariant, BBNotificationInFlightKey, BBNotificationStateStore
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.multiaccount.role import Roles
from dropbox.client.notifications.constants import BB_TEAM_STORAGE_CAMPAIGN_IDS, BB_TEAM_STORAGE_CAMPAIGN_VERSION_IDS
from dropbox.client.ui.common.bb_limit_notification import BBLimitNotification, BBLimitNotificationDecision
from dropbox.client_api.dropbox_connection import DROPBOX_TIMESTAMP_FORMAT, DropboxConnection
from dropbox.client_api.exceptions import TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.functions import bytesafe_json_dumps
from dropbox.shared.quota_info import QuotaInfo
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.threading import Lock
from dropbox.trace import TRACE
on_background_thread_future = make_on_thread_future_decorator(on_background_thread, 'on_background_thread_future')
MONTHLY_UPLOAD_QUOTA_REQUEST_TIMEOUT_SECONDS = 5
TEAM_STORAGE_BLUENOTE_RETRIES = 3
TEAM_STORAGE_BLUENOTE_RETRY_INITIAL_DELAY_SECONDS = 1
TEAM_STORAGE_BLUENOTE_RETRY_MAX_DELAY_SECONDS = 5

def _send_bluenote_request(connection = None, host_secret = None, request = None):
    if not host_secret:
        return FailedFuture.create(ValueError('Cannot send a Bluenote without a host secret'))
    
    try:
        return connection.new_conn.request('POST', 'apiv2server', '/2/megaphone_bluenote/send_bluenote', [
            ('Authorization', 'Dropbox-Host-Key ' + host_secret),
            ('Content-Type', 'application/json')], bytesafe_json_dumps(request).encode('utf-8'))
    except Exception:
        exc = None
        del exc
        return None
        None = 
        del exc


_send_bluenote_request_with_retry = (lambda connection = None, host_secret = None, request = FutureHelpers.with_retry(tries = TEAM_STORAGE_BLUENOTE_RETRIES, initial_sleep_secs = TEAM_STORAGE_BLUENOTE_RETRY_INITIAL_DELAY_SECONDS, max_sleep_secs = TEAM_STORAGE_BLUENOTE_RETRY_MAX_DELAY_SECONDS, exceptions = (TransientNetworkError,)): _send_bluenote_request(connection, host_secret, request))()

def _utc_now():
    return datetime.now(timezone.utc)

MonthlyUploadQuotaStatus = <NODE:12>()

def _is_valid_reset_date(reset_date = None):
    
    try:
        parsed_reset_date = datetime.strptime(reset_date, DROPBOX_TIMESTAMP_FORMAT)
    except (TypeError, ValueError):
        return False

    return parsed_reset_date.strftime(DROPBOX_TIMESTAMP_FORMAT) == reset_date


def _trace_invalid_response(reason = None):
    TRACE('BBLimitNotificationController: invalid monthly-upload quota response: %s', reason)


def _get_team_storage_info(account = None):
    quota_info = account.quota_info
# WARNING: Decompyle incomplete


class BBLimitNotificationController(Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

