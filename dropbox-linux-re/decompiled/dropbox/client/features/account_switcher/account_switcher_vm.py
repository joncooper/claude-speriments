# Source Generated with Decompyle++
# File: account_switcher_vm.pyc (Python 3.11)

from typing import Any, cast, Dict, Mapping, Optional, Tuple, Union
from typing_extensions import Literal
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.account_switcher.bridge_gen.bridge_interface_account_switcher_vm import AccountSwitcherVMBridgeInterface, AccountSwitcherVMObservableMixin
from dropbox.client.features.account_switcher.bridge_gen.linked_accounts import LinkedAccounts
from dropbox.client.features.account_switcher.util import PlanInfo, request_api_v2_plan_info
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.features.users.view_model.users_vm import convert_user
from dropbox.client.multiaccount.role import Roles
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client.tray.events import track_click as track_click_decorator, TrayEventName, TrayEventReporter, TrayEventTrigger
from dropbox.client.tray.tray_metrics.tray_action_metrics import get_tray_metrics_action_item, TrayActionMetrics, TrayMetricsActionItem, TrayMetricsActionMetric, TrayMetricsView
from dropbox.client.users import UserCacheRefreshError, UserInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.exception_decorators import report_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.trace import TRACE

def track_click(label = None, click_location = None, **extras):
    pass
# WARNING: Decompyle incomplete


class AccountSwitcherVM(Actor, AccountSwitcherVMBridgeInterface, AccountSwitcherVMObservableMixin):
    pass
# WARNING: Decompyle incomplete

