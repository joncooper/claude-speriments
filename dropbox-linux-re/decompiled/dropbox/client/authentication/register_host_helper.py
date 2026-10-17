# Source Generated with Decompyle++
# File: register_host_helper.pyc (Python 3.11)

import pprint
import socket
import sys
import uuid
from time import time as _time
from typing import Any, Callable, Dict, List, Optional, Tuple
from apex.util import process_architecture, system_architecture
from build_number import BUILD_KEY, BUILDID, is_frozen, is_store_managed, VERSION
from build_number.features import feature_enabled
from build_number.platform import IS_LINUX, IS_WINDOWS
from dropbox import event_names
from dropbox.build_common import get_build_number
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.auth_state import AuthState
from dropbox.client.authentication.auth_thread import _AuthenticationThreadImpl, on_auth_thread_blocking, wakeup_on_reconnect
from dropbox.client.authentication.helpers import clear_all_sync_state
from dropbox.client.authentication.linked_host_telemetry import get_linked_host_ids_for_telemetry, has_mti_team_accounts
from dropbox.client.authentication.types import AccountDataSource
from dropbox.client.benchmarking.startup import STARTUP_EVENT_BOOT_FAILED_TO_HANDLE_REGISTERED_HOST, STARTUP_EVENT_BOOT_FAILED_TO_REGISTER_HOST
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.device_info import get_device_info, UNSAFE_get_raw_machine_uuid
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY, FILE_PROVIDER_ROOT_CONVERSION_FAILURE_TIME
from dropbox.client.file_provider_cdm_migrator import FileProviderCdmMigrator, is_fp_cdm_migration_ongoing
from dropbox.client.high_trace import add_redacted_trace_value
from dropbox.client.installer_tag import InstallerTag
from dropbox.client.multiaccount.role import Roles
from dropbox.client.relocate_namespace_folders import DropboxArranger
from dropbox.client.session_metadata.interface import update_successful_startup
from dropbox.client.shell.multiaccount_shell_adapter import MultiaccountShellAdapter
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.status.label import StatusLabel
from dropbox.client.unlink_handlers import report_unlink_event, UnlinkReason
from dropbox.client.updatemanager.constants import IN_APP_UPDATE_CONFIG_KEY, UPDATEMANAGER_CONFIG_KEY
from dropbox.client.util import get_platform_info, get_update_manager_id, get_user_agent_dict, start_unlink_and_quit
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import HTTP429Error, is_transient_error, transient_error_from_network_issues, transient_error_from_server_load, transient_error_quick_retry, TransientErrorType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import python_version_string
from dropbox.i18n import trans
from dropbox.infinite.blacklist import InfiniteModuleBlacklist
from dropbox.metrics.camera_upload import CameraDeviceMetric, CameraEvent, CameraExtraMetric
from dropbox.model.types import FileId
from dropbox.nucleus.migration import SyncEngineMigration
from dropbox.nucleus.migration_state import SyncEngineStateManager
from dropbox.preferences import FP_DOWNGRADE, INFINITE_DOWNGRADE, OPT_LANG, OPT_OPT_VIDEO_UNSYNCED, OPT_VIDEO
from dropbox.proto.sync.root_pb2 import RootLayout
from dropbox.shared.util import safe_navigate
from dropbox.sync_root.interface import SyncRootType
from dropbox.sync_root.types import RemovalMode
from dropbox.trace import TRACE
if IS_LINUX:
    from lib.linuxffi.gnu.api import get_glibc_version
    from dropbox.system_info import get_linux_system_info
if IS_WINDOWS:
    from dropbox.win32.version import get_non_compatibility_mode_version
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class CachedRegisterHostParamsError(Exception):
    pass


