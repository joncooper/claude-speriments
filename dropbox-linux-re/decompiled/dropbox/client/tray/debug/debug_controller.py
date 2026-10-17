# Source Generated with Decompyle++
# File: debug_controller.pyc (Python 3.11)

import os
from typing import Any, Callable, List, Optional, Text
from mypy_extensions import KwArg, VarArg
from build_number import is_frozen
from dropbox.client.background_worker import on_background_thread
from dropbox.client.high_trace import send_trace_log
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.tray.debug.debug_cdm import CdmDebug
from dropbox.client.tray.debug.tray_debug import TrayDebugMenu
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem, SubMenu
from dropbox.client.ui.common.tray_popup_constants import TrayUpdateOptionsReason
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_returns_none
from dropbox.foundation.disk_space_status import DiskSpaceManager
from dropbox.foundation.disk_space_status.disk_space_manager_factory import DiskSpaceManagerFactory
from dropbox.foundation.environment import tray_debug_menu_is_enabled
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE, trace_threads
from dropbox.webdebugger.server import WebDebugger
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DebugController:
    
    def __init__(self = None, dropbox_app = None):
        self.dropbox_app = dropbox_app
        disk_space_manager = DiskSpaceManagerFactory.create(dropbox_app)
        self._disk_space_manager = disk_space_manager
        self._debug_menu = TrayDebugMenu(dropbox_app, disk_space_manager)
        self.cdm = CdmDebug(dropbox_app)
        self._debugging_options = None
        self._log_break_counter = 0
        self._log_break_dialog = None

    
    def insert_log_break(self = None):
        if not tray_debug_menu_is_enabled():
            return None
        if None:
            self._insert_log_break_mac()
            return None
        if None:
            self._insert_log_break_windows()
            return None

    
    def _emit_log_break(self = None, label = None):
        TRACE('#### DEBUG LOG BREAK: %s ####', label)

    _insert_log_break_mac = (lambda self = None: LogBreakDialog = LogBreakDialogimport dropbox.client.ui.cocoa.log_break_dialogself._log_break_dialog = LogBreakDialog(self._emit_log_break))()
    _insert_log_break_windows = (lambda self = None: LogBreakDialog = LogBreakDialogimport dropbox.client.ui.win32.log_break_dialogself._log_break_dialog = LogBreakDialog(self._emit_log_break)self._log_break_dialog.show())()
    
    def open_url_thunk(self = None, url = None, needs_login = None):
        pass
    # WARNING: Decompyle incomplete

    
    def open_webdebugger(self = None):
        webdebugger = WebDebugger()
        self.dropbox_app.dropbox_url_info.launch_full_url('http://localhost:%d' % webdebugger.port)

    
    def soft_resync(self = None):
        for account in self.dropbox_app.account_manager.linked_accounts:
            nucleus = self.dropbox_app.sync_engine_adapter.nucleus_api(account)
            if nucleus:
                nucleus.queue_resync()
            return None

    
    def debug_sfj_consistency_checker(self = None):
        for account in self.dropbox_app.account_manager.linked_accounts:
            nucleus = self.dropbox_app.sync_engine_adapter.nucleus_api(account)
            if nucleus:
                nucleus.debug_sfj_consistency_checker().catch(Exception, (lambda e, _: TRACE('Failed to request consistency check: %r', e)))
            return None

    
    def access_desktop(self = None):
        get_desktop_directory = get_desktop_directory
        import dropbox.mac.internal
        os.listdir(get_desktop_directory())

    
    def reconnect_all(self = None):
        self.dropbox_app.conn.reconnect()

    
    def _test_cycle_tray_icons(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def test_download_updator_via_cdn(self = None):
        self.dropbox_app.update_logic.handle_server_response({
            'update_to_dict': {
                'version': 'whatever',
                'blocklist': 'oR1MKlFfGFqECVUSNqt5vv_ndxUmCKwU3vBSlRv69Gk,zVIi3ny4FXK439T5t3bxDw1hJvIZwSekOYzSOdPk8bo,eJNIXpWOpYwteM_QImdN3jy0tCzUw6ZmLipXg9RctHg,-Y216KH4Dbf77PKKChmtzYUUxzwqRyb7i2Oz8FftFvY,F3CyWPt8hcmVmPUY5_uVL0fakJhXZUFw7Mhmyg3Ua-c,AJ-Vna2OvzVd0ESzNZAN6L3wGOtL9KK0iJmNH4EwrUs,uoz_mUKfw4o9AzsYMYBzlAmGSuxxSDzqwOlRoacUSC4,s1UmwnP7CZaP96ChXksV1VWLxyBDPsMEmDNwfKGjKJ8',
                'url': 'https://clientupdates.dropboxstatic.com/dbx-releng/client/Dropbox-darwin-update-2.3.12.tar.bz2' } })

    
    def make_debugging_options(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _make_debugging_options_non_frozen(self = None):
        return [
            MenuItem('Reconnect all', self.reconnect_all),
            MenuItem('Test Download Updater CDN', self.test_download_updator_via_cdn)]

    
    def create_debug_menu_options(self = None):
        return self._debug_menu.create_debug_menu_options()


