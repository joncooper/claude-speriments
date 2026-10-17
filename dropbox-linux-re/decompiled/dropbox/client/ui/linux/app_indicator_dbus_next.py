# Source Generated with Decompyle++
# File: app_indicator_dbus_next.pyc (Python 3.11)

from __future__ import absolute_import
import asyncio
import os
import sys
import threading
from datetime import datetime as _datetime
from typing import Dict, Iterable, List, Optional, Text, Tuple, Union
from dbus_next import Message, MessageFlag, MessageType
from dbus_next.aio import MessageBus
from dbus_next.signature import Variant
from build_number import is_frozen
from dropbox.client.config import ConfigDict
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem, MenuRadioItems, Separator, SubMenu
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread_future, report_ui_framework_event
from dropbox.client.ui.linux.asyncio_event_loop import AsyncioEventLoop
from dropbox.client.ui.linux.gtk_lib_app_indicator_loader import get_gtk_libappindicator_loader, SIGNAL_CALLBACK
from dropbox.client.util.linux import get_contents_root, get_repo_root_unfrozen
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import lrudict
from dropbox.gui import assert_message_queue
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
APP_INDICATOR_CATEGORY_APPLICATION_STATUS = 0
APP_INDICATOR_STATUS_PASSIVE = 0
APP_INDICATOR_STATUS_ACTIVE = 1
APP_INDICATOR_STATUS_ATTENTION = 2
TRAY_REFRESH_UPDATE_INTERVAL_SECS = 5

def gtk_callback(widget):
    gtk = get_gtk_libappindicator_loader().gtk
    maybe_action = gtk_callback.items[gtk.gtk_menu_item_get_accel_path(widget).decode('utf-8')]
    if maybe_action:
        maybe_action()
        return None

gtk_callback.items = lrudict(cache_size = 1000)
_gtk_callback = SIGNAL_CALLBACK(gtk_callback)

class WarningStrings(UIStrings):
    unsupported_env = UI('Dropbox requires App Indicator support to display the Dropbox tray icon. Dropbox will continue to run in the background. For full access to the tray icon, you will need to update your environment.')
    unsupported_env_title = UI('Unsupported desktop environment')
    missing_lib = UI('Dropbox can’t load the libappindicator library required for the tray icon. Dropbox will continue to run in the background. For full access to the tray icon, you will need to install this library.')
    missing_lib_title = UI('Missing libappindicator library')
    okay_btn = UI('OK')
    learn_more_btn = UI('Learn more')
    dont_ask_again_btn = UI("Don't show again")

LINUX_TRAY_HELP_URL = '/help/installs/dropbox-desktop-app-for-linux'
DESKTOP_ENV_HELP_FRAGMENT = 'Supported-desktop-environments'
MISSING_LIB_HELP_FRAGMENT = 'Required-software-libraries'

def maybe_show_desktop_environment_warning(app = None):
    pass
# WARNING: Decompyle incomplete


def maybe_show_missing_libappindicator_warning(app = None):
    pass
# WARNING: Decompyle incomplete


def should_load_app_indicator_tray_icon_dbus_next():
    
    async def async_should_load_app_indicator_tray_icon():
        pass
    # WARNING: Decompyle incomplete

    return asyncio.run(async_should_load_app_indicator_tray_icon())


class AppIndicatorDbusNextTrayIcon:
    pass
# WARNING: Decompyle incomplete

