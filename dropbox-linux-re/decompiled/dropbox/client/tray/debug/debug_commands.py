# Source Generated with Decompyle++
# File: debug_commands.pyc (Python 3.11)

from datetime import datetime
from typing import Any, Optional
from dropbox.client.main import DropboxApplication
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.navigation_service.manifest_registry import DEBUG_MENU_OVERRIDE_STORMCROW, EVENT_LOGGER_DISPLAY

class DebugCommands:
    
    def __init__(self = None, app = None):
        self.app = app

    
    def tray(self = None):
        ui_kit = self.app.ui_kit
    # WARNING: Decompyle incomplete

    
    def on_ui_thread(self = None, fn = None):
        return on_ui_thread(fn)()

    
    def stormcrow(self = None):
        self._nav_service().navigate(DEBUG_MENU_OVERRIDE_STORMCROW)

    
    def event_log(self = None):
        self._nav_service().navigate(EVENT_LOGGER_DISPLAY)

    
    def _nav_service(self = None):
        navigation_service = self.app.navigation_service
    # WARNING: Decompyle incomplete

    
    def start_profiler(self = None, reduced_profile_size = None, timeout = None):
        Profiler = Profiler
        import dropbox.client.features.chrome_profiler.profiler
        Profiler.start_singleton(datetime.now().strftime('profile_%Y-%m-%d_%H-%M-%S.json'), reduced_profile_size, timeout)

    
    def stop_profiler(self):
        Profiler = Profiler
        import dropbox.client.features.chrome_profiler.profiler
        Profiler.stop_singleton()


