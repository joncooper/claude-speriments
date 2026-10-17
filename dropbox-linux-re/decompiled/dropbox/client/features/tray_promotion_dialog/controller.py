# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import uuid
from time import time as _time
from typing import Any, List, Optional, Tuple, Union
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventState
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint, NotificationDialogSurface
from dropbox.client.features.tray_promotion_dialog.constants import DEBUG_DELAY_TRAY_PROMOTION_SECONDS, DELAY_TRAY_PROMOTION_SECONDS, DialogStopReason, PROMOTION_NOTIFICATION_HEIGHT, PROMOTION_NOTIFICATION_WIDTH, TRAY_PROMOTION_MAX_ATTEMPTS, TRAY_PROMOTION_STATE_CONFIG_KEY, TrayPromotionState, TWO_WEEKS_IN_SECONDS
from dropbox.client.features.tray_promotion_dialog.logger import DesktopPromotionLogger
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.trace import TRACE

class TrayPromotionController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

