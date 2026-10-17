# Source Generated with Decompyle++
# File: rpc_impl_test_service.pyc (Python 3.11)

import traceback
from typing import Any, Dict, Union
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.meta_engine_apis.generic_rpc_api import init_generic_rpc_api
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONish
from dropbox.foundation.html_views.electron.ipc.meta_engine_rpc import MetaEngineRpc
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class RpcImplTestService(Actor):
    pass
# WARNING: Decompyle incomplete