class RegisterHostHelper:
    FAILURE_WAIT_PERIOD_BASE = 15
    FIFTEEN_MINUTES = 900
    
    def __init__(self, app, authentication_thread = None, config_manager = None, status_controller = None, installer_tag = ('app', 'DropboxApplication', 'authentication_thread', '_AuthenticationThreadImpl', 'config_manager', 'ConfigurationManagerInterface', 'status_controller', 'StatusControllerInterface', 'installer_tag', 'InstallerTag', 'return', 'None')):
        self._app = app
        self._authentication_thread = authentication_thread
        self._config_manager = config_manager
        self._status_controller = status_controller
        self._installer_tag = installer_tag
        self._failure_backoff = self.FAILURE_WAIT_PERIOD_BASE
        self._error_count = 0
        self._conn = None
        self._error_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self._success_callbacks = Handler(recursive = False, handle_exc = report_exception)

    get_updating_from_param_from_config = (lambda local_config = None: last_updatemanager = local_config.config_dict.get(UPDATEMANAGER_CONFIG_KEY) if local_config.config_dict else Noneif last_updatemanager:
if VERSION > last_updatemanager:
last_updatemanagertry:
del local_config.config_dict[UPDATEMANAGER_CONFIG_KEY]except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.AUTH)last_update = local_config.config_dict.get(IN_APP_UPDATE_CONFIG_KEY) if local_config.config_dict else Noneif last_update and len(last_update) >= 4 and last_update[3] == get_build_number():
last_update[2])()
    register_host = (lambda self = None, account = None, local_config = on_auth_thread_blocking(), cached_response = (None,): self._conn = self._app.connwakeup_on_reconnect(self._authentication_thread, self._conn)# WARNING: Decompyle incomplete
)()
    
    def add_error_callback(self = None, callback = None, priority = None):
        self._error_callbacks.add_handler(callback, priority)

    
    def remove_error_callback(self = None, callback = None):
        self._error_callbacks.remove_handler(callback)

    
    def run_error_callbacks(self = None, transient_error = None, error_count = None):
        self._error_callbacks.run_handlers(transient_error, error_count)

    
    def add_success_callback(self = None, callback = None, priority = None):
        self._success_callbacks.add_handler(callback, priority)

    
    def remove_success_callback(self = None, callback = None):
        self._success_callbacks.remove_handler(callback)

    prepare_and_call_register_host = (lambda account, local_config, conn, installer_tag, install_type = None, is_first_run = None, sync_engine_version = staticmethod, is_autorestart = (None,), linked_host_ids_for_telemetry = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'conn', 'DropboxConnection', 'installer_tag', 'Optional[InstallerTag]', 'install_type', 'Optional[str]', 'is_first_run', 'bool', 'sync_engine_version', 'Optional[str]', 'is_autorestart', 'bool', 'linked_host_ids_for_telemetry', 'Optional[List[int]]', 'return', 'Dict[str, Any]'): try:
