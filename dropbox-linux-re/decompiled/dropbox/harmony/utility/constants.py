# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import Enum
INFINITE_PREFERENCES_KEXT_GANDALF = 'desktop-infinite-kext-install-ui'
HARMONY_NO_AX = 'desktop-harmony-activity-provider-shell'
HARMONY_RETRY_BLACKLIST = 'desktop-harmony-retry-blacklist'
PASS_VIEW_LOGGING_DISABLE_STORMCROW = 'desktop-pass-view-logging-disable'

class RetryBlacklistVariant:
    OFF = 'OFF'
    CONTROL = 'CONTROL'
    RETRY_ON_FOCUS = 'RETRY_ON_FOCUS'

CONFIG_KEY_HARMONY_ONBOARDING = 'harmony_onboarding'
CONFIG_KEY_HARMONY_MEV_FIRST_TIME_SETUP_COMPLETED = 'harmony_mev_first_time_setup_completed'
CONFIG_KEY_HARMONY_MEV_VISIBILITY_PREF_DID_MIGRATE = 'harmony_mev_visibility_pref_did_migrate'

class HarmonyInteractionStates:
    NOT_SEEN = 0
    HARMONY_SEEN = 1
    ONBOARDING_COMPLETE = 2


class HarmonyErrorStates(Enum):
    ACCESSIBILITY_DISABLED = 1
    AUTOMATION_DISABLED = 3

CONFIG_KEY_BADGE_HIDING_MODAL_SHOWN = 'harmony_badge_hiding_modal_seen'

class FileViewOriginType:
    UNKNOWN = 0
    BROWSE = 1
    CAROUSEL = 2
    PHOTOS = 3
    RECENTS = 4
    TRASH = 5
    VERSION_HISTORY = 6
    HARMONY = 7
    FILESYSTEM = 8
    TRAY = 9
    SERVER_VIEW = 10
    NOTIFICATION = 11
    EMAIL = 12
    PAPER = 13


class FileViewActionType:
    CLICK = 0
    TOOLBAR_VIEW_COMMENTS = 1
    TOOLBAR_OPEN_FILE = (2,)
    CONTEXT_MENU_VIEW_COMMENTS = 3
    CONTEXT_MENU_OPEN_FILE = 4
    SEARCH = 5

PRESENCE_APP_ID = 'harmony'
BEACON_AUTH_KEY = 'harmony'

class BeaconPlatform:
    WEB = 0
    IOS = 1
    ANDROID = 2
    DESKTOP = 3

DROPBOX_SERVER_USER_ID = 81554767
