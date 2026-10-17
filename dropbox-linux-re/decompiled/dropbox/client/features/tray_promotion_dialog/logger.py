# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from typing import Dict, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject, EventState
from dropbox.client.features.desktop_logging.logging_event import UserEventLoggingEvent
from dropbox.components.desktop_components import DesktopComponent

class DesktopPromotionLogger:
    log_event = (lambda account, event_action, session_id = None, event_state = None, action_surface = staticmethod, source = (None,), nopii_extras = ('account', 'AccountInterface', 'event_action', 'EventAction', 'session_id', 'str', 'event_state', 'EventState', 'action_surface', 'str', 'source', 'str', 'nopii_extras', 'Optional[Dict[str, str]]', 'return', 'None'): user_event = UserEventLoggingEvent(event_class = EventClass.DESKTOP_PROMOTIONS, event_object = EventObject.TRAY_PROMOTION, event_action = event_action, event_state = event_state, component = DesktopComponent.TRAY, extra_amis_tags = { }, extra_hive_dict_nopii = nopii_extras if nopii_extras else { }, feature_session_id = session_id, action_surface = action_surface, source = source, complied_table_name = None, amis_namespace = None, event_name = None)DesktopLogger.log_event(user_event, account))()

