# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from enum import StrEnum, unique
from typing import Any, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.logging_helpers import non_pii_extras
from dropbox.client.features.cloud_files_migration.constants import CLOUD_FILES_MIGRATION_EVENT_TABLE
from dropbox.event import report, sanitize_event_extra_dict
CloudFilesMigrationExtraKeys = <NODE:12>()
CloudFilesMigrationEvent = <NODE:12>()
CloudFilesMigrationSurfaceUI = <NODE:12>()

def _report_event(account = unique, event_name = unique, session_id = unique, action_surface = (None,), **extras):
    if account:
        extras[CloudFilesMigrationExtraKeys.IS_PAIRED.value] = False
        extras[CloudFilesMigrationExtraKeys.IS_PRIMARY.value] = account.is_primary
        extras[CloudFilesMigrationExtraKeys.PAIRED_ID.value] = None
    no_pii_extras = sanitize_event_extra_dict(non_pii_extras(extras))
    report(CLOUD_FILES_MIGRATION_EVENT_TABLE, account = account, event_name = event_name, feature_session_id = session_id, action_surface = action_surface, extra = no_pii_extras)


class CloudFilesMigrationLogger:
    report_event = (lambda account = None, event = None, session_id = staticmethod: pass# WARNING: Decompyle incomplete
)()
    report_ui_event = (lambda account = None, event = None, session_id = staticmethod, action_surface = (None,): pass# WARNING: Decompyle incomplete
)()

