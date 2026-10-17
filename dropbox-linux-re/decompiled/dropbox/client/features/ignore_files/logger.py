# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject, EventState
from dropbox.client.features.desktop_logging.logging_event import UserEventLoggingEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.raii2.quick import Destroyable

class IgnoreFilesNotificationLogger(Destroyable):
    
    def _report_event(self = None, account = None, action = None, state = (EventState.SUCCESS,)):
        DesktopLogger.log_event(UserEventLoggingEvent(event_class = EventClass.IGNORE_FILES, event_object = EventObject.IGNORE_FILES_NOTIFICATION, event_action = action, event_state = state, feature_session_id = '', action_surface = 'tray', source = 'ignore_files_notification', component = DesktopComponent.SYNC_ENGINE), account)

    
    def report_sticky_shown(self = None, account = None):
        self._report_event(account, action = EventAction.SHOWN)

    
    def report_cta_clicked(self = None, account = None):
        self._report_event(account, action = EventAction.OPEN)

    
    def report_secondary_action_clicked(self = None, account = None):
        self._report_event(account, action = EventAction.LINK)


