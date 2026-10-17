# Source Generated with Decompyle++
# File: infinite_ui_controller.pyc (Python 3.11)

from collections import defaultdict
from typing import cast, DefaultDict, Dict, Iterable, List, Optional, Set
from six import iteritems
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client.ui.infinite.recall_event_listener import InfiniteRecallEventListener
from dropbox.exception.reporting import report_bad_assumption
from dropbox.sync_engine_boundary.infinite.recall_events import InfiniteRecallDownloadProgress, InfiniteRecallEvent, InfiniteRecallStatus
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteRecallType, InfiniteUIAccountState, InfiniteUIControllerInterface, InfiniteUIInterface, InfiniteUIRequest, InfiniteUIState
from dropbox.trace import TRACE

class InfiniteUIController(InfiniteUIControllerInterface):
    
    def __init__(self = None, recall_event_listener = None, exposed_recall_types = None):
        self._exposed_recall_types = set(exposed_recall_types)
        self.show_personal = True
        self.show_business = True
        self._infinite_ui = None
        self._account_to_recall_ids = defaultdict(set)
        self._recall_id_to_ui_request = { }
        self._unexposed_recall_ids = set()
        recall_event_listener.on_recall_added(self._add_recall)
        recall_event_listener.on_recall_removed(self._remove_recall)
        recall_event_listener.on_progress_change(self._update_progress)
        recall_event_listener.on_status_change(self._update_status)

    register_ui = (lambda self = None, infinite_ui = None: self._infinite_ui = infinite_uiself._refresh_ui())()
    get_state = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    update_merge_state = (lambda self = None, show_personal = None, show_business = on_ui_thread(block = True): self.show_personal = show_personalself.show_business = show_business)()
    _refresh_ui = (lambda self = None: if self._infinite_ui:
TRACE('Pushing state: %r', self.get_state())self._infinite_ui.update_state(self.get_state())None)()
    _add_recall = (lambda self = None, account = None, recall_id = on_ui_thread(), recall_event = ('account', 'AccountInterface', 'recall_id', 'int', 'recall_event', 'InfiniteRecallEvent', 'return', 'None'): TRACE('Received add: %r', recall_event)if recall_event.recall_type in self._exposed_recall_types:
self._account_to_recall_ids[account].add(recall_id)account = cast(Account, account)self._recall_id_to_ui_request[recall_id] = InfiniteUIRequest.from_recall_event(account, recall_event)self._refresh_ui()NoneNone._unexposed_recall_ids.add(recall_id))()
    _remove_recall = (lambda self = None, account = None, recall_id = on_ui_thread(): if recall_id in self._unexposed_recall_ids:
Noneif None not in self._account_to_recall_ids[account]:
report_bad_assumption('Got remove event for Account %r and recall_id %r, but no add detected.', account, recall_id)NoneNone._account_to_recall_ids[account].discard(recall_id)del self._recall_id_to_ui_request[recall_id]self._refresh_ui())()
    _update_progress = (lambda self = None, account = None, recall_id = on_ui_thread(), progress = ('account', 'AccountInterface', 'recall_id', 'int', 'progress', 'InfiniteRecallDownloadProgress', 'return', 'None'): if recall_id in self._unexposed_recall_ids:
Noneif None not in self._account_to_recall_ids[account]:
report_bad_assumption('Got progress update for Account %r and recall_id %r, but no add detected.', account, recall_id)Noneexisting_ui_request = None._recall_id_to_ui_request[recall_id]new_ui_request = existing_ui_request.refresh_progress(progress)self._recall_id_to_ui_request[recall_id] = new_ui_requestself._refresh_ui())()
    _update_status = (lambda self = None, account = None, recall_id = on_ui_thread(), status = ('account', 'AccountInterface', 'recall_id', 'int', 'status', 'InfiniteRecallStatus', 'return', 'None'): if recall_id in self._unexposed_recall_ids:
self._unexposed_recall_ids.remove(recall_id)Noneif None not in self._account_to_recall_ids[account]:
report_bad_assumption('Got status update for Account %r and recall_id %r, but no add detected.', account, recall_id)Noneexisting_ui_request = None._recall_id_to_ui_request[recall_id]new_ui_request = existing_ui_request.refresh_status(status)self._recall_id_to_ui_request[recall_id] = new_ui_requestself._refresh_ui())()

