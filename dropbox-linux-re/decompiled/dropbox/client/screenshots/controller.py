# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import errno
import os
import unicodedata
import uuid
from datetime import datetime
from functools import partial
from os.path import getctime
from time import localtime, strftime
from typing import Callable, cast, FrozenSet, List, Optional, Set, Text, Tuple, TypeVar
from foundation.raii2 import destroying
from features.sync_everything.gating import SyncEverythingFeature
from features.sync_everything.v3.async_tools import async_queued_local_function
from features.sync_everything.v3.fp_utils import allow_dataless_recall, DatalessContext
from ui.common.pathways.folder_opener_controller import FolderOpenerController
from ui.common.utils import is_low_ui_mode
from constants import SCREENSHOTS_FOLDER_CONFIG_KEY, SCREENSHOTS_FOLDER_SERVER_KEY, SCREENSHOTS_PREFERENCE_SETTING_COPY_LINK_VALUE, SCREENSHOTS_SE_FOLDER_CONFIG_KEY
from provider import ScreenshotsProvider
from provider.constants import MAC_SCREENCAPTURE_XATTR, MOVED_SCREENRECORDING_XATTR_KEY, MOVED_SCREENSHOT_XATTR_KEY
from dropbox.async_timers import async_timers
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.client_shmodel import ClientShmodelOrigin
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client.multiaccount.role import Roles
from dropbox.client.multiaccount.selector import MultiAccountSelector
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.screenshots import Screenshot
from dropbox.client.screenshots.utils import copy_image_to_clipboard
from dropbox.client.transient_simple_metric.transient_simple_metric import report_transient_simple_metric, SimpleMetricCategoryWhitelist
from dropbox.client.ui.common.markup import MarkupStrings, show_markup_notification
from dropbox.client.ui.common.preferences_utils import PanelNames
from dropbox.client.ui.common.screenshots import ScreenshotsStrings
from dropbox.client.util import highlight_file
from dropbox.client_api.exceptions import TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.enum_utils import auto, AutoNameEnum
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.fsutil import can_access, create_unique_file_name, get_attr, move, set_attr
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.nfcdetector import is_nfc
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.preferences import COPY_IMAGE_OR_LINK, COPY_LINK_WINDOWS, OPT_SCREENSHOTS, OPT_SCREENSHOTS_PREV_DAILY_LOG_TIMESTAMP, OPT_SHOW_QUICK_ACTIONS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath, RRLowerServerPath, RRUnknownCaseServerPath, ServerPath
from dropbox.shared.util import db_lower
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError, OperationNotPermittedError
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class _ScreenshotProcessingThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

ScreenshotProcessingThread = db_thread(_ScreenshotProcessingThreadImpl)
_CN = TypeVar('_CN', bound = Callable[(..., None)])
_FileQueueType = List[Tuple[(Screenshot, bool, bool, bool)]]
SCREENSHOT_FP_COPY_LINK_DELAY_SECONDS = 2

def on_screenshot_thread(handle_exceptions = None, delay = None, debounce = None):
    return ScreenshotProcessingThread.on_queue(handle_exceptions = handle_exceptions, delay = delay, debounce = debounce)


class ScreenshotsActionOrigin(AutoNameEnum):
    splash = auto()
    preferences = auto()
    sync_everything = auto()


class ScreenshotsController(Actor):
    pass
# WARNING: Decompyle incomplete


class ScreenshotsCallbacks(object):
    
    def __init__(self):
        self._lock = Lock()
        self._callbacks = [
            None,
            None]

    callbacks = (lambda self: callbacks = []self._lockcallbacks = [
self._callbacks[0],
self._callbacks[1]]None(None, None))()
    
    def set_primary(self, cb):
        self._lock
        self._callbacks[0] = cb
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def set_secondary(self, cb):
        self._lock
        self._callbacks[1] = cb
        None(None, None)
        return None
        with None:
            if not None:
                pass



def root_relative_to_local_path(app = None, path = None, account = None):
    pass
# WARNING: Decompyle incomplete

