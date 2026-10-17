# Source Generated with Decompyle++
# File: active_account_tracker.pyc (Python 3.11)

from typing import List, Optional
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_1
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.signals import StandardSignal
from dropbox.trace import TRACE

class ActiveAccountTracker(Actor, MachineSingleton):
    pass
# WARNING: Decompyle incomplete

