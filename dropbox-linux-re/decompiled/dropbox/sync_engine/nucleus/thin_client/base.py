# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from abc import abstractmethod
from typing import cast, Dict, Optional, Text
from cffi_transport.exceptions import ServiceNotAvailableException
from google.protobuf.service import RpcController
from transitional_utils.futures import parasitic_future
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.transitional.wrapper_future import create_and_wrap_future
from dropbox.model.types import NsId
from dropbox.proto.nucleus.app_service_pb2 import LookupByFileIdReply, NucleusAPI, NucleusPhaseAgnosticAPI
from dropbox.proto.nucleus.common_api_types_pb2 import LocalLocationProperties, LookupByFileIdReq, RemoteLocationProperties
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto
from dropbox.sync_engine_boundary.exceptions import NucleusNotAvailableDuringAppShutdown

class NucleusThinClientBase:
    root_ns = (lambda self = None: pass)()
    get_queue_stats = (lambda self = None: pass)()
    stop = (lambda self = None, stop_reason = None: pass)()
    
    def thin_lookup_by_fileid(self = None, fileid = None):
        pass
    # WARNING: Decompyle incomplete

    
    def thin_lookup_remote_properties_by_fileid(self = None, fileid = None):
        get_remote_props = (lambda resp = None: resp.remote_properties if resp.HasField('remote_properties') else None)()
        return self.thin_lookup_by_fileid(fileid).then(get_remote_props)

    
    def thin_lookup_local_properties_by_fileid(self = None, fileid = None):
        local_props = (lambda resp = None: resp.local_properties if resp.HasField('local_properties') else None)()
        return self.thin_lookup_by_fileid(fileid).then(local_props)



class NucleusThinClient(NucleusPhaseAgnosticAPI, NucleusAPI, NucleusThinClientBase):
    pass

