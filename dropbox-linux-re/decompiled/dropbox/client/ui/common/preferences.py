# Source Generated with Decompyle++
# File: preferences.pyc (Python 3.11)

import functools
from collections import OrderedDict
from typing import Callable, cast, Optional, Text, Tuple
from build_number.features import feature_enabled
from preferences_utils import is_paid_user, PanelNames
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.camera_upload.camera_upload_metric_logger import CameraEvent, CameraExtraMetric, MetricsLogger as CameraLogger
from dropbox.client.camera_upload.types import CUDeviceUID
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.multiaccount.constants import Role
from dropbox.client.office.constants import OfficeAddInFailureReason
from dropbox.client.status.label import StatusLabel
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import PREFERENCES_BUTTON_CLICKED_ACTION, UI_ACTION_EVENT
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.raii2 import destroying
from dropbox.i18n import format_number, format_percent, get_current_code, set_user_interface_language, system_lang_code
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.model.types import FileId
from dropbox.observable import Observable
from dropbox.preferences import OPT_HARMONY, OPT_HARMONY_VISIBILITY
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_root.gating import is_file_provider_root_type
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.configuration_manager import CameraConfigurationManager, DeviceListing
    from dropbox.client.main import DropboxApplication
    from dropbox.infinite.state_machine import InfiniteStateMachine

def report_prefs_interaction(f, action_name = (None, None)):
    pass
# WARNING: Decompyle incomplete

set_web_locale = (lambda conn = None, account = None, new_code = on_background_thread: conn.set_web_locale(account, new_code))()

def change_client_language(dropbox_app, new_code, prompt = None, on_done = None, on_cancel = None, on_restart = ('dropbox_app', 'DropboxApplication', 'new_code', 'str', 'prompt', 'Callable', 'on_done', 'Callable[[], None]', 'on_cancel', 'Callable[[], None]', 'on_restart', 'Callable[[], None]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete

UNSUPPORTED_FS_HELP_URL = '/help/desktop-web/cant-establish-secure-connection#location'
BYTES_PER_GB = 1073741824
BYTES_PER_TB = 1000 * BYTES_PER_GB
BYTES_PER_PB = 1024 * BYTES_PER_TB

def format_quota_usage(in_use = None, quota = None):
    percentage = format_percent(0 if not quota else in_use / quota, frac_precision = 1)
    if quota / BYTES_PER_PB > 1:
        total_space_pb = format_number(quota / BYTES_PER_PB, frac_precision = 1)
        return PrefStrings.account_quota_usage_pb % dict(percentage = percentage, total_space = total_space_pb)
    if None / BYTES_PER_TB > 1:
        total_space_tb = format_number(quota / BYTES_PER_TB, frac_precision = 1)
        return PrefStrings.account_quota_usage_tb % dict(percentage = percentage, total_space = total_space_tb)
    total_space_gb = format_number(quota / BYTES_PER_GB, frac_precision = 1)
    return PrefStrings.account_quota_usage_gb % dict(percentage = percentage, total_space = total_space_gb)

HARMONY_LEVEL_ALWAYS = 0
HARMONY_LEVEL_VIEWERS = 1
HARMONY_LEVEL_NEVER = 2

def harmony_level_to_text(level = None):
    mapping = (PrefStrings.harmony_always, PrefStrings.harmony_viewers, PrefStrings.harmony_never)
    return mapping[level]


def get_harmony_level_from_local_config(local_config = None):
    harmony_enabled = local_config[OPT_HARMONY]
    harmony_visibility = local_config[OPT_HARMONY_VISIBILITY]
    if not harmony_enabled:
        return HARMONY_LEVEL_NEVER
    if None == 2:
        return HARMONY_LEVEL_VIEWERS


def get_harmony_level(dropbox_app = None):
    local_config = dropbox_app.config_manager.local_config(None)
    return get_harmony_level_from_local_config(local_config)


def office_addin_failure_reason(app = None):
    
    try:
        if app.office_addin_helper:
            return app.office_addin_helper.get_failure_reason()
    except Exception:
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.PREFERENCES_UI)



def refresh_office_addin_enabled(app = None, overwrite = None):
    
    try:
        if app.office_addin_helper:
            app.office_addin_helper.refresh_enabled(overwrite = overwrite)
            return None
        return None
    except Exception:
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.PREFERENCES_UI)
        return None



def get_cu_devices_list(camera_config = None):
    pass
# WARNING: Decompyle incomplete


def get_cu_label_for_device(device_name = None, role = None, account_manager = None):
    account = account_manager.account_for_role(role) if role else None
# WARNING: Decompyle incomplete


def clear_cu_device_from_list(camera_config = None, device_uid = None):
    camera_config.forget_device(device_uid)
# WARNING: Decompyle incomplete


def should_show_infinite_settings(state_machine = None, account = None, app = None):
    if not state_machine:
        TRACE('[Pref] Infinite state machine missing, not showing infinite prefs.')
        return False
    if not None:
        TRACE('[Pref] Account for pref page is missing, not showing infinite prefs.')
        return False
# WARNING: Decompyle incomplete


def update_root_policy(account = None, app = None):
    local_config = app.config_manager.local_config(account)
    root_infinite_policy = InfinitePolicyController.get_root_policy(local_config)
# WARNING: Decompyle incomplete

