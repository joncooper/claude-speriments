# Source Generated with Decompyle++
# File: location_changer.pyc (Python 3.11)

from typing import Any, Callable, Optional, Text
import objc
from AppKit import NSWindow
from dropbox.client.authentication.account import Account
from dropbox.client.ui.cocoa.dropbox_controls import DropboxLocationSheetMixin
from dropbox.gui import event_handler
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class CocoaLocationChangerWindow(DropboxLocationSheetMixin, NSWindow):
    
    def __new__(cls, app, account = None, dropbox_path = None, dropbox_folder = None, callback = (False,), care_about_existing_dropbox = ('app', 'DropboxApplication', 'account', 'Account', 'dropbox_path', 'Text', 'dropbox_folder', 'Text', 'callback', 'Callable[[CocoaLocationChangerWindow], None]', 'care_about_existing_dropbox', 'bool', 'return', 'CocoaLocationChangerWindow')):
        return CocoaLocationChangerWindow.alloc().initWithApp_andAccount_andPath_andFolder_andCallback_(app, account, dropbox_path, dropbox_folder, callback, care_about_existing_dropbox)

    
    def initWithApp_andAccount_andPath_andFolder_andCallback_(self, app, account = None, dropbox_path = None, dropbox_folder = None, callback = (False,), care_about_existing_dropbox = ('app', 'DropboxApplication', 'account', 'Account', 'dropbox_path', 'Text', 'dropbox_folder', 'Text', 'callback', 'Callable[(Ellipsis, None)]', 'care_about_existing_dropbox', 'bool', 'return', 'CocoaLocationChangerWindow')):
        self._CocoaLocationChangerWindow__dropbox_app = app
        self._CocoaLocationChangerWindow__account = account
        self._path = dropbox_path
        self._folder = dropbox_folder
        self._CocoaLocationChangerWindow__action = callback
        self._cancelled = callback
        self._care_about_existing_dropbox = care_about_existing_dropbox
        return self

    _action = (lambda self = None: self._CocoaLocationChangerWindow__action)()
    _account = (lambda self = None: self._CocoaLocationChangerWindow__account)()
    _dropbox_app = (lambda self = None: self._CocoaLocationChangerWindow__dropbox_app)()
    _sync_engine_adapter = (lambda self = None: self._CocoaLocationChangerWindow__sync_engine_adapter)()
    window = (lambda self = None: self._window)()
    
    def getFolderName(self = None):
        return self._folder

    open_location_changer = (lambda self = None: self.initialSelection = self._pathself._CocoaLocationChangerWindow__sync_engine_adapter = None
self._window = lambda : passself.changeLocation_(None))()
    changeLocation_ = (lambda self, sender: self._changeLocation_(sender))()()
    openPanelDidEnd_returnCode_contextInfo_ = (lambda self, sheet, returnCode, ctx: self._openPanelDidEnd_returnCode_contextInfo_(sheet, returnCode, ctx))()()
    
    def cancelled(self):
        pass
    # WARNING: Decompyle incomplete

    
    def dealloc(self):
        objc.super(CocoaLocationChangerWindow, self).dealloc()


