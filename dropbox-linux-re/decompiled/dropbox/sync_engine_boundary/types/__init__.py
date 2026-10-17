# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import
import time
from collections import namedtuple
from enum import Enum, IntEnum
from typing import Any, Callable, Dict, List, NamedTuple, NewType, Optional, Text, Union
from uuid import UUID
from dropbox.client_api.hashing import digest_to_base64
from dropbox.model.types import FileId, NsId
from dropbox.proto.namespace.namespace_entity_pb2 import NamespaceTypeValues
from dropbox.proto.nucleus.app_service_pb2 import ContainerActionResult, DiskUsageReply, GetFilesystemInfoReply, RegexExpectedErrorPair as RegexExpectedErrorPairProto, SetPathIgnoredStateReply
from dropbox.proto.nucleus.device_anchor_pb2 import DeviceAnchorInfo as DeviceAnchorInfoProto, DeviceAnchorState as DeviceAnchorStateProto, DeviceAnchorTargetType as DeviceAnchorTargetTypeProto, TargetMetadata as TargetMetadataProto
from dropbox.proto.nucleus.published_event_pb2 import ConflictResolutionAttemptEvent as ConflictResolutionAttemptEventProto, MountChanged as MountChangedProto
from dropbox.proto.nucleus.reactive_api_pb2 import SyncedFile as SyncedFileProto, SyncedSummary as SyncedSummaryProto, SyncedUserSummary as SyncedUserSummaryProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.trace import TRACE
DirectoryEntry = NamedTuple('DirectoryEntry', [
    ('filename', Text),
    ('is_dir', bool),
    ('mtime', int),
    ('size', int),
    ('fileid', FileId)])

class FileType(Enum):
    FILE = 0
    DIRECTORY = 1
    PLACEHOLDER = 2
    SYMLINK = 3


class TypedDirectoryEntry(NamedTuple):
    file_type: 'FileType' = 'TypedDirectoryEntry'
    is_directory = (lambda self = None: self.file_type == FileType.DIRECTORY)()


class FilesystemInfo(NamedTuple):
    name: 'Text' = 'FilesystemInfo'
    from_proto = (lambda cls = None, proto = None: is_supported = proto.supported == GetFilesystemInfoReply.Supportedfs_name = proto.nameFilesystemInfo(supported = is_supported, name = fs_name))()


def SyncOperation():
    '''SyncOperation'''
    make_new = (lambda cls, local_path, ns_id, event_type, direction, timestamp, blocklist, is_dir, is_cloud_content, user_id, host_int = None, is_placeholder = None, fileid = classmethod, task_duration_millis = ('local_path', 'Text', 'ns_id', 'NsId', 'event_type', 'SyncEventType', 'direction', 'SyncDirection', 'timestamp', 'Union[int, float]', 'blocklist', 'bytes', 'is_dir', 'bool', 'is_cloud_content', 'bool', 'user_id', 'Optional[int]', 'host_int', 'Optional[int]', 'is_placeholder', 'bool', 'fileid', 'FileId', 'task_duration_millis', 'Optional[int]', 'return', "'SyncOperation'"): SyncOperation(local_path, ns_id, event_type, direction, timestamp, blocklist, is_dir, is_cloud_content, user_id, host_int, is_placeholder, fileid, task_duration_millis))()
    from_sync_file = (lambda cls = None, synced_file = None: operation = synced_file.operation.WhichOneof('operation')if operation == 'commit_add':
event_type = SyncEventType.ADDdirection = SyncDirection.UPelif operation == 'commit_edit':
event_type = SyncEventType.EDITdirection = SyncDirection.UPelif operation == 'commit_delete':
event_type = SyncEventType.DELETEdirection = SyncDirection.UPelif operation == 'commit_move':
event_type = SyncEventType.MOVEdirection = SyncDirection.UPelif operation == 'reconstruct_add':
event_type = SyncEventType.ADDdirection = SyncDirection.DOWNelif operation == 'reconstruct_edit':
event_type = SyncEventType.EDITdirection = SyncDirection.DOWNelif operation == 'reconstruct_recall':
event_type = SyncEventType.RECALLdirection = SyncDirection.DOWNelif operation == 'reconstruct_delete':
event_type = SyncEventType.DELETEdirection = SyncDirection.DOWNelif operation == 'reconstruct_move':
event_type = SyncEventType.MOVEdirection = SyncDirection.DOWNelif operation == 'hide':
event_type = SyncEventType.SYNC_POLICY_CHANGEdirection = SyncDirection.UP# WARNING: Decompyle incomplete
)()

