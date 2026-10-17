# Source Generated with Decompyle++
# File: thumbnail_server.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import base64
import hashlib
import itertools
import os
from typing import Any, Callable, Dict, List, Optional, Sequence, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client_api.thumbnailer import Thumbnailer, ThumbnailSize
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.infinite import infinite_platform_supported
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.thumbnail_predictor import ThumbnailPredictor
from dropbox.infinite.thumbnail_request import ThumbnailRequest
from dropbox.infinite.util import report_infinite_event
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.threading import Lock
from dropbox.trace import TRACE, WARNING
MYPY = False
if MYPY:
    from dropbox.client.gandalf import Gandalf
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class _SmartSyncThumbnailingThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

SmartSyncThumbnailingThread = db_thread(_SmartSyncThumbnailingThreadImpl)
on_smart_sync_thumbnailing_thread = SmartSyncThumbnailingThread.on_queue
_MAX_THUMBNAIL_BATCH_SIZE = 25
_CLEANUP_INTERVAL_SECS = 300
_CACHE_LIFETIME_SECS = 300

class _ThumbnailCacheEntry:
    
    def __init__(self = None, image_data = None):
        self.image_data = image_data
        self.time_created = get_monotonic_time_seconds()
        self.num_requests = 0



class ThumbnailServer(object):
    
    def __init__(self, sync_engine_adapter = None, account_manager = None, gandalf = None, thumbnailer = ('sync_engine_adapter', 'SyncEngineAdapter', 'account_manager', 'AccountManagerInterface', 'gandalf', 'Gandalf', 'thumbnailer', 'Thumbnailer', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def setup(self = None):
        pass

    
    def teardown(self = None):
        if self._thread:
            self._thread.signal_stop()
            return None

    
    def _init_thumbnailing_thread(self = None):
        if not self._thread:
            self._inflight_requests_lock
            if not self._thread:
                self._thread = SmartSyncThumbnailingThread()
                self._thread.start()
            None(None, None)
            return None
        with None:
            if not None:
                pass
        return None

    
    def _get_item_from_cache(self = None, request = None):
        self._batching_lock
        if request in self._cache:
            cache_entry = self._cache[request]
            None(None, None)
            return 
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _add_prediction_input(self = None, account = None, request = None):
        if request.size != ThumbnailSize.W256H256:
            return None
        dirname = None.local_path.dirname
        self._batching_lock
        if dirname not in self._predictors:
            self._predictors[dirname] = ThumbnailPredictor(self._sync_engine_adapter, account, dirname, request.size, self._thumbnailer)
        self._predictors[dirname].add_request(request)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _get_predicted_requests(self = None, request = None):
        if request.size != ThumbnailSize.W256H256:
            return []
        dirname = None.local_path.dirname
    