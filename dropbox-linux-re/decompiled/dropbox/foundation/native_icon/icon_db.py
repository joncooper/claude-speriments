# Source Generated with Decompyle++
# File: icon_db.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import sqlite3
from contextlib import contextmanager
from time import time as _time
from typing import Any, Iterator, List, Optional, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.native_icon.ext_icon_table import ExtensionIconRecord, ExtensionIconTable
from dropbox.foundation.native_icon.folder_icon_table import FolderIconRecord, FolderIconTable
from dropbox.foundation.native_icon.path_icon_table import PathIconRecord, PathIconTable
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.sqlite3_definitions import SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor, locked_and_handled_3_default_return_none, locked_and_handled_4_default_return_none, locked_and_handled_5_default_return_none, VersionedSqlite3Cache
from dropbox.trace import TRACE
_30_DAYS_IN_SECONDS = 2592000
_MAX_ENTRIES = 1000
ENTRY_DELETE_COUNT = 100

def format_key_with_size(unformatted_key = None, size = None):
    return unformatted_key.lower() + '_' + Text(size)


class IconDB(VersionedSqlite3Cache):
    pass
# WARNING: Decompyle incomplete

