# Source Generated with Decompyle++
# File: file_locking_metrics_logger.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Union
from dropbox import event_names
from dropbox.client.transient_simple_metric.allowed_simple_metric import SimpleMetricCategoryWhitelist
from dropbox.client.transient_simple_metric.transient_simple_metric import report_transient_simple_metric
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.metrics.file_locking import FileLockingEvent

class FileLockingLogger:
    _FILE_LOCKING_EVENT_ALLOWED_KEYS = {
        'ns_id',
        'source',
        'lock_status',
        'is_placeholder'}
    SIMPLE_EVENT_FL_LOCKED_ACCESSED_BY_COLLABORATOR = 'file-locking-locked-accessed-by-collaborator'
    SIMPLE_EVENT_FL_CONTEXT_MENU_LOCK_CLICKED = 'file-locking-context-menu-lock-clicked'
    SIMPLE_EVENT_FL_CONTEXT_MENU_UNLOCK_CLICKED = 'file-locking-context-menu-unlock-clicked'
    SIMPLE_EVENT_FL_CONTEXT_MENU_REQUEST_UNLOCK = 'file-locking-context-menu-request-unlock-clicked'
    SIMPLE_EVENT_FL_FTUE_FSW_DIALOG_SHOWN = 'file-locking-ftue-fsw-dialog-shown'
    SIMPLE_EVENT_FL_FTUE_FSW_LOCK_CLICKED = 'file-locking-ftue-fsw-lock-clicked'
    SIMPLE_EVENT_FL_FTUE_CAROUSEL_LAUNCHED = 'file-locking-ftue-carousel-launched'
    report_collaborator_locked_file_accessed = (lambda cls = None, fileid = None, ext = classmethod: pass# WARNING: Decompyle incomplete
)()
    report_context_menu_lock_event = (lambda cls = None, fileid = None, ext = classmethod: pass# WARNING: Decompyle incomplete
)()
    report_context_menu_unlock_event = (lambda cls = None, fileid = None, ext = classmethod: pass# WARNING: Decompyle incomplete
)()
    report_context_menu_request_unlock_event = (lambda cls = None, fileid = None, ext = classmethod: pass# WARNING: Decompyle incomplete
)()
    report_ftue_fsw_show_dialog_event = (lambda cls = None, fileid = None, ext = classmethod: pass# WARNING: Decompyle incomplete
)()
    report_ftue_fsw_lock_event = (lambda cls = None, fileid = None, ext = classmethod: pass# WARNING: Decompyle incomplete
)()
    report_learn_more_click_event = (lambda cls = None, fileid = None, ext = classmethod: pass# WARNING: Decompyle incomplete
)()
    report_coauth_click_event = (lambda cls = None, fileid = None, ext = classmethod: pass# WARNING: Decompyle incomplete
)()
    _report_simple_event = (lambda cls = None, event = None, count = classmethod: report_transient_simple_metric(SimpleMetricCategoryWhitelist.FILE_LOCKING, event, count))()
    log = (lambda cls, event = None, fileid = None, team_id = classmethod, ext = ('event', 'str', 'fileid', 'str', 'team_id', 'Optional[str]', 'ext', 'Optional[str]', 'kwargs', 'Union[str, int]', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()

