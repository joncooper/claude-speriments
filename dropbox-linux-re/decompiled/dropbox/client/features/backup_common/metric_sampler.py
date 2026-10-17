# Source Generated with Decompyle++
# File: metric_sampler.pyc (Python 3.11)

from os import access, W_OK
from typing import Dict, List, Mapping, Optional, Tuple, Union
from dropbox import fsutil
from dropbox.client.features.backup_common.constants import CLOUD_DOCS_REGEX, DEFAULT_IGNORED_GLOBS, NUCLEUS_UNSYNCED_FILENAMES_REGEX
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.computer_backup.computer_backup_logging import ComputerBackupLogger
from dropbox.client.features.computer_backup.event_reporter import OperationEventReporter as CBOperationEventReporter
from dropbox.client.features.computer_backup.fully_synced_tracker import FirstSyncLoggingData as CBFirstSyncLoggingData
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventReporter as EDBOperationEventReporter
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.fully_synced_tracker import FirstSyncLoggingData as EDBFirstSyncLoggingData
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function
from dropbox.client.features.sync_everything.view_model.constants import KNOWN_FOLDER_NAME_MAP
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2.arc import Arc
from dropbox.fsutil import FileSystem
from dropbox.model.types import FileId
from dropbox.proto.nucleus.dbxignore_pb2 import DBXIgnoreVersion
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import DbxIgnoreContents, DeviceAnchorInfo, DeviceAnchorState, DeviceAnchorTargetType, ListDeviceAnchorsResult
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties, NonSyncingLocalPathException, SustainedFilesystemErrorsException, ValidPathWithoutFileIdException
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
REMOTE_UPLOAD_SAMPLE_SIZE = 10

class MetricSampler(Actor):
    pass
# WARNING: Decompyle incomplete

