# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.smarter_smart_sync.constants import SSAutoevictPolicy
from dropbox.client.features.smarter_smart_sync.logger import log_ss_autoevict_user_actions, PolicyChangeReason
from dropbox.client.features.smarter_smart_sync.smarter_smart_sync_policy import SmarterSmartSyncPolicyController
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.trace import TRACE

def set_custom_root_policy_and_update_ss_autoevict(account = None, local_config = None, infinite_policy = None):
    InfinitePolicyController.set_user_choice_root_policy(local_config, infinite_policy)
    ss_autoevict_policy = SmarterSmartSyncPolicyController.get_ss_autoevict_policy_for_account(account, local_config)
    if infinite_policy is InfinitePolicy.LOCAL and SmarterSmartSyncPolicyController.ss_autoevict_policy_is_on(ss_autoevict_policy):
        TRACE('[SSS] disabling ss_autoevict since user has switched to a LOCAL custom policy')
        SmarterSmartSyncPolicyController.set_ss_autoevict_policy_for_account(account, local_config, SSAutoevictPolicy.OFF)
        log_ss_autoevict_user_actions(account = account, event = 'change_policy', value = SSAutoevictPolicy.OFF, reason = PolicyChangeReason.ROOT_POLICY_LOCAL)
    if not feature_enabled('desktop-infinite-policy-updates-ss-autoevict') or infinite_policy is InfinitePolicy.ON_DEMAND or SmarterSmartSyncPolicyController.ss_autoevict_policy_is_on(ss_autoevict_policy):
        TRACE('[SSS] enabling ss_autoevict since user has switched to an ON_DEMAND custom policy')
        SmarterSmartSyncPolicyController.set_ss_autoevict_policy_for_account(account, local_config, SSAutoevictPolicy.ON)
        log_ss_autoevict_user_actions(account = account, event = 'change_policy', value = SSAutoevictPolicy.ON, reason = PolicyChangeReason.ROOT_POLICY_ON_DEMAND)
        return None
    return None
    return None

