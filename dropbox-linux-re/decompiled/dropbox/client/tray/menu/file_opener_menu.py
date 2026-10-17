# Source Generated with Decompyle++
# File: file_opener_menu.pyc (Python 3.11)

from collections import OrderedDict
from typing import Optional, Union
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client.tray.events import track_click, TrayEventName, TrayEventTrigger
from dropbox.client.tray.logging.pap_logging_helpers import ACCOUNT_MENU_ITEMS, log_select_desktop_surface_action_tray_low_ui
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.ui.common.tray_menu_options import TrayOption, TrayOptionStrings
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class TrayFileOpenerMenuItems(Destroyable):
    pass
# WARNING: Decompyle incomplete

