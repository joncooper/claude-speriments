# Source Generated with Decompyle++
# File: state_machine.pyc (Python 3.11)

from datetime import datetime
from typing import Callable, Dict, List, Optional
from build_number import is_test
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.client.features.file_provider_migration.config import FPMigrationStateStore
from dropbox.client.features.file_provider_migration.exceptions import InvalidStateTransitionException, NotEligibleForAutoMigration, NotEligibleForMigration
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FileProviderMigrationLogger, FPLoggerReportingParams, FPMigrationEligibilityCheckKeys
from dropbox.client.features.file_provider_migration.interfaces import FPMigrationStateStoreInterface
from dropbox.client.features.file_provider_migration.types import FileProviderMigrationState, StateMachineEvent
from dropbox.client.features.file_provider_migration.ui.controllers.post_migration_ui_controller import FPPostMigrationFlowUiController
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.raii2.arc import Arc
from dropbox.threading import Lock
from dropbox.trace import TRACE
StartMigrationCallable = Callable[([], None)]
NotificationFactory = Callable[([], Destroyable)]

class EligibilityCheckResult:
    
    def __init__(self = None, is_eligible = None, can_update_external_drive_to_be_eligible = None, auto_migration_deadline = (None, None, False), should_overwrite_deadline = ('is_eligible', 'bool', 'can_update_external_drive_to_be_eligible', 'Optional[bool]', 'auto_migration_deadline', 'Optional[datetime]', 'should_overwrite_deadline', 'bool')):
