# Source Generated with Decompyle++
# File: theme.pyc (Python 3.11)

from __future__ import absolute_import, division
import enum
from typing import Optional, Text
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from pynt.constants import HKEY_CURRENT_USER, KEY_READ
    from pynt.helpers.registry import registry_key, safe_read_registry_value
    from dropbox.win32.version import WIN10, WIN10_VERSION_1903, WINDOWS_VERSION
    
    class WindowsOSTheme(enum.Enum):
        DARK = enum.auto()
        LIGHT = enum.auto()

    
    class WindowsAppTheme(enum.Enum):
        DARK = enum.auto()
        LIGHT = enum.auto()

    
    def _get_theme_registry_value(value = None):
        if WINDOWS_VERSION.version_number() >= WIN10.version_number():
            hkey = registry_key(HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize', permission = KEY_READ)
            if hkey:
                None(None, None)
                return 
            None(None, None)
        else:
            with None:
                if not None:
                    pass

    
    def _is_support_light_theme():
        return WINDOWS_VERSION.version_number() >= WIN10_VERSION_1903

    
    def get_os_theme():
        if not _is_support_light_theme():
            return WindowsOSTheme.DARK
        value = _get_theme_registry_value('SystemUsesLightTheme')
        return WindowsOSTheme.LIGHT if value == 1 else WindowsOSTheme.DARK

    
    def get_app_theme():
        value = _get_theme_registry_value('AppsUseLightTheme')
    # WARNING: Decompyle incomplete

    return None
