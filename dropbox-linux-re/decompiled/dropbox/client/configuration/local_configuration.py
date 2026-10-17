# Source Generated with Decompyle++
# File: local_configuration.pyc (Python 3.11)

import contextlib
import json
import re
import threading
import unicodedata
from typing import AbstractSet, Any, Callable, cast, Dict, Iterator, List, Optional, Pattern, Set, Tuple, Union
from build_number import is_test
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict, HIDDEN_FILEID_SET_KEY
from dropbox.client.configuration.interface import ConcurrentConfigurationEditError, LocalConfigurationInterface
from dropbox.client.configuration.utils import DEFAULT_PREFERENCES, historical_key_migration, proxy_migration, type_safety_migration, unicode_migration
from dropbox.client.constants import AppDataPaths, LOCAL_FORM
from dropbox.client.databases import load_dropbox_config
from dropbox.client.deprecation import DEPRECATED_ALERT_SHOWN_CONFIG_KEY
from dropbox.client.high_trace import add_redacted_trace_value
from dropbox.client.mapreduce import DBKeyStore
from dropbox.client.unlink_cookie import HOST_SECRET_KEYNAME, read_unlink_cookie, write_unlink_cookie
from dropbox.client.util import safe_to_str
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.selective_sync_by_path_interface import FileIdRRServerPaths
from dropbox.threading import Lock, RLock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility
    from dropbox.model.types import FileId

def is_sensitive(key_name = None):
