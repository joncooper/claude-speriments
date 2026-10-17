# Source Generated with Decompyle++
# File: tray_controller.pyc (Python 3.11)

import secrets
from typing import Any, Dict, Optional, Sequence, Text, Union
from dropbox.client.notifications.legacy_notifications import StickyNotification
from dropbox.client.tray.events import TrayEventReporter
from dropbox.client.tray.tray_runtime_controller import TrayRuntimeController
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_popup_constants import TRAY_HEIGHT, TRAY_POPUP_A11Y_ID, TRAY_WIDTH, TrayPerformanceMetrics, TrayPopupViewType, TrayTriggerReason
from dropbox.client.ui.common.tray_popup_utils import mark_sticky
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread_returns_none, report_ui_framework_event_restricted
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.electron_context_menus import ElectronContextMenu
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc, InvocationCallback, SignalCallback
from dropbox.foundation.html_views.electron.view import ElectronBrowserWindow
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.foundation.performance.perf_session import perf_session_stopwatch_span, PerfSession
from dropbox.foundation.raii2 import Destroyable, destroying
from dropbox.gui import event_handler
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
if IS_MAC:
    from AppKit import NSApp, NSBackingStoreBuffered, NSBorderlessWindowMask, NSColor, NSEvent, NSEventMaskLeftMouseDown, NSEventMaskRightMouseDown, NSFloatingWindowLevel, NSHUDWindowMask, NSNonactivatingPanelMask, NSNotification, NSObject, NSPanel, NSPoint, NSStatusWindowLevel, NSUtilityWindowMask, NSWindowCollectionBehaviorCanJoinAllSpaces, NSWindowCollectionBehaviorFullScreenAuxiliary, NSWindowCollectionBehaviorTransient
    from Quartz import CGRectMake
    from dropbox.client.ui.cocoa.tray_popup.testing import is_patronus_tray_test
    from dropbox.foundation.html_views.cocoa.helpers import get_nsview_from_bridged_native_handle
    from dropbox.foundation.html_views.electron.tray_controller_native_helpers import EFTrayPopupMenuController, EFTrayTopBarPopupMenu
    from dropbox.mac.typed_objc import typed_python_method
elif IS_WINDOWS:
    from dropbox.client.ui.win32.theme import get_os_theme, WindowsOSTheme

class ElectronTrayController(Destroyable):
    pass
# WARNING: Decompyle incomplete

if IS_MAC:
    
    class TrayPanelDelegate(NSObject):
        _tray_controller: 'ElectronTrayController' = 'TrayPanelDelegate'
        register_tray_controller = (lambda self = None, tray_controller = None: self._tray_controller = tray_controller)()
        windowDidResignKey_ = (lambda self = None, _ = None: if not self._tray_controller.is_pinned:
self._tray_controller.close_tray('window_did_resign_key')None)()
        windowDidBecomeKey_ = (lambda self = None, _ = None: try:
self._tray_controller.on_tray_focus_gained()Noneexcept Exception:
e = NoneTRACE(f'''[TrayController] TrayPanelDelegate windowDidBecomeKey_ error: {e}''')e = Nonedel eNonee = Nonedel e)()

    
    class TrayPanel(NSPanel):
        
        def canBecomeKeyWindow(self):
            return True


    return None
