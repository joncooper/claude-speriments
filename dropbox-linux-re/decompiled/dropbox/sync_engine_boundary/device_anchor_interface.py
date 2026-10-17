# Source Generated with Decompyle++
# File: device_anchor_interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Callable, List, Optional, Text, Tuple
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.proto.nucleus.dbxignore_pb2 import DBXIgnoreVersion
from dropbox.proto.nucleus.device_anchor_pb2 import BreakBackupReason
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DbxIgnoreContents, DeviceAnchorInfo, DeviceAnchorTargetType, DeviceAnchorUnbindInfo, GetDeviceAnchorMetadataByPathResult, ListDeviceAnchorsResult, OneWaySyncRemediationInfo
from dropbox.sync_engine_boundary.types.backup_sync_progress import SyncProgressForComputerBackup, SyncProgressForComputerBackupSummary, SyncProgressForDeviceAnchor, SyncProgressForDeviceAnchorSummary

class SyncEngineDeviceAnchorInterface(ABC):
    validate_device_anchor_target = (lambda self = None, target_path = None, device_uuid = abstractmethod: raise NotImplementedError())()
    create_device_anchor = (lambda self, device_anchor_path, device_capacity, cb_target_path, device_uuid, globs_to_ignore = None, existing_location_fileid = None, existing_location_parent_fileid = abstractmethod, allow_unsafe_skip_validation_checks = (False, False), start_paused = ('device_anchor_path', 'LocalPath', 'device_capacity', 'int', 'cb_target_path', 'Optional[LocalPath]', 'device_uuid', 'Optional[Text]', 'globs_to_ignore', 'Optional[List[Text]]', 'existing_location_fileid', 'Optional[FileId]', 'existing_location_parent_fileid', 'Optional[FileId]', 'allow_unsafe_skip_validation_checks', 'bool', 'start_paused', 'bool', 'return', 'Future[DeviceAnchorInfo]'): raise NotImplementedError())()
    resolve_device_anchor = (lambda self = None, device_anchor_fileid = None: raise NotImplementedError())()
    resume_device_anchor = (lambda self = None, device_anchor_fileid = None: raise NotImplementedError())()
    pause_device_anchor = (lambda self = None, device_anchor_fileid = None, updated_anchor_capacity = abstractmethod: raise NotImplementedError())()
    delete_device_anchor = (lambda self = None, device_anchor_fileid = None, target_type = abstractmethod: raise NotImplementedError())()
    list_device_anchors = (lambda self = None, target_type = None, valid_only = abstractmethod: raise NotImplementedError())()
    break_backup_by_target_path = (lambda self = None, target_path = None: raise NotImplementedError())()
    break_backup_by_fileid = (lambda self = None, fileid = None, break_reason = abstractmethod: raise NotImplementedError())()
    get_dbx_ignore_contents = (lambda self = None, device_anchor_fileid = None: raise NotImplementedError())()
    set_dbx_ignore_contents = (lambda self = None, device_anchor_filedid = None, dbx_ignore_contents = abstractmethod: pass)()
    subscribe_to_backup_progress = (lambda self = None, fileid = None: raise NotImplementedError())()
    on_device_anchor_unbind = (lambda self = None, callback = None: raise NotImplementedError())()
    remove_on_device_anchor_unbind = (lambda self = None, token = None: raise NotImplementedError())()
    on_one_way_sync_remediation = (lambda self = None, callback = None: raise NotImplementedError())()
    remove_one_way_sync_remediation_callback = (lambda self = None, token = None: raise NotImplementedError())()
    on_silly_labrador_event = (lambda self = None, callback = None: raise NotImplementedError())()
    remove_silly_labrador_event_callback = (lambda self = None, token = None: raise NotImplementedError())()
    on_device_anchor_progress = (lambda self = None, callback = None: raise NotImplementedError())()
    remove_backup_sync_progress_callback = (lambda self = None, token = None: raise NotImplementedError())()
    on_computer_backup_progress = (lambda self = None, callback = None: raise NotImplementedError())()
    get_current_device_anchor_progress = (lambda self = None, fileid = None: raise NotImplementedError())()
    get_current_computer_backup_progress = (lambda self = None, fileid = None: raise NotImplementedError())()
    get_device_anchor_metadata_by_path = (lambda self = None, path = None: raise NotImplementedError())()


class UpdateHiddenStateError(Exception):
    pass


class DeviceAnchorParentError(UpdateHiddenStateError):
    pass


class DeviceAnchorError(Exception):
    pass


class AlreadyExistsDeviceAnchorError(DeviceAnchorError):
    pass


class PathInvalidDeviceAnchorError(DeviceAnchorError):
    pass


class TargetNotADirectoryDeviceAnchorError(DeviceAnchorError):
    pass


class TargetAlreadyBoundDeviceAnchorError(DeviceAnchorError):
    pass


class NotADeviceAnchorError(DeviceAnchorError):
    pass


class NotFoundDeviceAnchorError(DeviceAnchorError):
    pass


class TargetIsDescendantOfDropbox(DeviceAnchorError):
    pass


class TargetDoesNotExist(DeviceAnchorError):
    pass


class InvalidDeviceAnchorError(DeviceAnchorError):
    pass


class TargetIsNotWritable(DeviceAnchorError):
    pass


class OtherDeviceAnchorError(DeviceAnchorError):
    pass


class IOError(DeviceAnchorError):
    pass


class NoSpace(DeviceAnchorError):
    pass


class DBXIgnoreError(DeviceAnchorError):
    pass

