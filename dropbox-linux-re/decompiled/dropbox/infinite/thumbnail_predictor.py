# Source Generated with Decompyle++
# File: thumbnail_predictor.pyc (Python 3.11)

import math
import os
import time
from operator import attrgetter
from typing import Iterable, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client_api.thumbnailer import Thumbnailer, ThumbnailSize
from dropbox.infinite.thumbnail_request import ThumbnailRequest
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.shared.util import db_lower
from dropbox.sync_engine_boundary.types import FileTypeFilter
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.shared.local_path import LocalPath
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class _MissingRequestFilename(Exception):
    pass


class _PlaceholderDirEntry:
    __slots__ = [
        'lc_filename',
        'filename',
        'mtime',
        'size',
        'prev_predicted']
    
    def __init__(self = None, filename = None, mtime = None, size = ('filename', 'Text', 'mtime', 'int', 'size', 'int', 'return', 'None')):
        self.lc_filename = db_lower(filename)
        self.filename = filename
        self.mtime = mtime
        self.size = size
        self.prev_predicted = False

    
    def __repr__(self):
        return '_PlaceholderDirEntry - lc_filename: {}, filename: {}: mtime: {}, size: {}, prev_predicted: {}'.format(self.lc_filename, self.filename, self.mtime, self.size, self.prev_predicted)



class ThumbnailPredictor:
    MAX_PREDICTIONS = 50
    
    def __init__(self, sync_engine_adapter, account = None, dirname = None, size = None, thumbnailer = ('sync_engine_adapter', 'SyncEngineAdapter', 'account', 'AccountInterface', 'dirname', 'LocalPath', 'size', 'ThumbnailSize', 'thumbnailer', 'Thumbnailer', 'return', 'None')):
        self._sync_engine_adapter = sync_engine_adapter
        self._account = account
        self._dirname = dirname
        self._request_log = []
        self._dir_ents = None
        self.last_access_time = get_monotonic_time_seconds()
        self._size = size
        self._thumbnailer = thumbnailer

    
    def add_request(self = None, request = None):
        TRACE('Adding request to prediction input: %r', request)
    # WARNING: Decompyle incomplete

    
    def _get_directory_listing(self = None, previous_dir_ents = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_recently_requested_lc_filenames(self = None):
        return self._request_log()

    
    def _get_most_recently_requested_lc_filename(self = None):
        return self._get_recently_requested_lc_filenames()[0]

    
    def _sort_directory_listing(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_predictions_around_index(self = None, index = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_predictions_internal(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_predictions(self = None):
        self.last_access_time = get_monotonic_time_seconds()
    # WARNING: Decompyle incomplete


