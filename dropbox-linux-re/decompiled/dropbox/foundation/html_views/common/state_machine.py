# Source Generated with Decompyle++
# File: state_machine.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from enum import Enum
from hashlib import md5
from time import monotonic
from typing import Callable, Dict, List, NamedTuple, Optional, Text
from urllib.parse import urlparse
from six import add_metaclass, iteritems
from errors import ChromiumErrorCategory, ChromiumErrorCode
from interface import HtmlViewCertificateErrorData, HtmlViewContentErrorData, HtmlViewContentErrorType, HtmlViewCSPViolationErrorData, HtmlViewJavaScriptErrorData, HtmlViewJavaScriptErrorSource, HtmlViewJavaScriptErrorType, HtmlViewLoadErrorType
from logging import HtmlViewLogger, HtmlViewLoggerEvent
from dropbox.callbacks import create_weakref_callback, Handler
from dropbox.client.system_status.system_status_monitor_interface import SystemStatusMonitorInterface
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client.ui.ui_timer import UITimerFactory
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.common.threading import assert_on_ui_thread, UiEventFuture
from dropbox.foundation.html_views.metrics.bridge_gen.bridge_interface_internal_perf_session_checkpoints import InternalPerfSessionCheckpointsBridgeInterface
from dropbox.foundation.performance.perf_session import PerfSession
from dropbox.foundation.scheme_handler.types import CustomSchemeHandlerResult, CustomSchemeUrlRequest
from dropbox.threading import Lock
from dropbox.trace import TRACE
StateMachineNavigationRequest = NamedTuple('StateMachineNavigationRequest', [
    ('path', Text),
    ('parameters', List[Text])])
StartNavigationQueueEntry = NamedTuple('StartNavigationQueueEntry', [
    ('request', StateMachineNavigationRequest),
    ('start_request_func', Callable[([
        Text], None)]),
    ('abort_request_func', Callable[([], None)])])
HtmlViewErrorHandler = Callable[([
    HtmlViewLoadErrorType,
    HtmlViewLoggerEvent,
    str,
    int], None)]
HtmlViewLoadRequestedHandlers = Callable[([], None)]

class HtmlViewState(Enum):
    IDLE = 0
    LOAD_REQUESTED = 1
    LOAD_COMMITTED = 2
    LOADED = 3
    ERROR = 4
    ABORTED = 5
    TERMINATING = 6
    TERMINATED = 7


