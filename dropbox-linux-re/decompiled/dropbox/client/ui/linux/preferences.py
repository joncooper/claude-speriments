# Source Generated with Decompyle++
# File: preferences.pyc (Python 3.11)

from ctypes import c_void_p, CFUNCTYPE
from enum import IntEnum
from typing import Any, Callable, Dict, List, Optional, Text
from build_number import VERSION
from dropbox.client.notifications.preference_settings import NotificationPreferencesStringMapping
from dropbox.client.ui.common.preferences import change_client_language
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.client.ui.linux.gtk_lib_app_indicator_loader import get_gtk_libappindicator_loader
from dropbox.client.ui.linux.selective_sync_gtk import SelectiveSyncGTK
from dropbox.client.ui.native.location_changer import DropboxLocationChanger
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.i18n import get_available_languages
from dropbox.preferences import AUTO_PROXY, MANUAL_PROXY, NO_PROXY, NOTIF_HAS_MODIFIED_SUFFIX, OPT_LANG
from dropbox.threading import Lock
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
GTK_RESPONSE_DELETE_EVENT = -4

class PrefStrings(UIStrings):
    preferences = UI('Preferences')
    language_btn = UI('Language')
    notifications_btn = UI('Notifications')
    unlink_btn = UI('Unlink Dropbox...')
    move_dropbox_btn = UI('Move Dropbox...')
    more_preferences_btn = UI('More Settings...')
    selective_sync_btn = UI('Selective Sync...')
    ok_btn = UI('OK')
    cancel_btn = UI('Cancel')
    unlink_dialog_caption = UI('Unlink your Dropbox account?')
    unlink_dialog_message = UI("Are you sure you want to unlink this computer from Dropbox?\n\nThis will stop syncing your files, but won't delete the files in your Dropbox folder.")
    buildkey_and_version = UI('Dropbox <b>v%(version_string)s</b>')
    dropbox_location = UI('Location: <b>%(dropbox_path)s</b>')
    bandwidth_btn = UI('Bandwidth')
    bandwidth_dialog_caption = UI('Bandwidth Settings')
    bandwidth_unlimited = UI("Don't limit")
    bandwidth_custom = UI('Limit to (KB/s)')
    download_label = UI('Download rate')
    upload_label = UI('Upload rate')
    auto_limit_upload = UI('Limit automatically')
    proxies_colon = UI('Proxies:')
    proxy_tab_label = UI('Proxies')
    proxy_settings_label = UI('Proxy settings:')
    no_proxy_choice = UI('No proxy')
    auto_proxy_choice = UI('Auto-detect')
    manual_proxy_choice = UI('Manual')
    proxy_mode_label = UI('Proxy settings:')
    proxy_type_label = UI('Proxy type:')
    proxy_server_label = UI('Server:')
    proxy_port_label = UI('Port:')
    proxy_requires_password_checkbox = UI('Proxy server requires a password')
    proxy_username_label = UI('Username:')
    proxy_password_label = UI('Password:')
    proxy_server_not_set = UI('Please set a proxy server')
    proxy_server_not_set_explanation = UI('You must specify a proxy server.')


class BandwidthOption(IntEnum):
    NO_LIMIT = 0
    AUTO_LIMIT = 1
    CUSTOM_LIMIT = 2


class ProxyType(IntEnum):
    HTTP = 0
    SOCKS4 = 1
    SOCKS5 = 2

PROXY_TYPE_MAPPING = {
    'HTTP': ProxyType.HTTP,
    'SOCKS4': ProxyType.SOCKS4,
    'SOCKS5': ProxyType.SOCKS5 }

class MainMenuOption(IntEnum):
    LANGUAGE = 0
    NOTIFICATIONS = 1
    UNLINK_ACCOUNT = 2
    BANDWIDTH = 3
    PROXY = 4
    MOVE_DROPBOX_FOLDER = 5
    SELECTIVE_SYNC = 6

MAIN_MENU_MAPPING = {
    MainMenuOption.SELECTIVE_SYNC: PrefStrings.selective_sync_btn,
    MainMenuOption.MOVE_DROPBOX_FOLDER: PrefStrings.move_dropbox_btn,
    MainMenuOption.PROXY: PrefStrings.proxy_tab_label,
    MainMenuOption.BANDWIDTH: PrefStrings.bandwidth_btn,
    MainMenuOption.UNLINK_ACCOUNT: PrefStrings.unlink_btn,
    MainMenuOption.NOTIFICATIONS: PrefStrings.notifications_btn,
    MainMenuOption.LANGUAGE: PrefStrings.language_btn }

class ModalButtons(IntEnum):
    OK = 0
    CANCEL = 1

MODAL_BUTTONS_MAPPING = {
    ModalButtons.CANCEL: PrefStrings.cancel_btn,
    ModalButtons.OK: PrefStrings.ok_btn }

class PreferenceDialogCallbackArgs:
    
    def __init__(self = None, button_index = None, dropdown_index = None, checkbox_states = (None, None, None)):
        self.button_index = button_index
        self.dropdown_index = dropdown_index
        self.checkbox_states = checkbox_states if checkbox_states else []



class LinuxPreferencesController:
    pass
# WARNING: Decompyle incomplete

