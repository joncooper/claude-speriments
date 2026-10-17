# Source Generated with Decompyle++
# File: device_anchor.pyc (Python 3.11)

import os
from typing import Callable, Dict, List, Optional, Text, Tuple, Type
from google.protobuf.service import RpcController
from thin_client.exceptions import NucleusClientError
from base import NucleusModernClientBase
from nucleus_decorators import boundary_api
from dropbox.client.features.external_drive_backup.constants import ExternalDriveBackupUIStrings
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.metrics.function_usage import logged_method
from dropbox.model.types import FileId
from dropbox.platform import IS_WINDOWS
from dropbox.proto.nucleus.app_service_pb2 import GetCurrentComputerBackupSyncProgressReply, GetCurrentComputerBackupSyncProgressReq, GetCurrentDeviceAnchorSyncProgressReply, GetCurrentDeviceAnchorSyncProgressReq, SubscribeForBackupSyncProgressReply, SubscribeForBackupSyncProgressReq
from dropbox.proto.nucleus.dbxignore_pb2 import DBXIgnoreContents, DBXIgnoreLine, DBXIgnoreVersion
from dropbox.proto.nucleus.device_anchor_pb2 import BreakBackupByFileIdReply, BreakBackupByFileIdReq, BreakBackupByTargetPathReply, BreakBackupByTargetPathReq, BreakBackupReason as BreakBackupReasonProto, CreateDeviceAnchorReply, CreateDeviceAnchorReq, DeleteDeviceAnchorReply, DeleteDeviceAnchorReq, DeviceAnchorError as DeviceAnchorErrorProto, DeviceAnchorState as DeviceAnchorStateProto, DeviceAnchorTargetType as DeviceAnchorTargetTypeProto, GetDbxIgnoreContentsReply, GetDbxIgnoreContentsReq, GetDeviceAnchorMetadataByPathReply, GetDeviceAnchorMetadataByPathReq, ListDeviceAnchorsReply, ListDeviceAnchorsReq, PauseDeviceAnchorReply, PauseDeviceAnchorReq, ResolveDeviceAnchorReply, ResolveDeviceAnchorReq, ResumeDeviceAnchorReply, ResumeDeviceAnchorReq, SetDbxIgnoreContentsReply, SetDbxIgnoreContentsReq, ValidateAnchorTargetReply, ValidateAnchorTargetReq
from dropbox.proto.nucleus.published_event_pb2 import DeviceAnchorUnbindEvent as DeviceAnchorUnbindEventProto
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto, LocalPath as LocalPathProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.device_anchor_interface import AlreadyExistsDeviceAnchorError, DBXIgnoreError, DeviceAnchorError, InvalidDeviceAnchorError, IOError, NoSpace, NotADeviceAnchorError, NotFoundDeviceAnchorError, OtherDeviceAnchorError, PathInvalidDeviceAnchorError, SyncEngineDeviceAnchorInterface, TargetAlreadyBoundDeviceAnchorError, TargetDoesNotExist, TargetIsDescendantOfDropbox, TargetIsNotWritable, TargetNotADirectoryDeviceAnchorError
from dropbox.sync_engine_boundary.sync_engine_file_props_client_interface import SyncEngineFilePropsClientInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DbxIgnoreContents, DeviceAnchorInfo, DeviceAnchorState, DeviceAnchorTargetMetadata, DeviceAnchorTargetType, DeviceAnchorUnbindInfo, DeviceAnchorUnbindReason, DeviceIdVerificationAttrs, ErredDeviceAnchorInfo, GetDeviceAnchorMetadataByPathResult, HangDetails, ListDeviceAnchorsResult, OneWaySyncRemediationInfo
from dropbox.sync_engine_boundary.types.backup_sync_progress import SyncProgressForComputerBackup, SyncProgressForComputerBackupSummary, SyncProgressForDeviceAnchor, SyncProgressForDeviceAnchorSummary
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.trace import TRACE
MYPY = False
_DEVICE_ANCHOR_ERROR_MAP: 'Dict[int, Type[DeviceAnchorError]]' = {
    DeviceAnchorErrorProto.DBXIGNORE_ERROR: DBXIgnoreError,
    DeviceAnchorErrorProto.NO_SPACE: NoSpace,
    DeviceAnchorErrorProto.IO_ERROR: IOError,
    DeviceAnchorErrorProto.OTHER_DEVICE_ANCHOR_ERROR: OtherDeviceAnchorError,
    DeviceAnchorErrorProto.INVALID_DEVICE_ANCHOR: InvalidDeviceAnchorError,
    DeviceAnchorErrorProto.TARGET_IS_NOT_WRITABLE: TargetIsNotWritable,
    DeviceAnchorErrorProto.TARGET_DOES_NOT_EXIST: TargetDoesNotExist,
    DeviceAnchorErrorProto.TARGET_IS_DESCENDANT_OF_DROPBOX: TargetIsDescendantOfDropbox,
    DeviceAnchorErrorProto.DEVICE_ANCHOR_NOT_FOUND: NotFoundDeviceAnchorError,
    DeviceAnchorErrorProto.NOT_A_DEVICE_ANCHOR: NotADeviceAnchorError,
    DeviceAnchorErrorProto.TARGET_ALREADY_BOUND: TargetAlreadyBoundDeviceAnchorError,
    DeviceAnchorErrorProto.TARGET_NOT_A_DIRECTORY: TargetNotADirectoryDeviceAnchorError,
    DeviceAnchorErrorProto.DEVICE_ANCHOR_PATH_INVALID: PathInvalidDeviceAnchorError,
    DeviceAnchorErrorProto.DEVICE_ANCHOR_ALREADY_EXISTS: AlreadyExistsDeviceAnchorError,
    DeviceAnchorErrorProto.UNKNOWN_DEVICE_ANCHOR_ERROR: DeviceAnchorError }
# WARNING: Decompyle incomplete
