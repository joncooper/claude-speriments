# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.smarter_smart_sync.constants import SSAutoevictPolicy
from dropbox.client.features.smarter_smart_sync.logger import log_ss_autoevict_user_actions, PolicyChangeReason
from dropbox.client.features.smarter_smart_sync.smarter_smart_sync_policy import SmarterSmartSyncPolicyController
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.trace import TRACE

def set_dod_root_policy_and_update_ss_autoevict(account = None, local_config = None):
    TRACE('[Download on Demand] set root policy to ON_DEMAND and disable ss_autoevict: Account %r', account)
    InfinitePolicyController.set_user_choice_root_policy(local_config, InfinitePolicy.ON_DEMAND)
    set_ss_autoevict_off(account, local_config)


def set_ss_autoevict_off(account = None, local_config = None):
    TRACE('[Download on Demand] disable ss_autoevict: Account %r', account)
    current_sss_policy = SmarterSmartSyncPolicyController.get_ss_autoevict_policy_for_account(account, local_config)
    if SmarterSmartSyncPolicyController.ss_autoevict_policy_is_on(current_sss_policy):
        SmarterSmartSyncPolicyController.set_ss_autoevict_policy_for_account(account, local_config, SSAutoevictPolicy.OFF)
        log_ss_autoevict_user_actions(account = account, event = 'change_policy', value = SSAutoevictPolicy.OFF, reason = PolicyChangeReason.DOWNLOAD_ON_DEMAND)
        return None

