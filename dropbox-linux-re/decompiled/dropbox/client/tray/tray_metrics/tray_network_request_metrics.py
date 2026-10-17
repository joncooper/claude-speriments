# Source Generated with Decompyle++
# File: tray_network_request_metrics.pyc (Python 3.11)

from enum import Enum
from typing import Optional, Tuple, Type
from dropbox.client.features.home_feed.shared.util.const import SyncWorkerRequestStateMap
from dropbox.client.tray.tray_metrics.common import TrayMetrics
from dropbox.enum_utils import auto, AutoLowerNameEnum, StrAsPrefixlessValueTrait
from dropbox.exception import ExcInfo
from dropbox.foundation.futures import Future

class TrayMetricsEndpointName(AutoLowerNameEnum, StrAsPrefixlessValueTrait):
    FEED_BOLT_STATE = auto()
    FETCH_PENDING_MEMBERS = auto()
    NOTIFICATION_RECORD_SAVER_HOME_FILE_INFO = auto()
    PAIRED_ONBOARDING_MODULES_COMPLETED = auto()
    STARRED_PERSIST = auto()
    SUGGEST_DISMISS = auto()
    TEAM_DISCOVERY_CANCEL_JOIN_TEAM = auto()
    TEAM_DISCOVERY_JOIN_TEAM = auto()
    TEAM_DISCOVERY_TEAMS_LIST = auto()
    TEAM_DISCOVERY_USER = auto()
    USER_TO_TEAM_GET_INTERACTION_INFO = auto()
    ZOOM_CAN_SEND_MESSAGE = auto()
    TEST = auto()


class TrayMetricsAssistantTag(AutoLowerNameEnum, StrAsPrefixlessValueTrait):
    SYNC_WORKER_API = auto()
    IS_AGGREGATED_REQUEST = auto()
    RESPONSE_STATUS = auto()
    EXCEPTION_TYPE = auto()
    IS_EXPECTED_EXCEPTION = auto()


class TrayMetricsAssistantMetric(Enum, StrAsPrefixlessValueTrait):
    SYNC_WORKER_RELATED_API = 'sync_worker_related_api'


def report_sync_worker_metric(endpoint = None, request_future_state = None, expected_error_types = None, future_exc_info = (None,)):
    tags = {
        str(TrayMetricsAssistantTag.RESPONSE_STATUS): str(SyncWorkerRequestStateMap[request_future_state].name) }
# WARNING: Decompyle incomplete

