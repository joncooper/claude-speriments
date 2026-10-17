# Source Generated with Decompyle++
# File: startup.pyc (Python 3.11)

import os
from typing import Dict, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import PAPLoggingEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.pap.events.display.start_app_pb2 import Start_App
from dropbox.pap.events.enums.app_start_failure_reason_pb2 import AppStartFailureReason
from dropbox.proto.pap.event_state_pb2 import EventState
from dropbox.timed_event import StartupAnchoredTimedEvent
from dropbox.trace import debugging_features_are_enabled, TRACE
BENCHMARK_BLACKLIST_CLIENT_ARGS = [
    '/install',
    '/killdata',
    '/unlink',
    '/unlinkr',
    '/killeveryone',
    '/openext',
    '/restartexplorer',
    '/self_uninstall',
    '/testrun',
    '/uninstall',
    '/readonlyhelper',
    '/removedomains']
STARTUP_EVENT_RENDERED_TRAY = 'rendered_tray'
STARTUP_EVENT_LOAD_ACCOUNTS = 'begin_loading_accounts'
STARTUP_EVENT_CALL_REGISTER_HOST = 'call_register_host'
STARTUP_EVENT_REGISTER_HOST_RESPONDED = 'register_host_responded'
STARTUP_EVENT_ACCOUNTS_LOADED = 'account_loaded'
STARTUP_EVENT_SETUP_WIZARD_APPEARED = 'setup_wizard_appeared'
STARTUP_EVENT_SYNC_ENGINE_INITIALIZING = 'sync_engine_initializing'
STARTUP_EVENT_SYNC_ENGINE_INITIALIZED = 'sync_engine_initialized'
STARTUP_EVENT_CALL_INITIAL_LIST = 'initial_list_call'
STARTUP_EVENT_INITIAL_LIST_RESPONDED = 'initial_list_responded'
STARTUP_EVENT_FINISHED_COMPONENT_LOADING = 'loaded_startup_components'
STARTUP_EVENT_TRAY_READY_TO_LOAD_CONTENT = 'tray_ready_to_load_content'
STARTUP_EVENT_APPMODEL_FINISHED_LOADING = 'appmodel_finished_loading'
STARTUP_EVENT_APPMODEL_READY_SIGNALED = 'appmodel_ready_signaled'
STARTUP_EVENT_TRAY_UPDATE_CONTENT = 'tray_content_update'
STARTUP_EVENT_TRAY_LOCAL_VIEW_STATE_CHANGED = 'tray_local_view_state_changed'
STARTUP_EVENT_TRAY_ASSISTANT_STATE_CHANGED = 'tray_assistant_state_changed'
STARTUP_EVENT_TRAY_CREATE_LOCAL_VIEW_CONTENT_NAVIGATE = 'tray_create_local_view_content_navigate'
STARTUP_EVENT_TRAY_CREATE_ASSISTANT_CONTENT_NAVIGATE = 'tray_create_assistant_content_navigate'
STARTUP_EVENT_APP_STARTED = 'app_started'
STARTUP_EVENT_APP_STUCK = 'app_stuck'
STARTUP_EVENT_APP_CRASHED = 'app_crashed'
STARTUP_EVENT_BOOT_FAILED_STARTUP_HIGH = 'boot_failed_startup_high'
STARTUP_EVENT_BOOT_FAILED_TO_LOAD_ACCOUNTS = 'boot_failed_to_load_accounts'
STARTUP_EVENT_BOOT_FAILED_TO_SETUP_ROOT = 'boot_failed_to_setup_root'
STARTUP_EVENT_BOOT_FAILED_TO_START_APP = 'boot_failed_to_start_app'
STARTUP_EVENT_APP_CRASHING_REPEATEDLY_DUE_TO_MOVING = 'app_crashing_repeatedly_due_to_move_failure'
STARTUP_EVENT_APP_CRASHING_REPEATEDLY_DUE_TO_FAILED_CHECK_MERGE = 'app_crashing_repeatedly_due_to_failed_check_merge'
STARTUP_EVENT_APP_STARTUP_FAILED_UNKNOWN = 'app_startup_failed_unknown'
STARTUP_EVENT_BOOT_FAILED_TO_REGISTER_HOST = 'boot_failed_to_register_host'
STARTUP_EVENT_BOOT_FAILED_TO_HANDLE_REGISTERED_HOST = 'boot_failed_to_handle_registered_host'
STARTUP_EVENT_BOOT_FAILED_TO_CREATE_KEY_STORE_AND_UNLINK_COOKIE = 'boot_failed_to_create_key_store_and_unlink_cookie'
DUMMY_STARTUP_EVENT_BOOT_FAILED = 'DUMMY_EXIT_TO_AVOID_LOGGING'
STARTUP_EVENT_TRAY_READY_CLASSIC = 'tray_ready_sync_engine_classic'
STARTUP_EVENT_TRAY_READY_NUCLEUS = 'tray_ready_nucleus'
STARTUP_EVENT_READY_STATE_HELPER_VIEW_READY = 'ready_state_helper_view_ready'
APP_STARTUP_SUCCESS_EVENTS = [
    STARTUP_EVENT_APP_STARTED]
