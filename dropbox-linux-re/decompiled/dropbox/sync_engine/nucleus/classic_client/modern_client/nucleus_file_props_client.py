# Source Generated with Decompyle++
# File: nucleus_file_props_client.pyc (Python 3.11)

import dataclasses
import random as insecure_random
from time import monotonic
from typing import Collection, Dict, Mapping, Optional
from apex.metrics import Metric
from build_number import BuildChannel, dropbox_version
from google.protobuf.service import RpcController
from base import NucleusModernClientBase
from nucleus_decorators import boundary_api
import dropbox.proto.nucleus.app_service_pb2 as dropbox
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.metrics.constants import LOOKUP_FILEID_BATCH_ENABLED_TAG, SYNC_ENGINE_GENERATION_TAG, SYNC_ROOT_TYPE_TAG
from dropbox.model.types import FileId
from dropbox.proto.nucleus.app_service_pb2 import LookupByFileIdReply, LookupPropsByLocalPathReply, LookupPropsByLocalPathReq
from dropbox.proto.nucleus.common_api_types_pb2 import LookupByFileIdReq, LookupByLocalPathReq
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto, LocalPath as LocalPathProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.exceptions import NucleusNotAvailableDuringAppShutdown, NucleusProtoException
from dropbox.sync_engine_boundary.sync_engine_file_props_client_interface import SyncEngineFilePropsClientInterface
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties, UntrackedPathException
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
from dropbox.sync_engine_boundary.utils import backup_mode_args_to_engine_generation
from dropbox.trace import TRACE
BATCH_SIZE_SAMPLE_RATE = {
    BuildChannel.stable: 0.01,
    BuildChannel.beta: 0.1,
    BuildChannel.internal_alpha: 1,
    BuildChannel.developer: 1 }.get(dropbox_version.channel, 0.01)

class NucleusFilePropsClient(NucleusModernClientBase, SyncEngineFilePropsClientInterface):
    
    def _should_log_batch_size(self = None):
        return insecure_random.random() < BATCH_SIZE_SAMPLE_RATE

    
    def _log_batch_size(self = None, api_name = None, size = None, tags = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _lookup_local_path_properties(self = None, local_path = None, fileid_timeout = None):
        pass
    # WARNING: Decompyle incomplete

    lookup_local_path_properties = (lambda self = None, local_path = None, fileid_timeout = boundary_api: self._lookup_local_path_properties(local_path, fileid_timeout))()
    lookup_local_path_properties_batch = (lambda self = None, local_paths = None, fileid_timeout = boundary_api: pass# WARNING: Decompyle incomplete
)()
    
    def _lookup_properties_by_fileid_batch_internal(self = None, fileids = None):
        pass
    # WARNING: Decompyle incomplete

    lookup_properties_by_fileid_batch = (lambda self = None, fileids = None: self._lookup_properties_by_fileid_batch_internal(fileids))()
    
    def _lookup_properties_by_fileid(self = None, fileid = None):
        pass
    # WARNING: Decompyle incomplete

    lookup_properties_by_fileid = (lambda self = None, fileid = None: self._lookup_properties_by_fileid(fileid))()
    lookup_properties_by_local_path = (lambda self = None, local_path = None, retry_count = boundary_api, compute_inherited = (2, False): pass# WARNING: Decompyle incomplete
)()
    lookup_local_properties_by_fileid_batch = (lambda self = None, fileids = None: if len(fileids) == 0:
ResolvedFuture({ })
def convert(props = None):
res = { }for k, v in props.items():
res[k] = v.local_propertiesResolvedFuture(res)self._lookup_properties_by_fileid_batch_internal(fileids).then(convert))()
    
    def _lookup_local_properties_by_fileid(self = None, fileid = None):
        pass
    # WARNING: Decompyle incomplete

    lookup_local_properties_by_fileid = (lambda self = None, fileid = None: self._lookup_local_properties_by_fileid(fileid))()
    lookup_remote_properties_by_fileid_batch = (lambda self = None, fileids = None: 
def convert(props = None):
res = { }for k, v in props.items():
res[k] = v.remote_propertiesResolvedFuture(res)self._lookup_properties_by_fileid_batch_internal(fileids).then(convert))()
    
    def _lookup_remote_properties_by_fileid(self = None, fileid = None):
        pass
    # WARNING: Decompyle incomplete

    lookup_remote_properties_by_fileid = (lambda self = None, fileid = None: self._lookup_remote_properties_by_fileid(fileid))()

