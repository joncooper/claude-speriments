# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from typing import Dict, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject, EventState
from dropbox.client.features.desktop_logging.logging_event import UserEventLoggingEvent
from dropbox.components.desktop_components import DesktopComponent

def context_user_action_logging_helper(account, event_action, session_id = None, component = None, event_state = None, nopii_extras = ('account', 'AccountInterface', 'event_action', 'EventAction', 'session_id', 'str', 'component', 'DesktopComponent', 'event_state', 'Optional[EventState]', 'nopii_extras', 'Optional[Dict[str, str]]', 'return', 'None')):
    user_event = UserEventLoggingEvent(event_class = EventClass.OS_CONTEXT_MENU, event_object = EventObject.CONTEXT_MENU, event_action = event_action, event_state = event_state, component = component, extra_amis_tags = { }, extra_hive_dict_nopii = nopii_extras if nopii_extras else { }, feature_session_id = session_id, action_surface = 'context_menu', source = 'context_menu', complied_table_name = None, amis_namespace = None, event_name = None)
    DesktopLogger.log_event(user_event, account)

