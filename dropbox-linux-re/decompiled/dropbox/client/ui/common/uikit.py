# Source Generated with Decompyle++
# File: uikit.pyc (Python 3.11)

import collections
import os
import threading
import urllib.parse as urllib
from abc import ABCMeta, abstractmethod, abstractproperty
from collections import OrderedDict
from enum import Enum
from typing import Any, Callable, Dict, List, NamedTuple, Optional, Text, Tuple, TypeVar
from apex.metrics import Counter, Metric
from build_number import is_headless_enabled
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.sharing_modal.constants import ShareModalInitialScreen
from dropbox.client.message_queue import InstrumentedMessageQueue, StoppableMessageQueue
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId
from dropbox.client.status.interface import ClientStatusInterface
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes, IconType
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayState, TrayTriggerReason
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.client.util import hard_exit, hard_exit_runbox, safe_print
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import UI_FRAMEWORK_EVENT, UI_FRAMEWORK_RESTRICTED_EVENT
from dropbox.exception.reporting import report_exception, Severity
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.gui import assert_message_queue
from dropbox.i18n import trans
from dropbox.model.types import FileId
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIInterface, InfiniteUIKextInstallFlowSource
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.threading import RLock
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
MYPY = False
if MYPY:
    
    gandalf
    from dropbox.client.main import DropboxApplication
    import dropbox.client.gandalf, client
    from dropbox.client.multiaccount.selector import MultiAccountSelector
    from dropbox.client.ui.common.camera import CameraUI
    from dropbox.client.ui.common.dialogs import BaseDialogController
    from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
    from dropbox.client.ui.common.tray_ui_controller import TrayUiControllerBase
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

def show_remote_share_fallback_with_email_verification(*, dropbox_app, ui_kit, location_props, share_account, show_email_verification):
    pass
# WARNING: Decompyle incomplete


class SetupWizardPageType(Enum):
    UNSPECIFIED = 1
    SIGN_UP = 2
    SIGN_IN = 3


class FrameworkMetadata(NamedTuple):
    web_framework: 'str' = 'FrameworkMetadata'


class FrameworkProps(Enum, FrameworkMetadata):
    ELECTRON = FrameworkMetadata('Electron', 'Electron')
    COCOA = FrameworkMetadata('Cocoa', 'Electron')
    LINUX = FrameworkMetadata('Linux', 'Linux')
    LOW_UI_WIN = FrameworkMetadata('Win32', 'None')
    LOW_UI_MAC = FrameworkMetadata('Cocoa', 'None')
    WIN32 = FrameworkMetadata('Win32', 'None')
    HEADLESS = FrameworkMetadata('Headless', 'None')


class Closeable:
    
    def __init__(self = None, callback = None):
        self._callback = callback

    
    def close(self = None):
        self._callback()



class MainMessageQueue(InstrumentedMessageQueue):
    pass
# WARNING: Decompyle incomplete

MainMessageQueue.init_static_vars()
on_ui_thread = MainMessageQueue.on_queue
on_ui_thread_returns_none = MainMessageQueue.on_queue_returns_none
on_ui_thread_blocking = MainMessageQueue.on_queue_blocking
on_ui_thread_future = make_on_thread_future_decorator(on_ui_thread, 'on_ui_thread_future')

def _handle_ui_thread_exception(exc = None, exc_info = None):
    report_exception(severity = Severity.CRITICAL, exc_type = exc_info[0], exc_val = exc_info[1], exc_traceback = exc_info[2], component = DesktopComponent.UI_KIT)
    hard_exit_runbox("FATAL: Unhandled exception in @ensure_on_ui_thread code while run-box'ing.", DesktopComponent.HTML_VIEWS, exc_info)

_CBNone = TypeVar('_CBNone', bound = Callable[(..., None)])

def ensure_on_ui_thread():
    return MainMessageQueue.on_queue(block_only_on_main_thread = True, on_exception = _handle_ui_thread_exception)


def BaseUIKit():
    '''BaseUIKit'''
    pass
# WARNING: Decompyle incomplete

BaseUIKit = <NODE:27>(BaseUIKit, 'BaseUIKit', metaclass = ABCMeta)

def ExternalUIKit():
    '''ExternalUIKit'''
    pass
# WARNING: Decompyle incomplete

ExternalUIKit = <NODE:27>(ExternalUIKit, 'ExternalUIKit', MainMessageQueue, BaseUIKit, metaclass = ABCMeta)

class SimpleUIKit(BaseUIKit, StoppableMessageQueue, MainMessageQueue):
    
    def _should_post(self = None):
        return threading.current_thread().name != 'MainThread'

    initialize = (lambda self = None: pass)()
    mainloop = (lambda self = None: TRACE('Entering main loop')try:
self._run_loop()TRACE('Leaving main loop')Noneexcept:
TRACE('Leaving main loop'))()
    
    def exit_mainloop(self = None):
        self.signal_stop()



def should_create_headless_ui_kit():
    if is_headless_enabled():
        return True
    if None:
        TRACE('DISPLAY is %r', os.environ.get('DISPLAY'))
        return not os.environ.get('DISPLAY')


def create_ui_kit(app):
    if should_create_headless_ui_kit():
        TRACE('Loading headless UIKit')
        HeadlessUIKit = HeadlessUIKit
        import dropbox.client.ui.headless
        return HeadlessUIKit(app)
    if is_low_ui_mode():
        LowUIKit = LowUIKit
        import dropbox.client.ui.low_ui
        return LowUIKit(app)
    if None:
        RichWinUIKit = RichWinUIKit
        import dropbox.client.ui.win32.uikit
        return RichWinUIKit(app)
    if None:
        CocoaUIKit = CocoaUIKit
        import dropbox.client.ui.cocoa.uikit
        return CocoaUIKit(app)
# WARNING: Decompyle incomplete


class _ViewEventKey(NamedTuple):
    content_id: 'Optional[str]' = '_ViewEventKey'

_VIEW_EVENT_COUNTERS: 'Dict[_ViewEventKey, Counter]' = dict()

def record_view_event(machine_context = None, framework_props = None, event_name = None, content_id = ('machine_context', 'MachineContext', 'framework_props', 'FrameworkProps', 'event_name', 'str', 'content_id', 'Optional[str]', 'extra', 'Text', 'return', 'None'), **extra):
    pass
# WARNING: Decompyle incomplete


def report_ui_framework_event(event_name = None, framework_props = None, **extra):
    ALLOWED_NON_RESTRICTED_KEYS = {
        'hash',
        'count',
        'reason',
        'allowed',
        'ci_type',
        'display',
        'variant',
        'bounds_x',
        'bounds_y',
        'device_id',
        'vendor_id',
        'tray_width',
        'app_created',
        'desktop_env',
        'gtk_version',
        'reason_code',
        'tray_height',
        'active_flows',
        'is_light_mode',
        'has_active_flow',
        'is_tray_min_height',
        'requesting_function',
        'using_software_opengl',
        'global_tray_icon_bounds',
        'requested_delay_seconds',
        'has_active_blocking_flow'}
# WARNING: Decompyle incomplete


def report_ui_framework_event_restricted(event_name = None, framework_props = None, **extra):
    UI_FRAMEWORK_RESTRICTED_EVENT(event_name, event_name = framework_props.web_framework, framework_name = (lambda .0: pass# WARNING: Decompyle incomplete
), extra = extra.items()())

