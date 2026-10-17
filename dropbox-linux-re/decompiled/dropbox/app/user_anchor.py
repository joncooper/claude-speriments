# Source Generated with Decompyle++
# File: user_anchor.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.business_basic_upload_onboarding.trigger import BusinessBasicUploadOnboardingTrigger
from dropbox.client.features.cesna.launcher import CESNA_SC_RULE, CesnaTestLauncher
from dropbox.client.features.file_locking.file_locking_presence import FileLockingPresenceReporter
from dropbox.client.features.permission_after_upload.gating import permissions_after_upload_enabled
from dropbox.client.features.permission_after_upload.model.permissions_after_upload_model import PermissionsAfterUploadModel
from dropbox.client.features.quota_usage.manager import QuotaUsageManager
from dropbox.client.features.quota_usage.modal_over_quota_controller import ModalOverQuotaController
from dropbox.client.features.quota_usage.modal_over_quota_prevented_controller import ModalOverQuotaPreventedController
from dropbox.client.notifications.notifications_wrapper import NotificationsWrapper
from dropbox.client.ui.common.admin_selsync import AdminSelsyncUIController
from dropbox.client.ui.common.bb_limit_notification_controller import BBLimitNotificationController
from dropbox.client.ui.sync_engine_ui.bubbler import SyncEngineBubbler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager.user_anchor_interface import UserAnchorInterface
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FutureHelpers, sleep_async
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.raii2.wrappers import Replaceable
from dropbox.harmony.presence.document_presence_reporter import DocumentPresenceReporter
from dropbox.sync_engine_adapter.throttled_sync_failures_api import ThrottledSyncFailuresApi

class UserAnchor(UserAnchorInterface):
    pass
# WARNING: Decompyle incomplete

GEMINI_HOLDOUT_DUMMY_FEATURE = 'desktop-gemini-holdout'

class GatedFeatures(Actor):
    pass
# WARNING: Decompyle incomplete

