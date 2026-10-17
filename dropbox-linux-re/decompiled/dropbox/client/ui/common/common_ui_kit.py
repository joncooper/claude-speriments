# Source Generated with Decompyle++
# File: common_ui_kit.pyc (Python 3.11)

import uuid
from typing import Any, Callable, Dict, List, Optional, Text
from build_number.platform import IS_LINUX
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes, IconType
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.uikit import Closeable, ExternalUIKit, on_ui_thread_returns_none
from dropbox.client.ui.electron.office import OfficeSplashScreen
from dropbox.client.ui.electron.screenshots import ScreenshotsSelsyncSplashScreen, ScreenshotsSplashScreen
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.electron.electron_dialog_constants import ElectronDialogCallbackInfo
from dropbox.foundation.raii2 import destroying
from dropbox.threadutils import SafeValue
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.multiaccount.selector import MultiAccountSelector

class CommonUIKit(ExternalUIKit):
    pass
# WARNING: Decompyle incomplete

