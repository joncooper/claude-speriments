# Source Generated with Decompyle++
# File: dialog_constants.pyc (Python 3.11)

from enum import Enum
ALERT_DIALOG_FAILED_TO_DISPLAY: 'int' = -1

class DialogEventTypes(Enum):
    CALLBACK = 'callback'
    TRIGGERED = 'triggered'


class DialogFrameworkTypes(Enum):
    ELECTRON = 'electron'
    NATIVE = 'native'
    PRE_MIGRATION = 'pre_migration'


class DialogSourceTypes(Enum):
    FSW = 'fsw'
    VIEW = 'view'
    SPLASH = 'splash'
    OTHER = 'other'


class IconType(Enum):
    ERROR = 'error'
    INFO = 'info'
    WARN = 'warn'
    SHIELD = 'shield'

