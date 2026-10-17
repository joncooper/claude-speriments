# Source Generated with Decompyle++
# File: temp_volume.pyc (Python 3.11)

from typing import Dict
from google.protobuf.service import RpcController
from thin_client.exceptions import NucleusClientError
from nucleus_decorators import boundary_api
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.proto.fs_api.fs_api_service_pb2 import CreateTempVolumeReply, CreateTempVolumeReq, DropTempVolumeReply, DropTempVolumeReq, Filesystem as FilesystemProto
from dropbox.proto.nucleus.types_pb2 import LocalPath as LocalPathProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.temp_volume_interface import TempVolumeInterface
from dropbox.sync_engine_boundary.types import Filesystem, TempVolumeInfo
_FILE_SYSTEM_LOOKUP_MAP: 'Dict[int, Filesystem]' = {
    FilesystemProto.UDF: Filesystem.UDF,
    FilesystemProto.ExFAT: Filesystem.ExFAT,
    FilesystemProto.FAT32: Filesystem.FAT32,
    FilesystemProto.OsDefault: Filesystem.OsDefault,
    FilesystemProto.INVALID_FS: Filesystem.INVALID }
_PROTO_FILE_SYSTEM_LOOKUP_MAP: 'Dict[Filesystem, FilesystemProto]' = {
    Filesystem.UDF: FilesystemProto.UDF,
    Filesystem.ExFAT: FilesystemProto.ExFAT,
    Filesystem.FAT32: FilesystemProto.FAT32,
    Filesystem.OsDefault: FilesystemProto.OsDefault,
    Filesystem.INVALID: FilesystemProto.INVALID_FS }

class TempVolumeClient(TempVolumeInterface):
    create_temp_volume = (lambda self = None, file_system = None, size = boundary_api: pass# WARNING: Decompyle incomplete
)()
    drop_temp_volume = (lambda self = None, mount_path = None: 
def convert_reply(reply = None):
if reply.HasField('error'):
raise NucleusClientError(f'''drop_temp_volume exception: {reply.error!r}''')req = DropTempVolumeReq(mount_path = LocalPathProto(absolute_path = mount_path.to_unicode()))# WARNING: Decompyle incomplete
)()

