# Source Generated with Decompyle++
# File: electron_dialogs.pyc (Python 3.11)

MYPY = False
import uuid
from typing import Callable, Dict, List, Optional, Text
from dropbox.client.ui.common.uikit import Closeable, on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures.basic import EasyFuture
from dropbox.foundation.html_views.electron.adapters.electron_dialog_adapter import DIALOG_CLOSED, DIALOG_RESULT, ElectronDialogIpcAdapter
from dropbox.foundation.html_views.electron.electron_dialog_constants import DialogArgs, DialogIconType, DialogInfo, ElectronDialogCallbackInfo, QueuedDialogInfo, VisStyles
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.foundation.html_views.electron.managed_electron_view import ManagedElectronViewDefinition, ManagedElectronViewResult
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.threading import RLock
from dropbox.trace import TRACE
if MYPY:
    from dropbox.client.main import DropboxApplication

def get_unique_dialog_id():
    return str(uuid.uuid4())


class ElectronDialogController(Destroyable):
    pass
# WARNING: Decompyle incomplete

