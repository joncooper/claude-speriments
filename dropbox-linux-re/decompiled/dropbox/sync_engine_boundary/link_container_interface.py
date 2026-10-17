# Source Generated with Decompyle++
# File: link_container_interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Callable, Dict, Optional
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.proto.nucleus.link_container_pb2 import LinkContainerState
from dropbox.proto.per_node_metadata.link_node_pb2 import LinkNodeEntity
from dropbox.sync_engine_boundary.types import CallbackRemovalToken

class SyncEngineLinkContainerInterface(ABC):
    container_state = (lambda self = None, fileid = None: raise NotImplementedError())()
    dematerialize_container = (lambda self = None, fileid = None: raise NotImplementedError())()
    list_containers = (lambda self = None: raise NotImplementedError())()
    materialize_container = (lambda self = None, fileid = None: raise NotImplementedError())()
    on_link_container_changed = (lambda self = None, callback = None: raise NotImplementedError())()
    remove_on_link_container_changed = (lambda self = None, token = None: raise NotImplementedError())()

