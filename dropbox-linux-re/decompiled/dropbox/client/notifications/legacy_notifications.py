# Source Generated with Decompyle++
# File: legacy_notifications.pyc (Python 3.11)

import time
import uuid
from collections import OrderedDict
from datetime import timedelta
from typing import Any, Callable, Dict, List, Optional, Text, Tuple, Union
from xml.sax.saxutils import escape
from six import add_metaclass
from six.moves.urllib import parse as urlparse
from build_number import is_store_managed
from build_number.features import feature_enabled
from build_number.platform import IS_MAC
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.features.sync_and_storage.constants import SyncAndStorageActions, SyncAndStorageEntryPoint, SyncAndStorageViewVariant
from dropbox.client.features.sync_and_storage.utils import report_manage_space_event
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.gandalf import Gandalf
from dropbox.client.multiaccount.constants import PAIRED_STICKY_DISABLED_KEY, PAIRED_STICKY_DISABLED_TIMESTAMP_KEY, Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.notifications.events import get_render_info, NotificationSuppressReason, report_suppress
from dropbox.client.notifications.exceptions import MalformedPayloadException, StickyNotificationKeyError, UserNotificationActionError, UserNotificationActionNotAvailableError
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotificationType
from dropbox.client.notifications.model import UserNotification, UserNotificationInterface, UserNotificationSeenState, UserNotificationStatus
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.notifications.types import NotificationAction, NotificationAvatarIcon, NotificationIcon, NotificationImageType, NotificationInfo, NotificationRawType, NotificationRemoteIcon, NotificationSystemIcon, NotificationTok, NotificationType, StickyNotificationInfo
from dropbox.client.ui.common.html import HTMLTextConverter
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future
from dropbox.functions import calculate_num_days_remaining, snippet
from dropbox.i18n import format_bytes, format_number, trans, ungettext
from dropbox.infinite import infinite_exposed
from dropbox.infinite.notification_common import determine_soft_downgrade_text
from dropbox.metrics.pro_event_reporting import report_pro_event
from dropbox.platform import IS_WINDOWS
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUINotification, InfiniteUINotificationType
from dropbox.threading import Lock
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
from dropbox.win32.microsoft_store import launch_microsoft_store
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.notifications.model import LoudNotificationParams
DESKTOP_NOTIFICATION_OREF = 'dn'

class MetaUserNotification(type):
    pass
# WARNING: Decompyle incomplete

LegacyUserNotification = <NODE:12>()

class PairedUserNotification(LegacyUserNotification):
    pass
# WARNING: Decompyle incomplete


class MultiaccountLinkEnabledUserNotification(LegacyUserNotification):
    pass
# WARNING: Decompyle incomplete


class ActivityNewComment(LegacyUserNotification):
    pass
# WARNING: Decompyle incomplete


class SharedLink(LegacyUserNotification):
    pass
# WARNING: Decompyle incomplete


class DealExpirationWarningProxy(LegacyUserNotification):
    pass
# WARNING: Decompyle incomplete


class CreditCardWarningProxy(LegacyUserNotification):
    pass
# WARNING: Decompyle incomplete


class NewPhotos(LegacyUserNotification):
    pass
# WARNING: Decompyle incomplete


class GrowthEngagementProgress(LegacyUserNotification):
    pass
# WARNING: Decompyle incomplete

STICKY_PRIORITY_RANSOMWARE_INFECTION = 3
STICKY_PRIORITY_DEAL_EXPIRATION = 4
STICKY_PRIORITY_OS_VERSION_DEPRECATION = 5
STICKY_PRIORITY_BASIC_USER_TO_TEAM_SYNC_PAUSED = 6
STICKY_PRIORITY_HARD_DRIVE_IS_FULL_OR_LOW = 7
STICKY_PRIORITY_DEPRECATED_UPDATE = 8
STICKY_PRIORITY_OMAHA_NOSYNC = 9
STICKY_PRIORITY_CC_WARNING = 10
STICKY_PRIORITY_OUT_OF_QUOTA = 11
STICKY_PRIORITY_OQ_COMMIT_PREVENTED = 12
STICKY_PRIORITY_USER_TO_TEAM_ACTION_REQUIRED = 13
STICKY_PRIORITY_FLEX_FILE_NAMES = 14
STICKY_PRIORITY_SYNC_ERROR = 15
STICKY_PRIORITY_SLOW_SYNC_ALERT = 16
STICKY_PRIORITY_SLOW_SYNC_WARN = 17
STICKY_PRIORITY_ENCRYPTED_FOLDER_ENROLL = 18
STICKY_PRIORITY_FOLDER_IN_USE_ERROR = 19
STICKY_PRIORITY_FILE_PERMISSION_ERROR = 20
STICKY_PRIORITY_FINDER_YOSEMITE = 21
STICKY_PRIORITY_STUNNING_BUFFALO = 22
STICKY_PRIORITY_MAC_NOTIFICATIONS_AUTHORIZATION = 23
STICKY_PRIORITY_ERROR_SYNC_EVERYTHING = 24
STICKY_PRIORITY_MIGRATION = 25
STICKY_PRIORITY_BETA = 26
STICKY_PRIORITY_LOCAL_CONFLICT_NOTIFICATION = 27
STICKY_PRIORITY_DEGRADED_PLACEHOLDERS = 28
STICKY_PRIORITY_DROPBOX_RENAMED = 29
STICKY_PRIORITY_INFINITE_UI_HIGH_PRI_NOTIFICATION = 30
STICKY_PRIORITY_PROMPT_REINSTALL = 31
STICKY_PRIORITY_PAIRED = 32
STICKY_PRIORITY_LEGACY_TRAY_UPDATE = 33
STICKY_PRIORITY_INFINITE_UI_NOTIFICATION = 36
STICKY_PRIORITY_BLUENOTE = 37
STICKY_PRIORITY_ENABLE_SYNC_EVERYTHING = 38
STICKY_PRIORITY_CBOA_MIGRATION_NOTIFICATION = 39
STICKY_PRIORITY_OMAHA_PROMOTION = 40
STICKY_SYNC_DASHBOARD_ENTRY_POINT = 41
STICKY_PRIORITY_IGNORE_FILES = 42

