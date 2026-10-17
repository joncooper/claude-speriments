# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

from enum import auto, Enum
from typing import Any, Callable, Dict, List, Optional
from dropbox.api.v2.datatypes.external_drive_backup import CreateBackupWithBackupRootInfo, ExternalDriveEntry
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client_api.connection.exceptions import APIv2EndpointError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture

class ExternalBackupException(Exception):
    pass


class EdbFissionMigrationNeeded(ExternalBackupException):
    pass
# WARNING: Decompyle incomplete


class RequestFailedException(ExternalBackupException):
    pass
# WARNING: Decompyle incomplete


class RequestAssertion(RequestFailedException):
    pass
# WARNING: Decompyle incomplete

_CatchHandler = Callable[([
    Exception,
    ExcInfo], FailedFuture[Any])]
convert_to_failure = (lambda status_code = None, debug_message = None, report_severity = future_function: pass# WARNING: Decompyle incomplete
)()
RETRIABLE_APIv2_ERRORS = {
    'internal_error',
    'audit_log_error',
    'folder_update_error'}

def is_retriable(apiv2error = None):
