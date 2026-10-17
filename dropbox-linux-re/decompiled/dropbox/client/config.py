# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

from __future__ import absolute_import
import sys
from types import TracebackType
from typing import AbstractSet, Any, Iterator, MutableMapping, Optional, Text, Tuple, Type, ValuesView
from six import iteritems, reraise, string_types
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import trace_warn_if_called_on_main_thread
from dropbox.sqlite3_exceptions import ConnectionClosedError
from dropbox.sqlite3_helpers import Cursor, from_db_type, SqliteConnectionHub, to_db_type
from dropbox.threading import RLock
from dropbox.trace import TRACE, trace_stack
DROPBOX_MOVED_TO_DIFFERENT_VOLUME_KEY = 'dropbox_moved_to_different_volume'
HIDDEN_FILEID_SET_KEY = 'hidden_fileid_set'
UC_NUCLEUS_SE_KEY = 'nucleus'
UC_NUCLEUS_SE_VALUE = 'rian'

def post_create(conn):
    conn.text_factory = Text


def DBConfig():
    '''DBConfig'''
    INSERT_STATEMENT = 'INSERT OR REPLACE INTO config VALUES (?, ?)'
    ignored_keys = []
    ignored_keys.append('hw_opengl_failed_reason')
    ignored_keys.append('tray_icon_non_electron_promotion_state')
    ignored_keys.append('tray_icon_non_electron_promotion_state_time_logged')
    ignored_keys.append('tray_icon_electron_promotion_done')
    ignored_keys.append('last_tray_webview_tab_shown_v105')
    ignored_keys.append('hw_opengl_last_state')
    
    def create_tables(self = None, force = None):
        self.execute('CREATE TABLE %sconfig (key TEXT PRIMARY KEY NOT NULL, value BLOB)' % '' if force else 'IF NOT EXISTS ')

    
    def __getitem__(self = None, key = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __setitem__(self = None, key = None, value = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __delitem__(self = None, key = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self = None):
        return self.execute('SELECT count(*) FROM config').fetchone()[0]

    
    def __contains__(self = None, key = None):
