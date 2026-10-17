# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import Enum

class NotificationDialogEntryPoint(Enum):
    FINDER_CONTEXT_MENU = 'finder_context_menu'
    TRAY_MENU = 'tray_menu'
    UNKNOWN = 'unknown'
    TRAY_RECENTLY_CHANGED = 'tray-recently-changed'
    SCREENSHOTS = 'screenshots'
    SCREENRECORDINGS = 'screenrecordings'
    HARMONY = 'harmony'
    OFFICE_ADDIN = 'office_addin'
    APOLLO = 'apollo'
    TRAY_SUGGESTED_FILE = 'tray-suggested-file'
    TRAY_PROMOTION = 'tray-promotion'
    COPY_TO_DROPBOX_COPY_LINK = 'copy-to-dropbox-copy-link'
    COPY_TO_DROPBOX_SHARE = 'copy-to-dropbox-share'
    BASIC_USER_TO_TEAM = 'basic_user_to_team'


class NotificationDialogActions(Enum):
    VIEW_LAUNCHED = 'view_launched'


class NotificationDialogSurface(Enum):
    COPY_LINK_AND_SHARE = 'copy_link_and_share'
    PIN_DROPBOX_PROMOTION = 'pin_dropbox_promotion'
    COPY_TO_DROPBOX_OUTSIDE_DBX_ROOT = 'copy_to_dropbox_outside_dbx_root'
    BASIC_USER_TO_TEAM_ACTION_REQUIRED_NOTIFICATION = 'basic_user_to_team_action_required_notification'
    BASIC_USER_TO_TEAM_SYNCING_PAUSED_NOTIFICATION = 'basic_user_to_team_syncing_paused_notification'

