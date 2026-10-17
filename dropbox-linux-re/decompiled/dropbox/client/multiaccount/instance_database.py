# Source Generated with Decompyle++
# File: instance_database.pyc (Python 3.11)

from __future__ import absolute_import
import os
from collections import defaultdict
from pprint import pformat
from typing import Any, List, Optional, Text
from build_number.features import feature_enabled
from dropbox.assertions import assert_
from dropbox.client.constants import AppDataPaths
from dropbox.client.high_trace import add_redacted_trace_value
from dropbox.client.mapreduce import DBKeyStore
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.fileutils import safe_remove
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.functions import synchronized
from dropbox.platform import IS_WINDOWS
from dropbox.sqlite3_helpers import dict_like_row, from_db_type, locked_and_handled, to_db_type, VersionedSqlite3Cache
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.keystore.keystore_win32 import migrate_config_registry_to_appdata, migrate_instances_registry_to_appdata, remove_registry_keys

class UnknownInstanceDBVersionError(Exception):
    pass


class InstanceDB(VersionedSqlite3Cache):
    pass
# WARNING: Decompyle incomplete


def _instance_db_row_text_factory(conn):
    conn.text_factory = Text
    conn.row_factory = dict_like_row


class InstanceConfig(object):
    _INSTANCE_DB_FILENAME = 'instance.dbx'
    
    def __init__(self, app, directory, test_downgrade_version = (None, None)):
