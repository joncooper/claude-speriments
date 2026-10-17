# Source Generated with Decompyle++
# File: desired_root.pyc (Python 3.11)

from typing import Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.file_provider_migration.constants import FP_BY_DEFAULT_COHORT_STORMCROW, FP_BY_DEFAULT_COHORT_STORMCROW_FP_VARIANT, FP_BY_DEFAULT_COHORT_STORMCROW_MOUNTED_VARIANT
from dropbox.client.features.file_provider_migration.fp_by_default import force_start_on_fp, force_start_on_mounted
from dropbox.client.gandalf.base import Gandalf
from dropbox.sync_root.gating import cloud_files_eligible, file_provider_eligible
from dropbox.sync_root.types import SyncRootType, SyncRootTypeReason
from dropbox.trace import TRACE

def get_desired_sync_root_type(account_manager = None, account = None, gandalf = None, local_config = (True,), team_admin_fp_allowed = ('account_manager', 'AccountManagerInterface', 'account', 'AccountInterface', 'gandalf', 'Gandalf', 'local_config', 'LocalConfigurationInterface', 'team_admin_fp_allowed', 'bool', 'return', 'Tuple[SyncRootType, SyncRootTypeReason]')):
    pass
# WARNING: Decompyle incomplete

