# Source Generated with Decompyle++
# File: device_folder_interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Callable, List, Optional
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.proto.nucleus.app_service_pb2 import DirtyPathsReq, SuppressFSWsReq
from dropbox.proto.nucleus.reactive_api_pb2 import MergeProgress
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import OSFolderID, UserAccessType
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DeleteSuppressRestoredInfo, MergeIntoDropboxStatus, RegexExpectedErrorPair, UnmergeFromDropboxStatus

class SyncEngineDeviceFolderInterface(ABC):
    device_folders_using_app_fs = (lambda self = None: raise NotImplementedError())()
    allow_user_access = (lambda self = None, dst_path = None, access_type = abstractmethod: raise NotImplementedError())()
    bind_into_dropbox = (lambda self, os_folder_id = None, source_local_path = None, target_fileid = abstractmethod, target_path = ('os_folder_id', 'OSFolderID', 'source_local_path', 'LocalPath', 'target_fileid', 'FileId', 'target_path', 'LocalPath', 'return', 'Future[None]'): pass)()
    create_breadcrumbs = (lambda self = None, src_local_path = None, dst_local_path = abstractmethod: pass)()
    deny_user_access = (lambda self = None, dst_path = None, access_type = abstractmethod: raise NotImplementedError())()
    get_os_folder_path = (lambda self = None, os_folder_id = None: pass)()
    merge_into_dropbox = (lambda self, source_dir_local_path, destination_dir_fileid, destination_dir_path, create_dst_dir_if_necessary = None, should_deny_user_access = None, exclusion_list = abstractmethod, callback = ('source_dir_local_path', 'LocalPath', 'destination_dir_fileid', 'FileId', 'destination_dir_path', 'LocalPath', 'create_dst_dir_if_necessary', 'bool', 'should_deny_user_access', 'Optional[UserAccessType]', 'exclusion_list', 'List[RegexExpectedErrorPair]', 'callback', 'Optional[Callable[[MergeProgress], None]]', 'return', 'Future[MergeIntoDropboxStatus]'): pass)()
    on_engine_ready_for_redirection = (lambda self = None, callback = None: pass)()
    remove_breadcrumbs = (lambda self = None, src_local_path = None, dst_local_path = abstractmethod: pass)()
    remove_on_engine_ready_for_redirection = (lambda self = None, token = None: pass)()
    unbind_from_dropbox = (lambda self = None, os_folder_id = None, target_local_path = abstractmethod: pass)()
    unmerge_from_dropbox = (lambda self, source_dir_local_path, source_dir_fileid, source_parent_dir_fileid = None, destination_dir_path = None, exclusion_list = abstractmethod, allow_delete_device_dir = ('source_dir_local_path', 'LocalPath', 'source_dir_fileid', 'FileId', 'source_parent_dir_fileid', 'FileId', 'destination_dir_path', 'LocalPath', 'exclusion_list', 'List[RegexExpectedErrorPair]', 'allow_delete_device_dir', 'bool', 'return', 'Future[UnmergeFromDropboxStatus]'): pass)()
    dirty_paths = (lambda self = None, paths = None, reason = abstractmethod: raise NotImplementedError())()
    suppress_fsws = (lambda self = None, root_dir = None, reason = abstractmethod: raise NotImplementedError())()
    on_delete_suppressed_dir_restored = (lambda self = None, callback = None: raise NotImplementedError())()
    remove_delete_suppressed_dir_restored = (lambda self = None, callback = None: raise NotImplementedError())()


class DeviceFolderNucleusException(Exception):
    pass


class RedirectionError(DeviceFolderNucleusException):
    pass


class PermissionDeniedRedirectionError(RedirectionError):
    pass


class DirNotFoundRedirectionError(RedirectionError):
    pass


class FileIdRaceRedirectionError(RedirectionError):
    pass


class DirectoryNotEmptyRedirectionError(RedirectionError):
    pass


class OtherRedirectionError(RedirectionError):
    pass


class NucleusNotReadyRedirectionError(RedirectionError):
    pass


class NonFatalRedirectionError(RedirectionError):
    pass


class NotADirectoryRedirectionError(RedirectionError):
    pass

