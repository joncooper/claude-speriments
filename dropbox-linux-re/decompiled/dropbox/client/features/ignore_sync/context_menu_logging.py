# Source Generated with Decompyle++
# File: context_menu_logging.pyc (Python 3.11)

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional, Tuple
from uuid import uuid4
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.event import report

class IgnoreSyncEventType(Enum):
    IGNORE_SHOWN = 'ignore_shown'
    UNIGNORE_SHOWN = 'unignore_shown'
    IGNORE_CLICKED = 'ignore_clicked'
    UNIGNORE_CLICKED = 'unignore_clicked'
    IGNORE_FAILED_CLOUD_FILES = 'ignore_failed_cloud_files'
    IGNORE_FAILED_PLACEHOLDERS = 'ignore_failed_placeholders'
    IGNORE_CONFIRMATION_SUPPRESSED = 'ignore_confirmation_suppressed'
    IGNORE_CONFIRMATION_CONFIRMED = 'ignore_confirmation_confirmed'
    IGNORE_CONFIRMATION_CANCELLED = 'ignore_confirmation_cancelled'
    IGNORE_CONFIRMATION_SKIPPED = 'ignore_confirmation_skipped'
    IGNORE_FAILED_ENGINE_REQUEST = 'ignore_failed_engine_request'
    UNIGNORE_FAILED_ENGINE_REQUEST = 'unignore_failed_engine_request'


class IgnoreSyncEventKeys:
    PATH = 'path'
    CORRELATION_ID = 'correlation_id'
    VERB = 'verb'
    IS_IN_DEVICE_FOLDER = 'is_in_device_folder'
    IS_DEVICE_FOLDER = 'is_device_folder'
    IS_DIR = 'path_is_dir'
    IS_CLOUD_DOC = 'path_is_cloud_doc'
    PATH_SYNC_STATUS = 'path_sync_status'

_TABLE_NAME = 'ignore-sync-context-menu'
_EXTRA_FIELD_NAME = 'extra'
_SCHEMA_FIELD_KEYS = frozenset([
    IgnoreSyncEventKeys.PATH,
    IgnoreSyncEventKeys.CORRELATION_ID,
    IgnoreSyncEventKeys.VERB])

def new_correlation_id():
    return uuid4().hex

EventContext = <NODE:12>()

def _split_schema_fields_and_extra(info = None):
    schema_fields = { }
    extra = { }
    explicit_extra = info.get(_EXTRA_FIELD_NAME)
# WARNING: Decompyle incomplete


def report_ignore_sync_event(account = None, event_type = None, **info):
    (schema_fields, extra) = _split_schema_fields_and_extra(info)
# WARNING: Decompyle incomplete


def report_ignore_sync_event_from_context(context = None, event_type = None):
    pass
# WARNING: Decompyle incomplete