SyncOperation = <NODE:27>(SyncOperation, 'SyncOperation', NamedTuple('SyncOperation', [
    ('local_path', Text),
    ('ns_id', NsId),
    ('event_type', SyncEventType),
    ('direction', SyncDirection),
    ('timestamp', Union[(int, float)]),
    ('blocklist', bytes),
    ('is_dir', bool),
    ('is_cloud_content', bool),
    ('user_id', Optional[int]),
    ('host_int', Optional[int]),
    ('is_placeholder', bool),
    ('fileid', FileId),
    ('task_duration_millis', Optional[int])]))

class DropboxFolderDiskInfo(NamedTuple):
    dropbox_folder_size: 'Optional[int]' = 'DropboxFolderDiskInfo'
    from_proto = (lambda cls = None, proto = None: if proto:
DropboxFolderDiskInfo(free_space = proto.free_bytes, total_space = proto.total_bytes, dropbox_folder_size = proto.dropbox_used_bytes))()


def SyncOperationUserSummary():
    '''SyncOperationUserSummary'''
    from_proto = (lambda cls = None, proto = None: if not proto:
NoneSyncOperationUserSummary(user_id = proto.user_id, num_files = proto.num_files, num_files_added = proto.num_files_added, num_files_deleted = proto.num_files_deleted, num_files_edited = proto.num_files_edited))()

SyncOperationUserSummary = <NODE:27>(SyncOperationUserSummary, 'SyncOperationUserSummary', NamedTuple('SyncOperationUserSummary', [
    ('user_id', int),
    ('num_files', int),
    ('num_files_added', int),
    ('num_files_deleted', int),
    ('num_files_edited', int)]))

def SyncOperationSummary():
    '''SyncOperationSummary'''
    from_proto = (lambda cls = None, proto = None: if not proto:
Nonerecent_files = None# WARNING: Decompyle incomplete
)()

SyncOperationSummary = <NODE:27>(SyncOperationSummary, 'SyncOperationSummary', NamedTuple('SyncOperationSummary', [
    ('user_summary_list', List[SyncOperationUserSummary]),
    ('recent_files', List[SyncOperation])]))

class LocalRevisionState(Enum):
    UNKNOWN = 0
    SYNCED = 1
    LOCAL_ADD_PENDING = 2
    LOCAL_EDIT_PENDING = 3
    LOCAL_DELETE_PENDING = 4


def Revision():
    '''Revision'''
    pass

Revision = <NODE:27>(Revision, 'Revision', NamedTuple('Revision', [
    ('user_id', Optional[int]),
    ('ns_id', Optional[int]),
    ('timestamp', Optional[int]),
    ('local_revision_state', LocalRevisionState),
    ('fileid', Optional[bytes])]))

def MoveToDeletedCache():
    '''MoveToDeletedCache'''
    pass

MoveToDeletedCache = <NODE:27>(MoveToDeletedCache, 'MoveToDeletedCache', namedtuple('MoveToDeletedCache', [
    'local_path',
    'deleted_cache_path']))

