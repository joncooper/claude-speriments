# Source Generated with Decompyle++
# File: adapter.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import ContextManager, FrozenSet, List, Optional, Text, Tuple
from classic_client.callback_processor import CallbackProcessor
from thin_client.base import NucleusThinClient
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.proto.nucleus.sync_engine_pb2 import NetworkConfig
NUCLEUS_REPORT_QUEUE_STATS_JOB = 'nucleus_report_queue_stats'
NUCLEUS_REPORT_QUEUE_STATS_PERIOD_MINS = 60

class ThinAdapter(ABC):
    thin_client = (lambda self = None: pass)()
    callback_processor = (lambda self = None: pass)()
    
    def stop(self = None, timeout = None):
        return self.pause().block(timeout).result()

    
    def start(self = None):
        return self.unpause().block().result()

    pause = (lambda self = None: pass)()
    unpause = (lambda self = None: pass)()
    cleanup_engine = (lambda self = None: pass)()
    begin_dropbox_move = (lambda self = None, hidden_fileids = None: pass)()
    restart_app_and_sync_engine = (lambda self = None: pass)()
    get_bugreporter_stats = (lambda self = None: pass)()
    is_ready = (lambda self = None: pass)()
    is_migrating = (lambda self = None: pass)()
    network_settings_changed = (lambda self = None, network_config = None: pass)()

