# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject, EventState
from dropbox.client.features.desktop_logging.logging_event import UserEventLoggingEvent
from dropbox.components.desktop_components import DesktopComponent

class MovedToTrashLogger:
    
    def _report_event(self = None, account = None, action = None, event_object = (EventState.SUCCESS,), state = ('account', 'AccountInterface', 'action', 'EventAction', 'event_object', 'EventObject', 'state', 'EventState', 'return', 'None')):
        DesktopLogger.log_event(UserEventLoggingEvent(event_class = EventClass.MOVED_TO_TRASH, event_object = event_object, event_action = action, event_state = state, feature_session_id = '', action_surface = 'loud_notification', source = 'moved_to_trash_notification', component = DesktopComponent.SYNC_ENGINE), account)

    
    def report_loud_notif_shown(self = None, account = None):
        self._report_event(account, action = EventAction.SHOWN, event_object = EventObject.MOVED_TO_TRASH_LOUD_NOTIFICATION)

    
    def report_learn_more_clicked(self = None, account = None):
        self._report_event(account, action = EventAction.LINK, event_object = EventObject.MOVED_TO_TRASH_LOUD_NOTIFICATION)

    
    def report_open_recycle_bin_clicked(self = None, account = None):
        self._report_event(account, action = EventAction.OPEN, event_object = EventObject.MOVED_TO_TRASH_LOUD_NOTIFICATION)


