# Source Generated with Decompyle++
# File: generic_rpc_api.pyc (Python 3.11)

import json
import uuid
from dataclasses import dataclass
from typing import Any, Dict, Optional, Text, Union
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.generic_rpc_pb2 import GenericRpcRequest, GenericRpcResponse, MessageType
from dropbox.client.fenix.generated_types.shared_pb2 import AuthenticatedAccount
from dropbox.client.fenix.meta_engine_apis.base import GLOBAL_ACCOUNT_ID
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.generic_rpc_api_base import _GenericRpcBaseClass
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import EasyFuture
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONish
from dropbox.foundation.html_views.electron.ipc.rpc import InvocationCallback, SignalCallback
from dropbox.threading import Lock
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
ServiceHandlers = <NODE:12>()

class GenericRpcAPI(_GenericRpcBaseClass):
    pass
# WARNING: Decompyle incomplete

GENERIC_RPC_API_SINGLETON: 'Optional[GenericRpcAPI]' = None

def init_generic_rpc_api(app = None, electron_ipc = dataclass, event_hub = None):
    pass
# WARNING: Decompyle incomplete


def get_generic_rpc_api():
    pass
# WARNING: Decompyle incomplete

