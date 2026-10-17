# Source Generated with Decompyle++
# File: top_level_html_view_params.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import sys
from json import dumps
from typing import Any, Callable, Dict, Optional, Text, Type
from typing_extensions import Protocol
from weakref import ref as WeakRef
from build_number.features import feature_enabled
from lib.crashpad.api import add_simple_annotation
from dropbox.client.features.active_flow_tracker import ActiveFlowTracker
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exceptions import JavascriptError
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context import ContextInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context_menu.ui.menu_action_executor import MenuActionExecutor
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.bridge.error_reporting import ErrorReporter
from dropbox.foundation.html_views.bridge.impl import _marshall_object, json_box_records, MarshalledInstanceTracker
from dropbox.foundation.html_views.bridge.interface import ViewBridgeSerializable
from dropbox.foundation.html_views.bridge.routing import JavaScriptBridgeViewContext, TimedBridgeCallTracker
from dropbox.foundation.html_views.common import HtmlViewStateMachine
from dropbox.foundation.html_views.common.bridge_call_perf_logger_connection_impl import BridgeCallPerfLoggerConnectionImpl
from dropbox.foundation.html_views.common.bridge_gen.bridge_interface_lifecycle_coordinator import LifecycleCoordinatorBridgeInterface
from dropbox.foundation.html_views.common.bridge_gen.runtime_info import RuntimeInfo
from dropbox.foundation.html_views.common.bridge_gen.window_display_state import WindowDisplayState
from dropbox.foundation.html_views.common.bridge_gen.window_display_state_changed import WindowDisplayStateChanged
from dropbox.foundation.html_views.common.content_source import ContentSource
from dropbox.foundation.html_views.common.initial_content_data import InitialContentData
from dropbox.foundation.html_views.common.interactivity_tracking import InteractivityTracking
from dropbox.foundation.html_views.common.interface import HtmlViewLoadErrorType, ViewAnchorConfiguration, ViewAnchorInterface
from dropbox.foundation.html_views.common.logging import HtmlViewLogger, HtmlViewLoggerEvent
from dropbox.foundation.html_views.common.nav_param_manager import NavigationParameterManager
from dropbox.foundation.html_views.common.navigation_parameters import NavigationParameters
from dropbox.foundation.html_views.common.threading import UiEventFuture
from dropbox.foundation.html_views.common.view_context_impl import ViewContextImpl
from dropbox.foundation.html_views.theming.theming import Theming
from dropbox.foundation.navigation_service.bridge_gen.bridge_interface_activity_monitor import ActivityMonitorBridgeInterface
from dropbox.foundation.navigation_service.bridge_gen.bridge_interface_named_navigation_service import NamedNavigationServiceBridgeInterface
from dropbox.foundation.navigation_service.interface import NavigationError, NavigationServiceInterface
from dropbox.foundation.navigation_service.named_navigation_service import NamedNavigationService
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.performance import IfEnded, PerfSession
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.foundation.signals import Signal, SignalConnection, StandardSignal
from dropbox.foundation.signals.event import EventSignal
from dropbox.threading import Lock

def TeardownSignal():
    '''TeardownSignal'''
    pass
# WARNING: Decompyle incomplete

TeardownSignal = <NODE:27>(TeardownSignal, 'TeardownSignal', Destroyable, Signal[None])

class LifecycleCoordinator(LifecycleCoordinatorBridgeInterface, Destroyable):
    pass
# WARNING: Decompyle incomplete


class PerfSessionValidatorStrategy(Protocol):
    
    def validate_perf_session(self = None, perf_session = None):
        pass



class DefaultPerfSessionValidatorStrategy:
    
    def __init__(self = None, feature = None, component = None):
        self._feature = feature
        self._component = component

    
    def validate_perf_session(self = None, perf_session = None):
        session_data = perf_session.data
        if PerfSession.TTI_CHECKPOINT not in session_data.checkpoints:
            report_bad_assumption('{} did not log a TTI checkpoint'.format(self._feature), use_message_for_legacy_hash = True, component = self._component)
            report_app_framework_event('perf_session_missing_tti_checkpoint', feature = self._feature)
        if not perf_session.ended:
            report_bad_assumption('{} TTI perf session was not ended'.format(self._feature), use_message_for_legacy_hash = True, component = self._component)
            report_app_framework_event('perf_session_not_ended', feature = self._feature)
            return None



class TopLevelHtmlViewParams(Destroyable):
    pass
# WARNING: Decompyle incomplete