APP_STARTUP_FAILURE_EVENTS = [
    STARTUP_EVENT_APP_STUCK,
    STARTUP_EVENT_APP_CRASHED,
    STARTUP_EVENT_BOOT_FAILED_STARTUP_HIGH,
    STARTUP_EVENT_BOOT_FAILED_TO_LOAD_ACCOUNTS,
    STARTUP_EVENT_BOOT_FAILED_TO_SETUP_ROOT,
    STARTUP_EVENT_BOOT_FAILED_TO_START_APP,
    STARTUP_EVENT_APP_CRASHING_REPEATEDLY_DUE_TO_MOVING,
    STARTUP_EVENT_APP_CRASHING_REPEATEDLY_DUE_TO_FAILED_CHECK_MERGE,
    STARTUP_EVENT_BOOT_FAILED_TO_CREATE_KEY_STORE_AND_UNLINK_COOKIE,
    STARTUP_EVENT_BOOT_FAILED_TO_HANDLE_REGISTERED_HOST,
    STARTUP_EVENT_BOOT_FAILED_TO_REGISTER_HOST,
    STARTUP_EVENT_APP_STARTUP_FAILED_UNKNOWN]

class ClientStartupBenchmarker(object):
    
    def __init__(self = None, client_args = None, **info):
        self._startup_event = StartupAnchoredTimedEvent(client_primary_linked = False, client_secondary_linked = False, client_paired = False)
        self._startup_event.update(client_launch_time = self._startup_event.start_time)
        self._did_report_startup_benchmarking_event = False
        self._client_args = client_args if client_args else []
        self._endpoint_event_name_mapping = { }
        self._endpoint_event_name_mapping = {
            'list': {
                'pre_call': STARTUP_EVENT_CALL_INITIAL_LIST,
                'post_call': STARTUP_EVENT_INITIAL_LIST_RESPONDED },
            'register_host': {
                'pre_call': STARTUP_EVENT_CALL_REGISTER_HOST,
                'post_call': STARTUP_EVENT_REGISTER_HOST_RESPONDED } }
        ClientStartupBenchmarkerPerfSession = ClientStartupBenchmarkerPerfSession
        import dropbox.client.benchmarking.startup_perf_session
        self._client_startup_benchmarker_perf_session = ClientStartupBenchmarkerPerfSession(client_args)

    app_startup_started = (lambda self = None: self._startup_event.report['client_primary_linked'])()
    app_startup_succeeded = (lambda self = None: for event in APP_STARTUP_SUCCESS_EVENTS:
if f'''primary_{event}_time''' in self._startup_event.report:
TrueFalse)()
    app_startup_failed = (lambda self = None: for event in APP_STARTUP_FAILURE_EVENTS:
if f'''primary_{event}_time''' in self._startup_event.report:
TrueFalse)()
    
    def benchmark_startup_event(self = None, event_name = None, account = None):
        self._client_startup_benchmarker_perf_session.benchmark_startup_event(event_name, account)
        if not self._is_supported_startup_event(event_name):
            return None
    # WARNING: Decompyle incomplete

    
    def benchmark_network_event(self = None, endpoint = None, is_pre_call = None, account = (True, None)):
        self._client_startup_benchmarker_perf_session.benchmark_network_event(endpoint, is_pre_call, account)
        if not self._can_report_startup_events():
            return None
        if None not in self._endpoint_event_name_mapping:
            report_bad_assumption('Attempted to retrieve an event name for an unsupported endpoint!')
            return None
        call_timing = 'pre_call' if None else 'post_call'
        event_name = self._endpoint_event_name_mapping[endpoint][call_timing]
        self.benchmark_startup_event(event_name, account)

    
    def _can_report_startup_events(self = None):
