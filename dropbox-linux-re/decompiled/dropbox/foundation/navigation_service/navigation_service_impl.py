# Source Generated with Decompyle++
# File: navigation_service_impl.pyc (Python 3.11)

import os
import sys
import uuid
from typing import Any, Dict, List, Optional, Text, Tuple, Type, TypeVar
from apex.metrics import Metric, MetricsReporter
from build_number.features import feature_enabled
from embeddable_host import EmbeddableViewHost
from interface import MachineNavigationManifest, NavigationContentType, NavigationManifest, NavigationVisibilityConfig, NavigationWindowType, UserNavigationManifest, ViewBridgeSerializable, ViewHandle
from threading import NavigationServiceWorkerThread, on_navigation_service_thread, on_navigation_service_thread_future
from view_interface import ViewInterface
from view_manager_interface import StandaloneViewIdentifier, ViewManagerInterface
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.flow_tracker import BlockingFlow
from dropbox.client.ui.common.uikit import BaseUIKit, on_ui_thread, on_ui_thread_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.bridge.bridge_registration import bridge_class
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
from dropbox.foundation.html_views.common.js_parsing_mode import ELIMINATE_LAZY_JS_PARSING
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.html_views.electron.manager_factory import ElectronViewManagerFactory
from dropbox.foundation.legacy_views.manager_factory import LegacyViewManagerFactory
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.named_navigation_service import NamedNavigationService
from dropbox.foundation.navigation_service.navigation_service import EmbeddableHostManager, MachineUiDispatcherFactoryInterface, MachineUiDispatcherInterface, NavigationService, UserUiDispatcherFactoryInterface, UserUiDispatcherInterface
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.collection import WindowManagerDelegateCollection
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.foundation.performance.bridge_gen.perf_session_data import PerfSessionData
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.gui import assert_not_on_main_thread
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
_T = TypeVar('_T')
_P = TypeVar('_P', bound = Optional[ViewBridgeSerializable])
_EV = TypeVar('_EV')
MachineNavigationParams = Tuple[(NavigationManifest[_P], Optional[Text], Optional[_P], Text, Optional[NavigationWindowType], NavigationLoadPolicy, Optional[NavigationVisibilityConfig], PerfSession, Optional[int])]
UserNavigationParams = Tuple[(NavigationManifest[_P], Optional[Text], Optional[_P], Text, Optional[NavigationWindowType], NavigationLoadPolicy, Optional[NavigationVisibilityConfig], PerfSession)]
TTI_PLATFORM_OVERHEAD_METRICS_AMP_NAMESPACE = 'desktop_perf'
FEATURE_TAG_NAME = 'feature'
PRELOAD_TAG_NAME = 'preload'
CHROMIUM_HOST = 'chromium_host'
report_tti_perf_session_to_amp = (lambda metrics_reporter = None, data = None: pass# WARNING: Decompyle incomplete
)()
METRIC_PLATFORM_OVERHEAD_METRIC = 'platform_overhead'

def checkpoints_into_amp_metrics(checkpoints = None):
    nav_service_called = checkpoints.get('navigation_service called')
    loading_js_start = checkpoints.get('load_js_and_css.start')
    loading_js_end = checkpoints.get('load_js_and_css.end')
    loading_view_anchor_start = checkpoints.get('ViewAnchor load.start')
    loading_view_anchor_end = checkpoints.get('ViewAnchor load.end')
    tti = checkpoints.get('tti')
    app_code_start = checkpoints.get('application_code_start')
# WARNING: Decompyle incomplete


def _create_view_perf_session(manifest, user_bound, visibility_config = None, metrics_reporter = None, accessibility_mode = None, start_time = (None, None), perf_session_extras = ('manifest', 'NavigationManifest', 'user_bound', 'bool', 'visibility_config', 'Optional[NavigationVisibilityConfig]', 'metrics_reporter', 'MetricsReporter', 'accessibility_mode', 'Text', 'start_time', 'Optional[float]', 'perf_session_extras', 'Optional[Dict[Text, Text]]', 'return', 'PerfSession')):
    pass
# WARNING: Decompyle incomplete

ViewHandleImpl = <NODE:12>()
NavigationServiceImpl = <NODE:12>()
