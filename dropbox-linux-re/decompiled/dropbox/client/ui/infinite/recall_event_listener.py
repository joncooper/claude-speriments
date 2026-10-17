# Source Generated with Decompyle++
# File: recall_event_listener.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, Dict, Set
from six import iteritems
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.overrides import report_bad_assumption, report_exception
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.recall_events import InfiniteRecallDownloadProgress, InfiniteRecallEvent, InfiniteRecallStatus

class InfiniteRecallEventListener(object):
    
    def __init__(self = None, se_adapter = None):
        self._se_adapter = se_adapter
        self._account_to_recall_ids = { }
        self._recall_id_to_recall_event = { }
        self._add_callbacks = Handler(handle_exc = report_exception)
        self._progress_callbacks = Handler(handle_exc = report_exception)
        self._status_callbacks = Handler(handle_exc = report_exception)
        self._remove_callbacks = Handler(handle_exc = report_exception)

    
    def on_account_changed(self = None, account = None, change_status = None):
        if change_status == AccountChangeType.LINK:
            self.register_account(account)
            return None
        if None == AccountChangeType.REMOVE:
            self.unregister_account(account)
            return None

    on_recall_added = (lambda self = None, callback = None: self._add_callbacks.add_handler(callback)callback_args_list = []# WARNING: Decompyle incomplete
)()
    
    def on_progress_change(self = None, callback = None):
        self._progress_callbacks.add_handler(callback)

    
    def on_status_change(self = None, callback = None):
        self._status_callbacks.add_handler(callback)

    
    def on_recall_removed(self = None, callback = None):
        self._remove_callbacks.add_handler(callback)

    register_account = (lambda self = None, account = None: pass# WARNING: Decompyle incomplete
)()
    unregister_account = (lambda self = None, account = None: if account in self._account_to_recall_ids:
for recall_id in list(self._account_to_recall_ids[account]):
self._remove_recall_event(account, recall_id)del self._account_to_recall_ids[account]NoneNone)()
    process_recall_event = (lambda self = None, account = None, recall_event = on_ui_thread(): recall_id = recall_event.recall_idif recall_id not in self._recall_id_to_recall_event:
self._add_recall_event(account, recall_id, recall_event)else:
old_event = self._recall_id_to_recall_event[recall_id]self._update_recall_event(account, recall_id, old_event, recall_event)if recall_event.recall_status != InfiniteRecallStatus.ACTIVE:
self._remove_recall_event(account, recall_id)None)()
    
    def _add_recall_event(self = None, account = None, recall_id = None, recall_event = ('account', 'AccountInterface', 'recall_id', 'int', 'recall_event', 'InfiniteRecallEvent', 'return', 'None')):
        if account not in self._account_to_recall_ids:
            report_bad_assumption('Received InfiniteRecallEvent for Account %r after it was unregistered.', account)
            return None
        None._account_to_recall_ids[account].add(recall_id)
        self._recall_id_to_recall_event[recall_id] = recall_event
        self._add_callbacks.run_handlers(account, recall_id, recall_event)

    
    def _update_recall_event(self, account = None, recall_id = None, old_event = None, new_event = ('account', 'AccountInterface', 'recall_id', 'int', 'old_event', 'InfiniteRecallEvent', 'new_event', 'InfiniteRecallEvent', 'return', 'None')):
        if old_event.download_progress != new_event.download_progress:
            self._progress_callbacks.run_handlers(account, recall_id, new_event.download_progress)
        if old_event.recall_status != new_event.recall_status:
            self._status_callbacks.run_handlers(account, recall_id, new_event.recall_status)
        self._recall_id_to_recall_event[recall_id] = new_event

    
    def _remove_recall_event(self = None, account = None, recall_id = None):
        if account not in self._account_to_recall_ids:
            report_bad_assumption('Removing an InfiniteRecallEvent for Account %r after it was unregistered.', account)
            return None
        None._account_to_recall_ids[account].remove(recall_id)
        del self._recall_id_to_recall_event[recall_id]
        self._remove_callbacks.run_handlers(account, recall_id)


