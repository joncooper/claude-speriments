# Source Generated with Decompyle++
# File: harmony.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import List, Optional, Text, Tuple
from dropbox.client.product_span import ProductSpan
from dropbox.client.ui.common.harmony_strings import HarmonyStrings
from dropbox.event import report
from dropbox.event_names import HARMONY_EVENT
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.functions import md5_hash
from dropbox.harmony.model import HarmonyDocument
from dropbox.i18n import ungettext
from dropbox.shared.local_path import LocalPath
MYPY = False
if MYPY:
    from dropbox.harmony.models.harmony_user import HarmonyUser
MAX_DISPLAY_NAME_LENGTH = 20
MAX_TOOLTIP_ENTRY = 20

def get_overflow_tooltip_string(viewers = None):
    presence_strings = []
    idx = 0
# WARNING: Decompyle incomplete


def get_seen_state_tooltip_string(seen_state_strings = None):
    if len(seen_state_strings) > MAX_TOOLTIP_ENTRY:
        truncated = len(seen_state_strings) - MAX_TOOLTIP_ENTRY
        truncate_string = ungettext('+ %(truncated)s other viewed this file', '+ %(truncated)s others viewed this file', truncated)
        seen_state_strings = seen_state_strings[:MAX_TOOLTIP_ENTRY]
        seen_state_strings.append(truncate_string % dict(truncated = truncated))
    return '\n'.join(seen_state_strings)


def get_editor_banner_text(modifiers = None, local_modifying_time = None, coauthoring_enabled = None):
    center_text = True
    if not modifiers:
        return (None, None, center_text)
    count = len(modifiers)
# WARNING: Decompyle incomplete

log_event = (lambda event = None: data = {
'event': event,
'product_span_id': ProductSpan.instance().get_id() }# WARNING: Decompyle incomplete
)()
log_journal_event = (lambda event = None, window = None, trace = handle_exceptions: document = Nonelocal_path = Nonewindow_file = extra.pop('window_file', None)window_details = extra.pop('window_details', None)wid = extra.pop('wid', -1)aid = extra.pop('aid', -1)pid = extra.pop('pid', -1)app_version = extra.pop('app_version', -1)# WARNING: Decompyle incomplete
)()
