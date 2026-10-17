# Source Generated with Decompyle++
# File: file_provider_migration_logger.pyc (Python 3.11)

from enum import Enum, StrEnum, unique
from typing import Any, Dict, NamedTuple, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.logging_helpers import non_pii_extras
from dropbox.client.features.file_provider_migration.types import FileProviderMigrationState, StateMachineEvent
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_action_surface import FileProviderActionSurface as FileProviderActionSurfaceUI
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_migration_event import FileProviderMigrationEvent as FileProviderMigrationEventUI
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.foundation.stormcrow.machine import MachineStormcrow
FPMigrationEligibilityCheckKeys = <NODE:12>()
FPMigrationEligibilityResult = <NODE:12>()
FPMigrationTrigger = <NODE:12>()
FileProviderMigrationExtraKeys = <NODE:12>()
FileProviderMigrationEvent = <NODE:12>()

class FPLoggerReportingParams(NamedTuple):
    machine_stormcrow: 'MachineStormcrow' = 'FPLoggerReportingParams'


def build_report_event_args(migration_state = unique, account_count = unique, migration_trigger = None):
    extra = {
        FileProviderMigrationExtraKeys.PREVIOUS_STATE: str(migration_state.name.lower()) }
    extra[FileProviderMigrationExtraKeys.HAS_SECONDARY] = str(account_count > 1)
# WARNING: Decompyle incomplete


def _report_event(account = unique, event = unique, session_id = unique, action_surface = ('account', 'Optional[AccountInterface]', 'event', 'str', 'session_id', 'str', 'action_surface', 'Optional[str]', 'extra_dict', 'Any'), **extra_dict):
    no_pii_extras = sanitize_event_extra_dict(non_pii_extras(extra_dict))
    report('file-provider-migration-events', account = account, event = event, session_id = session_id, action_surface = action_surface, extra = no_pii_extras)


class FileProviderMigrationLogger:
    report_ui_event = (lambda account = None, event = None, session_id = staticmethod, action_surface = (None,): pass# WARNING: Decompyle incomplete
)()
    report_event = (lambda account = None, event = None, session_id = staticmethod: pass# WARNING: Decompyle incomplete
)()
    report_invalid_event = (lambda action = None, migration_state = None, fp_logger_reporting_params = staticmethod: extra = build_report_event_args(migration_state, fp_logger_reporting_params.account_count)extra[FileProviderMigrationExtraKeys.CURRENT_MIGRATE_ACTION_ATTEMPT] = str(action)# WARNING: Decompyle incomplete
)()

