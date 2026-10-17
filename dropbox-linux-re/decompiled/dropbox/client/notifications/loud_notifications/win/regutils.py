# Source Generated with Decompyle++
# File: regutils.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from pynt.helpers.registry import HKEY_CURRENT_USER, KEY_READ, registry_key, safe_read_registry_value
from build_number import BUILD_KEY
_DROPBOX_AUMID = BUILD_KEY + '.Desktop.Client'

def is_quiet_hours_enabled():
    hkey = registry_key(HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings', permission = KEY_READ)
    if hkey and safe_read_registry_value(hkey, 'NOC_GLOBAL_SETTING_TOASTS_ENABLED') == 0:
        None(None, None)
        return True
    None(None, None)


def is_dropbox_notifications_disabled():
    hkey = registry_key(HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\\' + _DROPBOX_AUMID, permission = KEY_READ)
    if hkey and safe_read_registry_value(hkey, 'Enabled') == 0:
        None(None, None)
        return True
    None(None, None)


def is_dropbox_banners_disabled():
    hkey = registry_key(HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\\' + _DROPBOX_AUMID, permission = KEY_READ)
    if hkey and safe_read_registry_value(hkey, 'ShowBanner') == 0:
        None(None, None)
        return True
    None(None, None)


def is_notifications_disabled():
    hkey = registry_key(HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PushNotifications', permission = KEY_READ)
    if hkey and safe_read_registry_value(hkey, 'ToastEnabled') == 0:
        None(None, None)
        return True
    None(None, None)

