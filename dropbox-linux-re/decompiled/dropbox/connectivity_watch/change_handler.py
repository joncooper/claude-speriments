# Source Generated with Decompyle++
# File: change_handler.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from enum import Enum
from time import time as _time
from typing import Callable, Dict, Optional
from google.protobuf.json_format import MessageToJson
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.connectivity_watch.watch_interface import ConnectivityReadAPI, ConnectivityState
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.overrides import TRACE
from dropbox.proto.nucleus.network_state_pb2 import NetworkFailureKind, NetworkState as EngineNetworkState
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.threading import Lock
ENGINE_CONNECTIVITY_STATUS_STORMCROW = 'desktop-sync-engine-network-connectivity-status'
STATUS_CHANGING_FAILURE_KINDS = {
    NetworkFailureKind.CONNECTION,
    NetworkFailureKind.NETWORK_CONFIGURATION,
    NetworkFailureKind.TRANSPORT_LAYER_SECURITY}
IGNORED_CONNECTION_STATE = 'ignored_connection_failure'

class _ConnectivityType(Enum):
    OS = 'OS'
    PRIMARY_ENGINE = 'PRIMARY_ENGINE'
    SECONDARY_ENGINE = 'SECONDARY_ENGINE'


class ConnectivityChangeHandler(ConnectivityReadAPI):
    
    def __init__(self = None, connection = None, update_tray_status_fn = None):
        self._lock = Lock()
        self._connection = connection
        self._update_tray_status_fn = update_tray_status_fn
        self._has_disconnected = False
        self._gandalf = None
        self._state_dict = { }
        for type in _ConnectivityType:
            self._state_dict[type] = ConnectivityState(ConnectivityState.UNKNOWN, _time())
            return None

    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf

    
    def set_initial_os_state(self = None, initial_state = None):
        self._lock
        self._state_dict[_ConnectivityType.OS] = initial_state
        self._set_state_as_status(initial_state)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def update_os_state(self = None, state = None):
        self._update_state(_ConnectivityType.OS, state)

    
    def update_primary_engine_state(self = None, network_state = None):
        self._update_state(_ConnectivityType.PRIMARY_ENGINE, _engine_state_to_connectivity_state(network_state), network_state)

    
    def update_secondary_engine_state(self = None, network_state = None):
        self._update_state(_ConnectivityType.SECONDARY_ENGINE, _engine_state_to_connectivity_state(network_state), network_state)

    
    def _set_state_as_status(self = None, state = None):
        self._update_tray_status_fn(state)
        if state.state == ConnectivityState.DISCONNECTED:
            self._has_disconnected = True
            return None

    
    def _is_engine_status_update_allowed(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _update_state(self = None, type = None, connectivity_state = None, network_state = (None,)):
        self._lock
        last_state = self._state_dict[type]
        state_changed = last_state.state != connectivity_state.state
        TRACE('Connectivity state updated. type=%s previous=%s current=%s', type, last_state.state, connectivity_state.state)
        if state_changed:
            self._state_dict[type] = connectivity_state
            if self._is_engine_status_update_allowed():
                update = self._resolve_tray_state()
                self._set_state_as_status(update)
            elif type == _ConnectivityType.OS:
                self._set_state_as_status(connectivity_state)
            if type == _ConnectivityType.OS:
                self._connection.reconnect()
            self._report_state(type, network_state)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _resolve_tray_state(self = None):
        if len(self._state_dict) < 1:
            return ConnectivityState(ConnectivityState.UNKNOWN, _time())
        for state in None._state_dict.values():
            if state.state == ConnectivityState.DISCONNECTED:
                
                return None, state
            return ConnectivityState(ConnectivityState.CONNECTED, _time())

    
    def _report_state(self = None, last_updated = None, network_state = None):
        known_states = self._state_dict.values()()
        extra = self._state_dict.items()()
        extra['last_updated'] = last_updated.value
        if network_state:
            extra['network_state'] = MessageToJson(network_state)
        sanitized_extra = sanitize_event_extra_dict(extra)
        if len(set(known_states)) > 1:
            report('network-connectivity-state', event_name = 'connectivity_mismatch', extra = sanitized_extra)
            return None
        if len(known_states) > 1:
            report('network-connectivity-state', event_name = 'connectivity_match', extra = sanitized_extra)
            return None
        return (lambda .0: pass# WARNING: Decompyle incomplete
)

    
    def last_os_disconnected_ts(self = None):
        state = self._state_dict.get(_ConnectivityType.OS)
    # WARNING: Decompyle incomplete

    
    def connectivity_states(self = None):
        self._lock
        None(None, None)
        return 
        with None:
            if not (lambda .0: pass# WARNING: Decompyle incomplete
), self._state_dict.items()():
                pass



def _engine_state_to_connectivity_state(engine_network_state = None):
    state = ConnectivityState.CONNECTED
    for failure in engine_network_state.failures:
        if failure.failure_kind in STATUS_CHANGING_FAILURE_KINDS:
            state = ConnectivityState.DISCONNECTED
        else:
            state = IGNORED_CONNECTION_STATE
        return ConnectivityState(state, _time())


def setup_engine_connectivity_watch(connectivity_change_handler = None, engine = None, account = None):
    pass
# WARNING: Decompyle incomplete

