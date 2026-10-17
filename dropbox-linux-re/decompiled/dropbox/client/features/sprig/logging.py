# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

from enum import StrEnum
from typing import Dict, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.components.desktop_components import DesktopComponent

class SprigActions(StrEnum):
    UPDATE_PRIMARY_ACCOUNT = 'update_primary_account'


class SprigTriggerPoints(StrEnum):
    INITALIZE_CONTROLLER = 'initialize_controller'
    LAUNCH_MEV = 'launch_mev'
    TRACK_EVENT = 'track_event'


def report_update_primary_account_event(account = None, action_surface = None, extra = None, session_id = (None, None)):
    event = NonUserLoggingEvent(event_name = SprigActions.UPDATE_PRIMARY_ACCOUNT.value, feature_session_id = session_id if session_id else '', action_surface = action_surface.value, source = 'desktop_sprig', component = DesktopComponent.DESKTOP_SPRIG, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(event, account)

