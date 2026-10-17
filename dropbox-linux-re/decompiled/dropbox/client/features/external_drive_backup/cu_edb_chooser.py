# Source Generated with Decompyle++
# File: cu_edb_chooser.pyc (Python 3.11)

import shutil
from enum import auto, Enum
from typing import Any, Dict, Optional
from dropbox.camera.util import find_dcim
from dropbox.camera.uuidstore import SDCardDevice
from dropbox.client.camera_upload.configuration_manager import CameraConfigurationManager
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.external_drive_backup.constants import EdbEventOnboardingVariant
from dropbox.client.features.external_drive_backup.disk_helpers import is_remote_drive
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.utils import drive_info_to_extra_dict, is_drive_writable
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.platform import IS_WINDOWS
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.client.features.external_drive_backup.disk_arbitration.windows import drive_info_helper, has_write_permission

class OnboardingSuppressionReasons(Enum):
    EDB_GATED_OFF = auto()
    EDB_ONBOARDING_GATED_OFF = auto()
    EDB_ONBOARDING_GATED_CONTROL = auto()
    FS_UNSUPPORTED = auto()
    REMOTE = auto()
    NOT_WRITABLE = auto()
    HIGH_USAGE = auto()
    FOUND_DCIM = auto()
    TRACKED_BY_CU = auto()
    EDB_DONT_SHOW_AGAIN = auto()
    CU_CONFIG_MISSING = auto()
    CU_SUPPRESSED = auto()
    DROPBOX_PARENT_DRIVE = auto()
    DROPBOX_BACKUP_PARENT_DRIVE = auto()
    FAILED_COMPUTE_PATHS = auto()
    TOO_EARLY = auto()
    LOW_CAPACITY = auto()
    TOO_MANY_PROMPTS = auto()
    ALREADY_SHOWN_ONBOARDING = auto()
    NUCLEUS_VALIDATION_FAILED = auto()
    UNKNOWN_UUID = auto()
    ZERO_DEVICE_CAPACITY = auto()
    EDB_PREFS_SUPPRESSED = auto()
    OFFLINE = auto()
    TEAM_POLICY_DISABLED = auto()
    SERVER_UNREACHABLE = auto()
    FAT_EXFAT_ON_VENTURA_SKIPPED = auto()
    LOW_UI_MODE = auto()


def CU_EDB_TRACE(fmt = None, session_id = None, *args):
    real_fmt = '[CU-EDB][{}] {}'.format(session_id if session_id else '', fmt)
# WARNING: Decompyle incomplete


def device_found_in_config(cu_config = None, device_uuid = None):
    devices_list = cu_config.get_all_devices_and_accounts()
    for uid, _, _ in devices_list:
        if uid == device_uuid:
            TRACE('CU-EDB: Device UUID found in CU %r', device_uuid)
            return True
        return None


def suppress_edb_onboarding(cu_config, user_context, fs_type, current_usage, capacity, is_remote, is_writable = None, mount_path = None, session_id = None, skip_cu_checks = (False, False), skip_edb_product_filters = ('cu_config', 'Optional[CameraConfigurationManager]', 'user_context', 'UserContext', 'fs_type', 'str', 'current_usage', 'float', 'capacity', 'str', 'is_remote', 'bool', 'is_writable', 'bool', 'mount_path', 'str', 'session_id', 'str', 'skip_cu_checks', 'bool', 'skip_edb_product_filters', 'bool', 'return', 'Optional[OnboardingSuppressionReasons]')):
    pass
# WARNING: Decompyle incomplete


def is_edb_preferred_device(machine_context = None, cu_config = None, device_uid = None, path = ('machine_context', 'MachineContext', 'cu_config', 'CameraConfigurationManager', 'device_uid', 'Optional[str]', 'path', 'Optional[str]', 'return', 'bool')):
    pass
# WARNING: Decompyle incomplete


def edb_suppression_checks_per_drive(user_context, fs_type, current_usage, capacity = None, is_remote = None, is_writable = None, session_id = (None, False), skip_edb_product_filters = ('user_context', 'UserContext', 'fs_type', 'str', 'current_usage', 'float', 'capacity', 'str', 'is_remote', 'bool', 'is_writable', 'bool', 'session_id', 'Optional[str]', 'skip_edb_product_filters', 'bool', 'return', 'Optional[OnboardingSuppressionReasons]')):
    if not ExternalDriveBackupFeature.allowed_for_user(user_context):
        CU_EDB_TRACE('gated_off', session_id)
        return OnboardingSuppressionReasons.EDB_GATED_OFF
    onboarding_variant = ExternalDriveBackupFeature.event_onboarding_variant_for_user(user_context)
    if onboarding_variant == EdbEventOnboardingVariant.TEAM_POLICY_DISABLED:
        CU_EDB_TRACE('team_policy_disabled', session_id)
        return OnboardingSuppressionReasons.TEAM_POLICY_DISABLED
    if None == EdbEventOnboardingVariant.OFF:
        CU_EDB_TRACE('onboarding_gated_off', session_id)
        return OnboardingSuppressionReasons.EDB_ONBOARDING_GATED_OFF
    if not ExternalDriveBackupFeature.event_onboarding_is_allowed_filesystem(user_context.stormcrow, fs_type):
        CU_EDB_TRACE('drive_fs_not_supported fs_type=%r', session_id, fs_type)
        return OnboardingSuppressionReasons.FS_UNSUPPORTED
    if None:
        CU_EDB_TRACE('drive_is_remote', session_id)
        return OnboardingSuppressionReasons.REMOTE
    if not None:
        CU_EDB_TRACE('drive_is_not_writable', session_id)
        return OnboardingSuppressionReasons.NOT_WRITABLE
    max_usage = ExternalDriveBackupFeature.event_onboarding_max_drive_usage(user_context.stormcrow)
    if skip_edb_product_filters and current_usage > max_usage:
        CU_EDB_TRACE('drive_usage_too_high drive_usage=%r, limit=%r', session_id, current_usage, max_usage)
        return OnboardingSuppressionReasons.HIGH_USAGE
    min_capacity = ExternalDriveBackupFeature.event_onboarding_min_drive_capacity(user_context.stormcrow)
    if skip_edb_product_filters and int(capacity) < min_capacity:
        CU_EDB_TRACE('drive_capacity_too_low drive_capacity=%r, limit=%r', session_id, capacity, min_capacity)
        return OnboardingSuppressionReasons.LOW_CAPACITY
    CU_EDB_TRACE('No per-drive EDB suppression reasons', session_id)
    if onboarding_variant == EdbEventOnboardingVariant.CONTROL:
        CU_EDB_TRACE('onboarding_gated_off_control', session_id)
        return OnboardingSuppressionReasons.EDB_ONBOARDING_GATED_CONTROL


class EDBContextMenuGating:
    allowed_drives_paths: 'Dict[str, str]' = dict()
    on_arrival = (lambda drive_info = None, user_context = None, session_id = staticmethod: pass# WARNING: Decompyle incomplete
)()
    is_drive_allowed_edb_context_menu = (lambda user_context = None, drive_path = None: if not IS_WINDOWS:
FalseCU_EDB_TRACE('allowed drives list: %r,  path to check is %r', None, EDBContextMenuGating.allowed_drives_paths, drive_path)drive_id = EDBContextMenuGating.allowed_drives_paths.get(drive_path, None)if not drive_id:
Falsedo_not_show_uuids = None.machine_config.edb_onboarding_do_not_show_uuidsif int(drive_id) in do_not_show_uuids:
False)()

