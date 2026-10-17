# Source Generated with Decompyle++
# File: db_exception.pyc (Python 3.11)

from __future__ import absolute_import
from types import TracebackType
from typing import Any, Optional
from dropbox.exception.reporting import report_bad_assumption
from dropbox.sqlite3_helpers import is_corrupted_db_exception
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
NEED_REBUILD_TABLES = [
    'file_journal',
    'config',
    'block_cache']

def handle_corrupted_db(app = None, exc_type = None, exc_value = None, exc_tb = ('app', 'DropboxApplication', 'exc_type', 'type', 'exc_value', 'BaseException', 'exc_tb', 'TracebackType', 'kw', 'Any', 'return', 'None'), **kw):
    pass
# WARNING: Decompyle incomplete

