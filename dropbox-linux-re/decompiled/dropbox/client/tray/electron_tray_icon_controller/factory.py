# Source Generated with Decompyle++
# File: factory.pyc (Python 3.11)

from typing import Callable, Iterable
from dropbox.client.benchmarking.startup import ClientStartupBenchmarker
from dropbox.client.fenix.journeys.tray.tray_status_service import TrayStatusService
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.tray.electron_tray_icon_controller.native_tray_icon_controller import NativeTrayIconController
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.platform import IS_MAC, IS_WINDOWS

def create_native_tray_icon_controller(machine_context, electron_host_driver, benchmarker, launch_func, exit_func = None, restart_func = None, status_controller = None, tray_status_service = ('machine_context', 'MachineContext', 'electron_host_driver', 'ElectronHostDriver', 'benchmarker', 'ClientStartupBenchmarker', 'launch_func', 'Callable[[], None]', 'exit_func', 'Callable[[ExitCode], None]', 'restart_func', 'Callable[[Iterable[str]], None]', 'status_controller', 'StatusControllerInterface', 'tray_status_service', 'TrayStatusService', 'return', 'NativeTrayIconController')):
    if IS_MAC:
        MacTrayIconController = MacTrayIconController
        import dropbox.client.tray.electron_tray_icon_controller.mac_tray_icon_controller
        return MacTrayIconController(machine_context, electron_host_driver, benchmarker, launch_func, exit_func, restart_func, status_controller, tray_status_service)
    if None:
        WinTrayIconController = WinTrayIconController
        import dropbox.client.tray.electron_tray_icon_controller.win_tray_icon_controller
        return WinTrayIconController(machine_context, electron_host_driver, benchmarker, launch_func, exit_func, restart_func, status_controller, tray_status_service)
    raise 'Linux is not supported'()