class MountChangeOperation(NamedTuple):
    is_family_shared_folder: 'bool' = 'MountChangeOperation'
    from_proto = (lambda cls = None, proto = None, make_path = classmethod: MountChangeOperation(fileid = FileId(proto.fileid), local_path = make_path(proto.local_path.valid_platform_path.absolute_path), ns_id = NsId(proto.ns_id), is_mount = proto.is_add, is_online_only = proto.is_online_only, is_sandbox = proto.properties.ns_type == NamespaceTypeValues.APP_SANDBOX, is_family_shared_folder = proto.properties.ns_type == NamespaceTypeValues.FAMILY_SHARED_FOLDER))()


class ConflictResolutionType(IntEnum):
    EDIT = 1
    PERMISSION = 2
    PATH_INACCESSIBLE = 3
    MOVE_REVERTED = 4
    LOCKED_FILE = 5


class ConflictResolutionAttempt(NamedTuple):
    conflict_type: 'ConflictResolutionType' = 'ConflictResolutionAttempt'
    from_proto = (lambda cls = None, proto = None, make_path = classmethod: resolution_type_dict = {
ConflictResolutionAttemptEventProto.OTHER: ConflictResolutionType.EDIT,
ConflictResolutionAttemptEventProto.LOCKED_FILE: ConflictResolutionType.LOCKED_FILE,
ConflictResolutionAttemptEventProto.SERVER_REJECTED_MOVE: ConflictResolutionType.MOVE_REVERTED,
ConflictResolutionAttemptEventProto.CONTENT: ConflictResolutionType.EDIT,
ConflictResolutionAttemptEventProto.PERMISSIONS: ConflictResolutionType.PERMISSION }# WARNING: Decompyle incomplete
)()


class BlockTransferType(object):
    UPLOAD = 0
    DOWNLOAD = 1


def BlockTransfer():
    '''BlockTransfer'''
    pass

BlockTransfer = <NODE:27>(BlockTransfer, 'BlockTransfer', namedtuple('BlockTransfer', [
    'local_path',
    'num_blocks_completed',
    'num_blocks_remaining']))

def BlockTransferList():
    '''BlockTransferList'''
    pass

BlockTransferList = <NODE:27>(BlockTransferList, 'BlockTransferList', namedtuple('BlockTransferList', [
    'transfer_type',
    'transfers']))
AdditionalAttributes = NamedTuple('AdditionalAttributes', [
    ('exif_manufacturer', Optional[Text]),
    ('exif_model', Optional[Text]),
    ('exif_datetime', Optional[Text]),
    ('file_datetime', Optional[Text]),
    ('file_hashfull', Optional[Text]),
    ('file_nameorig', Optional[Text]),
    ('client_import_time', Optional[Text]),
    ('client_timeoffset', Optional[Text]),
    ('client_platform', Optional[Text]),
    ('client_buildstring', Optional[Text]),
    ('client_userid', Optional[Text]),
    ('device_manufacturer', Optional[Text]),
    ('device_model', Optional[Text]),
    ('device_name', Optional[Text]),
    ('device_uid', Optional[Text]),
    ('device_serialnum', Optional[Text])])

class MergeFailureType(IntEnum):
    INVALID_DBX_FILENAME = 0
    PERMISSION_DENIED = 1
    SHARING_VIOLATION = 2
    OTHER = 3
    DISALLOWED_EXTENSION = 4
    CONFLICTED = 5


def RegexExpectedErrorPair():
    '''RegexExpectedErrorPair'''
    
    def into_proto(self = None):
        proto = RegexExpectedErrorPairProto()
        proto.regex = self.regex
        proto.error_code = self.error_code
        return proto

    from_proto = (lambda cls = None, proto = None: RegexExpectedErrorPair(proto.regex, proto.error_code))()

RegexExpectedErrorPair = <NODE:27>(RegexExpectedErrorPair, 'RegexExpectedErrorPair', NamedTuple('RegexExpectedErrorPair', [
    ('regex', Text),
    ('error_code', int)]))
