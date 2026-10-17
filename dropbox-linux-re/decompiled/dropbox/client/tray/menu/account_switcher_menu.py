# Source Generated with Decompyle++
# File: account_switcher_menu.pyc (Python 3.11)

from collections import OrderedDict
from typing import Callable, cast, Dict, Iterator, Optional, Text, Tuple, Union
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.multiaccount.role import Roles
from dropbox.client.notifications.notifications_wrapper import NotificationsWrapper
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client.tray.events import track_click, TrayEventName, TrayEventTrigger
from dropbox.client.tray.menu.recently_changed_menu import RecentlyChangedMenu
from dropbox.client.ui.common.dropbox_menu import AfterTrayMenuAction, MenuComponent, MenuItem, Separator, SubMenu
from dropbox.client.ui.common.preferences import format_quota_usage
from dropbox.client.ui.common.tray_menu_options import TrayOption, TrayOptionStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.account_manager import AccountModel
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.i18n import ungettext
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class AccountSwitcherMenu(Destroyable):
    pass
# WARNING: Decompyle incomplete


def _get_quota_info(account = None):
    if not account.quota_info:
        return None
# WARNING: Decompyle incomplete

