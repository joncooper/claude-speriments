# Source Generated with Decompyle++
# File: impl.pyc (Python 3.11)

import random as insecure_random
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Mapping, Optional, Tuple
from apex.stormcrow import ObserveAnyAccount, ObservedAccount, ObserverToken, ObserveSpecificAccount, StormcrowClient, StormcrowSnapshot, UpdatedFeatures
from build_number import is_frozen
from dropbox.account_context import deduce_account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType, AccountDataSource
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.gandalf.base import Gandalf as BaseGandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.proto.apex.account_pb2 import Account as AccountProto, DeviceId
from dropbox.threading import Lock
from dropbox.trace import TRACE
STORMCROW_EXPOSURE_TABLE_NAME = 'gandalf_variant'
PERIODIC_EXPOSURE_REPORT_WAIT_SECS = 43200
PERIODIC_EXPOSURE_REPORT_JITTER = 10800
FeatureData = <NODE:12>()

class Gandalf(BaseGandalf):
    
    def __init__(self = None, inner = None):
        self.inner = inner
        self.account_manager = None
        self._accounts_lock = Lock()
        self._machine_stormcrows_available = False
        self._known_accounts = { }
        self._change_callbacks = { }
        self._last_variant_val = { }
        self._logged_exposure = { }
        self._logged_exposure_lock = Lock()
        self._exposure_quiet_time = time.time() + 600
        self._next_exposure_report_secs = time.time() + 3600
        self._queued_exposure_report = False
        self._stormcrow_cache = None
        self._main_observer = self.inner.register_observer(self.handle_stormcrow_change)
        self._has_reported_mismatch = False

    
    def set_account_manager(self = None, account_manager = None):
        self.account_manager = account_manager

    
    def handle_stormcrow_change(self = None, unused_account_id = None, unused_updated_features = None, snapshot = ('unused_account_id', 'Optional[str]', 'unused_updated_features', 'UpdatedFeatures', 'snapshot', 'StormcrowSnapshot', 'return', 'None')):
        self._stormcrow_cache = snapshot

    
    def get_variant_value(self = None, feature = None, account_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def register_device(self = None):
        if self._machine_stormcrows_available:
            TRACE('[Stormcrow] Skipping machine stormcrow registration, already available')
            return None
        TRACE('[Stormcrow] Registering machine stormcrows for machine')
        self._accounts_lock
        self.inner.add_machine()
        self._machine_stormcrows_available = True
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def register_account(self = None, account = None, account_data_source = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _variant_trace_first_and_changes(self = None, feature = None, account = None, result = ('feature', 'str', 'account', 'Optional[AccountInterface]', 'result', 'Any', 'return', 'None')):
        if (account, feature) not in self._last_variant_val or result != self._last_variant_val[(account, feature)]:
            last_val = self._last_variant_val.get((account, feature), None)
            TRACE('Gandalf: variant for feature %s changed to %r from %r', feature, result, last_val, account = account)
            self._last_variant_val[(account, feature)] = result
            return None

    
    def get_variant(self = None, feature = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_variants_all_accounts(self = None, feature = None):
        variants = []
        machine_variant = self.get_variant_value(feature, None)
        if machine_variant:
            variants.append(machine_variant)
        for account in list(self._known_accounts.values()):
            user_variant = self.get_variant_value(feature, account.account_id)
            if user_variant:
                variants.append(user_variant)
            return variants()

    
    def add_on_changed_callback(self = None, callback = None, account = None):
        obs_account = ObserveAnyAccount
        if account.account_id:
            obs_account = ObserveSpecificAccount(account_id = account.account_id)
        token = self.inner.register_observer(ChangeHandler(callback), obs_account)
        self._change_callbacks[(callback, account.account_id)] = token

    
    def remove_on_changed_callback(self = None, callback = None, account = None):
        
        try:
            token = self._change_callbacks.pop((callback, account.account_id))
            self.inner.unregister_observer(token)
            return None
        except KeyError:
            return None


    
    def add_on_changed_callback_any_account(self = None, callback = None):
        token = self.inner.register_observer(ChangeHandler(callback))
        self._change_callbacks[(callback, None)] = token

    
    def remove_on_changed_callback_any_account(self = None, callback = None):
        
        try:
            token = self._change_callbacks.pop((callback, None))
            self.inner.unregister_observer(token)
            return None
        except KeyError:
            return None


    
    def all_features_for_account(self = None, account = None):
        return self.inner.get_features(str(account.account_id))

    
    def add_feature_overrides(self = None, features = None):
        self.inner.add_feature_overrides(features)

    
    def unset_forced_feature_override(self = None, feature = None):
        self.inner.clear_feature_override(feature)

    
    def all_feature_overrides(self = None):
        return self.inner.get_feature_overrides()

    
    def notify_refresh_observers(self = None):
        for callback, _ in list(self._change_callbacks.keys()):
            callback()
            return None

    
    def _get_variant_population(self = None, feature = None, account_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_accounts_changed(self = None, account = None, change_type = None):
        self._accounts_lock
        if change_type == AccountChangeType.REMOVE and account.host_int:
            self._logged_exposure_lock
            self._logged_exposure.pop(account, None)
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        inner_account = self._known_accounts.pop(account.host_int)
        if inner_account:
            self.inner.remove_account(inner_account)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _report_exposure(self, account = None, feature = None, variant = None, population_id = ('account', 'AccountInterface', 'feature', 'str', 'variant', 'Optional[str]', 'population_id', 'Optional[str]')):
        exposure_data = None
        self._logged_exposure_lock
        logged_exposure = self._logged_exposure.get(account)
    # WARNING: Decompyle incomplete

    _build_exposure_data = (lambda feature = None, variant = None, population_id = staticmethod: numeric_population_id = -1# WARNING: Decompyle incomplete
)()
    
    def periodic_exposure_report(self = None):
        pass
    # WARNING: Decompyle incomplete



class ChangeHandler:
    
    def __init__(self = None, callback = None):
        self.callback = callback

    
    def __call__(self = None, account_id = None, updated_features = None, snapshot = ('account_id', 'Optional[str]', 'updated_features', 'UpdatedFeatures', 'snapshot', 'StormcrowSnapshot')):
        
        try:
            self.callback()
            return None
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.GANDALF)
            return None



