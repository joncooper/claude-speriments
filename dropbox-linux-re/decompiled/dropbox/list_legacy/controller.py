# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import random as insecure_random
from typing import Any, Callable, Dict, Optional
from six import iteritems
from six.moves.queue import Empty, Queue
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf.base import Gandalf
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import HTTP403Error, HTTP429Error, is_transient_error, TransientErrorType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.list_legacy.out_of_band_response import OutOfBandResponse
from dropbox.sync_engine_boundary.constants import ON_LIST_VALID_KEYS
from dropbox.sync_engine_boundary.nucleus_p2p import P2PMetaDownloader
from dropbox.threading import RLock
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE

class P2PKeys:
    
    def __init__(self = None, key_map_to_refresh = None):
        self._key_map_to_refresh = key_map_to_refresh
        self._updated_key_map = { }

    
    def get_key_map_to_refresh(self = None):
        return self._key_map_to_refresh

    
    def get_updated_key_map(self = None):
        return self._updated_key_map

    
    def update_key_map(self = None, ret = None):
        for k, v in ret.items():
            if k in self._key_map_to_refresh:
                self._updated_key_map[k] = v
                self._key_map_to_refresh.pop(k)
            return None



class ListLegacyThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class ListLegacyAdapter(object):
    
    def __init__(self = None, conn = None):
        self._conn = conn
        self._instances = { }
        self._instance_lock = RLock()
        self._ready = { }

    
    def add_for_account(self = None, account = None, p2p_meta_downloader = None, gandalf = ('account', 'AccountInterface', 'p2p_meta_downloader', 'Optional[P2PMetaDownloader]', 'gandalf', 'Gandalf', 'return', 'None')):
        TRACE('Adding list legacy component for account %r', account)
        self._instance_lock
    # WARNING: Decompyle incomplete

    
    def remove_for_account(self = None, account = None, clear_state = None):
        TRACE('Removing list legacy component for account %r', account)
        self._instance_lock
        instance = self._instances.pop(account, None)
        if instance and clear_state:
            instance.stop()
        self._ready.pop(account, None)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def is_ready(self = None, account = None):
        if account in self._instances:
            pass
        return bool(self._ready.get(account))

    
    def mark_ready(self = None, account = None):
        if account in self._ready:
            self._ready[account] = True
            return None

    
    def start_refresh(self = None, account = None):
        instance = self._get_instance(account)
    # WARNING: Decompyle incomplete

    
    def add_self_removing_callback(self = None, account = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def add_list_legacy_callback(self = None, account = None, callback = None):
        instance = self._get_instance(account)
    # WARNING: Decompyle incomplete

    
    def _get_instance(self = None, account = None):
        return self._instances.get(account)

    
    def flush_for_testing(self = None):
        for instance in self._instances.values():
            instance.flush_for_testing()
            return None



class ListLegacyController(object):
    
    def __init__(self, account = None, conn = None, p2p_meta_downloader = None, gandalf = ('account', 'AccountInterface', 'conn', 'DropboxConnection', 'p2p_meta_downloader', 'Optional[P2PMetaDownloader]', 'gandalf', 'Gandalf', 'return', 'None')):
        self._account = account
        self._conn = conn
        self._gandalf = gandalf
        self._list_legacy_callbacks = Handler(recursive = False, handle_exc = report_exception, name = 'LIST_LEGACY')
        self._p2p_meta_downloader = p2p_meta_downloader
        self._thread = db_thread(ListLegacyThread)()
        self._thread.start()
    # WARNING: Decompyle incomplete

    
    def add_list_legacy_callback(self = None, callback = None, priority = None):
        self._list_legacy_callbacks.add_handler(callback, priority)

    
    def remove_list_legacy_callback(self = None, callback = None):
        self._list_legacy_callbacks.remove_handler(callback)

    
    def stop(self = None):
        self._thread.signal_stop()
        self._thread.join()

    
    def start_refresh(self = None):
        self._thread.enqueue(self._start_refresh)

    
    def get_namespace_key_map(self = None):
        if self._p2p_meta_downloader:
            return self._p2p_meta_downloader.get_namespace_key_map()

    
    def _start_refresh(self = None):
        key_map_to_refresh = self.get_namespace_key_map()
    # WARNING: Decompyle incomplete

    
    def flush_for_testing(self = None):
        self._thread.block_for_testing()


