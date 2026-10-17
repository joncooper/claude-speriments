# Source Generated with Decompyle++
# File: native.pyc (Python 3.11)

import os
from typing import Callable, Optional, Text
from  import DropboxLocationWindow
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.ui.native.location_changer import DropboxLocationChanger
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DropboxLocationWindowNative(DropboxLocationWindow):
    
    def __init__(self = None, app = None, account = None, callback = ('app', 'DropboxApplication', 'account', 'AccountInterface', 'callback', 'Callable[[Optional[Text], Optional[AccountInterface]], None]', 'return', 'None')):
        self._app = app
        self._account = account
        self._callback = callback
        self._is_open = False

    
    def show_location_preferences(self = None, base_path = None, folder_name = None, care_about_existing_dropbox = (False,)):
        self._is_open = True
        location_changer = DropboxLocationChanger(parent = None, app = self._app, account = self._account, sync_engine_adapter = None, start_location = base_path, dropbox_folder_name = folder_name, care_about_existing_dropbox = care_about_existing_dropbox)
        new_path = location_changer.get_new_dropbox_location()
        if new_path:
            self._callback(os.path.normpath(new_path), self._account)
        else:
            self._callback(None, None)
        self._is_open = False

    is_open = (lambda self = None: self._is_open)()

