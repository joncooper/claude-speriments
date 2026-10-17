# Source Generated with Decompyle++
# File: local_props.pyc (Python 3.11)

from enum import IntEnum
from typing import NamedTuple, Optional, Text, Union
from proto.database import icons_pb2
from proto.local_filesystem.device_anchor_pb2 import DeviceAnchorDetails as DeviceAnchorDetailsProto, DeviceAnchorInactiveReason as DeviceAnchorInactiveReasonProto, DeviceAnchorStatus as DeviceAnchorStatusProto
from shared.local_path import LocalPath
from shared.server_path import MRCasedServerPath, RRCasedServerPath
from sync_engine.file_system.abstract_file_system import AbstractFileSystem
from sync_engine.nucleus.thin_client.exceptions import NucleusClientError
from shortest_fileid_path import ShortestFileIdPath
from dropbox.exception.reporting import report_bad_assumption
from dropbox.model.types import FileId, NsId
from dropbox.proto.nucleus.common_api_types_pb2 import LocalLocationProperties as LocalLocationPropertiesProto
from dropbox.sync_engine_boundary.exceptions import NucleusProtoException
from dropbox.sync_engine_boundary.types.remote_props import FolderPolicyStatus
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.sync_engine_boundary.types.location_props import LocationProperties

class DefaultIcon:
    pass


class DBXIconType(IntEnum):
    INVALID = 0
    DROPBOX = 1
    CAMERA_UPLOADS = 2
    SHARED = 3
    SHARED_READ_ONLY = 4
    SHARED_VIEW_NAME_ONLY = 5
    TEAM_FOLDER = 6
    TEAM_FOLDER_READ_ONLY = 7
    TEAM_MEMBER_FOLDER = 8
    SANDBOX = 9
    DEVICE_FOLDER_MAC = 10
    DEVICE_FOLDER_WIN = 11
    DEVICE_FOLDER_GENERIC = 12
    DEVICE_FOLDER_DESKTOP = 13
    DEVICE_FOLDER_DOCUMENTS = 14
    DEVICE_FOLDER_DOWNLOADS = 15
    DEVICE_FOLDER_PICTURES = 16
    DEVICE_FOLDER_MUSIC = 19
    DEVICE_FOLDER_VIDEOS = 20
    VAULT = 17
    FAMILY_SHARED_FOLDER = 18
    ENCRYPTED_TEAM_FOLDER = 21


class LocalDirectoryProperties(NamedTuple):
    icon: 'Union[DefaultIcon, DBXIconType]' = 'LocalDirectoryProperties'
    default = (lambda : LocalDirectoryProperties(icon = DefaultIcon))()


class LocalFileProperties(NamedTuple):
    is_cloud_content: 'bool' = 'LocalFileProperties'
    default = (lambda is_cloud_content = None: LocalFileProperties(is_cloud_content))()

# WARNING: Decompyle incomplete
