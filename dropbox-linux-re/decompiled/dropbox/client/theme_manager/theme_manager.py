# Source Generated with Decompyle++
# File: theme_manager.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.theme_manager.types import Theme
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.platform import IS_MAC, IS_WINDOWS
if IS_WINDOWS:
    from dropbox.client.ui.win32.theme import get_app_theme, WindowsAppTheme
if IS_MAC:
    from AppKit import NSUserDefaults
DEFAULT_THEME = Theme.SYSTEM

def get_theme_preference(machine_context = None):
    primary_account_config = machine_context.primary_account_config
# WARNING: Decompyle incomplete


def set_theme_setting_to_value(machine_context = None, value = None):
    primary_account_config = machine_context.primary_account_config
# WARNING: Decompyle incomplete


def get_os_theme_setting():
    if IS_WINDOWS:
        return Theme.DARK if get_app_theme() == WindowsAppTheme.DARK else Theme.BRIGHT
    if None:
        defaults = NSUserDefaults.standardUserDefaults()
        return Theme.DARK if str(defaults.objectForKey_('AppleInterfaceStyle')) == 'Dark' else Theme.BRIGHT
    return None.BRIGHT


def get_current_theme_setting(machine_context = None):
    primary_account_config = machine_context.primary_account_config
# WARNING: Decompyle incomplete


def _log_theme_setting(theme_setting = None, display_theme = None, account = None):
    new_event = NonUserLoggingEvent(event_name = 'load_theme', feature_session_id = '', action_surface = 'theming', source = '', component = DesktopComponent.THEME_MANAGEMENT, extra_hive_dict_pii = {
        'theme_setting': theme_setting.value if theme_setting else 'none',
        'display_theme': display_theme.value if display_theme else 'none' }, extra_amis_tags = {
        'theme_setting': theme_setting.value if theme_setting else 'none',
        'display_theme': display_theme.value if display_theme else 'none' })
    DesktopLogger.log_event(new_event, account)


def _log_theme_preference_changed(theme_setting = None, display_theme = None, account = None):
    new_event = NonUserLoggingEvent(event_name = 'theme_changed', feature_session_id = '', action_surface = 'theming', source = '', component = DesktopComponent.THEME_MANAGEMENT, extra_hive_dict_pii = {
        'theme_setting': theme_setting.value if theme_setting else 'none',
        'display_theme': display_theme.value if display_theme else 'none' }, extra_amis_tags = {
        'theme_setting': theme_setting.value if theme_setting else 'none',
        'display_theme': display_theme.value if display_theme else 'none' })
    DesktopLogger.log_event(new_event, account)


def _get_primary_account(machine_context = None):
    accounts = machine_context.account_manager.account_models.keys()
    for account in accounts:
        if account.is_primary:
            
            return None, account
        return None

