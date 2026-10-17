# Source Generated with Decompyle++
# File: _impl.pyc (Python 3.11)

from typing import Optional, Protocol, runtime_checkable
from apex.context import ApexContext
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.client.features.preferences.preferences_ipc_adapter import PreferencesIpcAdapter
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.electron.adapters.cloud_files_migration_adapter import CloudFilesMigrationAdapter
from dropbox.foundation.html_views.electron.adapters.electron_account_manager import ElectronAccountManager
from dropbox.foundation.html_views.electron.adapters.electron_appmenu_driver import ElectronAppMenuDriver
from dropbox.foundation.html_views.electron.adapters.electron_dialog_adapter import ElectronDialogIpcAdapter
from dropbox.foundation.html_views.electron.adapters.electron_local_config import ElectronLocalConfigAdapter
from dropbox.foundation.html_views.electron.adapters.electron_metrics_reporter import ElectronMetricsReporter
from dropbox.foundation.html_views.electron.adapters.electron_theme_manager import ElectronThemeManager
from dropbox.foundation.html_views.electron.adapters.sample_ipc_adapter import SampleIpcAdapter
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.raii2.quick import Destroyable
if IS_MAC:
    from dropbox.client.ui.cocoa.application_delegate import ApplicationDelegateInterface
    from dropbox.foundation.html_views.electron.adapters.electron_appdelegate_driver import ElectronAppDelegateDriver
    HasAppDelegate = <NODE:12>()
if IS_WINDOWS:
    from dropbox.client.tray.electron_tray_icon_controller.win_tray_icon_controller import WinTrayIconGuidController

class ElectronIpcAdapters(Destroyable):
    pass
# WARNING: Decompyle incomplete

