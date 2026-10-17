# Source Generated with Decompyle++
# File: local_view_factory.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import random as insecure_random
import uuid
from typing import Callable, Dict, Generic, List, NamedTuple, Optional, Text, Tuple, TypeVar
import psutil
from build_number import is_frozen
from lib.crashpad.api import add_simple_annotation
from dropbox.client.features.bundle_policies import DEV_BUNDLE, FEATURE_TO_POLICY, Policy, PRELOAD_PROD_BUNDLE
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import CancelledFuture, FailedFuture, Future, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.bridge.interface import ViewBridgeSerializable
from dropbox.foundation.html_views.common import HtmlViewAffinityGroup, HtmlViewLogger, HtmlViewLoggerEvent, HtmlViewStateMachine, HtmlViewStateMachineStrategy, StateMachineNavigationRequest
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
from dropbox.foundation.html_views.common.content_metadata import StandaloneHtmlContentMetadata
from dropbox.foundation.html_views.common.embeddable_mixin import EmbeddableViewMixin
from dropbox.foundation.html_views.common.manager import HtmlViewManagerStrategy, PreEmbeddedStandaloneViewResult
from dropbox.foundation.html_views.common.navigation_rules import KNOWN_SCHEME_HANDLER_LOCAL, LOCAL_VIEW_STATIC_CONTENT_PATH_PREFIX
from dropbox.foundation.html_views.common.top_level_html_view_params import TopLevelHtmlViewParams
from dropbox.foundation.html_views.common.view import PlatformCanCreateStatus, PlatformHtmlViewCreationData, PlatformHtmlViewFactory, StandaloneHtmlView, ViewType
from dropbox.foundation.html_views.local.common.img_handler import LocalViewNativeImgHandler
from dropbox.foundation.html_views.local.common.interface import LocalViewFactoryInterface
from dropbox.foundation.html_views.local.common.metadata_registry import LOCAL_VIEWS_REGISTRY
from dropbox.foundation.html_views.local.common.preloader import ObjectPreloader, TryCreateMetadata
from dropbox.foundation.html_views.local.common.previews_handler import LocalViewPreviewsAssetHandler
from dropbox.foundation.html_views.local.common.view import LocalViewCreationCheckpoints
from dropbox.foundation.html_views.metrics.bridge_gen.bridge_interface_internal_perf_session_checkpoints import InternalPerfSessionCheckpointsBridgeInterface
from dropbox.foundation.html_views.metrics.html_view_metrics_reporter import HtmlViewMetricsReporter
from dropbox.foundation.html_views.theming.theming import Theming
from dropbox.foundation.navigation_service.bridge_gen.bridge_interface_activity_monitor import ActivityMonitorBridgeInterface
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface
from dropbox.foundation.navigation_service.view_interface import PRE_CONTENT_VIEW_ID, StandaloneViewIdentifier
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.performance import MultiEndCheckpointStrategy, PerfSession, RACY_OPTIONAL_CHECKPOINT
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.foundation.scheme_handler.interface import CustomSchemeRouterInterface
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
MB = 1048576
GB = MB * 1024
MEMORY_PER_PRELOADED_VIEW = 50 * MB
_EV = TypeVar('_EV', bound = EmbeddableViewMixin)
_O = TypeVar('_O')
WINDOW_DISPOSAL_AFTER_VIEW_EXTRACTED_DELAY_SEC = 10
STANDALONE_VIEW_PRELOAD_DELAY_SEC = 10
PRELOAD_VIEW_ID_MARKER = 'special view content id marker that represents preload case'

def should_launch_feature_bundle(policy = None):
    if not not (policy.is_in_preload):
        pass
    return bool(insecure_random.getrandbits(1))

LOCAL_VIEW_PRELOAD_COUNT = 1
LOCAL_VIEW_MAX_PRELOAD_MEMORY = 1 * GB

def PreloadedViewCount():
    '''PreloadedViewCount'''
    zero = (lambda reason = None: PreloadedViewCount(0, 0, reason, reason))()

PreloadedViewCount = <NODE:27>(PreloadedViewCount, 'PreloadedViewCount', NamedTuple('PreloadedViewcount', [
    ('embeddable', int),
    ('standalone', int),
    ('embeddable_reason', Text),
    ('standalone_reason', Text)]))
StandaloneViewCreationTuple = Tuple[(PlatformHtmlViewCreationData[_EV], _EV)]

def local_view_navigation_request(webview_id = None, view_content_id = None, is_prod_bundle_strategy = None, launch_perf_session = ('webview_id', 'Text', 'view_content_id', 'str', 'is_prod_bundle_strategy', 'bool', 'launch_perf_session', 'Optional[PerfSession]', 'return', 'StateMachineNavigationRequest')):
    pass
# WARNING: Decompyle incomplete


def AffinityGroupPreloader():
    '''AffinityGroupPreloader'''
    pass
# WARNING: Decompyle incomplete

AffinityGroupPreloader = <NODE:27>(AffinityGroupPreloader, 'AffinityGroupPreloader', Destroyable, Generic[_O])

def LocalViewFactory():
    '''LocalViewFactory'''
    pass
# WARNING: Decompyle incomplete

LocalViewFactory = <NODE:27>(LocalViewFactory, 'LocalViewFactory', LocalViewFactoryInterface, Destroyable, Generic[_EV])

def LocalViewManagerStrategy():
    '''LocalViewManagerStrategy'''
    pass
# WARNING: Decompyle incomplete

LocalViewManagerStrategy = <NODE:27>(LocalViewManagerStrategy, 'LocalViewManagerStrategy', HtmlViewManagerStrategy[(_EV, Context)])

def check_if_js_bundles_were_build_with_prod():
    if os.environ.get('IS_UNIT_TEST') == '1':
        return False
    is_prod_bundling_strategy = None
    if not is_frozen():
        if IS_MAC or IS_WINDOWS:
            bundle_strategy_file_path = './dropbox/local_views_build/build/bundling_strategy.txt'
            
            try:
                f = open(bundle_strategy_file_path)
                contents = f.read()
                is_prod_bundling_strategy = contents == 'prod'
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                pass
                            except IOError:
                                e = None
                                TRACE('!! Could not open path "%s"', bundle_strategy_file_path)
                                raise e
                                e = None
                                del e

                            return is_prod_bundling_strategy




