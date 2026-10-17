# Source Generated with Decompyle++
# File: machine_anchor.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.client.features.backup_auto_selsync.auto_selsync_manager import AutoSelSyncManager
from dropbox.client.features.backup_auto_selsync.bi_auto_selsync_manager import BackupAutoSelSyncManager
from dropbox.client.features.backup_common.backup_logging import BackupLogger
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.cloud_files_migration.migration_manager import CloudFilesMigrationManager
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.client.features.external_drive_backup.webdebugger import ExternalBackupWebDebugger
from dropbox.client.features.file_view_logging.file_view_logger_factory import create_view_logger
from dropbox.client.features.flexible_filenames.manager import FlexibleFilenamesManager
from dropbox.client.features.ignore_files.manager import IgnoreFilesManager
from dropbox.client.features.smarter_smart_sync.feature import SmarterSmartSyncFeature
from dropbox.client.features.smarter_smart_sync.smarter_smart_sync_manager import SmarterSmartSyncManager
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingLogger
from dropbox.client.features.sync_everything.v3.webdebugger import SyncEverythingWebDebugger
from dropbox.client.notifications.notifications_wrapper import MachineNotificationsWrapper
from dropbox.fileevents import FileEvents
from dropbox.foundation.app_model.machine_anchor_interface import MachineAnchorInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.file_events import FileEventsSingleton
from dropbox.foundation.html_views.theming.theming import Theming
from dropbox.foundation.raii2.arc import Arc
from dropbox.metrics.reporter import PeriodicMetricsReporter
from dropbox.platform import IS_WINDOWS

class MachineAnchor(MachineAnchorInterface):
    pass
# WARNING: Decompyle incomplete

