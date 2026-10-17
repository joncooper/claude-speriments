# Source Generated with Decompyle++
# File: sync_engine_file_props_client_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from abc import ABC, abstractmethod
from typing import Collection, Dict, Mapping, Optional
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties

class SyncEngineFilePropsClientInterface(ABC):
    lookup_local_path_properties = (lambda self = None, local_path = None, fileid_timeout = abstractmethod: raise NotImplementedError())()
    lookup_local_path_properties_batch = (lambda self = None, local_paths = None, fileid_timeout = abstractmethod: raise NotImplementedError())()
    lookup_properties_by_fileid_batch = (lambda self = None, fileids = None: raise NotImplementedError())()
    lookup_properties_by_fileid = (lambda self = None, fileid = None: raise NotImplementedError())()
    lookup_properties_by_local_path = (lambda self = None, local_path = None, retry_count = abstractmethod, compute_inherited = (2, False): raise NotImplementedError())()
    lookup_local_properties_by_fileid_batch = (lambda self = None, fileids = None: raise NotImplementedError())()
    lookup_local_properties_by_fileid = (lambda self = None, fileid = None: raise NotImplementedError())()
    lookup_remote_properties_by_fileid = (lambda self = None, fileid = None: raise NotImplementedError())()
    lookup_remote_properties_by_fileid_batch = (lambda self = None, fileids = None: raise NotImplementedError())()

