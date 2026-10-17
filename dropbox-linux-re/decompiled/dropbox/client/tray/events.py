# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

import contextlib
import functools
import uuid
from contextlib import contextmanager
from typing import Any, Callable, Dict, Generator, Mapping, NamedTuple, Optional, Text, Union
from mypy_extensions import TypedDict
from lib.crashpad.api import add_simple_annotation
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.product_span import ProductSpan
from dropbox.client.tray.tray_metrics.common import TrayMetrics
from dropbox.client.tray.tray_metrics.tray_action_metrics import TrayEmbedMetric, TrayFailureMetric, TrayMetric
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.components.desktop_components import DesktopComponent
from dropbox.enum_utils import auto, AutoLowerNameEnum, AutoNameEnum, StrAsPrefixlessValueTrait
from dropbox.event import report
from dropbox.event_names import ASSISTANT_CLIENT_TRAY_EVENTS, CLICK_TRAY
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.foundation.performance.perf_session import get_perf_timestamp
from dropbox.trace import TRACE
_tray_event_reporter: "Optional['TrayEventReporter']" = None
TrayEventSession = NamedTuple('TrayEventSession', [
    ('session_id', Text),
    ('timestamp', float)])
ANNOTATION_FORMAT = 'annotation_{}'
AnnotationValue = Union[(Text, int, float, bool)]
CombineFunction = Callable[([
    AnnotationValue,
    AnnotationValue], AnnotationValue)]
ViewCreateExtras = TypedDict('ViewCreateExtras', {
    'view_identifier': str,
    'error_stage': str }, total = False)
PopupCreateFailedExtras = TypedDict('PopupCreateFailedExtras', {
    'exc_type': str,
    'exc_value': str,
    'exc_trace': str })

class TrayEventName(AutoLowerNameEnum, StrAsPrefixlessValueTrait):
    ACCOUNT_SWITCH = auto()
    ADD_FILE_FROM_COMPUTER = auto()
    ADD_FOLDER_FROM_COMPUTER = auto()
    ADMIN_CONSOLE = auto()
    CREATE_FILE = auto()
    CREATE_FOLDER = auto()
    FIX_INOTIFY = auto()
    GEAR_MENU = auto()
    GET_MORE_SPACE = auto()
    HELP_CENTER = auto()
    IMPORTING = auto()
    LAUNCH_WEBSITE = auto()
    LINK_ACCOUNT = auto()
    LINK_CLIENT = auto()
    OPEN_DROPBOX_FOLDER = auto()
    OPEN_FOLDER = auto()
    OPEN_PERSONAL_DROPBOX = auto()
    OPEN_UPGRADE = auto()
    OUT_OF_SPACE = auto()
    PAUSE = auto()
    PREFERENCES = auto()
    QUIT = auto()
    QUIT_CONFIRM = auto()
    QUIT_CANCEL = auto()
    RESUME = auto()
    SEARCH_QUERY_STARTED = auto()
    SHOWN_UNLINKED_VIEW = auto()
    SIGN_IN = auto()
    SNOOZE_NOTIFICATIONS = auto()
    SNOOZE_SYNC = auto()
    TAB_CHANGE = auto()
    TRAY_MENU_SHOWN = auto()
    TRAY_POPUP_HIDDEN = auto()
    TRAY_POPUP_SHOWN = auto()
    TRAY_POPUP_TRIGGERED = auto()
    TURN_ON_NOTIFICATIONS = auto()
    VIEW_MORE_RESULTS = auto()
    VIEW_SYNC_ISSUES = auto()
    OPEN_INVITE_BUTTON_FAILURE = auto()
    OS_CONSENT = auto()
    from_string = (lambda event_name = None: try:
TrayEventName(event_name)except ValueError:
None)()


class TrayEventTrigger(AutoLowerNameEnum, StrAsPrefixlessValueTrait):
    BUTTON = auto()
    SNOOZE_DROPBOX_MENU = auto()
    GEAR_MENU = auto()
    FALLBACK_MENU = auto()
    from_string = (lambda event_trigger = None: try:
TrayEventTrigger(event_trigger)except ValueError:
None)()


class TrayEventFeature(AutoLowerNameEnum, StrAsPrefixlessValueTrait):
    CHROME = auto()
    ENG = auto()
    SEARCH = auto()


class TrayMenuReason(AutoNameEnum):
    UNKNOWN = auto()
    USER_INITIATED = auto()
    TRAY_POPUP_ERROR = auto()


