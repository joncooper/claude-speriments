# Source Generated with Decompyle++
# File: asset_cache_db.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import sqlite3
import time
from contextlib import contextmanager
from typing import Any, Iterator, List, Optional, Text
from dropbox.client.features.previews.model.asset_cache.url_asset_table import URLAssetRecord, URLAssetTable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.sqlite3_definitions import SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor, VersionedSqlite3Cache
from dropbox.trace import TRACE

class AssetCacheDB(VersionedSqlite3Cache):
    pass
# WARNING: Decompyle incomplete

