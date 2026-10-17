# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod
from typing import Any, Callable, Dict, Generic, List, Optional, Text, Tuple, TypeVar
from six import iteritems
from build_number import is_frozen
from lib.crashpad.api import add_simple_annotation
from  import HtmlViewLogger, HtmlViewLoggerEvent
from content_metadata import StandaloneHtmlContentMetadata
from embeddable_mixin import EmbeddableViewMixin
from threading import assert_on_html_view_thread
from top_level_html_view_params import TopLevelHtmlViewParams
from view import StandaloneHtmlView
from dropbox.callbacks import Handler
from dropbox.client.ui.common.uikit import MainMessageQueue, on_ui_thread, on_ui_thread_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.html_views.common import HtmlViewAffinityGroup
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
from dropbox.foundation.html_views.common.threading import on_html_view_thread_future, on_html_view_thread_returns_none
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.embeddable_host import EmbeddableViewHost
from dropbox.foundation.navigation_service.interface import NavigationVisibilityConfig, NavigationWindowType, ViewBridgeSerializable
from dropbox.foundation.navigation_service.view_manager_interface import EmbeddableViewFuture, StandaloneViewIdentifier, ViewInterface, ViewManagerInterface
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.collection_interface import WindowManagerDelegateCollectionInterface
from dropbox.foundation.performance import PerfSession, RACY_OPTIONAL_CHECKPOINT
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.foundation.stormcrow import NoStormcrowDataError
from dropbox.gui import assert_message_queue
from dropbox.repr_utils import easy_repr
from dropbox.threadutils import is_main_thread
from dropbox.trace import TRACE
_C = TypeVar('_C', bound = Context)
_EV = TypeVar('_EV', bound = EmbeddableViewMixin)
LOCAL_VIEW_RENDER_HIDDEN_OFFSCREEN_STORMCROW = 'desktop-local-view-render-hidden-offscreen'

class ActiveHtmlViewInfo(object):
    
    def __init__(self = None, logger = None, metadata = None, call_site_name = ('logger', 'HtmlViewLogger', 'metadata', 'StandaloneHtmlContentMetadata', 'call_site_name', 'Text', 'return', 'None')):
        self._logger = logger
        self._metadata = metadata
        self._call_site_name = call_site_name

    
    def __repr__(self = None):
        return easy_repr(self, 'logger', 'metadata', 'call_site_name', 'top_level_html_view_params')

    
    def __eq__(self = None, other = None):
