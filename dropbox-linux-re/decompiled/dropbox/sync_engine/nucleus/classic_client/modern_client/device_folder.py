# Source Generated with Decompyle++
# File: device_folder.pyc (Python 3.11)

import os
from typing import Callable, Dict, List, Optional, Type, TypeVar
from google.protobuf.empty_pb2 import Empty as EmptyPb
from google.protobuf.service import RpcController
from thin_client.exceptions import NucleusClientError
from base import NucleusModernClientBase
from nucleus_decorators import boundary_api
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.sync_everything.constants import SYNC_EVERYTHING_FEATURE_OFF_VARIANTS
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.event_reporter import OperationEventSession
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.fs_api.stormcrows import EXT_FS_AP_DEVICE_FOLDER_GATE
from dropbox.metrics.function_usage import logged_method
from dropbox.model.types import FileId
from dropbox.platform import IS_WINDOWS
from dropbox.proto.nucleus.app_service_pb2 import AccessType as AccessTypeProto, AllowUserAccessReply, AllowUserAccessReq, BindIntoDropboxReply, BindIntoDropboxReq, CreateBreadcrumbsReply, CreateBreadcrumbsReq, DenyUserAccessReply, DenyUserAccessReq, DirtyPathsReply, DirtyPathsReq, GetOSFolderPathReply, GetOSFolderPathReq, MergeFailedFilenameErrPair as MergeFileErrorPair, MergeIntoDropboxReply, MergeIntoDropboxReq, OSFolderID as OSFolderIDProto, RedirectionError as RedirectionErrorProto, RemoveBreadcrumbsReply, RemoveBreadcrumbsReq, ShouldDenyUserAccess, SuppressFSWsReply, SuppressFSWsReq, UnbindFromDropboxReply, UnbindFromDropboxReq, UnmergeFromDropboxReply, UnmergeFromDropboxReq
from dropbox.proto.nucleus.reactive_api_pb2 import MergeProgress, ReactiveRequest
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto, LocalPath as LocalPathProto
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import OSFolderID, UserAccessType
from dropbox.sync_engine_boundary.device_folder_interface import DeviceFolderNucleusException, DirectoryNotEmptyRedirectionError, DirNotFoundRedirectionError, FileIdRaceRedirectionError, NonFatalRedirectionError, NotADirectoryRedirectionError, NucleusNotReadyRedirectionError, OtherRedirectionError, PermissionDeniedRedirectionError, RedirectionError, SyncEngineDeviceFolderInterface
from dropbox.sync_engine_boundary.exceptions import NetworkPathException, OSFolderNotFoundException, UnknownPathException
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DeleteSuppressRestoredInfo, MergeFailedExtra, MergeFailedFilenameTuple, MergeFailureType, MergeIntoDropboxStatus, RegexExpectedErrorPair, UnmergeFromDropboxStatus
from dropbox.trace import TRACE
_T = TypeVar('_T')
_REDIRECTION_ERROR_MAP: 'Dict[int, Type[RedirectionError]]' = {
    RedirectionErrorProto.NOT_A_DIRECTORY: NotADirectoryRedirectionError,
    RedirectionErrorProto.NON_FATAL: NonFatalRedirectionError,
    RedirectionErrorProto.NUCLEUS_NOT_READY: NucleusNotReadyRedirectionError,
    RedirectionErrorProto.OTHER: OtherRedirectionError,
    RedirectionErrorProto.DIRECTORY_NOT_EMPTY: DirectoryNotEmptyRedirectionError,
    RedirectionErrorProto.FILEID_RACE: FileIdRaceRedirectionError,
    RedirectionErrorProto.DIR_NOT_FOUND: DirNotFoundRedirectionError,
    RedirectionErrorProto.PERMISSION_DENIED: PermissionDeniedRedirectionError,
    RedirectionErrorProto.UNKNOWN_MERGE_ERROR: RedirectionError }
# WARNING: Decompyle incomplete
