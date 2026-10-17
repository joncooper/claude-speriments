# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import time
from typing import Any, Callable, Dict, Optional, Text
from  import FileViewWatcher
from dropbox.callbacks import Handler
from dropbox.client.authentication.manager import Account
from dropbox.client.features.octave.gating import desktop_octave_enabled_from_gandalf
from dropbox.client.file_view_watcher.interrupt_counter import InterruptCounter
from dropbox.client.file_view_watcher.xpc_listener import ActivityProviderListener, OCTAVE_XPC_SERVICE_NAME
from dropbox.client.gandalf import Gandalf
from dropbox.client.message_queue import MessageQueueThread
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_bad_assumption
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
if IS_MAC:
    from macffi.xpc import XPCClient, XPCMessage
FILE_VIEW_WATCHER_LOG_PREFIX = 'FILE VIEW WATCHER'

class _FileViewWatcherMacProcessingThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

_FileViewWatcherMacProcessingThread = db_thread(_FileViewWatcherMacProcessingThreadImpl)
on_file_view_watcher_thread = _FileViewWatcherMacProcessingThread.on_queue

class FileViewWatcherMac(ActivityProviderListener, FileViewWatcher):
    XPC_INTERRUPTION_MAX_RETRIES = 5
    DEFAULT_VIEW_WINDOW_TIME = 1800
    
    def __init__(self = None, on_crash_callback = None, gandalf = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _setup_thread(self = None):
        self._thread = _FileViewWatcherMacProcessingThread()
        self._thread.start()

    
    def _post_connect(self = None, client = None):
        for _, path in self._watched_paths.items():
            self._add_watch(client, path)
            return None

    add_account = (lambda self = None, account = None: if account.root_mount_path:
self._watched_paths[account] = account.root_mount_pathif self._octave_client:
self._add_watch(self._octave_client, account.root_mount_path)NoneNone)()
    remove_account = (lambda self = None, account = None: if account not in self._watched_paths:
report_bad_assumption('Tried to remove a path watch for an account that had no watches.')if self._octave_client:
self._remove_watch(self._octave_client, self._watched_paths[account])del self._watched_paths[account])()
    change_path_for_account = (lambda self = None, account = None, path = on_file_view_watcher_thread: if not account or path:
report_bad_assumption('Tried to change path with invalid account or path.')if account not in self._watched_paths:
report_bad_assumption('Tried to change path for account that had no watch.')old_watch = self._watched_paths[account]if self._octave_client:
self._remove_watch(self._octave_client, old_watch)self._add_watch(self._octave_client, path)self._watched_paths[account] = path)()
    receive_file_view = (lambda self = None, client = None, message = on_file_view_watcher_thread, reply = (None,): path = message.content.get('path')if isinstance(path, Text):
self._view_callbacks.run_handlers(path, time.time())NoneTRACE('%s: malformed message from %s: %r', FILE_VIEW_WATCHER_LOG_PREFIX, client.name, message))()
    _debounced_message_callback = (lambda self = None, client = None, message = on_file_view_watcher_thread, reply = (None,): message_type = message.content.get('message_type')if message_type != 'seen':
NoneNone.receive_file_view(client, message, reply))()
    add_view_callback = (lambda self = None, callback = None: self._view_callbacks.add_handler(callback))()
    remove_view_callback = (lambda self = None, callback = None: self._view_callbacks.remove_handler(callback))()
    _on_gandalf_changed = (lambda self = None: octave_enabled = desktop_octave_enabled_from_gandalf(self._gandalf)if octave_enabled == self._octave_enabled:
Noneif None:
self._octave_enabled = Trueself._octave_interruption_counter = InterruptCounter()self._octave_client = self._client_from_name(OCTAVE_XPC_SERVICE_NAME)else:
self._octave_enabled = Falseself._octave_interruption_counter = Noneself._octave_client = Noneself._octave_enabled = octave_enabled)()
    _connection_interruption_callback = (lambda self = None, client = None: interruption_counter = Nonecrash_log_process_name = Noneif client.name == OCTAVE_XPC_SERVICE_NAME and self._octave_interruption_counter:
interruption_counter = self._octave_interruption_countercrash_log_process_name = 'dropboxactivityprovider'else:
report_bad_assumption('Unknown client: %s', client.name)NoneNone._crash_callbacks.run_handlers(crash_log_process_name)interruption_counter.increment()if interruption_counter.count <= self.XPC_INTERRUPTION_MAX_RETRIES:
self._restart_xpc_service(client)Nonereport_bad_assumption('%s XPC service was interrupted too many times.', client.name))()
    
    def _restart_xpc_service(self = None, client = None):
        TRACE('Connection to %s XPC Service was interrupted, starting again.', client.name)
        if client.name == OCTAVE_XPC_SERVICE_NAME:
            self._octave_client = self._client_from_name(OCTAVE_XPC_SERVICE_NAME)
            return None


