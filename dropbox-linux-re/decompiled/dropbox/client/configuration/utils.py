# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import absolute_import
from hashlib import md5
from typing import Any, Dict, Set, Text, Tuple
from six import integer_types
from build_number import IS_MAC
import dropbox.i18n as dropbox
from dropbox.client.autorestart import CONFIG_AUTORESTART_ATTEMPTS
from dropbox.client.features.accessibility.constants import AccessibilityGrantState, AccessibilityPromptState, OPT_AX_GRANT, OPT_AX_PROMPT, OPT_AX_PROMPT_COUNT
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeInterval
from dropbox.client.screenshots.controller import ScreenshotsController
from dropbox.client.util import enable_p2p_default
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
from dropbox.functions import make_bytes, make_unicode
from dropbox.legacy_crypto import aes_decrypt
from dropbox.preferences import AUTO_PROXY, HTTP, KEXT_LOAD_SUCCEEDED, LAST_FAILED_KEXT_LOAD, NOTIF_HAS_MODIFIED_SUFFIX, NOTIFICATIONS_PREFERENCE_ON, OPT_CAMERA_UPLOAD_WINDOWS, OPT_CB_STARTUP, OPT_DESKTOP_MIRAGE_ACCOUNT_ID, OPT_DND_END_TIME, OPT_DND_TIME_INTERVAL, OPT_DROPBOX_FOLDER_OPENER_APP, OPT_HARMONY, OPT_HARMONY_OUTSIDE_DROPBOX, OPT_HARMONY_VISIBILITY, OPT_LANG, OPT_NOTIFS_BLUENOTE_ASSIGNED_TASKS, OPT_NOTIFS_BLUENOTE_FOLLOWED_COMMENTS, OPT_NOTIFS_BLUENOTE_LEGACY, OPT_NOTIFS_BLUENOTE_MENTIONS, OPT_NOTIFS_BLUENOTE_SHARED_CONTENT, OPT_NOTIFS_BLUENOTE_VIEWS, OPT_NOTIFS_PREF_VERSION, OPT_NOTIFS_SYNC_ADD, OPT_NOTIFS_SYNC_EDIT_DELETE, OPT_NOTIFS_SYNC_LEGACY, OPT_OFFICE_ADDIN, OPT_P2P, OPT_PHOTO, OPT_SCREENSHOTS, OPT_STARTUP, OPT_TRAY_WINDOW_POSITION_DISPLAY_ID, OPT_TRAY_WINDOW_POSITION_X, OPT_TRAY_WINDOW_POSITION_Y, OPT_VIDEO
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, SEQUOIA
NOTIFICATION_PREFERENCES = (OPT_NOTIFS_BLUENOTE_ASSIGNED_TASKS, OPT_NOTIFS_BLUENOTE_FOLLOWED_COMMENTS, OPT_NOTIFS_BLUENOTE_LEGACY, OPT_NOTIFS_BLUENOTE_MENTIONS, OPT_NOTIFS_BLUENOTE_SHARED_CONTENT, OPT_NOTIFS_SYNC_ADD, OPT_NOTIFS_SYNC_EDIT_DELETE, OPT_NOTIFS_SYNC_LEGACY, OPT_NOTIFS_BLUENOTE_VIEWS)
# WARNING: Decompyle incomplete
