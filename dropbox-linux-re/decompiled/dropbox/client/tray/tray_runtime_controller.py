# Source Generated with Decompyle++
# File: tray_runtime_controller.pyc (Python 3.11)

import time
from collections import OrderedDict
from typing import Any, Dict, Mapping, Optional, Text
from build_number import dropbox_version
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountId
from dropbox.client.features.home_feed.shared.model.constants import ASSISTANT_FEATURES
from dropbox.client.features.home_feed.shared.model.user_active_tracker import UserActiveTracker
from dropbox.client.features.os_consent.os_consent_logging import OSConsentEvent, report_os_consent_event
from dropbox.client.flow_tracker import BlockingFlow, NonBlockingFlow
from dropbox.client.notifications.legacy_notifications import StickyNotification
from dropbox.client.status.label import StatusLabel
from dropbox.client.sync_progress.sync_progress_controller import SyncProgressController
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client.tray.constants import STORMCROW_DASH_ESV
from dropbox.client.tray.events import TrayEventReporter
from dropbox.client.tray.logging.pap_logging_helpers import log_select_tray_assistant
from dropbox.client.tray.os_consent_state import TrayOSConsentState
from dropbox.client.ui.common.tray_popup_constants import SYNC_ACTIVITY_FLOW, TRAY_FLOW_NAME, TrayTriggerReason
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import report_exceptions
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.wrappers import Replaceable
from dropbox.pap.events.enums.tray_variant_pb2 import TrayVariant as PAPTrayVariant
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.client.notifications.mac.mac_notifications_authorization_sticky_notification_controller import MacNotificationsAuthorizationStickyNotificationController

class TrayRuntimeController(Actor, MachineSingleton):
    pass
# WARNING: Decompyle incomplete

