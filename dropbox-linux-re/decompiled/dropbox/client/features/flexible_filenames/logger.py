# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject, EventState
from dropbox.client.features.desktop_logging.logging_event import UserEventLoggingEvent
from dropbox.client.features.flexible_filenames.consts import FlexibleFileNameStickyVariant
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.raii2.quick import Destroyable
EVENT_OBJECT_LOOKUP_MAP = {
    FlexibleFileNameStickyVariant.OPT_OUT: EventObject.FLEXIBLE_FILENAMES_OPT_OUT_NOTIFICATION,
    FlexibleFileNameStickyVariant.OPT_IN: EventObject.FLEXIBLE_FILENAMES_OPT_IN_NOTIFICATION }

class FlexibleFilenameNotificationLogger(Destroyable):
    
    def _report_event(self = None, account = None, action = None, event_object = (EventState.SUCCESS,), state = ('account', 'AccountInterface', 'action', 'EventAction', 'event_object', 'EventObject', 'state', 'EventState', 'return', 'None')):
        DesktopLogger.log_event(UserEventLoggingEvent(event_class = EventClass.FLEXIBLE_FILENAMES, event_object = event_object, event_action = action, event_state = state, feature_session_id = '', action_surface = 'tray', source = 'flexible_filenames_notification', component = DesktopComponent.SYNC_ENGINE), account)

    
    def report_sticky_shown(self = None, account = None, variant = None):
        event_object = EVENT_OBJECT_LOOKUP_MAP[variant]
        self._report_event(account, action = EventAction.SHOWN, event_object = event_object)

    
    def report_cta_clicked(self = None, account = None, variant = None):
        event_object = EVENT_OBJECT_LOOKUP_MAP[variant]
        self._report_event(account, action = EventAction.OPEN, event_object = event_object)

    
    def report_secondary_action_clicked(self = None, account = None, variant = None):
        event_object = EVENT_OBJECT_LOOKUP_MAP[variant]
        self._report_event(account, action = EventAction.LINK, event_object = event_object)

    
    def report_force_disable(self = None, account = None):
        self._report_event(account, action = EventAction.ENG, event_object = EventObject.FLEXIBLE_FILENAMES_FORCE_DISABLED)


