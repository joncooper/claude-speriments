# Source Generated with Decompyle++
# File: feed_update_client.pyc (Python 3.11)

from typing import Any, Dict, List, Optional, Text, Tuple, Union
from mypy_extensions import TypedDict
from dropbox.client.bolt.types import BoltAppID, BoltChannelId, BoltChannelState
from dropbox.client.features.bolt.bolt_client_for_app import BoltClientForApp, channel_data_for_identifiers
from dropbox.client.features.home_feed.shared.util.delayed_task_with_backoff import DelayedTaskWithExpBackoff
from dropbox.client.features.home_feed.shared.util.gating import get_bolt_rate_limit_settings
from dropbox.client.features.home_feed.shared.util.home_fetch_logger import HomeFetchLogger
from dropbox.client.features.home_feed.shared.util.network_request_handling import AssistantLossyRateLimiter, make_delayed_request_with_noop_handling, NoopResponse
from dropbox.client.features.home_feed.shared.util.signals import RepeatedEventSignalWithPayload
from dropbox.client.features.queued_method_runner import QueuedMethodRunner
from dropbox.client.tray.tray_metrics.tray_network_request_metrics import TrayMetricsEndpointName
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import get_jittered_seconds
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
FEED_BOLT_APP_ID = BoltAppID('feed_notification')
STARTUP_JITTER_HOURS = 0.5
ServerBoltData = TypedDict('ServerBoltData', {
    'bolt_token': Text,
    'revision_id': int,
    'bolt_unique_id': Text })
ServerResponse = Union[(Dict[(Text, Optional[ServerBoltData])], NoopResponse)]
BOLT_BACKOFF_TIME_IN_SECONDS = 1800
BOLT_RECONNECT_MAX_ATTEMPTS = 6

class AssistantFeedUpdateClient(Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

