# Source Generated with Decompyle++
# File: debug_cdm.pyc (Python 3.11)

from typing import NamedTuple, Optional, Text
from dropbox.client.background_worker import on_background_thread
from dropbox.client.ui.common.dropbox_menu import MenuItem, SubMenu
from dropbox.client.ui.icon_overlay import patch_context_menus_for_debugging
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath, MacOSXPath, WindowsPath
from dropbox.shared.util import db_lower
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
CdmDialogTestScenarioDetails = NamedTuple('CdmDialogTestScenarioDetails', [
    ('local_path', Optional[LocalPath]),
    ('error_detail', Text)])

class CdmDebug:
    
    def __init__(self = None, dropbox_app = None):
        self.dropbox_app = dropbox_app

    
    def make_cdm_debug_menu(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def cdm_debug_operations(self = None, operation = None):
        if operation == 'cdm_enable_context_menu_options':
            patch_context_menus_for_debugging(self.dropbox_app.status_thread, is_enabled = True)
            return None
        if None == 'cdm_disable_context_menu_options':
            patch_context_menus_for_debugging(self.dropbox_app.status_thread, is_enabled = False)
            return None

    cdm_migration_error_dialog = (lambda self = None: _get_temporary_arrange_error_alert_details = _get_temporary_arrange_error_alert_details_get_temporary_exception_alert_dialog_buttons = _get_temporary_exception_alert_dialog_buttonsimport dropbox.client.relocate_namespace_foldersif IS_WINDOWS:
in_use_local_path = WindowsPath('C:\\Program Files')non_existing_local_path = WindowsPath('C:\\NonExisting')elif IS_MAC:
in_use_local_path = MacOSXPath('/Users/vagrant/Dropbox')non_existing_local_path = MacOSXPath('/Users/vagrant/NonExisting')else:
Noneteam_name = Nonetest_scenarios = [
CdmDialogTestScenarioDetails(in_use_local_path, "Couldn't rename: %(path)s" % {
'path': in_use_local_path.to_unicode() }),
CdmDialogTestScenarioDetails(non_existing_local_path, "Couldn't rename: %(path)s" % {
'path': non_existing_local_path.to_unicode() }),
CdmDialogTestScenarioDetails(None, "Couldn't delete .dropbox-relocate file.")]# WARNING: Decompyle incomplete
)()
    
    def normalized_local_path(self = None, unicode_local_path = None):
        return db_lower(unicode_local_path)