MergeFailedExtra = NamedTuple('MergeFailedExtra', [
    ('disallowed_extension_code', Optional[int])])
MergeFailedFilenameTuple = NamedTuple('MergeFailedFilenameTuple', [
    ('filename', Text),
    ('error', MergeFailureType),
    ('extra', Optional[MergeFailedExtra])])

def MergeIntoDropboxStatus():
    '''MergeIntoDropboxStatus'''
    make_new = (lambda cls = None, failed_files_tuple = None: MergeIntoDropboxStatus(failed_files_tuple))()

MergeIntoDropboxStatus = <NODE:27>(MergeIntoDropboxStatus, 'MergeIntoDropboxStatus', NamedTuple('MergeIntoDropboxStatus', [
    ('failed_files', List[MergeFailedFilenameTuple])]))

class UnmergeFromDropboxStatus(NamedTuple):
    failed_files: 'Optional[List[MergeFailedFilenameTuple]]' = 'UnmergeFromDropboxStatus'


def DeleteSuppressRestoredFromAdd():
    '''DeleteSuppressRestoredFromAdd'''
    pass

DeleteSuppressRestoredFromAdd = <NODE:27>(DeleteSuppressRestoredFromAdd, 'DeleteSuppressRestoredFromAdd', NamedTuple('DeleteSuppressRestoredFromAdd', [
    ('path', LocalPath)]))

def DeleteSuppressRestoredFromMove():
    '''DeleteSuppressRestoredFromMove'''
    pass

DeleteSuppressRestoredFromMove = <NODE:27>(DeleteSuppressRestoredFromMove, 'DeleteSuppressRestoredFromMove', NamedTuple('DeleteSuppressRestoredFromMove', [
    ('src_path', LocalPath),
    ('dst_path', LocalPath)]))

def DeleteSuppressNodeUnsynced():
    '''DeleteSuppressNodeUnsynced'''
    pass

DeleteSuppressNodeUnsynced = <NODE:27>(DeleteSuppressNodeUnsynced, 'DeleteSuppressNodeUnsynced', NamedTuple('DeleteSuppressNodeUnsynced', [
    ('path', LocalPath)]))

def DeleteSuppressRestoredInfo():
    '''DeleteSuppressRestoredInfo'''
    
    def get_add(self = None):
        return self.action if isinstance(self.action, DeleteSuppressRestoredFromAdd) else None

    
    def get_move(self = None):
        return self.action if isinstance(self.action, DeleteSuppressRestoredFromMove) else None

    
    def get_unsync(self = None):
        return self.action if isinstance(self.action, DeleteSuppressNodeUnsynced) else None

    new_add = (lambda cls = None, fileid = None, path = classmethod: DeleteSuppressRestoredInfo(fileid, DeleteSuppressRestoredFromAdd(path)))()
    new_move = (lambda cls = None, fileid = None, src_path = classmethod, dst_path = ('fileid', 'FileId', 'src_path', 'LocalPath', 'dst_path', 'LocalPath'): DeleteSuppressRestoredInfo(fileid, DeleteSuppressRestoredFromMove(src_path, dst_path)))()
    new_unsync = (lambda cls = None, fileid = None, path = classmethod: DeleteSuppressRestoredInfo(fileid, DeleteSuppressNodeUnsynced(path)))()

DeleteSuppressRestoredInfo = <NODE:27>(DeleteSuppressRestoredInfo, 'DeleteSuppressRestoredInfo', NamedTuple('DeleteSuppressRestoredInfo', [
    ('fileid', FileId),
    ('action', Union[(DeleteSuppressRestoredFromAdd, DeleteSuppressRestoredFromMove, DeleteSuppressNodeUnsynced)])]))
CallbackRemovalToken = NewType('CallbackRemovalToken', UUID)

class SyncIconValidationException(Exception):
    pass


class LinkContainerError(Exception):
    pass
# WARNING: Decompyle incomplete


