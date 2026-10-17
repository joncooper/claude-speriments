# Source Generated with Decompyle++
# File: stormcrow_service.pyc (Python 3.11)

from typing import Any, cast, Dict, List, Optional
from build_number.features import feature_enabled
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.types.account import AuthenticatedAccount
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import assert_not_none
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import FutureHelpers
from dropbox.foundation.futures.basic import Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class StormcrowService(Actor):
    pass
# WARNING: Decompyle incomplete