class _FirstLoadState(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    DONE = 2


class StateTransitionResult(Enum):
    ALLOWED = 0
    DISALLOWED = 1


def BlockNavigationResult():
    '''BlockNavigationResult'''
    allow = (lambda : BlockNavigationResult(True, 'All checks passed'))()
    block_invalid_scheme = (lambda scheme = None: BlockNavigationResult(False, 'Invalid scheme: %r' % scheme))()
    block_invalid_host = (lambda host = None: BlockNavigationResult(False, 'Invalid host: %r' % host))()
    block_invalid_path = (lambda path = None: BlockNavigationResult(False, 'Invalid path: %r' % path))()

BlockNavigationResult = <NODE:27>(BlockNavigationResult, 'BlockNavigationResult', NamedTuple('BlockNavigationResult', [
    ('is_allowed', bool),
    ('reason', str)]))
HtmlViewStateMachineStrategy = <NODE:12>()

class HtmlViewStateMachine(object):
    LOADING_STATES = (HtmlViewState.LOAD_REQUESTED, HtmlViewState.LOAD_COMMITTED)
    _MAX_RETRY_ATTEMPTS = 2
    _STATE_TRANSITIONS: 'Dict[HtmlViewState, List[HtmlViewState]]' = {
        HtmlViewState.TERMINATING: [
            HtmlViewState.TERMINATED],
        HtmlViewState.TERMINATED: [],
        HtmlViewState.ABORTED: [
            HtmlViewState.LOAD_REQUESTED,
            HtmlViewState.ERROR,
            HtmlViewState.TERMINATED],
        HtmlViewState.ERROR: [
            HtmlViewState.LOAD_REQUESTED,
            HtmlViewState.LOAD_COMMITTED,
            HtmlViewState.ABORTED,
            HtmlViewState.TERMINATED],
        HtmlViewState.LOADED: [
            HtmlViewState.LOAD_REQUESTED,
            HtmlViewState.LOAD_COMMITTED,
            HtmlViewState.TERMINATED],
        HtmlViewState.LOAD_COMMITTED: [
            HtmlViewState.LOADED,
            HtmlViewState.ABORTED,
            HtmlViewState.ERROR,
            HtmlViewState.LOAD_REQUESTED,
            HtmlViewState.TERMINATING],
        HtmlViewState.LOAD_REQUESTED: [
            HtmlViewState.LOAD_REQUESTED,
            HtmlViewState.LOAD_COMMITTED,
            HtmlViewState.ABORTED,
            HtmlViewState.ERROR,
            HtmlViewState.TERMINATING],
        HtmlViewState.IDLE: [
            HtmlViewState.LOAD_REQUESTED,
            HtmlViewState.TERMINATED] }
    
    def __init__(self, logger = None, strategy = None, system_status_monitor = None, perf_session = ('logger', 'HtmlViewLogger', 'strategy', 'HtmlViewStateMachineStrategy', 'system_status_monitor', 'SystemStatusMonitorInterface', 'perf_session', 'Optional[PerfSession]', 'return', 'None')):
        self._logger = logger
        self._strategy = strategy
        self._status_monitor = system_status_monitor
        self._status_monitor.add_suspend_callback(self._on_system_suspend)
        self._status_monitor.add_resume_callback(self._on_system_resume)
        self._perf_session = perf_session
        self._request_timer = UITimerFactory.create()
        self._timer_callback = create_weakref_callback(self, HtmlViewStateMachine._handle_request_timeout)
        self._request = None
        self._request_url = None
        self._state = HtmlViewState.IDLE
        self._first_load_state = _FirstLoadState.NOT_STARTED
        self._abort_request_func = None
        self._start_request_func = None
        self._start_request_time = None
        self._request_retry_allowed = False
        self._request_retry_attempts = 0
        self._error_handlers = Handler()
        self._load_requested_handlers = Handler()
        self._navigation_success_handlers = Handler()
        self._load_progress_handlers = Handler()
        self._content_error_handlers = Handler()
        self._popup_handlers = Handler()
        self._num_loads_requested = 0
        self._num_loads_committed_after_request = 0
        self._terminated_future = UiEventFuture()
        self._terminated_future.ground(component = DesktopComponent.HTML_VIEWS)
        self._close_state_lock = Lock()
        self._current_close_future = None
        self._is_close_complete = False

    strategy = (lambda self = None: self._strategy)()
    logger = (lambda self = None: self._logger)()
    
    def block_invalid_navigation(self, url_scheme = None, url_host = None, path = None, is_main_frame = ('url_scheme', 'str', 'url_host', 'str', 'path', 'str', 'is_main_frame', 'bool', 'return', 'bool')):
        pass
    # WARNING: Decompyle incomplete

    
    def override_request_headers(self = None, url = None, is_main_frame = None, header_dict = ('url', 'Text', 'is_main_frame', 'bool', 'header_dict', 'Dict[Text, Text]', 'return', 'None')):
        if self._state == HtmlViewState.TERMINATED:
            return None
    # WARNING: Decompyle incomplete

    
    def process_custom_protocol_request(self = None, request = None, completion_handler = None):
        self._strategy.process_custom_protocol_request(request, completion_handler)

    
    def start_navigation(self = None, request = None, start_request_func = None, abort_request_func = ('request', 'StateMachineNavigationRequest', 'start_request_func', 'Callable[[Text], None]', 'abort_request_func', 'Callable[[], None]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _do_start_navigation(self = None, request = None, start_request_func = None, abort_request_func = ('request', 'StateMachineNavigationRequest', 'start_request_func', 'Callable[[Text], None]', 'abort_request_func', 'Callable[[], None]', 'return', 'None')):
        self._logger.start_new_session(request.path)
        self._logger.report_event(HtmlViewLoggerEvent.CONTENT_LOAD_TRIGGERED, path = request.path)
        if self._try_state_transition(HtmlViewState.LOAD_REQUESTED) == StateTransitionResult.ALLOWED:
            self._start_request_func