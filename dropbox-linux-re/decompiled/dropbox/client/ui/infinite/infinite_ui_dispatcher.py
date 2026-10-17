# Source Generated with Decompyle++
# File: infinite_ui_dispatcher.pyc (Python 3.11)

from collections import defaultdict
from typing import DefaultDict, Dict, List
from six import iteritems
from recall_event_listener import InfiniteRecallEventListener
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.recall_events import InfiniteRecallEvent
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIDispatcherInterface

class InfiniteUIDispatcher(InfiniteUIDispatcherInterface):
    
    def __init__(self = None, recall_event_listener = None, sync_engine_adapter = None):
        self._sync_engine_adapter = sync_engine_adapter
        self._recall_id_to_account = { }
        recall_event_listener.on_recall_added(self._on_recall_add)
        recall_event_listener.on_recall_removed(self._on_recall_remove)

    cancel = (lambda self = None, recall_ids = None: account_to_recall_ids = defaultdict(list)# WARNING: Decompyle incomplete
)()
    _on_recall_add = (lambda self = None, account = None, recall_id = on_ui_thread(), recall_event = ('account', 'AccountInterface', 'recall_id', 'int', 'recall_event', 'InfiniteRecallEvent', 'return', 'None'): self._recall_id_to_account[recall_id] = account)()
    _on_recall_remove = (lambda self = None, account = None, recall_id = on_ui_thread(): if recall_id not in self._recall_id_to_account:
report_bad_assumption('Got a remove for recall with recall_id %r without an earlier add.', recall_id)Noneif None != self._recall_id_to_account[recall_id]:
report_bad_assumption('Got a remove for recall with recall_id %r and Account %r, but added with Account %r', recall_id, account, self._recall_id_to_account[recall_id])del self._recall_id_to_account[recall_id])()

