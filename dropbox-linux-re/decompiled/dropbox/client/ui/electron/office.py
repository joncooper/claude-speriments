# Source Generated with Decompyle++
# File: office.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Callable
from build_number import BUILD_KEY
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.office import OfficeAddInStrings
from dropbox.foundation.html_views.electron.electron_dialog_constants import ElectronDialogCallbackInfo

class OfficeSplashScreen:
    
    def __init__(self, dialog_controller = None, allow_cb = None, deny_cb = None, close_cb = ('dialog_controller', 'DialogController', 'allow_cb', 'Callable[[], None]', 'deny_cb', 'Callable[[], None]', 'close_cb', 'Callable[[], None]', 'return', 'None')):
