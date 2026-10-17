# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import time
from typing import Callable, Optional, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.flexible_filenames.consts import FFN_VARIANT_STORMCROW, FlexibleFileNameStickyVariant, HELP_CENTER_LINK
from dropbox.client.features.flexible_filenames.gating import get_flexible_filenames_rules, save_flexible_filenames_rules, save_flexible_filenames_rules_default
from dropbox.client.features.flexible_filenames.logger import FlexibleFilenameNotificationLogger
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.notifications.legacy_notifications import FlexibleFileNameSticky
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2._impl import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method, async_queued_method_0
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.proto.nucleus.app_service_pb2 import FlexibleFilenamesConfigReply, UpdateConfigReply, UpdateConfigReq
from dropbox.proto.nucleus.sync_engine_pb2 import FlexibleFilenamesConfig, UpdatableAppConfig, UserConfig
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncOperationFailureReason
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailuresSummary
from dropbox.sync_engine_boundary.types.sync_progress import SyncingSnapshot, SyncProgress
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
FIVE_MINUTES_IN_SECONDS = 300
VARIANT_RULE_MAP = {
    FlexibleFileNameStickyVariant.OPT_OUT: FlexibleFilenamesConfig.Rules.OFF,
    FlexibleFileNameStickyVariant.OPT_IN: FlexibleFilenamesConfig.Rules.VERSION_0 }

class FlexibleFilenamesController(Actor):
    pass
# WARNING: Decompyle incomplete

