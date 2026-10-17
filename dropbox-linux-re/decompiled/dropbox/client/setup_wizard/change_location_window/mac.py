# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

import os
from typing import Callable, cast, Optional, Text
from  import DropboxLocationWindow
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.ui.cocoa.location_changer import CocoaLocationChangerWindow
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DropboxLocationWindowMac(DropboxLocationWindow):
    
    def __init__(self = None, app = None, account = None, callback = ('app', 'DropboxApplication', 'account', 'AccountInterface', 'callback', 'Callable[[Optional[Text], Optional[AccountInterface]], None]', 'return', 'None')):
        self._app = app
        self._account = account
        self._callback = callback
        self._is_open = False
        self._location_changer = None

    
    def show_location_preferences(self = None, base_path = None, folder_name = None, care_about_existing_dropbox = (False,)):
        self._is_open = True
        account = cast(Account, self._account)
        self._location_changer = CocoaLocationChangerWindow(self._app, account, base_path, folder_name, self._change_location_completed, care_about_existing_dropbox = care_about_existing_dropbox)
        self._location_changer.open_location_changer()

    is_open = (lambda self = None: self._is_open)()
    
    def _change_location_completed(self = None, window = None):
        if window:
            self._callback(os.path.normpath(window.targetPath), self._account)
        else:
            self._callback(None, None)
        self._location_changer = None
        self._is_open = False


