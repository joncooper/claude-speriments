# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import Enum, StrEnum

class SyncAndStorageEntryPoint(Enum):
    FINDER_CONTEXT_MENU = 'finder_context_menu'
    TRAY_DEBUG_MENU = 'tray_debug_menu'
    TRAY_MENU = 'tray_menu'
    STICKY_LOW_HD = 'low_hard_drive_sticky'
    STICKY_FULL_HD = 'full_hard_drive_sticky'


class SyncAndStorageActions(Enum):
    CONTEXT_MENU_SHOWN = 'context_menu_shown'
    STICKY_CREATED = 'sticky_created'
    STICKY_SHOWN = 'sticky_shown'
    STICKY_CLOSED = 'sticky_closed'
    VIEW_LAUNCHED = 'view_launched'


class SyncAndStorageViewVariant(StrEnum):
    EVICT = 'evict'
    RECALL = 'recall'

