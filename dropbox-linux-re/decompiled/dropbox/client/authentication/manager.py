# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

import json
import os
import string
import unicodedata
import uuid
from os.path import isdir as _isdir
from random import SystemRandom
from typing import Any, Callable, Dict, List, Optional, Set, Text, Tuple
from build_number import BuildVersion, is_test, VERSION
from build_number.features import feature_enabled
from dropbox.api.v2.datatypes.users import GetLinkedUsersRequest
from dropbox.assertions import assert_
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.auth_state import AuthState
from dropbox.client.authentication.auth_thread import _AuthenticationThreadImpl, assert_on_auth_thread, on_auth_thread, on_auth_thread_returns_none, wakeup_on_reconnect
from dropbox.client.authentication.helpers import clear_all_sync_state
from dropbox.client.authentication.interface import AccountChangeCallback, AccountManagerInterface
from dropbox.client.authentication.linked_host_telemetry import add_linked_host_id_for_telemetry, add_linked_team_host_id_for_telemetry, remove_linked_host_id_for_telemetry, remove_linked_team_host_id_for_telemetry
from dropbox.client.authentication.register_host_helper import RegisterHostHelper
from dropbox.client.authentication.types import AccountChangeType, AccountChangeTypeFilter, AccountDataSource
from dropbox.client.constants import DEFAULT_DROPBOX_FOLDER_NAME, DEFAULT_DROPBOX_PATH, LOCAL_FORM
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventClass
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.folder_tagger.folder_tagger import FolderTagger
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ping import DualPingSource, ping_and_report
from dropbox.client.session_metadata.interface import LegacySessionMetadata, update_successful_startup
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.status.label import StatusLabel
from dropbox.client.ui.common.auth_error import show_connection_error_dialog, show_multiaccount_disabled_alert, show_unlink_because_unpaired_alert, show_unlink_failure_dialog
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.client_api.apiv2.generated.users import Users
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.client_api.exceptions import HTTP429Error, is_transient_error, TransientErrorType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import sanitize_filename
from dropbox.foundation.environment import is_playwright_tests
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.i18n import trans
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.nucleus.migration_state import SyncEngineStateManager
from dropbox.platform import IS_MAC, platform
from dropbox.shared.util import db_lower
from dropbox.sqlite3_exceptions import DatabaseOrDiskFullError, DiskIOError
from dropbox.sqlite3_helpers import Cursor
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.desired_root import get_desired_sync_root_type
from dropbox.sync_root.helpers import folder_conflicts_with_icloud
from dropbox.sync_root.types import SyncRootInfo, SyncRootType, SyncRootTypeReason
from dropbox.threading import RLock
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
if IS_MAC:
    from dropbox.mac.version import CATALINA, MAC_VERSION
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
    from dropbox.client.gandalf import Gandalf
    from dropbox.client.installer_tag import InstallerTag
    from dropbox.client.main import DropboxApplication
    from dropbox.client.notifications.legacy_notifications import PairedUserNotification
    from dropbox.client_api.dropbox_connection import DropboxConnection

