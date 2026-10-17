# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional, Text
from sync_everything.constants import BACKUP_RESTORATIONS_ONBOARDING, SYNC_EVERYTHING_FEATURE_OFF_VARIANTS
from ui_utils import BackupImplementationUISwitcher
from dropbox.client.features.computer_backup.constants import CB_ANCHORS_RESTORATIONS_ONBOARDING, CB_DISABLE_BACKUP_SURVEY, CB_DISABLE_DURING_MIGRATION_BACKUP_SURVEY_KILLSWITCH
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.foundation.context.user import UserContext

class BackupRestorationsOnboardingFeature:
    _is_on_variant = (lambda variant = None: if variant is not None:
passvariant not in SYNC_EVERYTHING_FEATURE_OFF_VARIANTS)()
    is_on_cb_anchors = (lambda : BackupImplementationUISwitcher.anchors_used())()
    is_enabled = (lambda user_context = None: is_anchors = BackupImplementationUISwitcher.anchors_used()# WARNING: Decompyle incomplete
)()


class BackupUserSurveyFeature:
    _is_on_variant = (lambda variant = None: if variant is not None:
passvariant not in SYNC_EVERYTHING_FEATURE_OFF_VARIANTS)()
    is_disable_backup_survey_enabled = (lambda user_context = None: BackupUserSurveyFeature._is_on_variant(user_context.stormcrow.get_variant(CB_DISABLE_BACKUP_SURVEY)))()
    is_disable_backup_survey_during_migration_allowed = (lambda user_context = None: not BackupUserSurveyFeature._is_on_variant(user_context.stormcrow.get_variant(CB_DISABLE_DURING_MIGRATION_BACKUP_SURVEY_KILLSWITCH)))()