class MetaStickyNotification(type):
    pass
# WARNING: Decompyle incomplete

StickyNotification = <NODE:12>()

class BluenoteStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class DummyPairedNotification:
    
    def __init__(self, timestamp, team, other_email, other_account_id = None, other_uid = None, paired_role = None, paired_state = ('timestamp', 'Optional[int]', 'team', 'Optional[str]', 'other_email', 'Optional[str]', 'other_account_id', 'Optional[str]', 'other_uid', 'Optional[int]', 'paired_role', 'Optional[Role]', 'paired_state', 'bool', 'return', 'None')):
        self.nid = None
        self.timestamp = timestamp
        self.team = team
        self.other_email = other_email
        self.other_account_id = None
        self.other_uid = None
        self.paired_role = paired_role
        self.paired_state = paired_state



class DropboxRenamedStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class PairedStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class EncryptedFolderEnrollmentStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class DeprecatedStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class CreditCardWarningStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class DealExpirationWarningStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class QuotaFullStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class OqCommitPreventedStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class HardDriveV2StickyNotificationBase(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class HardDriveLowV2StickyNotification(HardDriveV2StickyNotificationBase):
    pass
# WARNING: Decompyle incomplete


class HardDriveFullV2StickyNotification(HardDriveV2StickyNotificationBase):
    pass
# WARNING: Decompyle incomplete


class HardDriveLowSelsyncV2StickyNotification(HardDriveV2StickyNotificationBase):
    pass
# WARNING: Decompyle incomplete


class HardDriveFullSelsyncV2StickyNotification(HardDriveV2StickyNotificationBase):
    pass
# WARNING: Decompyle incomplete


class HardDriveFullStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class ManageSpaceStickyNotificationBase(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class ManageSpaceHardDriveLowStickyNotification(ManageSpaceStickyNotificationBase):
    pass
# WARNING: Decompyle incomplete


class ManageSpaceHardDriveFullStickyNotification(ManageSpaceStickyNotificationBase):
    pass
# WARNING: Decompyle incomplete


class PromptReinstallStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class InfiniteUIStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class FilePermissionSyncErrorStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class SyncEverythingSetupStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class SyncEverythingErrorStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class ExternalDriveBackupLocalConflictStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class CBoAMigrationStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class BackupInstanceRootInvalidErrorStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class SyncErrorStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class FPAdminMigrationStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class FPAutoMigrationStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class FPMigrationStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class FPUpdateExternalDriveStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class MacNotificationsAuthorizationStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class SSRemovalMitigationDegradedPlaceholdersStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class CloudFilesMigrationStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class OSVersionDeprecatedStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class SyncSlowSelsyncRecommendationNotificationWarning(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class SyncSlowSelsyncRecommendationNotificationAlert(SyncSlowSelsyncRecommendationNotificationWarning):
    STICKY_KEY = 'slow_sync_selsync_recommendation_notification_alert'
    _priority = STICKY_PRIORITY_SLOW_SYNC_ALERT


class FlexibleFileNameSticky(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class IgnoreFilesSticky(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class OmahaPromotionStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class SyncDashboardEntryPointStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class BasicUserToTeamActionRequiredStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete


class BasicUserToTeamSyncPausedStickyNotification(StickyNotification):
    pass
# WARNING: Decompyle incomplete

