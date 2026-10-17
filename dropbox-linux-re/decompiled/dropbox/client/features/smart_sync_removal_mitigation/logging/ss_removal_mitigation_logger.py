# Source Generated with Decompyle++
# File: ss_removal_mitigation_logger.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Any, Dict
from dropbox import event_names
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.metrics.ss_removal_mitigation_events import SSRemovalMitigationEvent as SSRMEvent, SSRemovalMitigationExtraField as SSRMExtraField, SSRemovalMitigationWarningActionTaken as SSRMWarningActionTaken

class SSRemovalMitigationLogger:
    log_aef_event = (lambda cls = None, event = None, extra = classmethod: cls._log(event.value, extra))()
    log_dp_education_launched = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_EDUCATION_EXPOSED.value, extras))()
    log_dp_education_not_persisted = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_EDUCATION_NOT_PERSISTED.value, extras))()
    log_dp_education_acknowledged = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_EDUCATION_ACKNOWLEDGED.value, extras))()
    log_dp_education_learn_more_clicked = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_EDUCATION_LEARN_MORE_CLICKED.value, extras))()
    log_dp_sticky_exposed = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_STICKY_EXPOSED.value, extras))()
    log_dp_sticky_acknowledged = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_STICKY_ACKNOWLEDGED.value, extras))()
    log_dp_sticky_learn_more_clicked = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_STICKY_LEARN_MORE_CLICKED.value, extras))()
    log_dp_context_menu_warning_shown = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_CONTEXT_MENU_WARN_DISPLAYED.value, extras))()
    log_dp_context_menu_warning_action_taken = (lambda cls = None, action = None, dont_shown_again_checked = classmethod: extras = {
SSRMExtraField.DONT_SHOW_AGAIN_CHECKED.value: str(dont_shown_again_checked),
SSRMExtraField.ACTION_TAKEN.value: action.value }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_CONTEXT_MENU_WARN_ACTION.value, extras))()
    log_dp_pref_changed_warning_shown = (lambda cls = None: extras = { }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_PREF_CHANGED_WARN_DISPLAYED.value, extras))()
    log_dp_pref_changed_warning_action_taken = (lambda cls = None, action = None: extras = {
SSRMExtraField.ACTION_TAKEN.value: action.value }cls._log(SSRMEvent.DEGRADED_PLACEHOLDER_PREF_CHANGED_WARN_ACTION.value, extras))()
    _log = (lambda cls = None, event = None, extra = classmethod: try:
if not extra:
report(event_names.SS_REMOVAL_MITIGATION, event = event, extra = sanitize_event_extra_dict({ }))Noneexcept Exception:
sanitize_event_extra_dictreport_exception(severity = Severity.WARN, component = DesktopComponent.INFINITE)None)()

