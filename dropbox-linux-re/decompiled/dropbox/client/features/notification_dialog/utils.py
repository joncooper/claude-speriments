# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import Any, Dict, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.features.notification_dialog.constants import NotificationDialogActions, NotificationDialogEntryPoint, NotificationDialogSurface
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHub
from dropbox.components.desktop_components import DesktopComponent
from dropbox.shared.local_path import LocalPath

def report_copy_link_and_share_event(account = None, event_action = None, extra = None, source = (None, None, None), session_id = ('account', 'AccountInterface', 'event_action', 'NotificationDialogActions', 'extra', 'Optional[Dict[str, Any]]', 'source', 'Optional[str]', 'session_id', 'Optional[str]', 'return', 'None')):
    new_event = NonUserLoggingEvent(event_name = event_action.value, feature_session_id = session_id if session_id else '', action_surface = 'copy_link_and_share_window', source = source if source else '', component = DesktopComponent.SHARING, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(new_event, account)


def launch_copy_link_share_view(event_hub, account, local_path = None, file_id = None, session_id = None, source = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'local_path', 'LocalPath', 'file_id', 'Text', 'session_id', 'Text', 'source', 'NotificationDialogEntryPoint', 'return', 'None')):
    event_hub.launch_journey(UserJourneyNames.NOTIFICATION_DIALOG_FLOW, session_id, {
        'accountId': account.account_id,
        'sessionId': session_id,
        'source': source.value,
        'surface': NotificationDialogSurface.COPY_LINK_AND_SHARE.value,
        'localPath': Text(local_path),
        'dropboxFileId': file_id }).ground(component = DesktopComponent.SHARING)
    report_copy_link_and_share_event(account, NotificationDialogActions.VIEW_LAUNCHED, None, source.value, session_id)

