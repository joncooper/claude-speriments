# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from enum import IntEnum
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.infinite import infinite_exposed
from dropbox.platform import IS_MAC
from dropbox.sync_root.gating import is_file_provider_root_type
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, MONTEREY_1203
SS_REMOVAL_MITIGATION_DEGRADED_PLACEHOLDERS = 'desktop-smart-sync-removal-mitigation-degraded-placeholders'
SS_REMOVAL_MITIGATION_DP_STICKY_ACKNOWLEDGED_CONFIG_KEY = 'smart_sync_mitigation_dp_sticky_acknowledged'
SHOULD_SHOW_CONTEXT_MENU_ALERT_CONFIG_KEY = 'should_show_context_menu_alert_config_key'

class MitigationEligibilityChecker:
    _need_mitigation = False
    need_mitigation = (lambda cls = None: cls._need_mitigation)()
    set_need_mitigation = (lambda cls = None, need_mitigation = None: TRACE('Setting need_mitigation flag in helper: %r', need_mitigation)cls._need_mitigation = need_mitigation)()


def ss_removal_mitigation_degraded_placeholders_enabled(gandalf = None, account = None):
