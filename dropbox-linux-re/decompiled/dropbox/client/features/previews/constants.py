# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import Enum
PREVIEWS_UNSUPPORTED_EXTENSIONS = [
    'paper',
    'pdf']

class PreviewEntryPoint(Enum):
    FINDER_CONTEXT_MENU = 'finder_context_menu'
    SYNC_HISTORY = 'sync_history'
    SEARCH = 'search'
    ACTIVITY = 'activity'
    NOTIFICATION = 'notification'
    NOTIFICATION_HANDOFF = 'notification_handoff'


class PreviewActions(Enum):
    CONTEXT_MENU_SHOWN = 'context_menu_shown'
    VIEW_LAUNCHED = 'view_launched'

