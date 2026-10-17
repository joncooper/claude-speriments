# Source Generated with Decompyle++
# File: high_trace.pyc (Python 3.11)

import base64
import copy
import datetime
import errno
import json
import logging
import os
import re
import socket
import sys
import time
import zlib
from dataclasses import dataclass
from enum import auto, Enum
from hashlib import md5
from threading import current_thread as _current_thread
from typing import Any, Callable, cast, Dict, Iterator, List, Optional, Text, Tuple, Union
import sentry_sdk
from six import iteritems
import build_number
from build_number import dropbox_version, is_full_msix
from build_number.environment import limited_support_cookie_is_set, magic_trace_key_is_set
import dropbox
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.constants import AppDataPaths
from dropbox.client.logging import _is_temporary_log_path, _ts_from_log_path
from dropbox.client.logging.dbxlog_logger import DbxLogger
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client.quit_handlers import QuitHandlerPriorities
from dropbox.client.rtrace_api import register_rtrace_api, unregister_rtrace_api
from dropbox.client.trace_tracker import TraceTracker
from dropbox.client.unsent_exceptions import _unsent_exceptions, _unsent_exceptions_lock
from dropbox.client.util import get_update_manager_id, get_update_manager_logs
from dropbox.client_api.exceptions import DropboxServerError, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import report
from dropbox.exception.severity import Severity
from dropbox.foundation.environment import is_integration_tests
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_bytes
from dropbox.handler_registries import add_trace_handler, remove_trace_handler
from dropbox.infinite import win_crashdump_upload_enabled
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.util import report_infinite_event
from dropbox.legacy_crypto import aes_encrypt
from dropbox.legacy_crypto.dropboxy import encrypt_blob, generate_session_key, PUBLIC_KEY_TUPLE
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sqlite3_exceptions import DatabaseOrDiskFullError, DiskIOError
from dropbox.sqlite3_helpers import Cursor
from dropbox.trace import TRACE, TraceSegment, WARNING
if IS_WINDOWS:
    from dropbox.client.util.win import sample_process as sample_process_native
    from dropbox.infinite.win.service_proxy import InfiniteService, ServiceFailedToConnectError
    from dropbox.infinite.win.util import trace_recent_service_info
elif IS_MAC:
    from dropbox.client.util.mac import sample_process as sample_process_native
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility
    from dropbox.threadutils import SafeValue
report_exception = dropbox.exception.reporting.report_exception
report_bad_assumption = dropbox.exception.reporting.report_bad_assumption
NUCLEUS_READONLY_SERVER_BUCKET = 'nucleus_readonly'

class PanicParseError(Exception):
    pass


class LogUploadOrdering(Enum):
    LISTDIR = auto()
    NEWEST_FIRST = auto()

LogSourceInfo = <NODE:12>()
TraceCallback = Callable[([
    TraceSegment], None)]

def track_magic():
    if build_number.is_frozen():
        if magic_trace_key_is_set():
            WARNING('User is using DBDEV magic')
            return None
        if limited_support_cookie_is_set():
            report_bad_assumption('User is using time-limited cookie', trace_locals = False)
            return None
        return None


class _RtraceThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

RtraceThread = db_thread(_RtraceThreadImpl)
_on_rtrace_thread_returns_none = RtraceThread.on_queue_returns_none
_on_rtrace_thread_blocking = RtraceThread.on_queue_blocking
_assert_on_rtrace_thread = RtraceThread.assert_on_queue

