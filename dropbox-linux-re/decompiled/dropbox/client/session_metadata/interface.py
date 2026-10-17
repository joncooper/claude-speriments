# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

import json
import time
from typing import Any, Callable, cast, Dict, Optional, Text, Tuple, Union
from build_number import VERSION
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.shared.quota_info import QuotaEntityData, QuotaInfo
from dropbox.threading import Lock
from dropbox.trace import TRACE

class LegacySessionMetadata(object):
    
    def __init__(self = None):
        self._params_lock = Lock()
        self._params = { }
        self._on_metadata_updated = Handler(recursive = False, handle_exc = report_exception)

    
    def on_accounts_changed(self = None, account = None, account_change_type = None):
        if account_change_type == AccountChangeType.REMOVE:
            self._params_lock
            self._params.pop(account, None)
            None(None, None)
            return None
        with None:
            if not None:
                pass
        return None

    
    def handle_initial_server_response(self = None, account = None, server_response_data = None):
        self._params_lock
        self._params[account] = server_response_data
        TRACE('[Hermes]: Successfully added initial server data for account %r', account)
        None(None, None)

    _parse_relevant_server_response_data = (lambda cls = None, server_response_data = None: relevant_server_updates = { }for relevant_update in ('features', 'ui_flags', 'quota_info', 'in_use', 'quota'):
resp_value = server_response_data.get(relevant_update, None)if resp_value:
relevant_server_updates[relevant_update] = resp_valuerelevant_server_updates)()
    
    def handle_info_update(self = None, account = None, server_response_data = None):
        if account not in self._params:
            report_bad_assumption('Attempting to update server data for an unregistered account!')
            return None
        relevant_data = None._parse_relevant_server_response_data(server_response_data)
        self._params_lock
        self._params[account].update(relevant_data)
        TRACE('[Hermes]: Successfully updated server data for account %r', account)
        None(None, None)

    
    def add_on_session_metadata_updated_callback(self = None, callback = None):
        self._on_metadata_updated.add_handler(callback)

    
    def remove_on_session_metadata_updated_callback(self = None, callback = None):
        self._on_metadata_updated.remove_handler(callback)

    
    def _parse_quota_block(self = None, quota_type = None, params = None):
        info_block = params['quota_info'][quota_type]
        return (info_block['in_use'], info_block['quota'])

    
    def get_quota_info(self = None, account = None):
        self._params_lock
        params = self._params[account]
        if 'quota_info' in params:
            if 'team' in params['quota_info']:
                (root_in_use, root_quota) = self._parse_quota_block('team', params)
                if 'user' in params['quota_info']:
                    (home_in_use, home_quota) = self._parse_quota_block('user', params)
                else:
                    (root_in_use, root_quota) = self._parse_quota_block('user', params)
            else:
                root_quota = params['quota']
                root_in_use = params['in_use']
        root_entity_data = QuotaEntityData(data_in_use = root_in_use, sync_quota = root_quota)
        home_entity_data = None
    # WARNING: Decompyle incomplete

    
    def serialize(self = None, account = None):
        self._params_lock
        None(None, None)
        return 
        with None:
            if not None, json.dumps(self._params[account]):
                pass

    
    def get_stormcrow_feature_data(self = None, account = None):
        if account not in self._params:
         