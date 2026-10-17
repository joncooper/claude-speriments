# Source Generated with Decompyle++
# File: machine_ui_dispatcher.pyc (Python 3.11)

from abc import ABCMeta, abstractproperty
from typing import Callable, Optional, Text
from six import add_metaclass
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.auth_state import AuthState
from dropbox.client.features.account_pairing.pairing_controller import PairingController
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.driver_analytics.common import run_driver_analytics
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.client.features.foundation.custom_url_scheme_handler import CustomURLSchemeHandler
from dropbox.client.features.foundation.custom_url_scheme_handler.registrar import URLSchemeRegistrar
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.tray.tray_lifetime_adapter import TrayLifetimeAdapter
from dropbox.client.ui.common.dnd_notification_controller import DNDNotificationController
from dropbox.client.url_schemes.client_url_scheme_handler import DesktopClientURLSchemeHandler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.navigation_service.navigation_service import MachineUiDispatcherFactoryInterface, MachineUiDispatcherInterface, NavigationServiceInterface
AttemptLinkFunc = Callable[([
    Optional[Account],
    Optional[Callable[([
        AuthState], None)]],
    bool], bool)]
LinkSecondaryFunc = Callable[([
    Text], None)]
MachineUiDispatcherDependencyProviderInterface = <NODE:12>()

class MachineUiDispatcherFactory(MachineUiDispatcherFactoryInterface):
    
    def __init__(self = None, dependency_provider = None):
        self._dependency_provider = dependency_provider

    
    def create_dispatcher(self = None, machine_context = None, navigation_service = None):
        return MachineUiDispatcher(machine_context, navigation_service, self._dependency_provider.url_scheme_registrar, self._dependency_provider.attempt_link, self._dependency_provider.link_secondary)



class MachineUiDispatcher(MachineUiDispatcherInterface):
    pass
# WARNING: Decompyle incomplete

