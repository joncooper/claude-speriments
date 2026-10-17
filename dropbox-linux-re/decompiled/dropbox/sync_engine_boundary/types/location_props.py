# Source Generated with Decompyle++
# File: location_props.pyc (Python 3.11)

from dataclasses import dataclass
from typing import Callable, Optional, Tuple
from proto.nucleus.app_service_pb2 import LookupByFileIdReply
from sync_engine.file_system.abstract_file_system import AbstractFileSystem
from sync_engine_boundary.types.local_props import LocalDirectoryProperties, LocalFileProperties, LocalLocationProperties
from sync_engine_boundary.types.remote_props import DirectoryProperties, MountProperties, RemoteLocationProperties
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.model.types import FileId, NsId
LocationProperties = <NODE:12>()
