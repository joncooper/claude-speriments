# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import binascii
import os
from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Dict, NamedTuple, Optional, Text
from apex.metrics import Metric
from six import add_metaclass, iteritems
from build_number import VERSION
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.ui.common.uikit import FrameworkProps
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import LOCAL_VIEWS_EVENT, LOCAL_VIEWS_RESTRICTED_EVENT, POPOVERS_EVENT, POPOVERS_RESTRICTED_EVENT, SERVER_VIEWS_EVENT, STANDALONE_SERVER_VIEWS_RESTRICTED_EVENT
from dropbox.foundation.context import ContextInterface
from dropbox.foundation.platform_version import PLATFORM_VERSION
from dropbox.functions import make_unicode
from dropbox.platform import platform
from dropbox.trace import TRACE

class HtmlViewLoggerEvent(Enum):
    _DEBUG_DO_NOT_USE = 'debug_do_not_use'
    ACCOUNT_ERROR = 'account_error'
    BEFORE_WINDOW_CREATED = 'before_window_created'
    CONTENT_ID_SET = 'content_id_set'
    SYSTEM_SUSPENDED_WHILE_LOADING = 'system_suspended_while_loading'
    PRELOADED_VIEW_ACTIVATED = 'preloaded_view_activated'
    PRELOADED_VIEW_DISCARDED = 'preloaded_view_discarded'
    EMBEDDABLE_QML_VIEW_CREATED = 'embeddable_qml_view_created'
    EMBEDDABLE_VIEW_CREATION_TRIGGERED = 'embeddable_view_creation_triggered'
    EMBEDDABLE_VIEW_CREATED = 'embeddable_view_created'
    EMBEDDABLE_VIEW_FAILED_TO_CREATE = 'embeddable_view_failed_to_create'
    EMBEDDABLE_VIEW_DESTROYED = 'embeddable_view_destroyed'
    EMBEDDABLE_VIEW_DESTROYING = 'embeddable_view_destroying'
    EMBEDDABLE_VIEW_WEBCONTENTS_CREATED = 'embeddable_view_webcontents_created'
    FACTORY_CONSTRUCTING_WINDOW = 'factory_constructing_window'
    FEATURE_ENABLED = 'feature_enabled'
    INIT_SUCCESSFUL = 'init_successful'
    INVALID_LOAD_PROGRESS = 'invalid_load_progress_report'
    INVALID_STATE_TRANSITION = 'invalid_state_transition'
    IS_ALLOWED = 'is_allowed'
    JSB_TRANSPORT_FAILED_TO_OPEN = 'js_bridge_transport_failed_to_open'
    ON_SUPPORTED_PLATFORM = 'on_supported_platform'
    ON_SUPPORTED_HARDWARE = 'on_supported_hardware'
    POPOVER_CREATION_TRIGGERED = 'popover_creation_triggered'
    POPOVER_CREATION_SUCCEEDED = 'popover_creation_succeeded'
    POPOVER_CREATION_FAILED = 'popover_creation_failed'
    POPOVER_CONTENT_LOAD_TRIGGERED = 'popover_content_load_triggered'
    POPOVER_CONTENT_LOAD_SUCCEEDED = 'popover_content_load_succeeded'
    POPOVER_CONTENT_LOAD_FAILED = 'popover_content_load_failed'
    POPOVER_INITIAL_SHOW_TRIGGERED = 'popover_initial_show_triggered'
    POPOVER_INITIAL_SHOW_SUCCEEDED = 'popover_initial_show_succeeded'
    POPOVER_INITIAL_SHOW_FAILED = 'popover_initial_show_failed'
    POPOVER_SHOW_TRIGGERED = 'popover_show_triggered'
    POPOVER_SHOW_SUCCEEDED = 'popover_show_succeeded'
    POPOVER_SHOW_FAILED = 'popover_show_succeeded'
    PROXY_UNSUPPORTED = 'proxy_unsupported'
    MAIN_FRAME_CERTIFICATE_ISSUE = 'main_frame_certificate_issue'
    CONTENT_BAD_ASSUMPTION = 'content_bad_assumption'
    CONTENT_FAILED_TO_LOAD = 'content_failed_to_load'
    CONTENT_FAILED_TO_LOAD_NO_INTERNET = 'content_failed_to_load_no_internet'
    CONTENT_FAILED_TO_LOAD_TRANSIENT = 'content_failed_to_load_transient'
    CONTENT_NETWORK_ERROR = 'content_network_error'
    CONTENT_HTTP_ERROR = 'content_http_error'
    CONTENT_CERTIFICATE_ISSUE = 'content_certificate_issue'
    CONTENT_CSP_ERROR = 'content_csp_error'
    CONTENT_I18N_ERROR = 'content_i18n_error'
    CONTENT_ISSUE = 'content_issue'
    CONTENT_JAVASCRIPT_ERROR = 'content_js_error'
    CONTENT_LOADED = 'content_loaded'
    CONTENT_LOADED_TRANSIENT = 'content_loaded_transient'
    CONTENT_LOADING = 'content_loading'
    CONTENT_LOAD_DISALLOWED = 'content_load_disallowed'
    CONTENT_LOAD_NAVIGATION_COMMITTED = 'content_load_navigation_committed'
    CONTENT_LOAD_UNEXPECTED_NAVIGATION_COMMITTED = 'content_load_unexpected_navigation_committed'
    CONTENT_LOAD_RECOVERED = 'content_load_recovered'
    CONTENT_LOAD_SKIPPED = 'content_load_skipped'
    CONTENT_LOAD_TRIGGERED = 'content_load_triggered'
    CONTENT_LOAD_REQUESTED_WHILE_LOADING = 'content_load_requested_while_loading'
    CONTENT_LOAD_TIMEOUT = 'content_load_timeout'
    CONTENT_LOAD_PROGRESS = 'content_load_progress'
    CONTENT_LOAD_PROGRESS_COMPLETED = 'content_load_progress_completed'
    CONTENT_LOAD_PLATFORM_ABORT_REQUESTED = 'content_load_platform_abort_requested'
    CONTENT_LOAD_PLATFORM_REQUESTED = 'content_load_platform_requested'
    CONTENT_REQUESTED_CROSS_ORIGIN_SUB_RESOURCE = 'content_requested_cross_origin_sub_resource'
    CONTENT_FEATURE_FAILED_TO_LOAD = 'content_feature_failed_to_load'
    CONTENT_FEATURE_LOADED = 'content_feature_loaded'
    CONTENT_FEATURE_LOAD_CANCELLED = 'content_feature_load_cancelled'
    CONTENT_FEATURE_LOAD_TRIGGERED = 'content_feature_load_triggered'
    CONTENT_RENDER_FAILED = 'content_render_failed'
    CONTENT_RENDER_FAILED_FOREGROUND_UNKNOWN = 'content_render_failed_foreground_unknown'
    CONTENT_RENDER_FAILED_FOREGROUND = 'content_render_failed_foreground'
    RENDERER_PROCESS_CRASHED = 'renderer_process_crashed'
    JS_BRIDGE_ERROR = 'js_bridge_error'
    REACT_FORMAT_ERROR = 'react_format_error'
    JS_PY_DPI_MISMATCH = 'js_py_dpi_mismatch'
    WINDOW_CLOSED = 'window_closed'
    WINDOW_CLOSE_PENDING = 'window_close_pending'
    WINDOW_CONTENT_SET = 'window_content_set'
    WINDOW_CREATED = 'window_created'
    WINDOW_DISPLAYED = 'window_displayed'
    WINDOW_FAILED_TO_CREATE = 'window_failed_to_create'
    WINDOW_RETRIGGERED = 'window_retriggered'
    WINDOW_TRIGGERED = 'window_triggered'
    WINDOW_SHOWN = 'window_shown'
    WINDOW_HIDDEN = 'window_hidden'
    WINDOW_EMBEDDED_VIEW = 'window_embedded_view'
    WINDOW_EXTRACTED_VIEW = 'window_extracted_view'


