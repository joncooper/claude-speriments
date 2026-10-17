# Source Generated with Decompyle++
# File: tray_ui_controller.pyc (Python 3.11)

from abc import abstractmethod
from collections import OrderedDict
from typing import Any, Optional, Text, Tuple
from build_number import is_electron_application
from build_number.features import feature_enabled
from build_number.platform import IS_WINDOWS
from dropbox.client.gandalf import Gandalf
from dropbox.client.status.interface import ClientStatusInterface
from dropbox.client.tray.common.tray_icon_state import TrayIconState, TrayIconStatus
from dropbox.client.tray.events import TrayEventReporter
from dropbox.client.tray.tray_runtime_controller import TrayRuntimeController
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayState, TrayTriggerReason, TrayUpdateOptionsReason
from dropbox.client.ui.common.uikit import ensure_on_ui_thread
from dropbox.foundation.context import Context
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.navigation_service.embeddable_host import EmbeddableViewHost
from dropbox.foundation.raii2.arc import Arc
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.tray.tray_controller import ElectronTrayController

class TrayUiControllerBase:
    
    def __init__(self = None, app = None):
