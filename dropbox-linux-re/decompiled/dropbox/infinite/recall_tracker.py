# Source Generated with Decompyle++
# File: recall_tracker.pyc (Python 3.11)

from collections import deque
from typing import Callable, Deque, Dict, Optional, Set, Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.threading import Lock
RECALL_TRACKER_TIMEOUT_SEC = 3600

class RecallTracker(object):
    
    def __init__(self = None, sync_engine_adapter = None):
        self._sync_engine_adapter = sync_engine_adapter
        self._request_id = 0
        self._account_to_request_ids = { }
        self._path_to_request_ids = { }
        self._request_id_to_request = { }
        self._prune_queue = deque()
        self._on_sync_completed_token = None
        self._lock = Lock()

    
    def recall_path(self = None, account = None, local_path = None, callback = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'callback', 'Callable[[], None]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _on_sync_completed_summary(self = None, sync_summary = None):
        self._lock
        self._prune_requests()
        for synced_file in sync_summary.recent_sync_completions:
            if not synced_file.state.is_placeholder:
                lowered_local_path = synced_file.state.local_path.db_lower().to_unicode()
                if lowered_local_path in self._path_to_request_ids:
                    recalled_request_ids = self._path_to_request_ids[lowered_local_path].copy()
                    self._on_recalled(recalled_request_ids)
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def _on_recalled(self = None, request_ids = None):
        for request_id in request_ids:
            callback = self._request_id_to_request[request_id][2]
            callback()
        except Exception:
            report_exception(severity = Severity.DEBUG, component = DesktopComponent.INFINITE)
        self._remove_request(request_id)
        continue

    
    def _prune_requests(self = None):
        current_monotonic_time = get_monotonic_time_seconds()
    # WARNING: Decompyle incomplete

    
    def _add_request(self = None, account = None, local_path = None, callback = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'callback', 'Callable[[], None]', 'return', 'None')):
        request_id = self._request_id
        if account not in self._account_to_request_ids:
            set() = self, self._request_id += 1, ._request_id
            nucleus_api = self._sync_engine_adapter.nucleus_api(account)
            if nucleus_api:
                self._on_sync_completed_token = nucleus_api.on_sync_completed_summary(self._on_sync_completed_summary)
        u_local_path = Text(local_path)
        if u_local_path not in self._path_to_request_ids:
            self._path_to_request_ids[u_local_path] = set()
        self._account_to_request_ids[account].add(request_id)
        self._path_to_request_ids[u_local_path].add(request_id)
        self._request_id_to_request[request_id] = (account, local_path, callback)
        self._prune_queue.append((get_monotonic_time_seconds(), request_id))

    
    def _remove_request(self = None, request_id = None):
        (account, local_path, _) = self._request_id_to_request[request_id]
        self._account_to_request_ids[account].remove(request_id)
    # WARNING: Decompyle incomplete