hostname = socket.gethostname()except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.AUTH)hostname = 'localhost'platform_version = Noneif is_first_run:
platform_version = get_user_agent_dict().get('version')update_manager_id = Noneif is_frozen():
update_manager_id = get_update_manager_id()glibc_version = Nonelinux_info = Noneif IS_LINUX:
try:
glibc_version = get_glibc_version()linux_info = get_linux_system_info()except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.AUTH)updating_from = RegisterHostHelper.get_updating_from_param_from_config(local_config)se_state = SyncEngineStateManager.get_sync_engine_state(local_config)se_state_int = int(se_state) if se_state else 0true_platform_version = Noneif IS_WINDOWS:
true_win_ver = get_non_compatibility_mode_version()true_platform_version = true_win_ver[1] if true_win_ver else None# WARNING: Decompyle incomplete
)()
    
    def _try_register_host(self = None, account = None, local_config = None, cached_response = (None,)):
        add_redacted_trace_value(account.host_secret, '[host secret]')
        TRACE('Registering w/ host secret %s', account.host_secret, account = account)
        retry = True
        auth_state = None
        register_host_response = None
    # WARNING: Decompyle incomplete

    
    def _set_offline_startup_status_on_error(self = None, e = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _on_register_host_error(self = None, account = None, e = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_paired_account_from_server_data(self = None, register_host_response = None):
        secondary_email = register_host_response.get('secondary_email', None)
        secondary_uid = register_host_response.get('secondary_uid', None)
        secondary_account_id = register_host_response.get('secondary_account_id', None)
        if not secondary_email and secondary_uid or secondary_account_id:
            return None
        team = None.get('org_name', None)
        team_id = register_host_response.get('team_id', None)
        role_str = register_host_response.get('role', None)
        secondary_role = Roles.PERSONAL if role_str else None
        secondary_root_ns_id = register_host_response.get('secondary_root_ns_id', None)
        secondary_home_ns_id = register_host_response.get('secondary_home_ns_id', None)
        secondary_root_ns_id_fileid = None
        if 'secondary_root_ns_id_fileid' in register_host_response:
            secondary_root_ns_id_fileid = FileId(register_host_response['secondary_root_ns_id_fileid'])
        account = Account()
        account.email = secondary_email
        account.uid = secondary_uid
        account._account_id = secondary_account_id
        account.team = team
        account.team_id = team_id
        account.role = secondary_role
        account.root_ns_id = secondary_root_ns_id
        account.home_ns_id = secondary_home_ns_id
        account.root_ns_fileid = secondary_root_ns_id_fileid
        return account

    
    def _on_register_host_success(self, register_host_response = None, account = None, local_config = None, account_data_source = ('register_host_response', 'Dict[str, Any]', 'account', 'Account', 'local_config', 'LocalConfigurationInterface', 'account_data_source', 'AccountDataSource', 'return', 'AuthState')):
        if 'email' in register_host_response:
            pass
        linked = register_host_response['email']
        auth_state = None
        if feature_enabled('multi-team-accounts-prod'):
            paired_account = None
        else:
            paired_account = self._get_paired_account_from_server_data(register_host_response)
            account._paired_account_id = paired_account._account_id if paired_account else None
            account.paired_uid = paired_account.uid if paired_account else None
    # WARNING: Decompyle incomplete

    _sync_prefs_from_ui_flags = (lambda account = None, local_config = None: pass# WARNING: Decompyle incomplete
)()
    
    def _update_cdm_relocation_status(self = None):
        self._status_controller.set_status_label(None, StatusLabel.LABEL_CDM_RELOCATE, True, clear_previous = True)

    
    def _handle_joining_leaving_cdm_team(self = None, account = None, ret = None):
        root_ns_id = int(ret['root_ns_id'])
        home_ns_id = int(ret['home_ns_id'])
        home_ns_path = ret['home_ns_path']
        relocate_ok = bool(ret['ever_in_cdm_v1'])
        TRACE('in _handle_joining_leaving_cdm_team, root_ns_id = %r, home_ns_id = %r, relocate_ok = %r, is_fresh_link = %r', root_ns_id, home_ns_id, relocate_ok, account.is_fresh_link)
        if not home_ns_id != root_ns_id and relocate_ok:
            report_bad_assumption('User had a root/home mismatch but relocate_ok was False')
        dropbox_path = self._app.get_dropbox_path(account)
    # WARNING: Decompyle incomplete

    _update_config_for_tmr_migration_if_requested = (lambda config = None, account = None: if account.root_layout != RootLayout.TMR_ROOT:
Falseold_root_ns = None.config_dict.get('root_ns', None)old_home_ns = config.config_dict.get('home_ns', None)# WARNING: Decompyle incomplete
)()
    _restart_fp_extension = (lambda config = None: pass# WARNING: Decompyle incomplete
)()


def handle_changed_host_secret(app = None, local_config = None, account = None, new_host_secret = (None,)):
    destroy_root_from_config = destroy_root_from_config
    import dropbox.client.startup_handlers
    TRACE('Host id changed.  Going to clear all sync state.')
    if feature_enabled('multi-team-accounts-prod'):
        is_multiaccount = app.instance_config.get_linked_account_count() > 1
    else:
        is_multiaccount = app.account_manager.has_configured_non_primary_accounts
    app.instance_config.reset_instance_row(local_config.instance_id)
    
    try:
        destroy_root_from_config(app.root_manager, app.file_system, local_config, is_primary = account.is_primary, mode = RemovalMode.PRESERVE)
    except Exception:
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.AUTH)

    app.close_typescript_databases(local_config.appdata_path)
    clear_all_sync_state(local_config, account)
    report_unlink_event(reason_code = UnlinkReason.HOST_ID_CHANGED, is_primary = account.is_primary)
    if is_multiaccount:
        if account.is_primary:
            start_unlink_and_quit('/unlinkr', app.dialog_controller)
            return None
        None.restart([
            '/unlinksecondary'])
        return None
    None.restart()

