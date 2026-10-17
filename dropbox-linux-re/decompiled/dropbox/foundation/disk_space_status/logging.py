# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import binascii
import os
from enum import Enum
from typing import Optional, Text
from dropbox.event import report
from dropbox.event_names import ONBOARDING_EVENT
from dropbox.functions import make_unicode
from dropbox.i18n import get_current_code

class DiskSpaceLoggerEvent(Enum):
    NOTIFICATION_TRIGGERED = 'notification_triggered'
    VIEW_CLICKED_CHOOSE_FOLDERS = 'view_clicked_choose_folders'
    VIEW_CLICKED_DISK_CLEANUP = 'view_clicked_disk_cleanup'
    VIEW_CLICKED_DROPBOX_LINK = 'view_clicked_dropbox_link'
    VIEW_CLICKED_LEARN_MORE = 'view_clicked_learn_more'
    VIEW_CLOSED = 'view_closed'
    VIEW_OPEN_TRIGGERED = 'view_open_triggered'


class DiskSpaceLoggerTrigger(Enum):
    STATE_TRANSITION = 'state_transition'
    TIMEOUT = 'timeout'

FULL_HARD_DRIVE_CLEANUP_MODULE = 'full_hard_drive_cleanup'
FULL_HARD_DRIVE_SEL_SYNC_MODULE = 'full_hard_drive_sel_sync'
LOW_HARD_DRIVE_CLEANUP_MODULE = 'low_hard_drive_cleanup'
LOW_HARD_DRIVE_SEL_SYNC_MODULE = 'low_hard_drive_sel_sync'

class DiskSpaceLogger(object):
    _SESSION_ID_LEN = 32
    
    def __init__(self = None, module_name = None, trigger = None, variant = (None,), session_id = ('module_name', 'Text', 'trigger', 'DiskSpaceLoggerTrigger', 'variant', 'Text', 'session_id', 'Optional[Text]', 'return', 'None')):
        self._module_name = module_name
        self._trigger = trigger
        self._variant = variant
    # WARNING: Decompyle incomplete

    session_id = (lambda self = None: self._session_id)()
    module_name = (lambda self = None: self._module_name)()
    trigger = (lambda self = None: self._trigger)()
    variant = (lambda self = None: self._variant)()
    
    def report(self = None, event_name = None, **event_details):
        report_data = dict(onboarding_name = self._module_name, onboarding_session_id = self._session_id, event_name = event_name.value, stormcrow_variant = self._variant, locale = get_current_code(), trigger = self._trigger.value, event_details = event_details)
    # WARNING: Decompyle incomplete


