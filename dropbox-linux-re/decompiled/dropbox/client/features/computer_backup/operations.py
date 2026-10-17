# Source Generated with Decompyle++
# File: operations.pyc (Python 3.11)

from __future__ import annotations, division
import re
from abc import ABC, abstractmethod
from os import unlink
from os.path import exists as _exists
from typing import Any, Callable, cast, Dict, List, NamedTuple, Optional, Set, Text, Tuple, TypeVar, Union
from dropbox import fsutil
from dropbox.api.v2.datatypes.device_sync import ComputerBackupFolderRestoreEntry, ComputerBackupFolderType, EmailType, RestoreComputerBackupFolderInput, SyncFolderType, UpdateComputerBackupResult
from dropbox.client.features.backup_common.base_event_reporter import EventReporter
from dropbox.client.features.backup_common.constants import CB_ANCHOR_EXTENSION, DEFAULT_IGNORED_GLOBS
from dropbox.client.features.backup_common.logging_helpers import convert_folder_id_to_nopii_name, convert_folder_id_to_nopii_value
from dropbox.client.features.backup_common.utils import path_to_glob
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.backup_instance.types import BackupInstance
from dropbox.client.features.backup_instance.utils import remove_folder
from dropbox.client.features.computer_backup.computer_backup_logging import ComputerBackupLogger
from dropbox.client.features.computer_backup.computer_backup_state import ComputerBackupState, KnownCBFolder
from dropbox.client.features.computer_backup.constants import BackupStatus, CBFolderId, ComputerBackupStatus, ComputerBackupUIStrings
from dropbox.client.features.computer_backup.errors import convert_to_failure, RequestAssertion, RequestFailedException
from dropbox.client.features.computer_backup.event_reporter import OperationEventReporter, OperationEventSession
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.computer_backup.server_interface import AsyncCopyTransientException, catch_and_convert_network_exceptions, catch_and_convert_network_exceptions_complete_restore_computer_backup, CBFolderInput, folder_id_to_api, FolderToRestoreInput, os_folder_id_from_api, RestoreUpdateCBInput, ServerInterface
from dropbox.client.features.computer_backup.trace import CB_TRACE, CB_WARN
from dropbox.client.features.computer_backup.utils import get_all_os_folders_paths, get_third_party_providers_nopii_from_folder_list, wrap_return_or_try_again
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event_label import ComputerBackupEventLabel
from dropbox.client.features.sync_everything.constants import COMPLETE_RESTORE_DELAY_SECS, CustomFolderRequest, EXP_BACKOFF_BASE, FolderIgnorePaths, KnownFolderRequest, MAX_COMPLETE_RESTORE_ATTEMPTS
from dropbox.client.features.sync_everything.v3.async_tools import assert_not_on_actor_thread, assert_on_actor_thread, async_queued_local_function, future_function, future_sequence, FutureGenerator
from dropbox.client.features.sync_everything.v3.fp_utils import allow_dataless_recall, DatalessContext
from dropbox.client.features.sync_everything.v3.server_interface import os_folder_id_to_api as os_folder_id_to_se_api
from dropbox.client.features.sync_everything.v3.utils import check_app_states_inside_known_folder, check_illegal_nesting_inside_known_folder, debug_known_folder_locations, get_third_party_providers, home_mount_path, is_another_provider_syncing, is_folder_ignored
from dropbox.client.features.sync_everything.view_model.bridge_gen.app_state import AppState
from dropbox.client.features.sync_everything.view_model.bridge_gen.folder_status_type import FolderStatusType
from dropbox.client.features.sync_everything.view_model.bridge_gen.in_use_provider import InUseProvider
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_error import RedirectError
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult, OperationResultData
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.types.ids import FileID
from dropbox.functions import retry, RetryException
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.device_anchor_interface import DeviceAnchorError, DeviceAnchorTargetType, NotADeviceAnchorError, NotFoundDeviceAnchorError
from dropbox.sync_engine_boundary.device_folder_interface import NucleusNotReadyRedirectionError
from dropbox.sync_engine_boundary.exceptions import NetworkPathException
from dropbox.sync_engine_boundary.file_system_exceptions import FileSystemError, OperationNotPermittedError
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import DbxIgnoreContents
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
_PreviousValue = TypeVar('_PreviousValue')
_FolderAccessInfo = NamedTuple('_FolderAccessInfo', [
    ('abs_path', LocalPath),
    ('fileid', Optional[FileId])])

class Operation(ABC, Actor):
    pass
# WARNING: Decompyle incomplete

UpdateOpEvents = NamedTuple('UpdateOpEvents', [
    ('overall_event', ComputerBackupEvent),
    ('server_update_event', ComputerBackupEvent),
    ('per_folder_fut_event', ComputerBackupEvent),
    ('per_folder_cancel_fut_event', ComputerBackupEvent),
    ('final_server_update_event', ComputerBackupEvent),
    ('final_server_disable_event', ComputerBackupEvent),
    ('final_l0_folder_delete_event', ComputerBackupEvent)])
RestoreOpEvents = NamedTuple('RestoreOpEvents', [
    ('overall_event', ComputerBackupEvent),
    ('per_folder_fut_event', ComputerBackupEvent)])
DisableOpEvents = NamedTuple('DisableOpEvents', [
    ('overall_disable_event', ComputerBackupEvent),
    ('server_disable_event', ComputerBackupEvent),
    ('l1_folder_delete_event', ComputerBackupEvent),
    ('l0_folder_delete_event', ComputerBackupEvent)])

class UpdateOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class DisableOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class PauseOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class ResumeOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class RenameOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class EnableBackupSanityCheckOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class MarkQuotaExemptOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class ClearAllQuotaExemptOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class RestoreOperation(UpdateOperation):
    pass
# WARNING: Decompyle incomplete

