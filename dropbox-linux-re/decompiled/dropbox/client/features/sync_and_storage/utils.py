# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import Any, Dict, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.features.sync_and_storage.constants import SyncAndStorageActions, SyncAndStorageEntryPoint, SyncAndStorageViewVariant
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.infinite import infinite_exposed
from dropbox.trace import TRACE

def report_manage_space_event(account, event_action = None, view_variant = None, extra = None, source = (None, None, None), session_id = ('account', 'AccountInterface', 'event_action', 'SyncAndStorageActions', 'view_variant', 'SyncAndStorageViewVariant', 'extra', 'Optional[Dict[str, Any]]', 'source', 'Optional[str]', 'session_id', 'Optional[str]', 'return', 'None')):
    if not extra:
        extra = { }
        extra['view_variant'] = view_variant.value
    new_event = NonUserLoggingEvent(event_name = event_action.value, feature_session_id = session_id if session_id else '', action_surface = 'sync_and_storage_window', source = source if source else '', component = DesktopComponent.SYNC_AND_STORAGE_UI, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(new_event, account)


def manage_space_enabled(gandalf = None, account = None):
    pass
# WARNING: Decompyle incomplete


def launch_sync_and_storage_view(event_hub = None, account = None, session_id = None, source = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'session_id', 'Text', 'source', 'SyncAndStorageEntryPoint', 'return', 'None')):
    variant = SyncAndStorageViewVariant.RECALL if source == SyncAndStorageEntryPoint.TRAY_DEBUG_MENU else SyncAndStorageViewVariant.EVICT
    event_hub.launch_journey(UserJourneyNames.SYNC_AND_STORAGE_FLOW, session_id, {
        'sessionId': session_id,
        'activeAccount': convert_to_local_account(account),
        'source': source.value,
        'viewVariant': variant.value }).ground(component = DesktopComponent.SYNC_AND_STORAGE_UI)
    report_manage_space_event(account, SyncAndStorageActions.VIEW_LAUNCHED, variant, None, source.value, session_id)