class DropboxLog(object):
    MAX_LOGDIR_SIZE = 52428800
    UNSENT_EXCEPTION_FLUSH_INTERVAL = 900
    VERSION = 1
    EXACT_LOG_FILE_NAME_PATTERN = re.compile('([0-9]+-)?([0-9,a-f]+-)?([0-9,a-f]){8}$')
    
    def __init__(self = None, app = None, logger = None):
        self.app = app
        log_dir = DropboxLog.get_log_dir(0)
        log_source_info = LogSourceInfo(user_id = 0, host_id = 0, email = 'None')
        self.log_dirs = [
            (log_dir, log_source_info)]
        self.logger = logger
        self.next_unsent_exception_flush = None
        (self.header, self.log_key) = generate_session_key(PUBLIC_KEY_TUPLE)
        self._accounts = { }
        self.sync_engine_version_by_account = { }
        self.primary_account = None
        self.trace_tracker = None
        self.prefix = ''

    get_log_dir = (lambda instance_id = None: instance_folder = '%d' % instance_idos.path.join(AppDataPaths.dropbox_appdata_path, 'logs', instance_folder))()
    cleanup = (lambda self = None: self._report_logger_stats(self.logger.name, self.logger.get_stats()))()
    
    def _initialize_trace_tracker(self = None):
        tracker = self._get_log_tracker()
        self.trace_tracker = self.app.config_manager.get_config_value_for_account(self.primary_account, tracker.CONFIG_KEY, tracker)
        return self.trace_tracker

    
    def _get_log_tracker(self = None):
        return TraceTracker()

    
    def _update_config_with_trace_tracker(self = None):
        
        try:
            self.app.config_manager.update_config_for_account(self.primary_account, self.trace_tracker.CONFIG_KEY, self.trace_tracker)
            return None
        except (DatabaseOrDiskFullError, DiskIOError, Cursor.UnableToOpenSQLiteDatabase):
            ex = None
            TRACE('!! Unable to set trace tracker information, may send duplicate traces, cause: %r', ex)
            ex = None
            del ex
            return None
            ex = None
            del ex


    add_raw_log_dir = (lambda self = None, path = None: TRACE('Watching new directory %r', path)log_source_info = LogSourceInfo(use_current_account = True)self.log_dirs.append((path, log_source_info)))()
    
    def add_account(self = None, account = None):
        self.logger.add_redacted_value(account.host_secret, '[host secret]')
        if account:
            self._accounts[account.host_secret] = account
            if account.is_primary == self.app.mbox.is_primary:
                self.primary_account = account
                return None
            return None

    
    def remove_account(self = None, account = None):
        if account:
            self._accounts.pop(account.host_secret, None)
            self.sync_engine_version_by_account.pop(account, None)
            return None

    
    def add_redacted_value(self = None, redacted_value = None, placeholder = None):
        self.logger.add_redacted_value(redacted_value, placeholder)

    
    def set_sync_engine_version(self = None, account = None, sync_engine_version = None):
        pass
    # WARNING: Decompyle incomplete

    
    def encrypt_blob(self = None, blob = None, timestamp = None):
        return encrypt_blob(self.header, self.log_key, self.VERSION, int(timestamp), blob)

    
    def sample_process(self = None):
        if IS_LINUX:
            return None
        ret = sample_process_native(os.path.join(self.app.appdata_path, 's%08x' % int(time.time())))
        if not ret:
            TRACE('Error sampling process')
            return None
        ret = base64.b64encode(zlib.compress(ret))
        for j in range(0, len(ret), 200):
            TRACE('SAMPLE:: %s', ret[j:j + 200])
            return None

    
    def report_trace_stats(self = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _report_logger_stats(self = None, name = None, stats = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_log_files(self = None, *, load_contents, ordering, include_in_progress):
        pass
    # WARNING: Decompyle incomplete

    
    def get_all_log_files_newest_to_oldest(self = None, include_in_progress = None):
        pass
    # WARNING: Decompyle incomplete

    flush = (lambda self = None, force = None: self.logger.flush(force)if self._should_send_traces():
logdir_size = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.get_all_log_files_newest_to_oldest()())
            if logdir_size > self.MAX_LOGDIR_SIZE:
                self.send_all(ordering = LogUploadOrdering.NEWEST_FIRST if force else None)
                return None
            return sum
)()
    send_traces_immediately = (lambda self = None, trace_start = None, encrypted_traces = _assert_on_rtrace_thread(), error_msg = (None,): WARNING('%s; sending traces immediately', error_msg)if not self._should_send_traces():
length = len(encrypted_traces)WARNING('Discarding traces because connection is not initialized or this is run-box! %d encrypted bytes lost.', length)self.report_trace_stats(log_ts = trace_start, written_bytes = length, deleted_bytes = length)Nonetry:
if self.primary_account:
account = self.primary_accountelse:
account = Account.get_dummy_account()WARNING('Sending traces with dummy account: account=%r', account)log_source_info = LogSourceInfo(user_id = account.uid, host_id = account.host_int, email = account.email)self.send_to_server(account, trace_start, encrypted_traces, log_source_info)length = len(encrypted_traces)self.report_trace_stats(log_ts = trace_start, written_bytes = length, sent_bytes = length)Noneexcept (socket.error, DropboxServerError, TransientNetworkError):
report_exception(severity = Severity.TRACE, component = DesktopComponent.TRACES)Noneexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.TRACES)None)()
    
    def report_unsent_exceptions(self = None, force = None):
        if force and self.next_unsent_exception_flush and self.next_unsent_exception_flush > time.time():
            return None
        self.next_unsent_exception_flush = time.time() + self.UNSENT_EXCEPTION_FLUSH_INTERVAL
        if not getattr(self.app, 'conn', None):
            return None
        sentry_sdk.get_client().flush()
        _unsent_exceptions_lock()
        to_report = iteritems(_unsent_exceptions)()
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def _trim_exceptions_dir(self = None, older_than = None):
        exc_dir = os.path.join(AppDataPaths.dropbox_appdata_path, 'exceptions')
        
        try:
            entries = os.listdir(exc_dir)
        except FileNotFoundError:
            return None
            except OSError:
                report_exception(severity = Severity.TRACE, component = DesktopComponent.TRACES)
                return None

        for exc_file in entries:
            exc_file = os.path.join(exc_dir, exc_file)
            if os.path.splitext(exc_file)[1] != '.exc':
                continue
            mtime = os.stat(exc_file).st_mtime
        except OSError:
            report_exception(severity = Severity.WARN, component = DesktopComponent.TRACES)
            continue
        if mtime < older_than:
            os.remove(exc_file)
            TRACE('Removed old exception %r %r', mtime, exc_file)
            continue
            except PermissionError:
                report_exception(severity = Severity.TRACE, component = DesktopComponent.TRACES)
                continue
            except OSError:
                report_exception(severity = Severity.WARN, component = DesktopComponent.TRACES)
                continue
        continue

    
    def send_finder_crashes(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def send_fileproviderd_crashes(self = None):
        pass
    # WARNING: Decompyle incomplete

    send_kernel_panics = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def report_watchdog_failure(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _trim_log_dir(self = None, older_than = None):
        total_log_size = 0
        for fn, _, st in self.get_all_log_files_newest_to_oldest(include_in_progress = True):
            should_remove = False
            ts = None
            ts = _ts_from_log_path(fn)
        except ValueError:
            pass
        if total_log_size + st.st_size > self.MAX_LOGDIR_SIZE:
            should_remove = True
            TRACE('Log directory size exceeded; deleting log file %r of size %d', fn, st.st_size)
    # WARNING: Decompyle incomplete

    
    def _should_send_traces(self = None):
        if not self.app.conn:
            return False

    
    def logs_to_process_full(self = None, *, ordering):
        return cast('Iterator[Tuple[Text, LogSourceInfo, bytes]]', self.get_log_files(load_contents = True, ordering = ordering, include_in_progress = False))

    
    def logs_to_process_paths_only(self = None, *, ordering, include_in_progress):
        return cast('Iterator[Tuple[Text, LogSourceInfo]]', self.get_log_files(load_contents = False, ordering = ordering, include_in_progress = include_in_progress))

    send_all = (lambda self = None, *, ordering: self.logger.flush(force = True)if not self._should_send_traces():
Noneif None.primary_account:
account = self.primary_accountelse:
account = Account.get_dummy_account()WARNING('Sending traces with dummy account: account=%r', account)if not only_upload_with_host_secret and account.host_secret:
TRACE("Not uploading traces because there's no host secret associated with the primary account")NoneNone.send_finder_crashes()self.send_fileproviderd_crashes()total_size = 0if not self.app.gandalf and self.app.gandalf.allows('desktop-client-cap-traces', account = self.primary_account) and self.trace_tracker and self._initialize_trace_tracker():
WARNING('Not tracking trace sizes. Account not set but gandalf was before send trace request.')try:
if server_request and self.trace_tracker and self.trace_tracker.over_trace_quota():
TRACE('Over sent trace quota. Not sending additional traces.')self.report_trace_stats(over_quota = True)self._trim_log_dir(older_than = latest)if self.trace_tracker:
remaining_log_files = (lambda .0: [ path[0] for path in .0 ])(self.logs_to_process_paths_only()())
                    self.trace_tracker.prune_deleted_traces(remaining_log_files)
                self._report_logger_stats(self.logger.name, self.logger.get_stats())
                return None
            for fn, log_source_info, contents in None.logs_to_process_full(ordering = ordering):
                ts = _ts_from_log_path(fn)
                
                try:
                    pass
                except ValueError:
                    report_bad_assumption('Got weird trace file named %r' % fn)
                    
                    try:
                        continue
                        
                        try:
                            if latest and latest >= ts:
                                continue
                            if self.trace_tracker and self.trace_tracker.already_sent(fn):
                                TRACE('Not sending already sent trace %d (%r)', ts, fn)
                                self.report_trace_stats(log_ts = ts, avoided_duplicate_bytes = len(contents))
                                os.remove(fn)
                                
                                try:
                                    pass
                                except Exception:
                                    report_exception(severity = Severity.TRACE, component = DesktopComponent.TRACES)
                                    
                                    try:
                                        pass
                                    try:
                                        continue
                                        TRACE('Sending trace %d (%r)', ts, fn)
                                        self.send_to_server(account, ts, contents, log_source_info)
                                        
                                        try:
                                            total_size += len(contents)
                                            if self.trace_tracker:
                                                self.trace_tracker.record_trace_sent(fn, len(contents))
                                                self._update_config_with_trace_tracker()
                                            self.report_trace_stats(log_ts = ts, sent_bytes = len(contents))
                                            os.remove(fn)
                                            
                                            try:
                                                continue
                                                except Exception:
                                                    report_exception(component = DesktopComponent.TRACES)
                                                    
                                                    try:
                                                        continue
                                                        
                                                        try:
                                                            except (socket.error, DropboxServerError, TransientNetworkError):
                                                                report_exception(severity = Severity.TRACE, component = DesktopComponent.TRACES)
                                                                
                                                                try:
                                                                    pass
                                                                except Exception:
                                                                    report_exception(severity = Severity.CRITICAL, component = DesktopComponent.TRACES)
                                                                    
                                                                    try:
                                                                        pass
                                                                    try:
                                                                        if send_update_manager_logs:
                                                                            total_size += self._send_update_manager_logs()
                                                                        self._trim_log_dir(older_than = latest)
                                                                        if self.trace_tracker:
                                                                            remaining_log_files = (lambda .0: [ path[0] for path in .0 ])(self.logs_to_process_paths_only()())
                                                                            self.trace_tracker.prune_deleted_traces(remaining_log_files)
                                                                        self._report_logger_stats(self.logger.name, self.logger.get_stats())
                                                                        return None
                                                                    except:
                                                                        self._trim_log_dir(older_than = latest)
                                                                        if self.trace_tracker:
                                                                            remaining_log_files = (lambda .0: [ path[0] for path in .0 ])(self.logs_to_process_paths_only()())
                                                                            self.trace_tracker.prune_deleted_traces(remaining_log_files)
                                                                        self._report_logger_stats(self.logger.name, self.logger.get_stats())












)()
    
    def send_to_server(self, account = None, ts = None, contents = None, log_source_info = ('account', 'AccountInterface', 'ts', 'float', 'contents', 'bytes', 'log_source_info', 'LogSourceInfo', 'return', 'None')):
        sync_engine_version = self.sync_engine_version_by_account.get(account, 'unknown')
        if log_source_info.use_current_account:
            user_id = account.uid if account.uid else 0
            host_id = 