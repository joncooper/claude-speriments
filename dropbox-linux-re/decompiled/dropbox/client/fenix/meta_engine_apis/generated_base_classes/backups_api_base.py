# Source Generated with Decompyle++
# File: backups_api_base.pyc (Python 3.11)

from typing import Dict, Callable, Optional
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.meta_engine_api import MetaEngineBaseClass
from dropbox.client.fenix.meta_engine_apis.base import serialize_protobuf_response, wrap_typed_handler
from abc import abstractmethod
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.client.fenix.generated_types.backups_pb2 import ListComputerBackupsReply, ListComputerBackupsReq, ListExternalDriveBackupsReply, ListExternalDriveBackupsReq
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveEvent, ReactiveRequest
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class _BackupServiceBaseClass(MetaEngineBaseClass):
    pass
# WARNING: Decompyle incomplete

