# Source Generated with Decompyle++
# File: static_menu.pyc (Python 3.11)

from collections import OrderedDict
from datetime import datetime
from os import makedirs, path
from shutil import copytree, ignore_patterns, make_archive
from subprocess import call
from tempfile import TemporaryDirectory
from typing import Optional, Union
from uuid import uuid4
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.constants import AppDataPaths
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.eligibility_cache import FenixEligibilityCache, FenixEligibilityGates
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.fenix.journeys.app_shell.constants import Views as AppShellViews
from dropbox.client.fenix.journeys.app_shell.utils import launch_appshell
from dropbox.client.multiaccount.role import Roles
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client.tray.events import track_click, TrayEventName, TrayEventTrigger
from dropbox.client.tray.logging.pap_logging_helpers import ACCOUNT_MENU_ITEMS, log_select_desktop_surface_action_tray_low_ui
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
from dropbox.client.ui.common.tray_menu_options import TrayOption, TrayOptionStrings
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.navigation_service.manifest_registry import DEBUG_MENU_OVERRIDE_STORMCROW, EVENT_LOGGER_DISPLAY
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.metrics.pro_event_reporting import report_pro_event
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_WINDOWS:
    from os import startfile
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class TrayStaticMenuItems(Destroyable):
    pass
# WARNING: Decompyle incomplete

