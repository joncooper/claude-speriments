# Source Generated with Decompyle++
# File: icon_utils.pyc (Python 3.11)

from typing import Dict, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.fenix.journeys.tray.constants import DESKTOP_TRAY_ICON_PROMOTION_ENABLED, NOTIFY_ICON_SETTINGS, NOTIFY_ICON_SETTINGS_PUBLISHER_VALUE, TrayIconEventNames
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    import winreg
    from build_number import is_full_msix
    from dropbox.client.tray.common.win_tray_utils import Win32TrayIconHelper
    from dropbox.win32.version import WIN11_VERSION_2109, WINDOWS_VERSION

def report_tray_icon_util_event(account, event_name = None, session_id = None, action_surface = None, source = ('', '', { }), extra = ('account', 'AccountInterface', 'event_name', 'TrayIconEventNames', 'session_id', 'str', 'action_surface', 'str', 'source', 'str', 'extra', 'Dict[str, str]', 'return', 'None')):
    event = NonUserLoggingEvent(event_name = event_name.value, feature_session_id = session_id, action_surface = action_surface, source = source, component = DesktopComponent.TRAY, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(event, account)


def can_promote_tray_icon(gandalf = None, account = None):
