# Source Generated with Decompyle++
# File: admin_preference.pyc (Python 3.11)

from typing import Optional, Union
from dropbox.client.configuration.admin_preference.gating import desktop_settings_propagation_stormcrow_enabled
from dropbox.client.configuration.admin_preference.reader import AdminPreferenceSetting
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from dropbox.client.configuration.admin_preference.reader.windows import AdminPreferenceReaderWin as AdminPreferenceReader
else:
    from dropbox.client.configuration.admin_preference.reader.unix import AdminPreferenceReaderUNIX as AdminPreferenceReader
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility

class AdminPreference:
    
    def __init__(self = None, app = None):
        self._app = app

    
    def get_admin_preference(self = None, preference_key = None):
        
        try:
            if not self._is_desktop_settings_propagation_stormcrow_enabled():
                return None
            admin_preference = AdminPreferenceReader.get_admin_preference(preference_key)
            return admin_preference
        except Exception:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.DATABASES)
            return None


    
    def _is_desktop_settings_propagation_stormcrow_enabled(self = None):
        
        try:
            app_model_watcher = self._app.app_model_watcher
            if not app_model_watcher:
                return False
            machine_stormcrow = None.get_app_model().machine_context.stormcrow
            return desktop_settings_propagation_stormcrow_enabled(machine_stormcrow)
        except:
            return True


    
    def is_preference_locked(self = None, preference_key = None):
        admin_preference_setting = self.get_admin_preference(preference_key)
        if admin_preference_setting:
            return admin_preference_setting.is_locked_setting


