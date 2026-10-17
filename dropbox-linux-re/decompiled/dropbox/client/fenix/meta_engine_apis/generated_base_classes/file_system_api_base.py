# Source Generated with Decompyle++
# File: file_system_api_base.pyc (Python 3.11)

from typing import Dict, Callable, Optional
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.meta_engine_api import MetaEngineBaseClass
from dropbox.client.fenix.meta_engine_apis.base import serialize_protobuf_response, wrap_typed_handler
from abc import abstractmethod
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.client.fenix.generated_types.file_system_pb2 import BoolResult, DiskSpaceInfo, FileSystemPathReq
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class _FileSystemBaseClass(MetaEngineBaseClass):
    pass
# WARNING: Decompyle incomplete

