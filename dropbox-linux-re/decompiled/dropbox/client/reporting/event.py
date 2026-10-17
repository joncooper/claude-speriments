# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)

import collections
import json
import random as insecure_random
import threading
from time import time as _time
from typing import Any, Callable, Deque, Dict, List, Optional, Text, Tuple, Union
from apex.metrics import Metric
from six import iteritems
from six.moves import zip as izip
from dropbox.account_context import deduce_account
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.logging.event_logger import AggregateEvent
from dropbox.client.reporting.request_status import RequestStatusReporter
from dropbox.client.reporting.util import AvroTypeError, get_reporting_metadata, report_amp_metrics
from dropbox.client.unlink_cookie import HOST_SECRET_KEYNAME
from dropbox.client.util import get_user_agent_dict
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import HTTP429Error, is_transient_error
from dropbox.client_typing import JSONable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import add_report_handler, AGGREGATE_TIMEOUT, flush_deferred_reports, report_aggregate_event
from dropbox.event_names import ASSISTANT_CLIENT_TRAY_EVENTS, CLICK_BUBBLE, CLICK_CONTEXT, CLICK_TRAY, CLICK_TRAY_POPUP, COLLAB_BROWSE_PERF_LOGGING_EVENT, FRESHLY_LINKED, HARMONY_EVENT, NOTIFICATIONS_EVENTS, PERF_SESSIONS_EVENT, PREFERENCES, PRO_EVENTS, RENDER_DROPBOX_FOLDER_ICON_OVERLAYS, RENDER_ICON_OVERLAYS, SEARCH_ACTIVITY_EVENTS, SHOW_BUBBLE, TRAY_MENU, TRAY_POPUP, VIEW_CONTEXT_MENU, VIEW_TOOLBAR_MENU, WIN_DRAG_AND_DROP
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_unicode
from dropbox.gui import message_sender, spawn_thread_with_name
from dropbox.native_event import AutoResetEvent
from dropbox.threading import Lock
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility
    from dropbox.sync_engine_adapter.adapter import SyncEngineReportInterface
ANALYTICS_EVENT_LOGGER_DATA_NAMES = {
    PERF_SESSIONS_EVENT,
    COLLAB_BROWSE_PERF_LOGGING_EVENT,
    ASSISTANT_CLIENT_TRAY_EVENTS,
    SEARCH_ACTIVITY_EVENTS,
    CLICK_BUBBLE,
    CLICK_CONTEXT,
    CLICK_TRAY,
    CLICK_TRAY_POPUP,
    PREFERENCES,
    FRESHLY_LINKED,
    HARMONY_EVENT,
    RENDER_DROPBOX_FOLDER_ICON_OVERLAYS,
    RENDER_ICON_OVERLAYS,
    SHOW_BUBBLE,
    TRAY_MENU,
    TRAY_POPUP,
    VIEW_CONTEXT_MENU,
    VIEW_TOOLBAR_MENU,
    WIN_DRAG_AND_DROP,
    NOTIFICATIONS_EVENTS,
    PRO_EVENTS}
ANALYTICS_EVENT_LOGGER_BUFFER_SIZE = 200

class EventReporterThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class EventReporterManager(object):
    ANALYTICS_EVENT_LOGGER_BUFFER: 'Deque[Tuple[str, Dict[str, Any]]]' = collections.deque(maxlen = ANALYTICS_EVENT_LOGGER_BUFFER_SIZE)
    
    def __init__(self = None, buildno = None, dropbox_app = None, *args, **kwargs):
        self.buildno = buildno
        self.dropbox_app = dropbox_app
        self.args = args
        self.kwargs = kwargs
        self.client_req_stat_reporter = RequestStatusReporter()
        self.lock = Lock()
        self.threads = { }
        self.conn = None
        add_report_handler(self._handle_report)
        report_aggregate_event.pre.add_handler(self._handle_report_aggregate_event)
        self._sync_engine_adapter = None
        flush_deferred_reports()

    
    def add_report_account(self = None, account = None):
        self.lock
        if account in self.threads:
            None(None, None)
            return None
    # WARNING: Decompyle incomplete

    
    def report_percentage_values_updated(self = None, timing_report_percent = None, timing_report_percent_url = None, account = ('timing_report_percent', 'int', 'timing_report_percent_url', 'Dict[Text, Any]', 'account', 'AccountInterface', 'return', 'None')):
        self.client_req_stat_reporter.report_percentage_values_updated(timing_report_percent, timing_report_percent_url, account)

    
    def remove_report_account(self = None, account = None):
        self.lock
        if account in self.threads:
            self.threads[account].signal_stop()
            self.threads[account].join()
            self.threads.pop(account)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def set_conn(self = None, conn = None):
        self.conn = conn
        for thread in self.threads.values():
            thread.set_conn(conn)
            return None

    
    def on_sync_engine_ready(self = None, sync_engine_adapter = None, account = None):
        self._sync_engine_adapter = sync_engine_adapter
        self.client_req_stat_reporter.on_sync_engine_ready(sync_engine_adapter, account)
        for thread in self.threads.values():
            thread.on_sync_engine_ready(sync_engine_adapter)
            return None

    
    def flush_in_reporting_thread(self = None):
        for thread in self.threads.values():
            thread.set_wakeup_event()
            return None

    flush_async = (lambda self = None: self.flush_events(True))()
    flush_events = (lambda self = None, force = None, bypass_chillout = message_sender(spawn_thread_with_name('FLUSH'), block = True, dont_post = (lambda : threading.current_thread().name != 'MainThread')): TRACE('Flushing events')for thread in list(self.threads.values()):
thread.flush_events(force, bypass_chillout)None)()
    
    def debug_upload_events(self = None):
        self.flush_events(force = True)

    
    def get_thread_for_account(self = None, account = None):
        if len(self.threads) == 0:
            TRACE('Creating a new event reporting thread with no account')
            self.add_report_account(None)
            return list(self.threads.values())[0]
        None.lock
        if account and account in self.threads:
            None(None, None)
            return 
        TRACE('Unable to find thread for account %r -- resorting to primary', account)
        if primary and primary in self.threads:
            None(None, None)
            return 
        TRACE('Unable to find thread for primary account, resorting to first available')
        None(None, None)
        return 
        with None:
            if not self.dropbox_app.account_manager.primary if self.dropbox_app.account_manager else None, list(self.threads.values())[0]:
                pass

    
    def _get_associated_account(self = None, kwdict = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_report(self = None, data_name = None, trace = None, **info):
        info.setdefault('ts', _time())
        account = self._get_associated_account(info)
        if 'account' in info:
            info.pop('account')
        thread = self.get_thread_for_account(account)
    # WARNING: Decompyle incomplete

    get_recent_events = (lambda cls = None: list(cls.ANALYTICS_EVENT_LOGGER_BUFFER))()
    
    def _handle_report_aggregate_event(self = None, data_name = None, data = None, ts = (None, AGGREGATE_TIMEOUT), approx_timeout = ('data_name', 'Text', 'data', 'Dict[Text, int]', 'ts', 'float', 'approx_timeout', 'float', 'metadata', 'object', 'return', 'None'), **metadata):
        pass
    # WARNING: Decompyle incomplete

    
    def report_failed_request(self = None, url = None, data = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def report_client_timing(self = None, timing_report = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete


REPORT_PERCENT_URL = {
    'subscribe': 0,
    'exception': 0,
    'send_trace': 0,
    'report_formatted_trace': 0,
    'report_events': 1,
    'client/hourly_refresh': 1 }
