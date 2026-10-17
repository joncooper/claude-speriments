# Source Generated with Decompyle++
# File: view_anchor.pyc (Python 3.11)

from typing import Dict, List, Optional
from dropbox.client.features.api_v2.api_v2 import ApiV2ClientUntyped
from dropbox.client.features.backup_app.bridge_gen.bridge_interface_backup_app_view_anchor import BackupAppViewAnchorBridgeInterface
from dropbox.client.features.backup_app.view_model.bridge_gen.bridge_interface_backup_app_view_model import BackupAppViewModelBridgeInterface
from dropbox.client.features.backup_app.view_model.utils import get_platform_type
from dropbox.client.features.backup_app.view_model.view_model import BackupAppViewModel
from dropbox.client.features.client_status.view_model.client_status_vm import ClientStatusVM
from dropbox.client.features.external_drive_backup.view_model.external_drive_backup_view_model import ExternalDriveBackupManagerViewModel
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.utils import get_problematic_applications
from dropbox.client.features.sync_everything.v3.ux_param_utils import translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_sync_everything_manager_view_model import SyncEverythingManagerViewModelBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.platform_type import PlatformType
from dropbox.client.features.sync_everything.view_model.bridge_gen.stormcrow_values import StormcrowValues
from dropbox.client.features.sync_everything.view_model.sync_everything_manager_view_model import SyncEverythingManagerViewModel
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.common.interface import ViewAnchorConfiguration
from dropbox.foundation.html_views.common.view_anchor import ViewAnchorBase
from dropbox.foundation.raii2 import destroying
from dropbox.infinite import is_user_running_cloud_files
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper

class BackupAppViewAnchor(BackupAppViewAnchorBridgeInterface, ViewAnchorBase):
    pass
# WARNING: Decompyle incomplete

