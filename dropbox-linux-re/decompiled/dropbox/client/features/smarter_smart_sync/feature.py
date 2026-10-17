# Source Generated with Decompyle++
# File: feature.pyc (Python 3.11)

from typing import Optional
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.smart_sync_removal_mitigation.helpers import ss_removal_mitigation_degraded_placeholders_enabled
from dropbox.client.gandalf import Gandalf
from dropbox.foundation.stormcrow import MachineStormcrowInterface
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.infinite import dod_for_non_fp_enabled, is_user_running_cloud_files
from dropbox.sync_root.gating import is_file_provider_root_type
_SMARTER_SMART_SYNC_KILL_SWITCH_NAME = 'desktop-smarter-smart-sync-kill-switch'
_SMARTER_SMART_SYNC_FEATURE_NAME = 'desktop-smarter-smart-sync'
_SMARTER_SMART_SYNC_STORMCROW_NAME = 'desktop-smarter-smart-sync'
_SMARTER_SMART_SYNC_FOR_CF_STORMCROW_NAME = 'desktop-smarter-smart-sync-for-cf'
_SS_AUTOEVICT_DISK_CHECK_STORMCROW_FEATURE_NAME = 'desktop-smarter-smart-sync-based-on-disk-check'
_SS_AUTOEVICT_EXCLUDE_EXPLICIT_RECALL = 'desktop-download-on-demand-autoevict-exclude-explicit-recall'
_SS_AUTOEVICT_STORMCROW_ON_VARIANT = 'ON'
_SS_AUTOEVICT_STORMCROW_OFF_VARIANT = 'OFF'
_SS_AUTOEVICT_STORMCROW_UI_ONLY_VARIANT = 'ON_UI_ONLY'
_SS_AUTOEVICT_STORMCROW_MONITOR_VARIANT = 'MONITOR'
_SS_AUTOEVICT_STORMCROW_FORCED_ON_VARIANT = 'FORCED_ON'

class SmarterSmartSyncFeature:
    manager_can_start = (lambda stormcrow = None: if feature_enabled(_SMARTER_SMART_SYNC_FEATURE_NAME):
passnot stormcrow.allows_any_account(_SMARTER_SMART_SYNC_KILL_SWITCH_NAME))()
    allowed_for_user = (lambda stormcrow = None: 