def HtmlViewLoggerTableConfiguration():
    '''HtmlViewLoggerTableConfiguration'''
    pass

HtmlViewLoggerTableConfiguration = <NODE:27>(HtmlViewLoggerTableConfiguration, 'HtmlViewLoggerTableConfiguration', NamedTuple('HtmlViewLoggerTableConfiguration', [
    ('default', str),
    ('restricted', str)]))
HtmlViewLoggerStrategy = <NODE:12>()

class ServerViewLoggerStrategy(HtmlViewLoggerStrategy):
    pass
# WARNING: Decompyle incomplete


class LocalViewLoggerStrategy(HtmlViewLoggerStrategy):
    pass
# WARNING: Decompyle incomplete

PopoverLoggerStrategy = LocalViewLoggerStrategy

class HtmlViewLogger:
    _SESSION_ID_LEN = 32
    _EVENT_SUPERCATEGORY_MAP = {
        HtmlViewLoggerEvent.CONTENT_HTTP_ERROR: [
            HtmlViewLoggerEvent.CONTENT_FAILED_TO_LOAD],
        HtmlViewLoggerEvent.MAIN_FRAME_CERTIFICATE_ISSUE: [
            HtmlViewLoggerEvent.CONTENT_FAILED_TO_LOAD],
        HtmlViewLoggerEvent.CONTENT_NETWORK_ERROR: [
            HtmlViewLoggerEvent.CONTENT_FAILED_TO_LOAD] }
    STANDALONE_SERVER_VIEWS_TABLES = HtmlViewLoggerTableConfiguration(SERVER_VIEWS_EVENT, STANDALONE_SERVER_VIEWS_RESTRICTED_EVENT)
    LOCAL_VIEWS_TABLES = HtmlViewLoggerTableConfiguration(LOCAL_VIEWS_EVENT, LOCAL_VIEWS_RESTRICTED_EVENT)
    POPOVERS_TABLES = HtmlViewLoggerTableConfiguration(POPOVERS_EVENT, POPOVERS_RESTRICTED_EVENT)
    AMP_NAMESPACE = 'desktop_ui_framework'
    create_server_view_logger = (lambda trigger = None, base_url = None, context = staticmethod, framework_props = ('trigger', 'Text', 'base_url', 'Text', 'context', 'ContextInterface', 'framework_props', 'FrameworkProps', 'return', "'HtmlViewLogger'"): logger = HtmlViewLogger(HtmlViewLogger.STANDALONE_SERVER_VIEWS_TABLES, {
'base_url': base_url,
'server_view_session': make_unicode(binascii.hexlify(os.urandom(HtmlViewLogger._SESSION_ID_LEN))),
'framework_name': framework_props.web_framework }, trigger, ServerViewLoggerStrategy(context))logger)()
    create_local_view_logger = (lambda trigger = None, base_url = None, context = staticmethod, framework_props = ('trigger', 'Text', 'base_url', 'Text', 'context', 'ContextInterface', 'framework_props', 'FrameworkProps', 'return', "'HtmlViewLogger'"): logger = HtmlViewLogger(HtmlViewLogger.LOCAL_VIEWS_TABLES, {
'base_url': base_url,
'html_view_session': make_unicode(binascii.hexlify(os.urandom(HtmlViewLogger._SESSION_ID_LEN))),
'framework_name': framework_props.web_framework }, trigger, LocalViewLoggerStrategy(context))logger)()
    create_popover_logger = (lambda trigger = None, base_url = None, context = staticmethod, framework_props = ('trigger', 'Text', 'base_url', 'Text', 'context', 'ContextInterface', 'framework_props', 'FrameworkProps', 'return', 'HtmlViewLogger'): logger = HtmlViewLogger(HtmlViewLogger.POPOVERS_TABLES, {
'base_url': base_url,
'html_view_session': make_unicode(binascii.hexlify(os.urandom(HtmlViewLogger._SESSION_ID_LEN))),
'framework_name': framework_props.web_framework }, trigger, PopoverLoggerStrategy(context))logger)()
    
    def __init__(self, table_config = None, logging_configuration = None, trigger = None, strategy = ('table_config', 'HtmlViewLoggerTableConfiguration', 'logging_configuration', 'Dict[Text, Text]', 'trigger', 'Text', 'strategy', 'HtmlViewLoggerStrategy', 'return', 'None')):
        self._data = dict(trigger = trigger, base_url = '', build_number = VERSION, platform = platform, platform_version = PLATFORM_VERSION, load_session = '')
        for key, val in iteritems(logging_configuration):
            self._data[key] = val
            self._content_id = None
            self._component = DesktopComponent.HTML_VIEWS
            self._trigger = trigger
            self._table_config = table_config
            self._strategy = strategy
            self._machine_id = str(UNSAFE_get_raw_machine_uuid())
            self._view_session = self._strategy.get_logger_session(logging_configuration)
            self._preloaded_view_activated = False
            return None

    view_session = (lambda self = None: self._view_session)()
    
    def report_event(self = None, event_name = None, restricted = None, **extra):
        self._report_amp_event(event_name)
        for key, val in iteritems(extra):
            if not isinstance(val, Text):
                extra[key] = Text(val)
            event_names = [
                event_name]
            if event_name in self._EVENT_SUPERCATEGORY_MAP:
                event_names.extend(self._EVENT_SUPERCATEGORY_MAP[event_name])
        if event_name == HtmlViewLoggerEvent.PRELOADED_VIEW_ACTIVATED:
            self._preloaded_view_activated = True
    # WARNING: Decompyle incomplete

    
    def _report_event(self = None, event_name = None, data = None, table_name = ('event_name', 'HtmlViewLoggerEvent', 'data', 'Dict[Text, object]', 'table_name', 'Text', 'extra', 'object', 'return', 'None'), **extra):
        data['event_name'] = event_name.value
        data[self._strategy.event_details_column_name] = extra
    # WARNING: Decompyle incomplete

    
    def _report_amp_event(self = None, event_name = None):
        tags = { }
        tags['ci_type'] = os.environ.get('CI_TYPE', 'none')
        tags['preloaded_view_activated'] = str(self._preloaded_view_activated)
        if not self.content_id:
            tags['content_id'] = 'UNKNOWN'
            if not self._trigger:
                tags['trigger'] = 'UNKNOWN'
        tags['component'] = str(self.component.name) if self.component else 'UNKNOWN'
        reporter = self._strategy.context.metrics_reporter.child(tags)
        full_event_name = f'''{self._strategy.metrics_path_prefix}{event_name.value}'''
        counter = reporter.create_counter(Metric(self.AMP_NAMESPACE, full_event_name), { })
        counter.increment(1)
        counter.record()
        machine_set_event_name = f'''{self._strategy.metrics_path_prefix}{event_name.value}/machine_ids'''
        machine_set = reporter.create_set(Metric(self.AMP_NAMESPACE, machine_set_event_name), { })
        machine_set.observe(self._machine_id)

    
    def start_new_session(self = None, base_url = None):
        self._data['base_url'] = base_url
        self._data['load_session'] = make_unicode(binascii.hexlify(os.urandom(self._SESSION_ID_LEN)))
        TRACE('HtmlViewLogger load_session=%r, url=%r', self._data['load_session'], base_url)

    
    def set_content_metadata(self = None, content_id = None, component = None):
        self._content_id = content_id
        self._component = component

    component = (lambda self = None: self._component)()
    content_id = (lambda self = None: self._content_id)()

