# Source Generated with Decompyle++
# File: view.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod, abstractproperty
from enum import IntEnum
from typing import Callable, Generic, List, NamedTuple, Optional, Text, TypeVar
from lib.crashpad.api import add_simple_annotation
from  import HtmlViewLogger, HtmlViewLoggerEvent, HtmlViewStateMachine
from content_metadata import StandaloneHtmlContentMetadata
from embeddable_mixin import EmbeddableViewMixin
from threading import assert_on_html_view_thread
from top_level_html_view_params import TopLevelHtmlViewParams
from dropbox.callbacks import Handler
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.common import HtmlViewFeatures
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
from dropbox.foundation.html_views.common.interface import HtmlViewAffinityGroup
from dropbox.foundation.html_views.common.threading import on_html_view_thread_future, UiEventFuture
from dropbox.foundation.navigation_service.embeddable_host import EmbeddableViewHost
from dropbox.foundation.navigation_service.interface import NavigationDisabledError
from dropbox.foundation.navigation_service.view_manager_interface import StandaloneViewIdentifier, ViewInterface
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.performance import PerfSession, RACY_OPTIONAL_CHECKPOINT
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.gui import assert_message_queue
from dropbox.threading import Lock
from dropbox.trace import TRACE
_V = TypeVar('_V', bound = EmbeddableViewMixin)

class ViewType(IntEnum):
    SERVER_VIEW = 0
    LOCAL_VIEW = 1


class PlatformStandaloneHtmlViewInterface(object):
    get_view_id = (lambda self = None: pass)()
    destroy = (lambda self = None: pass)()
    close_view = (lambda self = None, close_reason = None: pass)()
    show_view = (lambda self = None: pass)()
    render_offscreen = (lambda self = None: pass)()
    hide_view = (lambda self = None: pass)()
    autoclose_view = (lambda self = None, close_timeout_secs = None: pass)()
    foreground_view = (lambda self = None: pass)()
    add_view_closed_handler = (lambda self = None, callback = None: pass)()
    remove_view_closed_handler = (lambda self = None, callback = None: pass)()
    is_foreground = (lambda self = None: pass)()

PlatformHtmlViewInitFunc = Callable[([
    StandaloneViewIdentifier,
    StandaloneHtmlContentMetadata,
    MachineContext,
    PerfSession,
    WindowManagerDelegateInterface], Future[None])]

def PlatformHtmlViewCreationData():
    '''PlatformHtmlViewCreationData'''
    
    def __init__(self = None, platform_view = None, embeddable_host = None, init_func = (None,)):
        self._platform_view = platform_view
        self._embeddable_host = embeddable_host
        self._init_func = init_func

    platform_view = (lambda self = None: self._platform_view)()
    embeddable_host = (lambda self = None: self._embeddable_host)()
    init_func = (lambda self = None: self._init_func)()

PlatformHtmlViewCreationData = <NODE:27>(PlatformHtmlViewCreationData, 'PlatformHtmlViewCreationData', Generic[_V])
PlatformCanCreateStatus = NamedTuple('PlatformCanCreateStatus', [
    ('result', bool),
    ('message', str),
    ('events', List[HtmlViewLoggerEvent])])

def PlatformHtmlViewFactory():
    '''PlatformHtmlViewFactory'''
    framework_props = (lambda self = None: pass)()
    create_blank_standalone = (lambda self, metadata = None, perf_session = None, context = abstractmethod, window_manager_delegate = ('metadata', 'StandaloneHtmlContentMetadata', 'perf_session', 'PerfSession', 'context', 'MachineContext', 'window_manager_delegate', 'WindowManagerDelegateInterface', 'return', 'Future[PlatformHtmlViewCreationData[_V]]'): pass)()
    create_standalone = (lambda self, view_id, metadata, perf_session = None, context = None, window_manager_delegate = abstractmethod, web_view = ('view_id', 'StandaloneViewIdentifier', 'metadata', 'StandaloneHtmlContentMetadata', 'perf_session', 'PerfSession', 'context', 'MachineContext', 'window_manager_delegate', 'WindowManagerDelegateInterface', 'web_view', '_V', 'return', 'Future[PlatformHtmlViewCreationData[_V]]'): pass)()
    create_pre_embedded_standalone = (lambda self = None, perf_session = None, context = abstractmethod, web_view = ('perf_session', 'PerfSession', 'context', 'MachineContext', 'web_view', '_V', 'return', 'Future[PlatformHtmlViewCreationData[_V]]'): pass)()
    create_embeddable = (lambda self, state_machine, top_level_html_view_params = None, scheme_name = None, affinity_group = abstractmethod, view_type = ('state_machine', 'HtmlViewStateMachine', 'top_level_html_view_params', 'Transferable[TopLevelHtmlViewParams]', 'scheme_name', 'Text', 'affinity_group', 'HtmlViewAffinityGroup', 'view_type', 'ViewType', 'return', 'Future[_V]'): pass)()
    validate_can_create = (lambda cls = None, context = classmethod: events = []if not HtmlViewFeatures.is_feature_only_enabled():
PlatformCanCreateStatus(False, 'Feature or stormcrow disabled', events)None.append(HtmlViewLoggerEvent.FEATURE_ENABLED)if not HtmlViewFeatures.is_platform_supported():
PlatformCanCreateStatus(False, 'Unsupported platform', events)None.append(HtmlViewLoggerEvent.ON_SUPPORTED_PLATFORM)if not HtmlViewFeatures.is_hardware_supported():
PlatformCanCreateStatus(False, 'Unsupported hardware', events)None.append(HtmlViewLoggerEvent.ON_SUPPORTED_HARDWARE)if not cls.try_initialize_framework():
PlatformCanCreateStatus(False, 'Could not initialize framework', events)None.append(HtmlViewLoggerEvent.INIT_SUCCESSFUL)PlatformCanCreateStatus(True, '', events))()()
    ensure_can_create_embeddable = (lambda cls = None, context = None, logger = classmethod: pass# WARNING: Decompyle incomplete
)()
    ensure_can_create_standalone = (lambda cls = None, context = None, logger = classmethod: if not HtmlViewFeatures.is_feature_only_enabled():
raise NavigationDisabledError('Feature disabled')logger.report_event(HtmlViewLoggerEvent.FEATURE_ENABLED))()
    try_initialize_framework = (lambda cls = None: True)()

PlatformHtmlViewFactory = <NODE:27>(PlatformHtmlViewFactory, 'PlatformHtmlViewFactory', Generic[_V])

def StandaloneHtmlView():
    '''StandaloneHtmlView'''
    pass
# WARNING: Decompyle incomplete

StandaloneHtmlView = <NODE:27>(StandaloneHtmlView, 'StandaloneHtmlView', ViewInterface, EmbeddableViewHost[_V])
