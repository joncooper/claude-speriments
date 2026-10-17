# Source Generated with Decompyle++
# File: embeddable_mixin.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod
from typing import Callable, Optional, Text, TypeVar
from  import HtmlViewLoadErrorType, HtmlViewLogger, HtmlViewLoggerEvent, HtmlViewStateMachine
from dropbox.callbacks import Handler
from dropbox.client.ui.common.uikit import on_ui_thread_future
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.common import StateMachineNavigationRequest
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
from dropbox.foundation.html_views.common.interface import HtmlViewContentErrorData, HtmlViewContentErrorType
from dropbox.foundation.html_views.common.threading import on_html_view_thread_future
from dropbox.foundation.html_views.common.top_level_html_view_params import TopLevelHtmlViewParams
from dropbox.foundation.navigation_service.view_interface import PRE_CONTENT_VIEW_ID, StandaloneViewIdentifier
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.gui import assert_message_queue
from dropbox.threading import Lock
from dropbox.trace import TRACE
Self = TypeVar('Self', bound = 'EmbeddableViewMixin')

class EmbeddableViewMixin:
    pass
# WARNING: Decompyle incomplete

