# Source Generated with Decompyle++
# File: ux_param_utils.pyc (Python 3.11)

from typing import Dict, List, Optional, Text, Tuple
from dropbox.client.authentication.interface import Account
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.gating import BackupRestorationsOnboardingFeature, BackupUserSurveyFeature
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_accounts
from dropbox.client.features.backup_restorations_onboarding.bridge_gen.eligible_backups import EligibleBackups
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.sync_everything.gating import BackupAppFeature, BackupSkuModalFeature, SyncEverythingFeature, SyncEverythingOnboardingFeature
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.stormcrow_values import StormcrowValues
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.multiaccount.values import MultiaccountStrings
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.platform import IS_MAC

def translate_role(role = None):
    if role == Roles.PERSONAL:
        return BIDLRole.PERSONAL
    return None.BUSINESS


def get_platform():
    if IS_MAC:
        return 'mac'


def get_folders_experiment_variant(user_context = None):