class TrayEventReporter(object):
    instance = (lambda : pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self = None):
        self._curr_session = None
        self._prev_session = None
        self._annotations = { }
        self._dismiss_perf_session = None
        self.tray_style = ''

    session_annotations = (lambda self = None: self._annotations)()
    
    def new_tray_session(self = None):
        if self._curr_session:
            TRACE('Detected an existing tray session.')
            self.end_tray_session(tag = 'existing_session')
        self._curr_session = TrayEventSession(uuid.uuid4().hex, get_perf_timestamp())
        self._annotations = dict()
        time_since_previous = self._curr_session.timestamp - self._prev_session.timestamp if self._prev_session else 0
        previous_session_id = self._prev_session.session_id if self._prev_session else ''
        self.report_to_assistant_tray('tray_session_start', extras = dict(previous_session_id = previous_session_id, time_since_previous_session = Text(float(time_since_previous))))

    
    def end_tray_session(self = None, tag = None):
        if not self._curr_session:
            TRACE('Ended without an existing tray session.')
        duration = float(get_perf_timestamp() - self._curr_session.timestamp) if self._curr_session else 0
        extra_params = self._annotations.items()()
        extra_params['tag'] = tag
        extra_params['duration'] = Text(duration)
        self.report_to_assistant_tray('tray_session_end', extras = extra_params)
        if self._curr_session:
            TrayMetrics.log_tray_metric_with_tags(TrayMetric.TRAY_SESSION_LENGTH.value, { }, duration)
        self._prev_session = self._curr_session
        self._curr_session = None
        self._dismiss_perf_session = None

    
    def current_session_timestamp(self = None):
        if not self._curr_session:
            return None
        return None._curr_session.timestamp

    
    def current_session_id(self = None):
        if not self._curr_session:
            return None
        return None._curr_session.session_id

    
    def reset_dismiss_tracker(self = None, last_action = None, extra = None):
        self._dismiss_perf_session = PerfSession('tray_dismiss', 'TrayContentType.ASSISTANT_VIEW', log_to_amp_namespace = PerfSessionAmpLoggingNamespace.TRAY)
        str_extra = extra.items()()
        str_extra['last_action'] = last_action
        self._dismiss_perf_session.add_extras(str_extra)

    
    def commit_dismiss_tracker(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def end_dismiss_tracker(self = None):
        if self._dismiss_perf_session:
            self._dismiss_perf_session.add_extra('tray_session_id', str(self.current_session_id()))
            self._dismiss_perf_session.end()
            self._dismiss_perf_session = None
            return None

    show_unlinked_view = (lambda cls = None: cls.instance().report_to_assistant_tray('show_unlinked_view'))()
    show_prompt = (lambda cls = None: cls.instance().report_to_assistant_tray('show_prompt'))()
    confirm_prompt = (lambda cls = None: cls.instance().report_to_assistant_tray('confirm_prompt'))()
    dismiss_prompt = (lambda cls = None: cls.instance().report_to_assistant_tray('dismiss_prompt'))()
    embedded_view_create_begin = (lambda cls = None, extra = None: cls.instance().report_to_assistant_tray('embedded_view_begin', extras = extra, feature = TrayEventFeature.ENG)TrayMetrics.log_tray_metric_with_tags(TrayEmbedMetric.TRAY_EMBED_TRIGGER.value, { }, 1))()
    embedded_view_create_success = (lambda cls = None, extra = None: cls.instance().report_to_assistant_tray('embedded_view_success', extras = extra, feature = TrayEventFeature.ENG)TrayMetrics.log_tray_metric_with_tags(TrayEmbedMetric.TRAY_EMBED_SUCCESS.value, { }, 1))()
    embedded_view_create_failed = (lambda cls = None, extra = None: cls.instance().report_to_assistant_tray('embedded_view_failed', extras = extra, feature = TrayEventFeature.ENG)TrayMetrics.log_tray_metric_with_tags(TrayEmbedMetric.TRAY_EMBED_FAILURE.value, {
'error_stage': extra.get('error_stage', 'unknown') }, 1))()
    content_view_broken = (lambda cls = None: cls.instance().report_to_assistant_tray('tray_content_broken', feature = TrayEventFeature.ENG))()
    missing_popup_controller = (lambda cls = None: cls.instance().report_to_assistant_tray('missing_popup_controller', feature = TrayEventFeature.ENG)TrayMetrics.log_tray_metric_with_tags(TrayFailureMetric.TRAY_MISSING_POPUP_CONTROLLER.value, { }, 1))()
    new_session_context = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()()
    new_session = (lambda cls = None: cls.instance().new_tray_session())()
    end_session = (lambda cls = None: cls.instance().end_tray_session())()
    menu_shown = (lambda cls = None, reason = None: cls.instance().report_to_assistant_tray('tray_menu_shown', extras = {
'reason': str(reason) })TrayMetrics.log_tray_metric_with_tags(str(TrayMetric.SHOWN_MENU), {
'reason': str(reason) }, 1)report('tray-menu'))()
    popup_create_failed = (lambda cls = None, extra = None: cls.instance().report_to_assistant_tray('tray_popup_create_failed', extras = extra, feature = TrayEventFeature.ENG))()
    popup_triggered = (lambda cls = None, reason = None: cls.instance().report_to_assistant_tray(str(TrayEventName.TRAY_POPUP_TRIGGERED), extras = {
'reason': str(reason) })TrayMetrics.log_tray_metric_with_tags(str(TrayMetric.TRIGGERED_TRAY), {
'reason': str(reason) }, 1))()
    popup_shown = (lambda cls = None, extra = None: cls.instance().report_to_assistant_tray(str(TrayEventName.TRAY_POPUP_SHOWN), extras = extra)if 'active_tray_content_view' not in extra:
report_bad_assumption('TrayEventReporter.popup_shown called without active_tray_content_view extra')TrayMetrics.log_tray_metric_with_tags(str(TrayMetric.SHOWN_TRAY), {
'current_visible_content': extra.get('active_tray_content_view', 'MISSING') }, 1)report('tray-popup', sticky_not = extra['sticky_not']))()
    popup_hidden = (lambda cls = None: cls.instance().report_to_assistant_tray(str(TrayEventName.TRAY_POPUP_HIDDEN)))()
    os_window_did_show = (lambda cls = None: add_simple_annotation('last_tray_visibility_action', 'show')cls.instance().report_to_assistant_tray('tray_os_window_did_show', feature = TrayEventFeature.ENG))()
    os_window_did_hide = (lambda cls = None: add_simple_annotation('last_tray_visibility_action', 'hide')cls.instance().report_to_assistant_tray('tray_os_window_did_hide', feature = TrayEventFeature.ENG)cls.instance().end_dismiss_tracker())()
    os_window_will_hide = (lambda cls = None: cls.instance().commit_dismiss_tracker())()
    os_menu_did_show = (lambda cls = None: cls.instance().report_to_assistant_tray('tray_os_menu_did_show', feature = TrayEventFeature.ENG))()
    os_menu_did_hide = (lambda cls = None: cls.instance().report_to_assistant_tray('tray_os_menu_did_hide', feature = TrayEventFeature.ENG)cls.instance().end_dismiss_tracker())()
    popover_created = (lambda cls = None, popover_name = None: cls.instance().report_to_assistant_tray('created_tray_popover', extras = {
'popover_name': popover_name }, feature = TrayEventFeature.ENG))()
    content_refreshed = (lambda cls = None, extra = None: ctxtmgr = contextlib.nullcontext() if cls.tray_session_id() else cls.new_session_context()ctxtmgrcls.instance().report_to_assistant_tray('tray_content_refreshed', extras = extra)None(None, None)Nonewith None:
if not None:
pass)()
    set_tray_style = (lambda cls = None, tray_style = None: instance = cls.instance()instance.tray_style = tray_style)()
    get_common_extras = (lambda cls = None: instance = cls.instance()common_extras = { }common_extras['tray_style'] = instance.tray_stylecommon_extras)()
    popup_reentrant = (lambda cls = None: cls.instance().report_to_assistant_tray('tray_popup_reentrant', feature = TrayEventFeature.ENG))()
    popup_debounced_reentrancy = (lambda cls = None: cls.instance().report_to_assistant_tray('tray_popup_debounced_reentrancy', feature = TrayEventFeature.ENG))()
    bad_render = (lambda cls = None, message = None, extra = classmethod: extra['message'] = messagecls.instance().report_to_assistant_tray('render_bad_assumption', extras = extra, feature = TrayEventFeature.ENG))()
    tray_session_timestamp = (lambda cls = None: cls.instance().current_session_timestamp())()
    tray_session_id = (lambda cls = None: cls.instance().current_session_id())()
    add_annotation = (lambda cls = None, name = None, new_value = classmethod, combine = (None,): pass# WARNING: Decompyle incomplete
)()
    report_to_assistant_tray = (lambda cls, event_name = None, action_location = None, extras = classmethod, account = (None, None, None, TrayEventFeature.CHROME), feature = ('event_name', 'str', 'action_location', 'Optional[str]', 'extras', 'Optional[Mapping[Text, Any]]', 'account', 'Optional[AccountInterface]', 'feature', 'Optional[TrayEventFeature]', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()


def report_tray_click(event_name = None, label = None, click_location = None, **extras):
    pass
# WARNING: Decompyle incomplete


def track_click(event_name = None, label = None, click_location = None, **extras):
    pass
# WARNING: Decompyle incomplete

