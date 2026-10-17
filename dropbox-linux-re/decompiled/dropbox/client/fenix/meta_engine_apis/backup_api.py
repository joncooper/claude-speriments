# Source Generated with Decompyle++
# File: backup_api.pyc (Python 3.11)

import uuid
from typing import Dict, List, Optional
from base import named_partial
from dropbox.api.v2.datatypes.external_drive_backup import ListBackupsResult as ExternalDriveListBackupsResult
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_app.view_model.bridge_gen.device_backup_info import DeviceBackupInfo
from dropbox.client.features.backup_app.view_model.bridge_gen.external_drive_backup_info import ExternalDriveBackupInfo
from dropbox.client.features.backup_app.view_model.utils import list_backups_result_to_device_backup_list, list_drive_backups_result_to_drive_backup_list
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.external_drive_backup.api_utils import list_backups as list_drive_backups
from dropbox.client.features.external_drive_backup.errors import RequestFailedException as EdbRequestFailedException
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.sync_everything.v3.api_utils import list_backups
from dropbox.client.features.sync_everything.v3.errors import RequestFailedException as ComputerBackupRequestFailedException
from dropbox.client.features.sync_everything.v3.ux_param_utils import translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.backups_pb2 import ListComputerBackupsReply, ListComputerBackupsReq, ListExternalDriveBackupsReply, ListExternalDriveBackupsReq
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.backups_api_base import _BackupServiceBaseClass
from dropbox.client.fenix.type_converter import convert_python_device_backup_to_protobuf, convert_python_external_drive_backup_to_protobuf, convert_sync_status_to_protobuf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.raii2.arc import Arc
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveEvent, ReactiveRequest
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.sync_engine_status import SyncEngineStatus
from dropbox.threading import RLock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class BackupAPI(_BackupServiceBaseClass):
    pass
# WARNING: Decompyle incomplete

