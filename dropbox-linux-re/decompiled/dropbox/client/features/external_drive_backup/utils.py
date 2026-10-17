# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import os
import sys
from datetime import datetime, timezone
from os import access, scandir, W_OK
from os.path import isdir as _isdir, relpath as _relpath, sep as _sep
from typing import Callable, cast, Dict, List, Optional, Text, Tuple, TypeVar
import psutil
from dropbox.api.v2.datatypes.external_drive_backup import ExternalDriveEntry
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.constants import APPLE_DOUBLE_REGEX, CLOUD_DOCS_REGEX, DBXIGNORE_FILENAME, DEFAULT_IGNORED_GLOBS, NUCLEUS_UNSYNCED_FILENAMES_REGEX
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_accounts
from dropbox.client.features.backup_common.utils import convert_dbx_ignore_line_to_path, DEFAULT_IGNORED_GLOBS_V123, invalid_exclamation_character_class_regex
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.external_drive_backup.api_utils import list_backups
from dropbox.client.features.external_drive_backup.constants import DISABLED_EDB_STATE_ENUMS, EXP_BACKOFF_BASE, FREE_SPACE_BUFFER, HELP_CENTER_ARTICLE_URL, MAX_LIST_BACKUPS_BLOCKING_TIME_SEC, OQ_MAX_RUNTIME, SeamlessFissionMigrationVariant
from dropbox.client.features.external_drive_backup.disk_helpers import is_readonly_drive
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.errors import convert_to_failure, RequestFailedException
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventReporter, OperationEventSession
from dropbox.client.features.external_drive_backup.fission_migration_info import FissionMigrationDictType, FissionMigrationStatus, SeamlessFissionMigrationDictType, SeamlessFissionMigrationInfo, SeamlessFissionMigrationState
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.types import DeviceAnchorMigrationInfo, MaybeReconstructDeviceAnchorMigInfo, SeparatedAnchorsByEngineAndState, SeparatedAnchorsByState
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.bridge_interface_external_drive_backup_manager_view_model import FetchSubFoldersResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.fetch_sub_folders_error_types import FetchSubFoldersErrorTypes
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.get_dbx_ignore_contents_error_types import GetDbxIgnoreContentsErrorTypes
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.get_dbx_ignore_contents_result import GetDbxIgnoreContentsResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.sub_folder_info import SubFolderInfo
from dropbox.client.features.sync_everything.v3.api_utils import get_plan_name
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.fs_utils import _is_ignored_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity, UnexpectedNoneError
from dropbox.fastwalk import fastwalk
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, FutureHelpers, IncompleteFutureException, ResolvedFuture, sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2 import destroying
from dropbox.i18n import GB, TB
from dropbox.model.types import FileId
from dropbox.proto.nucleus.dbxignore_pb2 import DBXIgnoreVersion
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.device_anchor_interface import DeviceAnchorError, TargetDoesNotExist
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import DbxIgnoreContents, DeviceAnchorInfo, DeviceAnchorState, DeviceAnchorTargetType, ListDeviceAnchorsResult
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info

def migration_info_to_extra_dict(migration_info = None):
    return {
        'nopii_anchor_fileid': migration_info.device_anchor_fileid,
        'nopii_drive_uuid': migration_info.target_uuid,
        'nopii_drive_capacity': str(migration_info.capacity) }


def seamless_mig_info_to_extra_dict(migration_info = None):
    return migration_info_to_extra_dict(DeviceAnchorMigrationInfo.from_seamless_mig_info(migration_info))


def device_anchor_info_to_extra_dict(device_anchor_info = None):
    capactiy = 'None'
    if device_anchor_info.device_verification_attrs:
        capactiy = str(device_anchor_info.device_verification_attrs.capacity)
    return {
        'nopii_anchor_fileid': str(device_anchor_info.device_anchor_fileid),
        'nopii_drive_uuid': str(device_anchor_info.target_uuid),
        'nopii_drive_capacity': str(capactiy) }


def disk_usage_and_vmem_to_extra_dict(user_context = None):
    
    try:
        vmem = psutil.virtual_memory()
        if user_context.account.root_mount_path:
            disk_usage = psutil.disk_usage(user_context.account.root_mount_path)
        else:
            disk_usage = psutil.disk_usage(os.path.expanduser('~'))
        vmem_total = str(vmem.total)
        vmem_available = str(vmem.available)
        vmem_percent = str(vmem.percent)
        vmem_used = str(vmem.used)
        vmem_free = str(vmem.free)
        disk_usage_total = str(disk_usage.total)
        disk_usage_used = str(disk_usage.used)
        disk_usage_free = str(disk_usage.free)
        disk_usage_percent = str(disk_usage.percent)
    except Exception:
        vmem_total = ''
        vmem_available = ''
        vmem_percent = ''
        vmem_used = ''
        vmem_free = ''
        disk_usage_total = ''
        disk_usage_used = ''
        disk_usage_free = ''
        disk_usage_percent = ''

    return {
        'nopii_vm_total': vmem_total,
        'nopii_vm_avail': vmem_available,
        'nopii_vm_perc': vmem_percent,
        'nopii_vm_used': vmem_used,
        'nopii_vm_free': vmem_free,
        'nopii_diskmem_total': disk_usage_total,
        'nopii_diskmem_used': disk_usage_used,
        'nopii_diskmem_free': disk_usage_free,
        'nopii_diskmem_perc': disk_usage_percent }


def try_get_device_anchor_mig_info_from_std_da(device_anchor_info = None):
    pass
# WARNING: Decompyle incomplete


def get_reconstructed_mig_info(mig_info1 = None, mig_info2 = None):
    if mig_info1.is_from_reconstruct:
        return mig_info1
    if None.is_from_reconstruct:
        return mig_info2


def get_list_device_anchor_mig_info(mig_info1 = None, mig_info2 = None):
    if not mig_info1.is_from_reconstruct:
        return mig_info1
    if not None.is_from_reconstruct:
        return mig_info2


def is_maybe_reconstruct_in_abort_state(mig_info = None):
    if mig_info.list_device_anchor_state is not None:
        pass
    return mig_info.list_device_anchor_state in (DeviceAnchorState.BROKEN, DeviceAnchorState.PERMANENTLY_FAILED)


def compute_driving_seamless_variant(machine_context = None, variants = None, dedup_maybe_mig_infos = None):
    if SeamlessFissionMigrationVariant.SEAMLESS_FULL in variants:
        return SeamlessFissionMigrationVariant.SEAMLESS_FULL
    linked_accounts = len(machine_context.account_manager.linked_accounts) > 1
    if SeamlessFissionMigrationVariant.any_allowed_paired_variants(variants) and linked_accounts:
        return SeamlessFissionMigrationVariant.SEAMLESS_P3_LINKED_ACCT
    if SeamlessFissionMigrationVariant.any_allowed_multibackup_variants(variants) and len(dedup_maybe_mig_infos) > 1:
        return SeamlessFissionMigrationVariant.SEAMLESS_P2_MULTIBKP
    if len(variants) > 0:
        return SeamlessFissionMigrationVariant.SEAMLESS_P1_BASE
    return None.OFF


def drive_info_to_extra_dict(drive_info = None):
    os_access = is_os_access_writable(drive_info.mount_path)
# WARNING: Decompyle incomplete


def is_os_access_writable(mount_path = None):
    
    try:
        return access(mount_path, W_OK)
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)
        return None



def is_drive_writable(raw_path = None, media_writable = None):
