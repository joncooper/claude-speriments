# Source Generated with Decompyle++
# File: remote_props.pyc (Python 3.11)

from enum import Enum
from typing import NamedTuple, Optional, Text, Union
from sync_engine.file_system.abstract_file_system import AbstractFileSystem
from exceptions import NucleusProtoException
from dropbox.model.types import NsId
from dropbox.proto.nucleus.common_api_types_pb2 import DirPNMBehaviors, MountProperties as MountPropertiesProto, RemoteLocationProperties as RemoteLocationPropertiesProto
from dropbox.proto.per_node_metadata.link_node_pb2 import LinkNodeAction
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath
RemoteDirectoryPropertiesProto = RemoteLocationPropertiesProto.RemoteDirectoryProperties
RemoteFilePropertiesProto = RemoteLocationPropertiesProto.RemoteFileProperties
DirPnmBehaviorsProto = DirPNMBehaviors
FilePnmBehaviorsProto = RemoteLocationPropertiesProto.RemoteFileProperties.FilePNMBehaviors
DeviceInfoProto = DirPNMBehaviors.DeviceInfo
ThirdPartyFissionMountPointProto = DirPNMBehaviors.ThirdPartyFissionMountPoint

class DeviceInfo(NamedTuple):
    user_id: 'Optional[int]' = 'DeviceInfo'
    from_proto = (lambda proto = None: DeviceInfo(device_id = proto.device_id, user_id = None if proto.user_id == -1 else proto.user_id))()


class ThirdPartyFissionMountPoint(NamedTuple):
    from_proto = (lambda proto = None: ThirdPartyFissionMountPoint())()


class DirPnmBehaviors(NamedTuple):
    third_party_fission_mount_point: 'Optional[ThirdPartyFissionMountPoint]' = 'DirPnmBehaviors'
    default = (lambda : DirPnmBehaviors(False, False, False, False, False, False, None, None, None))()
    from_proto = (lambda proto = None: DirPnmBehaviors(proto.suppress_delete, proto.suppress_move, proto.suppress_selsync, proto.suppress_ns_partition, proto.suppress_shared_link, proto.hide_extension, proto.link_node.action if proto.HasField('link_node') else None, DeviceInfo.from_proto(proto.device_info) if proto.HasField('device_info') else None, ThirdPartyFissionMountPoint.from_proto(proto.third_party_fission_mount_point) if proto.HasField('third_party_fission_mount_point') else None))()


class FilePnmBehaviors(NamedTuple):
    link_node_action: 'Optional[LinkNodeAction.V]' = 'FilePnmBehaviors'
    default = (lambda : FilePnmBehaviors(False, False, False, None))()
    from_proto = (lambda proto = None: FilePnmBehaviors(proto.suppress_delete, proto.suppress_move, proto.suppress_shared_link, proto.link_node.action if proto.HasField('link_node') else None))()


class DirectoryProperties(NamedTuple):
    pnm_behaviors: 'DirPnmBehaviors' = 'DirectoryProperties'
    default = (lambda : DirectoryProperties(DirPnmBehaviors.default()))()
    from_proto = (lambda proto = None: DirectoryProperties(pnm_behaviors = DirPnmBehaviors.from_proto(proto.pnm_behaviors)))()


class MountProperties(NamedTuple):
    is_encrypted_folder: 'bool' = 'MountProperties'
    default = (lambda : MountProperties(is_dropbox_folder = False, is_tmf = False, target_ns_id = NsId(1234), is_sandbox = False, is_confidential = False, is_team_shared_folder = False, is_encrypted_folder = False, is_no_access = False, can_mount_shared_folders = False, pnm_behaviors = DirPnmBehaviors.default()))()
    from_proto = (lambda proto = None: MountProperties(is_dropbox_folder = proto.is_dropbox_folder, is_tmf = proto.is_tmf, target_ns_id = NsId(proto.target_ns_id), is_sandbox = proto.is_sandbox, is_confidential = proto.is_confidential, is_team_shared_folder = proto.is_team_shared_folder, is_no_access = proto.is_no_access, can_mount_shared_folders = proto.can_mount_shared_folders, pnm_behaviors = DirPnmBehaviors.from_proto(proto.pnm_behaviors), is_encrypted_folder = proto.is_encryped_folder))()


class FileLikeProperties(NamedTuple):
    pnm_behaviors: 'FilePnmBehaviors' = 'FileLikeProperties'
    default = (lambda : FileLikeProperties(pnm_behaviors = FilePnmBehaviors.default()))()
    from_proto = (lambda proto = None: FileLikeProperties(pnm_behaviors = FilePnmBehaviors.from_proto(proto.pnm_behaviors)))()


class FolderPolicyStatus(Enum):
    UnknownFolderPolicyStatus = 0
    Local = 1
    OnlineOnly = 2
    Mixed = 3
    Hidden = 4
    ImplicitLocal = 5
    from_proto = (lambda policy_status = None: mapping = {
RemoteLocationPropertiesProto.FolderPolicyStatus.ImplicitLocal: FolderPolicyStatus.ImplicitLocal,
RemoteLocationPropertiesProto.FolderPolicyStatus.Hidden: FolderPolicyStatus.Hidden,
RemoteLocationPropertiesProto.FolderPolicyStatus.Mixed: FolderPolicyStatus.Mixed,
RemoteLocationPropertiesProto.FolderPolicyStatus.OnlineOnly: FolderPolicyStatus.OnlineOnly,
RemoteLocationPropertiesProto.FolderPolicyStatus.Local: FolderPolicyStatus.Local,
RemoteLocationPropertiesProto.FolderPolicyStatus.UnknownFolderPolicyStatus: FolderPolicyStatus.UnknownFolderPolicyStatus }mapping[policy_status])()


class RemoteLocationProperties(NamedTuple):
    aggregated_remote_size_bytes: 'int' = 'RemoteLocationProperties'
    is_in_ignore_set = (lambda self = None: self.policy_status == FolderPolicyStatus.Hidden)()
    is_view_name_only = (lambda self = None: 