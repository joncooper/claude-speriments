# Source Generated with Decompyle++
# File: change_location_dialog_api.pyc (Python 3.11)

import os
from typing import Callable, Optional, TYPE_CHECKING
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.account_cache import FenixAccountCache
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.change_location_dialog_pb2 import OpenChangeLocationDialogReply, OpenChangeLocationDialogReq
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.change_location_dialog_api_base import _ChangeLocationDialogBaseClass
from dropbox.client.fenix.meta_engine_apis.meta_engine_utils import proto_to_authenticated_account_dict
from dropbox.client.setup_wizard.change_location_window import DropboxLocationWindow
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures.basic import EasyFuture, Future, ResolvedFuture
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.trace import TRACE
if TYPE_CHECKING:
    from dropbox.client.main import DropboxApplication

class ChangeLocationDialogAPI(_ChangeLocationDialogBaseClass):
    pass
# WARNING: Decompyle incomplete

