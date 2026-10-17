# Source Generated with Decompyle++
# File: selective_sync_gtk.pyc (Python 3.11)

import ctypes
import ctypes.util as ctypes
from typing import Any, Dict, List, Optional, Set
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.client.ui.common.selective_sync_v2 import CheckState, RemoteFolder, SelectiveSyncBase, SelectiveSyncStrings
from dropbox.client.ui.linux.gtk_lib_app_indicator_loader import get_gtk_libappindicator_loader
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class SelectiveSyncGTK(SelectiveSyncBase):
    
    def __init__(self = None, app = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    gtk = (lambda self = None: self._gtk)()
    
    def _complete_initial_load(self = None):
        self._refresh_select_all()
        self.gtk.gtk_widget_set_sensitive(self.select_all_checkbox, True)
        self._initial_load_done = True

    
    def _populate_home_children(self = None, children = None, home = None):
