# Source Generated with Decompyle++
# File: recently_changed_menu.pyc (Python 3.11)

from typing import cast, Dict, List, Optional
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.tray.events import TrayEventName, TrayEventReporter, TrayEventTrigger
from dropbox.client.tray.logging.pap_logging_helpers import ACCOUNT_MENU_ITEMS, log_select_desktop_surface_action_tray_low_ui
from dropbox.client.tray.sync_history import RECENTLY_CHANGED_FILES_CAP, SyncHistoryModel
from dropbox.client.tray.sync_history_types import SyncQueueItem, SyncQueueUserAction
from dropbox.client.ui.common.dropbox_menu import MenuItem
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.functions import snippet
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncEventType
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
SQI_USER_ACTION_TO_SE_EVENT_TYPE = {
    SyncQueueUserAction.DELETE: SyncEventType.DELETE,
    SyncQueueUserAction.EDIT: SyncEventType.EDIT,
    SyncQueueUserAction.ADD: SyncEventType.ADD }

class RecentlyChangedFile:
    SUPPORTED_FILE_TYPES = {
        'bmp',
        'jpg',
        'png',
        'psd',
        'jpeg'}
    
    def __init__(self, timestamp, event_type = None, user_context = None, local_path = None, external_editor_name = (None, False), edited_by_me = ('timestamp', 'float', 'event_type', 'Optional[int]', 'user_context', 'UserContext', 'local_path', 'LocalPath', 'external_editor_name', 'Optional[str]', 'edited_by_me', 'bool', 'return', 'None')):
        self.display_name = str(local_path.basename)
        self.name = str(local_path.basename)
        self.local_path = local_path
        self.timestamp = timestamp
        self.event_type = event_type
        self.key = id(self)
        self.user_context = user_context
        self.account = user_context.account
        self.role = user_context.account.role
        self.external_editor_name = external_editor_name
        self.edited_by_me = edited_by_me

    
    def perform_action(self = None):
        TrayEventReporter.report_to_assistant_tray(str(TrayEventName.OPEN_DROPBOX_FOLDER), action_location = str(TrayEventTrigger.FALLBACK_MENU), extras = dict(action_detail = 'file_action'))
        if is_low_ui_mode():
            log_select_desktop_surface_action_tray_low_ui(account = self.account, session_id = None, action_element = ACCOUNT_MENU_ITEMS, account_menu_items_navigation = 'open_recent_file')
        local_path = self.local_path.to_unicode()
        foc = destroying(FolderOpenerController.instance())
        foc().open_dropbox_folder_highlight_file(pathway_origin = ApolloPathwayOrigin.TRAY_RECENTLY_CHANGED, account = self.account, file_path = local_path)
        None(None, None)
        return None
        with None:
            if not None:
                pass



class RecentlyChangedFilesStrings(UIStrings):
    empty_state_message = UI('No recently changed files')


class _PerUserRecentlyChangedMenu(Destroyable):
    pass
# WARNING: Decompyle incomplete


class RecentlyChangedMenu(Destroyable):
    pass
# WARNING: Decompyle incomplete


def _included_history_event(sync_queue_item = None):