class FileTypeFilter:
    
    def __init__(self, include_files = None, include_directories = None, include_placeholders = None, include_symlinks = ('include_files', 'bool', 'include_directories', 'bool', 'include_placeholders', 'bool', 'include_symlinks', 'bool', 'return', 'None')):
        self.include_files = include_files
        self.include_directories = include_directories
        self.include_placeholders = include_placeholders
        self.include_symlinks = include_symlinks

    all = (lambda cls = None: FileTypeFilter(True, True, True, True))()


class HangReason(Enum):
    RESOLVER = 1
    REINDEXER = 2
    FRONTIER = 3
    UNKNOWN = 4
    from_proto = (lambda cls = None, hang_details = None: if hang_details.resolver:
HangReason.RESOLVERif None.reindexer:
HangReason.REINDEXERif None.remote_frontier or hang_details.local_frontier:
HangReason.FRONTIERNone.UNKNOWN)()


class HangDetails(NamedTuple):
    hang_reason: 'HangReason' = 'HangDetails'
    from_proto = (lambda cls = None, device_anchor_info = None: if device_anchor_info.HasField('device_anchor_hang'):
HangDetails(is_device_anchor_specific_hang = True, hang_reason = HangReason.from_proto(device_anchor_info.device_anchor_hang))if None.HasField('hang'):
HangDetails(is_device_anchor_specific_hang = False, hang_reason = HangReason.from_proto(device_anchor_info.hang)))()


class SetPathIgnoredStateErrorReason(Enum):
    IS_PLACEHOLDER = 1
    IS_CLOUD_DOC = 2
    HAS_PLACEHOLDERS = 3
    HAS_CLOUD_DOCS = 4
    HAS_PLACEHOLDERS_AND_CLOUD_DOCS = 5
    from_proto = (lambda cls = None, proto = None: if not proto.HasField('error'):
Nonemapping = {
SetPathIgnoredStateReply.Error.Reason.HAS_PLACEHOLDERS_AND_CLOUD_DOCS: SetPathIgnoredStateErrorReason.HAS_PLACEHOLDERS_AND_CLOUD_DOCS,
SetPathIgnoredStateReply.Error.Reason.HAS_CLOUD_DOCS: SetPathIgnoredStateErrorReason.HAS_CLOUD_DOCS,
SetPathIgnoredStateReply.Error.Reason.HAS_PLACEHOLDERS: SetPathIgnoredStateErrorReason.HAS_PLACEHOLDERS,
SetPathIgnoredStateReply.Error.Reason.IS_CLOUD_DOC: SetPathIgnoredStateErrorReason.IS_CLOUD_DOC,
None.Error.Reason.IS_PLACEHOLDER: SetPathIgnoredStateErrorReason.IS_PLACEHOLDER }mapping[proto.error.reason])()


class DeviceAnchorState(Enum):
    INVALID = 0
    ACTIVE = 1
    BACKUP_PAUSED = 2
    BROKEN = 3
    UNPLUGGED = 4
    PERMANENTLY_FAILED = 5
    from_proto = (lambda proto = None: mapping = {
DeviceAnchorStateProto.PERMANENTLY_FAILED: DeviceAnchorState.PERMANENTLY_FAILED,
DeviceAnchorStateProto.UNPLUGGED: DeviceAnchorState.UNPLUGGED,
DeviceAnchorStateProto.BROKEN: DeviceAnchorState.BROKEN,
DeviceAnchorStateProto.BACKUP_PAUSED: DeviceAnchorState.BACKUP_PAUSED,
DeviceAnchorStateProto.ACTIVE: DeviceAnchorState.ACTIVE,
DeviceAnchorStateProto.INVALID_DEVICE_ANCHOR_STATE: DeviceAnchorState.INVALID }mapping[proto])()


