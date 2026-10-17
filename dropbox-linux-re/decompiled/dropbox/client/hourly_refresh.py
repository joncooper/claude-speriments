# Source Generated with Decompyle++
# File: hourly_refresh.pyc (Python 3.11)

import functools
import os
import time
from typing import Any, Callable, Dict, Iterable, Optional, Text
from build_number import dropbox_version, is_frozen
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client.ping import DualPingSource, ping_and_report
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.updatemanager import UpdateManager
from dropbox.client_api.exceptions import HTTP429Error, is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import get_jittered_seconds
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.infinite import infinite_exposed
from dropbox.infinite.blacklist import InfiniteModuleBlacklist
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.list_legacy.out_of_band_response import OutOfBandResponse, OutOfBandResponseSource
from dropbox.metrics.windows_package_reporter import WindowsPackageReporter
from dropbox.model.types import FileId
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.exceptions import NamespaceNotMountedError
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties, OutsideDropboxException
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.session_metadata.interface import LegacySessionMetadata

class _HourlyRefreshThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

HourlyRefreshThread = db_thread(_HourlyRefreshThreadImpl)
on_refresh_thread = HourlyRefreshThread.on_queue

class HourlyRefreshController(object):
    _BOOT_WAIT_TIMEOUT = 60
    
    def __init__(self, app, account_manager, gandalf = None, status_controller = None, sync_engine_adapter = None, session_metadata = ('app', 'DropboxApplication', 'account_manager', 'AccountManagerInterface', 'gandalf', 'Gandalf', 'status_controller', 'StatusControllerInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'session_metadata', 'LegacySessionMetadata', 'return', 'None')):
        self._app = app
        self._account_manager = account_manager
        self._gandalf = gandalf
        self._status_controller = status_controller
        self._sync_engine_adapter = sync_engine_adapter
        self._session_metadata = session_metadata
        self._initial_call = True
        self._next_update_manager_ping = time.time() + get_jittered_seconds(hours = 1)
        self._windows_package_reporter = WindowsPackageReporter(app)
        self._refresh_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_refresh_callback = self._refresh_callbacks.add_handler
        self.remove_refresh_callback = self._refresh_callbacks.remove_handler
        self._init_refresh_thread()

    
    def _init_refresh_thread(self = None):
        self._thread = HourlyRefreshThread()
        self._thread.start()

    
    def _handle_hourly_refresh(self = None, account = None, hourly_refresh_response = None):
        self._session_metadata.handle_info_update(account, hourly_refresh_response)
        if 'infinite_recall_blacklist' in hourly_refresh_response and account.is_primary:
            self._app.handle_infinite_recall_blacklist(hourly_refresh_response['infinite_recall_blacklist'])
        if 'infinite_module_blacklist' in hourly_refresh_response and account.is_primary:
            blacklist = InfiniteModuleBlacklist(hourly_refresh_response['infinite_module_blacklist'].get('black_list'))
            blacklist.store_blacklist_in_user_config(self._app.config_manager.local_config(account))
        if account.is_primary:
            supported_exts = hourly_refresh_response['thumbnail_supported_extensions'] if 'thumbnail_supported_extensions' in hourly_refresh_response else None
            self._app.handle_supported_thumbnail_extensions(supported_exts)
    # WARNING: Decompyle incomplete

    
    def _do_refresh(self = None, one_time = None):
        pass
    # WARNING: Decompyle incomplete

    start_refresh = (lambda self = None, one_time = None: TRACE('Hourly refresh starting.')self._do_refresh(one_time))()

