# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from enum import auto, Enum

class AutoSelsyncAmpMetricType(Enum):
    oneoff_events = auto()
    perf = auto()
    operation_event = auto()
    ui_event = auto()


class BackupAutoSelSyncEventLabel(Enum):
    start = auto()
    fail = auto()
    done = auto()
    perf = auto()


class BackupAutoSelSyncEvent(Enum):
    auto_selsync_validate = auto()
    auto_selsync_validate_per_account = auto()
    auto_selsync_out_nonlocal = auto()
    auto_selsync_do_selsync_action = auto()
    auto_selsync_alert = auto()
    hide_bi_folder_fails = auto()
    auto_selsync_alert_backup_on_web_btn = auto()
    auto_selsync_alert_backup_settings_btn = auto()
    call_list_devices_server = auto()
    call_list_drives_server = auto()

