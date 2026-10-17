# Source Generated with Decompyle++
# File: win_installer_restart.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Text
from pynt.constants import KEY_ALL_ACCESS, KEY_WOW64_32KEY, REG_DWORD
from pynt.helpers.registry import create_registry_key, registry_key, safe_delete_regvalue, safe_read_registry_value, set_registry_value
from six.moves.winreg import HKEY_CURRENT_USER
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.win32.win_cache import DROPBOX_REG_KEY
INSTALLER_RESTART_KEY = 'NoRestartAfterInstall'
INSTALLER_RESTART_STORMCROW_KEY = 'InstallerRestartStormcrow'

class InstallerRestartRegistryError(Exception):
    pass


def installer_should_not_restart_app():
    if os.environ.get('DBDEV_DISABLE_WINDOWS_INSTALLER_RESTART'):
        return True
    return _installer_restart_flag_enabled(INSTALLER_RESTART_KEY)


def set_installer_restart_flag():
    _set_installer_restart_flag(INSTALLER_RESTART_KEY)


def _set_installer_restart_stormcrow_flag():
    _set_installer_restart_flag(INSTALLER_RESTART_STORMCROW_KEY)


def remove_installer_restart_flag():
    _remove_installer_restart_flag(INSTALLER_RESTART_KEY)


def remove_installer_restart_stormcrow_flag():
    _remove_installer_restart_flag(INSTALLER_RESTART_STORMCROW_KEY)


def save_installer_restart_stormcrow_flag():
    _set_installer_restart_stormcrow_flag()


def _installer_restart_flag_enabled(flag = None):
    
    try:
        key = registry_key(HKEY_CURRENT_USER, DROPBOX_REG_KEY, permission = KEY_ALL_ACCESS | KEY_WOW64_32KEY)
        if key:
            enabled = safe_read_registry_value(key, flag)
            
            try:
                None(None, None)
                return 
                
                try:
                    None(None, None)
                    return False
                    with None:
                        if not None, enabled == 1:
                            
                            try:
                                
                                try:
                                    return None
                                except Exception:
                                    report_exception(severity = Severity.WARN, component = DesktopComponent.INSTALLER)
                                    return False







def _set_installer_restart_flag(flag = None):
    
    try:
        (key, _, _) = create_registry_key(HKEY_CURRENT_USER, DROPBOX_REG_KEY, permission = KEY_ALL_ACCESS | KEY_WOW64_32KEY, restrict_to_current_user = False)
        if key:
            set_registry_value(key, flag, REG_DWORD, 1)
        else:
            raise InstallerRestartRegistryError("Couldn't set key %s in registry" % flag)
        
        try:
            None(None, None)
            return None
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            report_exception(severity = Severity.WARN, component = DesktopComponent.INSTALLER)
                            return None






def _remove_installer_restart_flag(flag = None):
    
    try:
        safe_delete_regvalue(HKEY_CURRENT_USER, DROPBOX_REG_KEY, flag, delete_key = True, permission = KEY_ALL_ACCESS | KEY_WOW64_32KEY)
        return None
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.INSTALLER)
        return None


