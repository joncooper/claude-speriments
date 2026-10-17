# Source Generated with Decompyle++
# File: external_context_menu_sharing_service.pyc (Python 3.11)

from typing import cast, Optional, Text
from dropbox.client.client_shmodel import ClientShmodelOrigin
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class ExternalContextMenuSharingService(Actor):
    pass
# WARNING: Decompyle incomplete

