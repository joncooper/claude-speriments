# Source Generated with Decompyle++
# File: smarter_smart_sync_policy.pyc (Python 3.11)

from typing import Callable, Optional, Union
from build_number import dropbox_version
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.smarter_smart_sync.constants import SS_AUTOEVICT_ADMIN_POLICY_NAME, SS_AUTOEVICT_ON_VARIANTS, SS_AUTOEVICT_POLICY_NAME, SSAutoevictPolicy
from dropbox.client.features.smarter_smart_sync.feature import _SMARTER_SMART_SYNC_KILL_SWITCH_NAME, _SMARTER_SMART_SYNC_STORMCROW_NAME, _SS_AUTOEVICT_STORMCROW_FORCED_ON_VARIANT, _SS_AUTOEVICT_STORMCROW_MONITOR_VARIANT, _SS_AUTOEVICT_STORMCROW_ON_VARIANT
from dropbox.client.features.smarter_smart_sync.logger import log_ss_autoevict_user_actions, PolicyChangeReason
from dropbox.client.gandalf import Gandalf
from dropbox.client.multiaccount.role import Roles
from dropbox.client_api.exceptions import HTTP401Error, HTTP429Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import sleep_async
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.infinite import dod_for_non_fp_enabled
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.shared.util import safe_navigate
from dropbox.sqlite3_helpers import Cursor
from dropbox.sync_root.gating import is_file_provider_root_type
from dropbox.trace import TRACE

class SmarterSmartSyncPolicyController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