class DeviceAnchorTargetType(IntEnum):
    UNSPECIFIED = 0
    EXTERNAL_DRIVE = 1
    COMPUTER_BACKUP_FOLDER = 2
    from_proto = (lambda proto = None: if proto == DeviceAnchorTargetTypeProto.EXTERNAL_DRIVE:
DeviceAnchorTargetType.EXTERNAL_DRIVEif None == DeviceAnchorTargetTypeProto.COMPUTER_BACKUP_FOLDER:
DeviceAnchorTargetType.COMPUTER_BACKUP_FOLDERNone.UNSPECIFIED)()
    from_metadata_proto = (lambda proto = None: if proto.HasField('backup_folder_path'):
DeviceAnchorTargetType.COMPUTER_BACKUP_FOLDERif None.HasField('target_path') or proto.HasField('device_uuid'):
DeviceAnchorTargetType.EXTERNAL_DRIVENone.UNSPECIFIED)()


class DeviceIdVerificationAttrs(NamedTuple):
    capacity: 'Optional[int]' = 'DeviceIdVerificationAttrs'
    from_proto = (lambda cls = None, proto = None: if proto.device_verification_attrs and proto.device_verification_attrs.device_capacity:
capacity = proto.device_verification_attrs.device_capacity.capacityDeviceIdVerificationAttrs(capacity))()


class DeviceAnchorInfo(NamedTuple):
    target_type: 'DeviceAnchorTargetType' = 'DeviceAnchorInfo'


class DeviceAnchorUnbindReason(IntEnum):
    RECONSTRUCT_ADD = 0
    RECONSTRUCT_DELETE = 1
    RECONSTRUCT_MOVE_OUT = 2
    RECONSTRUCT_MOVE_IN = 3
    RECONSTRUCT_EDIT = 4
    RECONSTRUCT_HIDE = 5
    RECONSTRUCT_RECALL = 6
    REMAKE_PLACEHOLDER = 7
    LOCAL_ADD_BAD_DEVICE_ANCHOR = 8
    LOCAL_EDIT_BAD_DEVICE_ANCHOR = 9
    REQUESTED_BY_APP = 10
    REMOTE_CHANGE = 11
    IGNORED = 12
    FILE_PROVIDER_MIGRATION = 13
    SEAMLESS_FISSION_MIGRATION = 14
    CBOA_ABANDONED_ANCHORS = 15
    CBOA_ONE_WAY_SYNC_CONFLICTED_ANCHOR = 16


class DeviceAnchorUnbindInfo(NamedTuple):
    target_type: 'DeviceAnchorTargetType' = 'DeviceAnchorUnbindInfo'


class Filesystem(IntEnum):
    INVALID = 1
    OsDefault = 2
    FAT32 = 3
    ExFAT = 4
    UDF = 5


class TempVolumeInfo(NamedTuple):
    mount_path: 'Optional[LocalPath]' = 'TempVolumeInfo'


class ErredDeviceAnchorInfo(NamedTuple):
    error: 'Text' = 'ErredDeviceAnchorInfo'


class ListDeviceAnchorsResult(NamedTuple):
    erred_device_anchors: 'List[ErredDeviceAnchorInfo]' = 'ListDeviceAnchorsResult'


class OneWaySyncRemediationInfo(NamedTuple):
    device_anchor_fileid: 'FileId' = 'OneWaySyncRemediationInfo'


class DbxIgnoreContents(NamedTuple):
    dbxignore_lines: 'List[Text]' = 'DbxIgnoreContents'


class DeviceAnchorTargetMetadata(NamedTuple):
    backup_folder_path: 'Optional[LocalPath]' = 'DeviceAnchorTargetMetadata'


class GetDeviceAnchorMetadataByPathResult(NamedTuple):
    was_anchor_in_canopy: 'bool' = 'GetDeviceAnchorMetadataByPathResult'
    
    def is_edb(self = None):
        return bool(self.metadata.device_uuid) if self.metadata else False


