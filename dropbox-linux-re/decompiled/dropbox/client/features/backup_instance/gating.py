# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional, Sequence, Set
from build_number.platform import IS_LINUX
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_instance.constants import BI_FEATURE_OFF_VARIANTS, CBOA_PAUSE_ON_RELINK_KILLSWITCH, TEST_ONLY_BI_FEATURE_GATE_NAME, TEST_ONLY_DISABLED_VARIANT
from dropbox.client.features.backup_instance.utils import BI_TRACE
from dropbox.foundation.context.user import UserContext

class BackupInstanceFeature:
    forced_allowed_accounts: 'Set[AccountInterface]' = set()
    add_to_force_allowed = (lambda account = None: BackupInstanceFeature.forced_allowed_accounts.add(account))()
    is_on_variant = (lambda variants = None: if not variants:
False# WARNING: Decompyle incomplete
)()
    is_feature_enabled = (lambda : not IS_LINUX)()
    is_allowed_for_user = (lambda user_context = None, ignore_force_allowed = None: test_only_stormcrow_variant = user_context.stormcrow.get_variant(TEST_ONLY_BI_FEATURE_GATE_NAME)if test_only_stormcrow_variant == TEST_ONLY_DISABLED_VARIANT:
BI_TRACE('Fission Disabled for test', None)Falseis_featue_enabled = None.is_feature_enabled()BI_TRACE('Checking backupinstance allowed for user: is_feature_enabled (%r) ', None, is_featue_enabled)is_featue_enabled)()
    is_pause_cboa_anchors_on_start_enabled = (lambda user_context = None: 