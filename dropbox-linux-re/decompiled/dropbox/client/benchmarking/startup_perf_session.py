# Source Generated with Decompyle++
# File: startup_perf_session.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import time
from typing import Dict, List, Optional
import psutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.benchmarking.startup import BENCHMARK_BLACKLIST_CLIENT_ARGS, STARTUP_EVENT_CALL_INITIAL_LIST, STARTUP_EVENT_CALL_REGISTER_HOST, STARTUP_EVENT_FINISHED_COMPONENT_LOADING, STARTUP_EVENT_INITIAL_LIST_RESPONDED, STARTUP_EVENT_REGISTER_HOST_RESPONDED, STARTUP_EVENT_SETUP_WIZARD_APPEARED, STARTUP_EVENT_SYNC_ENGINE_INITIALIZED, STARTUP_EVENT_SYNC_ENGINE_INITIALIZING, STARTUP_EVENT_TRAY_ASSISTANT_STATE_CHANGED
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.performance import CheckpointBehavior, OnDupe, PerfSession
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.trace import debugging_features_are_enabled, TRACE

class ClientStartupBenchmarkerPerfSession:
    
    def __init__(self = None, client_args = None, **info):
        self._client_primary_linked = False
        self._client_secondary_linked = False
        self._client_paired = False
        self._client_ui_ready = True
        self._client_args = client_args if client_args else []
        self._system_uptime_seconds = 0
        self._has_blacklisted_args = False
        for arg in self._client_args:
            if arg in BENCHMARK_BLACKLIST_CLIENT_ARGS:
                self._has_blacklisted_args = True
            
            self._startup_perf_session = None
            if not self._has_blacklisted_args:
                self._startup_perf_session = PerfSession.create('dropbox_startup', self._get_startup_scenario(), log_to_amp_namespace = PerfSessionAmpLoggingNamespace.DESKTOP_PERFORMANCE)
        self._endpoint_event_name_mapping = { }
        self._endpoint_event_name_mapping = {
            'list': {
                'pre_call': STARTUP_EVENT_CALL_INITIAL_LIST,
                'post_call': STARTUP_EVENT_INITIAL_LIST_RESPONDED },
            'register_host': {
                'pre_call': STARTUP_EVENT_CALL_REGISTER_HOST,
                'post_call': STARTUP_EVENT_REGISTER_HOST_RESPONDED } }

    
    def _get_startup_scenario(self = None):
        UNKNOWN = 'unknown'
        MANUAL_LAUNCH = 'manual_launch'
        SYSTEM_STARTUP = 'system_startup'
        UPDATE = 'update'
        
        try:
            self._system_uptime_seconds = time.time() - psutil.boot_time()
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.INITIALIZATION)

        if '/firstrunupdate' in self._client_args or '/firstrunupdatemanual' in self._client_args:
            return UPDATE
        if None in self._client_args:
            return SYSTEM_STARTUP
        if None._system_uptime_seconds == 0:
            return UNKNOWN
        if None._system_uptime_seconds > 900:
            return MANUAL_LAUNCH

    
    def _update_extras_and_get_account_prefix(self = None, account = None):
        account_prefix = ''
        if account:
            if account.is_paired:
                self._client_paired = True
            if account.is_primary:
                account_prefix = 'primary_'
                if account.linked:
                    self._client_primary_linked = True
                else:
                    account_prefix = 'secondary_'
                    if account.linked:
                        self._client_secondary_linked = True
        return account_prefix

    
    def benchmark_startup_event(self = None, event_name = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def benchmark_network_event(self = None, endpoint = None, is_pre_call = None, account = (True, None)):
        if not self._can_report_startup_events():
            return None
        if None not in self._endpoint_event_name_mapping:
            report_bad_assumption('Attempted to retrieve an event name for an unsupported endpoint!')
            return None
        call_timing = 'pre_call' if None else 'post_call'
        event_name = self._endpoint_event_name_mapping[endpoint][call_timing]
        self.benchmark_startup_event(event_name, account)

    
    def _benchmark_complete(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _is_benchmark_complete(self = None):
        if self._startup_perf_session is not None:
            pass
        return self._startup_perf_session.ended

    
    def _can_report_startup_events(self = None):
