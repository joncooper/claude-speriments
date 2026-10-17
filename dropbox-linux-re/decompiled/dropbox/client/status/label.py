# Source Generated with Decompyle++
# File: label.pyc (Python 3.11)

from enum import Enum
from typing import Optional, Union
from dropbox.pap.events.enums.next_status_label_pb2 import NextStatusLabel as PAPNextStatusLabel
from dropbox.pap.events.enums.previous_status_label_pb2 import PreviousStatusLabel as PAPPreviousStatusLabel
from dropbox.pap.events.enums.status_label_pb2 import StatusLabel as PAPStatusLabel

class PAPStatusLabelType(Enum):
    PAP_STATUS_LABEL = 'PAP_STATUS_LABEL'
    PAP_PREVIOUS_STATUS_LABEL = 'PAP_PREVIOUS_STATUS_LABEL'
    PAP_NEXT_STATUS_LABEL = 'PAP_NEXT_STATUS_LABEL'


class StatusLabel(Enum):
    LABEL_IMPORTING = 'importing'
    LABEL_LOW_DISK_SPACE = 'low_disk_space'
    LABEL_CANT_WATCH = 'cant_watch_dropbox'
    LABEL_CANT_UNMOUNT_NAMESPACE = 'cant_unmount_namespace'
    LABEL_CANT_MOUNT = 'cant_mount_dropbox'
    LABEL_NO_ROOT_PERMISSION = 'no_root_permission'
    LABEL_PAUSED = 'paused'
    LABEL_UPDATING = 'updating'
    LABEL_CONNECTING = 'connecting'
    LABEL_PRELINK = 'waiting_for_link'
    LABEL_BLANK = 'nil'
    LABEL_OVERQUOTA = 'overquota'
    LABEL_MIGRATING = 'migrating'
    LABEL_MIGRATING_SYNC_ENGINE = 'migrating_sync_engine'
    LABEL_MOVING = 'moving'
    LABEL_PAUSING = 'pausing'
    LABEL_CONNECTING_ENGINE = 'connecting_engine'
    LABEL_STARTING = 'starting'
    LABEL_INITIALIZING = 'initializing'
    LABEL_EF_ENROLLMENT_BLOCKING = 'encrypted_folder_enrollment_blocking'
    LABEL_EF_ENROLLMENT_NON_BLOCKING = 'encrypted_folder_enrollment_non_blocking'
    LABEL_REINDEXING = 'reindexing'
    LABEL_SELSYNC = 'selsync'
    LABEL_CDM_RELOCATE = 'rearranging'
    LABEL_SYNCING_WITH_ERRORS = 'syncing_with_errors'
    LABEL_FILES_BLOCKED_BY_OVER_QUOTA = 'files_blocked_by_over_quota'
    LABEL_ERROR = 'error'
    LABEL_SYNCING = 'syncing'
    LABEL_LISTING = 'listing'
    LABEL_HASH_STATUS = 'hash_status'
    LABEL_DOWNLOAD_STATUS = 'download_status'
    LABEL_UPLOAD_STATUS = 'upload_status'
    LABEL_UPLOAD_FAILURE = 'upload_failure'
    LABEL_DOWNLOAD_FAILURE = 'download_failure'
    LABEL_HASH_FAILURE = 'hash_failure'
    convert_to_pap_status_label = (lambda cls = None, label = None, type_ = classmethod: try:
label_value = label.value.upper()if type_ == PAPStatusLabelType.PAP_STATUS_LABEL:
PAPStatusLabel.Value(label_value)if None == PAPStatusLabelType.PAP_PREVIOUS_STATUS_LABEL:
PAPPreviousStatusLabel.Value(label_value)if None == PAPStatusLabelType.PAP_NEXT_STATUS_LABEL:
PAPNextStatusLabel.Value(label_value)raise ValueError(f'''Unexpected PAP status label type {type_}''')except ValueError:
None)()

TRANSFER_LABELS = {
    StatusLabel.LABEL_HASH_STATUS,
    StatusLabel.LABEL_DOWNLOAD_STATUS,
    StatusLabel.LABEL_UPLOAD_STATUS}
APP_NOT_READY_LABELS = {
    StatusLabel.LABEL_CANT_WATCH,
    StatusLabel.LABEL_CANT_UNMOUNT_NAMESPACE,
    StatusLabel.LABEL_CANT_MOUNT,
    StatusLabel.LABEL_NO_ROOT_PERMISSION,
    StatusLabel.LABEL_CONNECTING,
    StatusLabel.LABEL_PRELINK,
    StatusLabel.LABEL_UPDATING,
    StatusLabel.LABEL_CONNECTING_ENGINE,
    StatusLabel.LABEL_STARTING,
    StatusLabel.LABEL_INITIALIZING}
