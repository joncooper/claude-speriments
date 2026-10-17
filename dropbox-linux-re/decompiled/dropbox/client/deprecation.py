# Source Generated with Decompyle++
# File: deprecation.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Any, Callable, Dict, List, NamedTuple, Optional, Text, Tuple, TypeVar
from build_number import is_store_managed, VERSION
from dropbox.assertions import assert_
from dropbox.client.authentication.types import AccountDataSource
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.notifications.legacy_notifications import DeprecatedStickyNotification
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.util import hard_exit
from dropbox.client_api.exceptions import HTTP429Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import get_jittered_seconds
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_1
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.functions import calculate_num_days_remaining
from dropbox.i18n import trans, ungettext
from dropbox.platform import IS_WINDOWS
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.trace import TRACE
from dropbox.win32.microsoft_store import launch_microsoft_store
MYPY = False
if MYPY:
    from dropbox.client.authentication.interface import AccountManagerInterface
    from dropbox.client.main import DropboxApplication
FULLY_DEPRECATED_STATE = 'full'
SOON_DEPRECATED_STATE = 'soon'
ALERT_DEPRECATED_STATE = 'alert'
DEPRECATED_ALERT_SHOWN_CONFIG_KEY = 'deprecated_alert_shown'
START_DELAY = 55
PERIODIC_DELAY_HOURS_LONG = 1.5
PERIODIC_DELAY_HOURS_SHORT = 0.1
_T = TypeVar('_T')

def DeprecationResponse():
    '''DeprecationResponse'''
    create = (lambda response = None: DeprecationResponse(deprecated_state = response.get('deprecated_state'), deprecated_time = response.get('deprecated_time'), update_to_dict = response.get('update_to_dict')))()

DeprecationResponse = <NODE:27>(DeprecationResponse, 'DeprecationResponse', NamedTuple('DeprecationResponse', [
    ('deprecated_state', Optional[str]),
    ('deprecated_time', Optional[int]),
    ('update_to_dict', Optional[Dict[(str, Any)]])]))

def run_with_retry(f = None, retry_count = None, get_sleep_secs = None):
    pass
# WARNING: Decompyle incomplete


class DeprecationRequestController(Actor):
    pass
# WARNING: Decompyle incomplete


class DeprecationLogic(object):
    
    def __init__(self = None, dropbox_app = None):
        self.dropbox_app = dropbox_app
        self.local_config = dropbox_app.config_manager.local_config(None)
        self.deprecated_state = None
        self.deprecated_time = None

    
    def _get_fully_deprecated_msg(self = None):
        return trans("You're using an old version of Dropbox. Please update to the latest version to continue using Dropbox.")

    
    def _get_soon_deprecated_msg(self = None, deprecated_time = None):
        days_to_deprecation = self._get_days_to_deprecation(deprecated_time)
        msg = ungettext("You're using an old version of Dropbox. Please update within the next %(num_days)s day to continue using Dropbox.", "You're using an old version of Dropbox. Please update within the next %(num_days)s days to continue using Dropbox.", days_to_deprecation) % dict(num_days = days_to_deprecation)
        return msg

    
    def _get_days_to_deprecation(self = None, deprecated_time = None):
        days_to_deprecation = calculate_num_days_remaining(deprecated_time)
        TRACE('DEPRECATION: days to deprecation: %r', days_to_deprecation)
        if days_to_deprecation < 1:
            report_bad_assumption('DEPRECATION: days_to_deprecation=%r < 1', days_to_deprecation, component = DesktopComponent.DEPRECATION)
            days_to_deprecation = 1
        return days_to_deprecation

    
    def show_deprecation_alert(self = None, running_headless = None):
        pass
    # WARNING: Decompyle incomplete

    
    def handle_response(self = None, response = None):
        self.deprecated_state = response.get('deprecated_state')
        running_headless = self.dropbox_app.ui_kit.running_headless()
        if self.deprecated_state == FULLY_DEPRECATED_STATE:
            TRACE('!! DEPRECATION: Server sent fully deprecated flag for build %s', VERSION)
            self.show_deprecation_alert(running_headless)
            return None
    # WARNING: Decompyle incomplete

    
    def _get_download_url(self = None):
        return self.dropbox_app.dropbox_url_info.construct_full_url('/downloading', query_pieces = [
            'from_client=True'])

    
    def launch_deprecated_download_link(self = None, source = None):
        report('deprecation', event = '%s-update-button-clicked' % source)
        if is_store_managed():
            launch_microsoft_store()
            return None
        None.dropbox_app.desktop_login.login_and_redirect('downloading?from_client=True')

    get_deprecation_status = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    report_compatibility_mode_version = (lambda : if IS_WINDOWS:
get_non_compatibility_mode_version = get_non_compatibility_mode_versionWINDOWS_VERSION_STRING = WINDOWS_VERSION_STRINGimport dropbox.win32.versiontry:
true_os_info_tup = get_non_compatibility_mode_version()if true_os_info_tup:
(build_tup, real_winver) = true_os_info_tupbuild_string = '.'.join(map(str, build_tup))report('windows-compatibility-mode', compatibility_version = WINDOWS_VERSION_STRING, true_windows_version = real_winver, true_windows_buildno = build_string)NoneNoneexcept Exception:
report_exception(severity = Severity.DEBUG, component = DesktopComponent.DEPRECATION)NoneNone)()