class AccountManager(AccountManagerInterface):
    _TYPE_PRIMARY = 'primary'
    _TYPE_SECONDARY = 'secondary'
    _TYPE_PAIRED = 'paired'
    
    def __init__(self, app, authentication_thread, config_manager, status_controller = None, installer_tag = None, register_host_helper = None, boot_callbacks = ('app', 'DropboxApplication', 'authentication_thread', '_AuthenticationThreadImpl', 'config_manager', 'ConfigurationManagerInterface', 'status_controller', 'StatusControllerInterface', 'installer_tag', 'InstallerTag', 'register_host_helper', 'RegisterHostHelper', 'boot_callbacks', 'Handler[Callable[[], None]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_key(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _setup_webdebugger_hooks(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _can_startup_asynchronously(self = None, account = None, local_config = None, is_autorestart = ('account', 'Account', 'local_config', 'LocalConfigurationInterface', 'is_autorestart', 'bool', 'return', 'bool')):
        if is_autorestart:
            return False
    # WARNING: Decompyle incomplete

    
    def _report_linked_accounts(self = None, accounts_data_source = None):
        if num_linked > 0:
            stormcrow_var = self._session_metadata.stormcrow_variant_for_account('desktop-async-startup', self.primary)
            report('accounts-linked', num_linked_accounts = num_linked, link_type = accounts_data_source.value, offline_startup_enabled = stormcrow_var == 'ALL_OFFLINE')
            return None
        return None if feature_enabled('multi-team-accounts-prod') else sum

    load_known_accounts = (lambda self = None, on_link_complete = None: pass# WARNING: Decompyle incomplete
)()
    
    def _load_account(self = None, account = None, on_link_complete = None, offline_startup_allowed = ('account', 'Account', 'on_link_complete', 'Callable[[Account, bool], None]', 'offline_startup_allowed', 'bool', 'return', 'Optional[AuthState]')):
        pass
    # WARNING: Decompyle incomplete

    
    def _register_host_online(self = None, account = None, local_config = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _try_initial_hourly_refresh(self = None, account = None):
        auth_state = AuthState(account, None)
        conn = self._app.conn
    # WARNING: Decompyle incomplete

    
    def _run_known_accounts_linked_callbacks(self = None):
        self._known_accounts_linked_callbacks.run_handlers()

    unlink = (lambda self = None, account = None: if not account or account.host_int:
NoneNone._config_manager.clear_state_for_account(account)self._remove_account(account)if not feature_enabled('multi-team-accounts-prod'):
paired_account = Account()for key in ('email', 'uid', 'team', 'role'):
setattr(paired_account, key, getattr(account, key))paired_account._account_id = account.account_idself.paired_pending_link = paired_accountif account.is_primary and self.primary:
self.primary.paired_host_secret = Noneremove_linked_host_id_for_telemetry(account.host_int)remove_linked_team_host_id_for_telemetry(account.host_int)account.linked = Falseaccount.link_sources = set()self._accounts_changed_callbacks.run_handlers(account, AccountChangeType.REMOVE))()
    
    def _remove_account(self = None, account = None):
        self._lock
        if feature_enabled('multi-team-accounts-prod'):
            known_account = self._accounts_by_uid.get(self._get_key(account))
            if known_account == account:
                self._accounts_by_uid.pop(self._get_key(account), None)
                None(None, None)
                return None
            TRACE('!! Unknown account given to _remove_account, account: %r, known: %r', account, known_account)
            None(None, None)
            return None
        known_account = None._accounts_by_type[self._TYPE_PRIMARY if account.is_primary else self._TYPE_SECONDARY]
        if account != known_account:
            TRACE('!! Unknown account given to _remove_account, account: %r, known: %r', account, known_account)
            None(None, None)
            return None
        if None.is_primary:
            self._accounts_by_type.pop(self._TYPE_PRIMARY, None)
        else:
            self._accounts_by_type.pop(self._TYPE_SECONDARY, None)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def add_account(self = None, account = None, primary = None):
        if not account:
            return None
    # WARNING: Decompyle incomplete

    
    def on_account_linked(self = None, account = None):
        if not account or account.host_int:
            return None
        add_linked_host_id_for_telemetry(account.host_int)
        if account.is_dfb_user:
            add_linked_team_host_id_for_telemetry(account.host_int)
        self._accounts_changed_callbacks.run_handlers(account, AccountChangeType.LINK)

    
    def handle_paired_notification(self = None, notification = None):
        if feature_enabled('multi-team-accounts-prod'):
            TRACE('Ignoring paired notifications because multi-team-accounts-prod is enabled.')
            return None
        paired_account = Account()
        paired_account.team = notification.team
        paired_account.role = Roles.PERSONAL if notification.paired_role == Roles.BUSINESS else Roles.BUSINESS
        paired_account.email = notification.other_email
        paired_account._account_id = notification.other_account_id
        paired_account.uid = notification.other_uid
        self.paired_pending_link = paired_account
        self._accounts_changed_callbacks.run_handlers(paired_account, AccountChangeType.PAIRED)

    
    def get_new_sync_root_type(self = None, account = None, local_config = None, gandalf = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'gandalf', 'Gandalf', 'return', 'Tuple[SyncRootType, Set[SyncRootType], SyncRootTypeReason]')):
        TRACE('[RootManager] get_new_sync_root_type for account: %r', account, account = account)
        (desired_root_type, root_type_reason) = get_desired_sync_root_type(self, account, gandalf, local_config, team_admin_fp_allowed = self._is_team_admin_fp_allowed(account))
        TRACE('[RootManager] desired root type is %r because of %r', desired_root_type, root_type_reason, account = account)
    # WARNING: Decompyle incomplete

    _FP_POLICY_CHECK_TIMEOUT_SECONDS = 5
    
    def _is_team_admin_fp_allowed(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_valid_path_in_unlink_cookie(self = None, account = None, local_config = None):
        unlink_cookie = local_config.unlink_cookie
        TRACE('[RootManager] Looking for valid mount path in unlink cookie: %r', unlink_cookie)
        if not unlink_cookie:
            return None
        path_from_cookie = None.get('path')
    # WARNING: Decompyle incomplete

    
    def is_standard_dropbox_location(self = None, path = None):
        return 'Dropbox' in os.path.basename(path)

    
    def get_new_dropbox_location(self = None, account = None, local_config = None, override_path = (None, True), use_cookie = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'override_path', 'Optional[str]', 'use_cookie', 'bool', 'return', 'str')):
        TRACE('[RootManager] get_new_dropbox_location account: %r, override_path: %r, use_cookie: %r', account, override_path, use_cookie, account = account)
    # WARNING: Decompyle incomplete

    
    def get_display_name_account_component(self = None, account = None, unsanitized_name_replacement = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_current_dropbox_name(self = None, account = None, suffix = None):
        pass
    # WARNING: Decompyle incomplete

    _resolve_name_collision = (lambda base_name = None, existing_names = None, suffixed_name = staticmethod, normalize_name = ('base_name', 'str', 'existing_names', 'Set[str]', 'suffixed_name', 'Callable[[int], str]', 'normalize_name', 'Callable[[str], str]', 'return', 'str'): base_name_key = normalize_name(base_name)if base_name or base_name_key not in existing_names:
base_namemax_suffix = len(existing_names) + 2for suffix in range(2, max_suffix + 1):
candidate = suffixed_name(suffix)if normalize_name(candidate) not in existing_names:
None, candidateraise RuntimeError('Unable to generate a unique Dropbox account name from %r within %d suffix attempts' % (base_name, max_suffix)))()
    _get_lower_case_folder_name = (lambda name = None: Text(db_lower(name)))()
    _get_lower_case_display_name = (lambda name = None: name.casefold())()
    
    def _get_other_existing_names_for_account(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _resolve_folder_name_collisions(self = None, account = None, dropbox_name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _resolve_generated_fp_domain_display_name_collision(self = None, account = None, existing_names = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_other_existing_fp_domain_display_names_for_account(self = None, account = None):
        existing_names = set()
        for linked_account in self.linked_accounts_all:
            if account is linked_account:
                pass
            else:
                display_name = self._resolve_generated_fp_domain_display_name_collision(linked_account, existing_names)
                existing_names.add(self._get_lower_case_display_name(display_name))
            return existing_names

    
    def _resolve_fp_domain_display_name_collisions(self = None, account = None, domain_name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def generate_fp_domain_display_name(self = None, account = None):
        domain_name = self.get_display_name_account_component(account)
        if feature_enabled('multi-team-accounts-prod'):
            return self._resolve_fp_domain_display_name_collisions(account, domain_name)
    # WARNING: Decompyle incomplete

    
    def generate_dropbox_name(self = None, account = None, suffix = None):
        dropbox_name = self._generate_dropbox_name(account, suffix)
        if feature_enabled('multi-team-accounts-prod'):
            resolved_dropbox_name = self._resolve_folder_name_collisions(account, dropbox_name)
            if resolved_dropbox_name != dropbox_name:
                TRACE('Resolved Dropbox folder name collision from %r to %r', dropbox_name, resolved_dropbox_name)
            return resolved_dropbox_name
        if not None.is_primary:
            primary_dropbox_name = self.primary.folder_name
            if not primary_dropbox_name:
                primary_dropbox_name = self._generate_dropbox_name(self.primary)
            if dropbox_name.lower() == primary_dropbox_name.lower():
                dropbox_name = self._generate_dropbox_name(account, suffix = '2')
                report_bad_assumption('Detected a folder name that is the same as the primary.  Renaming the folder name to %r.', dropbox_name)
        return dropbox_name

    
    def _generate_dropbox_name(self = None, account = None, suffix = None):
        suffix = '' if not suffix else ' %s' % suffix
        custom_display_name = self.get_display_name_account_component(account, unsanitized_name_replacement = '-')
        if custom_display_name:
            if account.has_tmf:
                ret = f'''{custom_display_name!s} {DEFAULT_DROPBOX_FOLDER_NAME!s}{suffix!s}'''
            else:
                ret = f'''{DEFAULT_DROPBOX_FOLDER_NAME!s} ({custom_display_name!s}{suffix!s})'''
        else:
            TRACE('MULTIACCOUNT: _generate_dropbox_name called, but falling back on default folder %r (team: %r, role: %r)', DEFAULT_DROPBOX_FOLDER_NAME, account.team, account.role)
            ret = DEFAULT_DROPBOX_FOLDER_NAME
        return unicodedata.normalize(LOCAL_FORM, ret)

    
    def get_account(self = None, host_int = None):
        for account in self.linked_accounts_all:
            if account.host_int == host_int:
                
                return None, account
            return None

    
    def account_for_uid(self = None, uid = None):
        for account in self.linked_accounts_all:
            if account.uid == uid:
                
                return None, account
            return None

    
    def add_accounts_changed_callback(self = None, callback = None, event_filter = None, priority = (0, 0)):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_accounts_changed_callback(self = None, callback = None):
        callback_wrapper = self._callback_cache.pop(callback, None)
        if callback_wrapper:
            self._accounts_changed_callbacks.remove_handler(callback_wrapper)
            return None

    
    def add_known_accounts_linked_callback(self = None, callback = None, priority = None):
        self._known_accounts_linked_callbacks.add_handler(callback, priority)

    
    def remove_known_accounts_linked_callback(self = None, callback = None):
        self._known_accounts_linked_callbacks.remove_handler(callback)

    
    def add_multiaccount_linking_enabled_changed_callback(self = None, callback = None):
        self._multiaccount_linking_enabled_changed_callbacks.add_handler(callback)

    
    def remove_multiaccount_linking_enabled_changed_callback(self = None, callback = None):
        self._multiaccount_linking_enabled_changed_callbacks.remove_handler(callback)

    
    def update_multiaccount_linking_enabled(self = None, linking_enabled = None):
        if self.primary:
            self.primary.disable_multiaccount_link = not linking_enabled
            self._multiaccount_linking_enabled_changed_callbacks.run_handlers(linking_enabled)
            return None

    
    def account_for_role(self = None, role = None):
        pass
    # WARNING: Decompyle incomplete

    
    def can_link_secondary(self = None):
