# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Any, Callable, Dict, Iterable, Optional
from constants import CONFIG_VERSION
from dropbox.assertions import assert_
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from sqlite_backend import SQLiteBackendCursor

def upgrade_single_version(trans, upgrade_fn, from_version = None, upgrade_version = None, final_version = None, args = ('trans', 'SQLiteBackendCursor', 'upgrade_fn', 'Callable[(Ellipsis, None)]', 'from_version', 'int', 'upgrade_version', 'int', 'final_version', 'int', 'args', 'Iterable[Any]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete

