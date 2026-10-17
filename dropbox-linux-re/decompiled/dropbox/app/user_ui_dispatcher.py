# Source Generated with Decompyle++
# File: user_ui_dispatcher.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractproperty
from typing import Optional
from six import add_metaclass
from dropbox.client.dynamic_contents.dynamic_contents_manager import DynamicContentsManager
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.client.features.file_locking.file_locking_controller import FileLockingController
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.quota_usage.modal_over_quota_controller import ModalOverQuotaController
from dropbox.client.features.quota_usage.modal_over_quota_prevented_controller import ModalOverQuotaPreventedController
from dropbox.client.features.sync.sync_prioritization.sync_prioritization import SyncPrioritization
from dropbox.client.features.sync_error.controller.sync_error_controller import SyncErrorController
from dropbox.client.features.sync_error.feature import SyncErrorsFeature
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.features.sync_everything.sync_everything_notification_controller import SyncEverythingNotificationController
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.html_views.common.threading import assert_on_ui_thread
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface
from dropbox.foundation.navigation_service.navigation_service import UserUiDispatcherFactoryInterface, UserUiDispatcherInterface
UserUiDispatcherDependencyProviderInterface = <NODE:12>()

class UserUiDispatcherFactory(UserUiDispatcherFactoryInterface):
    
    def __init__(self = None, dependency_provider = None):
        self._dependency_provider = dependency_provider

    create_dispatcher = (lambda self = None, user_context = None, navigation_service = assert_on_ui_thread(): UserUiDispatcher(self._dependency_provider.legacy_ui_launcher, self._dependency_provider.dynamic_contents_manager, user_context, navigation_service))()


class UserUiDispatcher(UserUiDispatcherInterface):
    pass
# WARNING: Decompyle incomplete

