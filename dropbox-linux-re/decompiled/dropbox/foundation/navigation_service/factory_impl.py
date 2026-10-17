# Source Generated with Decompyle++
# File: factory_impl.pyc (Python 3.11)

from typing import Optional
from apex.context import ApexContext
from build_number import is_electron_application
from factory import NavigationServiceContext, NavigationServiceFactory
from navigation_service import MachineUiDispatcherFactoryInterface, NavigationService, UserUiDispatcherFactoryInterface
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.electron.adapters._impl import ElectronIpcAdapters
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class NavigationServiceContextImpl(NavigationServiceContext):
    pass
# WARNING: Decompyle incomplete


class NavigationServiceContextStub(NavigationServiceContext):
    pass
# WARNING: Decompyle incomplete


class NavigationServiceFactoryImpl(NavigationServiceFactory):
    
    def __init__(self, ui_kit, machine_ui_dispatcher_factory, user_ui_dispatcher_factory = None, electron_ipc = None, sync_engine_adapter = None, client_session_id = (None,), apex_context = ('ui_kit', 'BaseUIKit', 'machine_ui_dispatcher_factory', 'MachineUiDispatcherFactoryInterface', 'user_ui_dispatcher_factory', 'UserUiDispatcherFactoryInterface', 'electron_ipc', 'Optional[ElectronIpc]', 'sync_engine_adapter', 'SyncEngineAdapter', 'client_session_id', 'Optional[str]', 'apex_context', 'Optional[ApexContext]', 'return', 'None')):
        self._ui_kit = ui_kit
        self._sync_engine_adapter = sync_engine_adapter
        self._machine_ui_dispatcher_factory = machine_ui_dispatcher_factory
        self._user_ui_dispatcher_factory = user_ui_dispatcher_factory
        self._electron_ipc = electron_ipc
        self._client_session_id = client_session_id
        self._apex_context = apex_context

    
    def create(self = None, machine_context = None):
        pass
    # WARNING: Decompyle incomplete


