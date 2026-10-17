# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from collections import defaultdict
from typing import Any, Dict, Optional, Text, Tuple, Union
import six
from six import iteritems
from build_number import is_full_msix
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.background_worker import on_background_thread
from dropbox.client.client_shmodel import ClientShmodel, ClientShmodelOrigin
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.gandalf import Gandalf
from dropbox.client.office.constants import AdminSetting, CONFIG_KEY_USER_INTERACTED_WITH_ADDIN_SETTINGS, OfficeAddInFailureReason, OfficeAddInMetrics, OfficeAddInPolicy, STORMCROW_FEATURE_OFFICE_ADDIN
from dropbox.client.office.interface import OfficeAddInHelperFactoryInterface, OfficeAddInHelperInterface
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import DropboxServerError, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import OFFICE_ADDIN_EVENT
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.preferences import OPT_OFFICE_ADDIN
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.exceptions import UnmountedPathError
from dropbox.trace import TRACE

class BaseOfficeAddInHelper(OfficeAddInHelperInterface):
    _SUPPORTED_APPS: 'Tuple[Text, ...]' = tuple()
    _SUPPORTED_AIDS: 'Tuple[Text, ...]' = tuple()
    _MIN_SUPPORTED_VERSION: 'Optional[int]' = None
    is_supported = (lambda : if is_full_msix():
Falsefeature_enabled('native-office-addin'))()
    is_allowed = (lambda gandalf = None: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self, gandalf, sync_engine_adapter, account_manager, local_config = None, ui_kit = None, client_shmodel = None, conn = ('gandalf', 'Gandalf', 'sync_engine_adapter', 'SyncEngineAdapter', 'account_manager', 'AccountManagerInterface', 'local_config', 'LocalConfigurationInterface', 'ui_kit', 'BaseUIKit', 'client_shmodel', 'ClientShmodel', 'conn', 'DropboxConnection', 'args', 'Any', 'kwargs', 'Any', 'return', 'None'), *args, **kwargs):
        self._gandalf = gandalf
        self._local_config = local_config
        self._ui_kit = ui_kit
        self._client_shmodel = client_shmodel
        self._addin_enabled = False
        self._admin_setting_by_account = defaultdict((lambda : AdminSetting.Unknown))
        self._account_manager = account_manager
        self._sync_engine_adapter = sync_engine_adapter
        self._conn = conn
        gandalf.add_on_changed_callback_any_account(self.refresh_enabled)
        account_manager.add_accounts_changed_callback(self._on_accounts_changed)
        local_config.add_pref_callback(OPT_OFFICE_ADDIN, self._on_preference_updated)
        self._is_showing_dialog = False
        self._is_disabled_in_app = False
        self._get_admin_setting()

    
    def install(self = None, install_dir = None):
        raise NotImplementedError

    
    def uninstall(self = None, uninstall_dir = None):
        raise NotImplementedError

    refresh_enabled = (lambda self = None, overwrite = None: is_supported = BaseOfficeAddInHelper.is_supported()is_user_enabled = self._is_user_enabled()is_allowed = BaseOfficeAddInHelper.is_allowed(self._gandalf)is_admin_allowed = self._is_admin_allowed()if is_supported:
if is_user_enabled:
if is_allowed:
should_enable = is_admin_allowedif should_enable != self._addin_enabled:
TRACE('Office Add-In enabled-state changed. Now: %r', should_enable)self.report_addin_helper_event(event = OfficeAddInMetrics.ADDIN_ENABLED if should_enable else OfficeAddInMetrics.ADDIN_DISABLED, trace = False)if should_enable:
self._enable(overwrite)else:
self._disable()self._addin_enabled = should_enable)()
    
    def initialize_window_tracking(self = None, machine_context = None):
        raise NotImplementedError

    
    def clear_window_tracking(self = None):
        raise NotImplementedError

    
    def set_admin_setting(self = None, account = None, is_allowed = None):
        setting = AdminSetting.Unknown
    # WARNING: Decompyle incomplete

    
    def show_shared_content_dialog(self = None, local_path = None, is_folder = None):
        server_path = None
        account = None
    # WARNING: Decompyle incomplete

    
    def copy_dropbox_link(self = None, unicode_local_path = None, is_folder = None):
        server_path = None
        local_path = None
        account = None
        file_id = None
    # WARNING: Decompyle incomplete

    
    def report_addin_helper_event(self = None, trace = None, **event_dict):
        unicode_event_dict = iteritems(event_dict)()
        BaseOfficeAddInHelper.report_addin_event(unicode_event_dict, trace = trace)

    report_addin_event = (lambda event_dict = None, trace = None: pass# WARNING: Decompyle incomplete
)()
    
    def get_failure_reason(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def allows_any_account(self = None, feature = None):
        return self._gandalf.allows_any_account(feature)

    
    def _enable(self = None, overwrite = None):
        raise NotImplementedError

    
    def _disable(self = None):
        pass

    
    def _supports_application(self = None, aid = None):
        return aid in self._SUPPORTED_AIDS

    
    def _supports_version(self = None, office_version = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _is_user_enabled(self = None):
        return self._local_config[OPT_OFFICE_ADDIN]

    
    def _is_admin_allowed(self = None):
        business_account = self._account_manager.business
        if not business_account is None:
            pass
        return self._admin_setting_by_account[business_account] == AdminSetting.Allowed

    
    def _user_has_seen_setting(self = None):
        return self._local_config.config_dict.get(CONFIG_KEY_USER_INTERACTED_WITH_ADDIN_SETTINGS, False)

    
    def _get_admin_setting(self = None):
        for account in self._account_manager.linked_accounts:
            if account.is_dfb_user and self._admin_setting_by_account[account] == AdminSetting.Unknown:
                self._get_current_account(account)
            return None

    _get_current_account = (lambda self = None, account = None: if not account.is_dfb_user:
report_bad_assumption('Attempting to get admin setting for non-team user')Noneenabled = None# WARNING: Decompyle incomplete
)()
    
    def _on_accounts_changed(self = None, account = None, account_change_type = None):
        if account_change_type == AccountChangeType.REMOVE:
            del self._admin_setting_by_account[account]
        self._get_admin_setting()
        self.refresh_enabled()

    
    def _on_preference_updated(self = None, *args, **kwargs):
        self.report_addin_helper_event(event = OfficeAddInMetrics.PREFERENCES_UPDATED, user_enabled = self._is_user_enabled(), trace = False)
        self._local_config.config_dict[CONFIG_KEY_USER_INTERACTED_WITH_ADDIN_SETTINGS] = True
        self.refresh_enabled()



class BaseOfficeAddInHelperFactory(OfficeAddInHelperFactoryInterface):
    _CLASS = BaseOfficeAddInHelper
    _args: 'Tuple[Any, ...]' = tuple()
    _kwargs: 'Dict[str, Any]' = dict()
    _initialized = False
    _addin_helper: 'Optional[OfficeAddInHelperInterface]' = None
    initialize_factory = (lambda cls = None: if cls._initialized:
Nonecls._initialized = Nonecls._args = argscls._kwargs = kwargs)()
    get_addin_helper = (lambda cls = None: if not cls._initialized:
None# WARNING: Decompyle incomplete
)()

