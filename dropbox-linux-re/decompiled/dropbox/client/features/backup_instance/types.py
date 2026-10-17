# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from abc import ABC
from enum import auto, Enum
from dropbox.enum_utils import AutoNameEnum
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.raii2.arc import Arc
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface

class DestroyableNucleus(ABC, NucleusInterface, Destroyable):
    pass

BackupInstance = Arc[DestroyableNucleus]

class BackupInstanceAmpNamespace(Enum):
    oneoff_events = auto()
    perf = auto()
    operation_event = auto()
    ui_event = auto()


class BackupInstanceEventLabel(Enum):
    start = auto()
    fail = auto()
    done = auto()
    perf = auto()


class BackupInstanceActionSurface(Enum):
    root_invalid_sticky = auto()
    root_invalid_native_dialog = auto()


class BackupInstanceEvent(Enum):
    backup_instance_init = auto()
    backup_instance_init_per_account = auto()
    backup_instance_dtor_unpause = auto()
    backup_instance_ctor_unpause = auto()
    backup_instance_pause_all = auto()
    backup_instance_unpause_all = auto()
    backup_instance_auto_relink_attempt = auto()
    get_or_create_instance = auto()
    get_instance = auto()
    root_validation_result = auto()
    root_computation_attempt_result = auto()
    set_local_instance_on_relink = auto()
    instance_access_should_have_existed = auto()
    manager_initial_startup = auto()
    manager_on_account_changed = auto()
    non_fp_instance_creation = auto()
    nucleus_restart_requested = auto()
    hide_bi_folder_fails = auto()
    apply_time_machine_ignore_attr_fail = auto()
    show_root_invalid_error = auto()
    select_dismiss = auto()
    select_view_help_center = auto()
    auto_selsync_validate = auto()
    auto_selsync_validate_per_account = auto()
    auto_selsync_do_selsync_action = auto()
    isotope_disabled = auto()


class RootValidationResult(AutoNameEnum):
    MATCHING_DOT_DROPBOX = auto()
    MISSING_FOLDER = auto()
    EMPTY_FOLDER = auto()
    EMPTY_DOT_DROPBOX = auto()
    NOT_A_DIR = auto()
    MISMATCHED_DOT_DROPBOX = auto()
    NONEMPTY_MISSING_DOT_DROPBOX = auto()


class RootValidationError(Exception):
    pass

