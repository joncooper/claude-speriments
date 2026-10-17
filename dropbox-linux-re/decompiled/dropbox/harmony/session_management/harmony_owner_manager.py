# Source Generated with Decompyle++
# File: harmony_owner_manager.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, Optional, Tuple
from dropbox.client.config import ConfigDict
from dropbox.client.configuration.context_aware_config_dict import ContextAwareConfigDict
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_2
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.signals import SignalConnection, StandardSignal
from dropbox.harmony.badge.badge_preferences import BadgeVisibility
from dropbox.harmony.logger.event_types import OwnerManagerEvents
from dropbox.harmony.logger.logging import Logger
from dropbox.harmony.session_management.harmony_mev_owner import HarmonyMEVOwner
from dropbox.harmony.session_management.harmony_session_update_tracker import HarmonyUpdateInfo
from dropbox.harmony.window_tracking.shell import ShellTracker
from dropbox.platform import IS_WINDOWS
from dropbox.preferences import OPT_HARMONY, OPT_HARMONY_VISIBILITY
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.foundation.navigation_service.interface import NavigationServiceInterface
HarmonyDocumentUpdate = Tuple[(UserContext, HarmonyUpdateInfo)]

class HarmonyOwnerManager(Actor):
    pass
# WARNING: Decompyle incomplete

