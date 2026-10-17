# Source Generated with Decompyle++
# File: databases.pyc (Python 3.11)

from __future__ import absolute_import
import binascii
import os
import shutil
from contextlib import closing, contextmanager
from os import replace as _replace
from typing import Any, Iterator, List, Optional, Text, Union
from build_number import dropbox_version
from dropbox import fileutils
from dropbox.assertions import assert_
from dropbox.client.config import ConfigDict
from dropbox.client.configuration.context_aware_config_dict import ContextAwareConfigDict
from dropbox.client.constants import AppDataPaths
from dropbox.client.fenix.sqlite3.sqlite_constants import TYPESCRIPT_SQLITE_DATABASE_FILENAMES
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_remove, tempfilename
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.platform import IS_WINDOWS
from dropbox.sqlite3_helpers import MISNAMED_ENCRYPTED_DATABASES
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility
    from dropbox.client.mapreduce import DBKeyStore
_CONFIG_ENC_FILENAME = 'config.dbx'
_FILE_CACHE_ENC_FILENAME = 'filecache.dbx'
_NUCLEUS_DB_DIRNAME = 'sync'
_NUCLEUS_FP_DB_DIRNAME = 'sync_fp'
CONFIG_SCHEMA_VERSION = 2

def delete_nucleus_dbs(database_dir = None):
    for db_name in (_NUCLEUS_DB_DIRNAME, _NUCLEUS_FP_DB_DIRNAME):
        db_dirpath = os.path.join(database_dir, db_name)
        if os.path.exists(db_dirpath):
            TRACE('Running rmtree on Nucleus sync dir %r', db_dirpath)
            shutil.rmtree(db_dirpath)
            continue
            except Exception:
                e = None
                if isinstance(e, PermissionError):
                    pass
                else:
                    report_exception(severity = Severity.WARN, component = DesktopComponent.DATABASES)
                TRACE('rmtree failed on Nucleus directory, trying listdir + deletion of individual files')
                for filename in os.listdir(db_dirpath):
                    file_path = os.path.join(db_dirpath, filename)
                    safe_remove(file_path)
                except Exception:
                    if isinstance(e, FileNotFoundError):
                        pass
                    else:
                        report_exception(severity = Severity.WARN, component = DesktopComponent.DATABASES)
                e = None
                del e
                continue
                e = None
                del e
                continue
                return None


def clear_appdata_for_unlink(clear_unlink_cookie, except_for, database_dir, clearing_secondary_appdata = (False, frozenset(), None, False)):
    pass
# WARNING: Decompyle incomplete


def cleanup_single_database(database_dir = None, db_name = None, corruptdb_key = None):
    db_path = os.path.join(database_dir, db_name)
    report_app_framework_event_restricted('cleanup_single_database', db_path = db_path, db_name = db_name)
# WARNING: Decompyle incomplete


def cleanup_corrupt_databases(database_dir = None, corruptdb_name = None, corruptdb_key = None):
    pass
# WARNING: Decompyle incomplete

new_config_file = (lambda database_dir = None, keystore = None: pass# WARNING: Decompyle incomplete
)()

def clear_appdata_without_unlink(database_dir = None):
    clear_appdata_for_unlink(except_for = {
        'hostkeys',
        'config.dbx',
        'dropbox.pid'}, database_dir = database_dir)


def reinitialize_databases(config = None, database_dir = None, key = None):
    clear_appdata_without_unlink(database_dir)
    db_config = config
    db_config.clear()
    db_config['config_schema_version'] = CONFIG_SCHEMA_VERSION
    if key:
        db_config.connection.teresa(key)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def load_dropbox_config(database_dir = None, keystore = None, app = None):
    database_dir = Text(database_dir)
    config_db_path = os.path.join(database_dir, _CONFIG_ENC_FILENAME)
    for old_db_file in (os.path.join(database_dir, 'dropbox.db'), os.path.join(database_dir, 'migrate.db')):
        safe_remove(old_db_file)
        if not os.path.exists(config_db_path):
            new_config_file(database_dir, keystore)
            TRACE('Creating new empty config file: %r', config_db_path)
            None(None, None)
        else:
            with None:
                if not None:
                    pass
    TRACE('Using Configuration %r', config_db_path)
    config = None
# WARNING: Decompyle incomplete

