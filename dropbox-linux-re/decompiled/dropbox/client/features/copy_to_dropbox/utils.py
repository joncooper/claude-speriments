# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import Any, Dict, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.copy_to_dropbox.constants import ExternalContextMenuSharingActions, ExternalContextMenuSharingSource, ExternalContextMenuSharingStormcrowVariants, ExternalContextMenuSharingSurface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE
COPY_TO_DROPBOX_OUTSIDE_DBX_ROOT_FEATURE_NAME = 'desktop-copy-to-dropbox-outside-dbx-root'
EXTERNAL_CONTEXT_MENU_SHARING_SURFACE = 'external_context_menu_sharing'

def get_copy_to_dropbox_variant(gandalf = None, account = None):
    pass
# WARNING: Decompyle incomplete


def report_copy_to_dropbox_outside_dbx_event(account = None, event_action = None, extra = None, source = (None, None, None), session_id = ('account', 'AccountInterface', 'event_action', 'ExternalContextMenuSharingActions', 'extra', 'Optional[Dict[str, Any]]', 'source', 'Optional[str]', 'session_id', 'Optional[str]', 'return', 'None')):
    new_event = NonUserLoggingEvent(event_name = event_action.value, feature_session_id = session_id if session_id else '', action_surface = EXTERNAL_CONTEXT_MENU_SHARING_SURFACE, source = source if source else '', component = DesktopComponent.FILE_TRANSFER, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(new_event, account)


def do_copy_to_dropbox(event_hub = None, account = None, session_id = None, pathlist = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'session_id', 'str', 'pathlist', 'List[Text]', 'return', 'None')):
    TRACE('[Copy to Dropbox] do_copy_to_dropbox %r', pathlist)
    event_hub.on_external_context_menu_sharing_copy_start('copy_link', str(account.account_id), session_id, str(pathlist[0]))
    report_copy_to_dropbox_outside_dbx_event(account, ExternalContextMenuSharingActions.COPY_LINK_CLICKED, None, ExternalContextMenuSharingSource.CONTEXT_MENU.value, session_id)


def do_share_from_dropbox(event_hub = None, account = None, session_id = None, pathlist = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'session_id', 'str', 'pathlist', 'List[Text]', 'return', 'None')):
    TRACE('[Copy to Dropbox] do_share_from_dropbox %r', pathlist)
    event_hub.on_external_context_menu_sharing_copy_start('share', str(account.account_id), session_id, str(pathlist[0]))
    report_copy_to_dropbox_outside_dbx_event(account, ExternalContextMenuSharingActions.SHARE_CLICKED, None, ExternalContextMenuSharingSource.CONTEXT_MENU.value, session_id)


def debug_launch_external_context_menu_sharing_view(event_hub, action, account = None, session_id = None, surface = None, local_path = ('event_hub', 'EventHub', 'action', 'str', 'account', 'AccountInterface', 'session_id', 'Text', 'surface', 'ExternalContextMenuSharingSurface', 'local_path', 'Optional[LocalPath]', 'return', 'None')):
    event_hub.launch_journey(UserJourneyNames.EXTERNAL_CONTEXT_MENU_SHARING_FLOW, session_id, {
        'account': convert_to_local_account(account),
        'sessionId': session_id,
        'filePath': local_path,
        'surface': surface.value,
        'action': action,
        'folderName': 'Debug Folder' }).ground(component = DesktopComponent.CONTEXT_MENU_UI)

