# Source Generated with Decompyle++
# File: kext_install_ui.pyc (Python 3.11)

from enum import Enum
from typing import Any, Callable, NamedTuple, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.startup.mac import update_and_fix_binaries_if_needed
from dropbox.client.ui.cocoa.alert_dialog.alert_dialog import CocoaAlertDialog
from dropbox.client.ui.cocoa.constants import ENTER_KEY, ESCAPE_KEY
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.uikit import BaseUIKit, on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import assert_message_queue
from dropbox.i18n import trans
from dropbox.infinite import infinite_hard_optout
from dropbox.infinite.state_machine import infinite_platform_supported, InfiniteState, InfiniteStateMachine
from dropbox.mac.internal import binaries_ready, BINARIES_READY_TIMEOUT, restart_macos_host
from dropbox.mac.system_preferences import open_security_pane_general
from dropbox.mac.version import HIGH_SIERRA, MacVersion
from dropbox.preferences import KEXT_LOAD_SUCCEEDED
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIKextInstallFlowSource
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
if infinite_platform_supported():
    from dropbox.infinite.state_machine import KextManager
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import ConfigurationManagerInterface

class KextScreenType(Enum):
    ALERT = 'alert'
    PREFS = 'prefs'
    DONE = 'done'
    RESTART = 'restart'


class KextBridgeResponse(Enum):
    ALERTED = 'alerted'
    INSTALLED = 'installed'
    RESTART = 'restart'

KEXT_INSTALL_UI_SERVER_VIEW_PATH = '/client/kext_install_ui'
KEXT_WITH_SMARTSYNC_ONBOARD_WIDTH = 965
KEXT_WITH_SMARTSYNC_ONBOARD_HEIGHT = 570
KEXT_INSTALL_UI_WIDTH = 310
KEXT_INSTALL_UI_HEIGHT = 510
_ACCESS_POLL_INTERVAL = 1
_ACCESS_POLL_TIMEOUT = 300

def _report_kext_install_event(event_name = None, **extra_dict):
    extra_dict['flow_variant'] = 'native'
    sanitized_extra_dict = sanitize_event_extra_dict(extra_dict)
    report('infinite-kext', event_name = event_name, extra = sanitized_extra_dict)

_KEXT_INSTALL_FLOW_ACTIVE = False
launch_kext_onboarding = (lambda uikit, state_machine = None, source = None, done_callback = on_ui_thread(), abort_callback = (None, None, False), fresh_link = ('uikit', 'BaseUIKit', 'state_machine', 'InfiniteStateMachine', 'source', 'InfiniteUIKextInstallFlowSource', 'done_callback', 'Optional[Callable[[], None]]', 'abort_callback', 'Optional[Callable[[], None]]', 'fresh_link', 'bool', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()

def should_do_kext_onboarding(state_machine = None, gandalf = None, config_manager = None, account = (None,)):
    if not infinite_platform_supported():
        return False
# WARNING: Decompyle incomplete


def _show_kext_alert_or_install(state_machine, alert_shown_callback = None, kext_installed_callback = None, restart_needed_callback = None, failed_callback = ('state_machine', 'InfiniteStateMachine', 'alert_shown_callback', 'Callable[[], None]', 'kext_installed_callback', 'Callable[[], None]', 'restart_needed_callback', 'Callable[[], None]', 'failed_callback', 'Callable[[], None]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def _after_root_password_prompt(state_machine, alert_shown_callback = None, kext_installed_callback = None, restart_needed_callback = None, failed_callback = ('state_machine', 'InfiniteStateMachine', 'alert_shown_callback', 'Callable[[], None]', 'kext_installed_callback', 'Callable[[], None]', 'restart_needed_callback', 'Callable[[], None]', 'failed_callback', 'Callable[[], None]', 'return', 'None')):
    if binaries_ready.value:
        _report_kext_install_event('attempt_load')
        _load_unapproved_kext(state_machine, block = True)
        if _kext_is_installed(state_machine):
            kext_installed_callback()
            return None
        if None.is_pending_reboot():
            TRACE('Infinite state machine requires a reboot (%r).', state_machine.last_infinite_pager_error)
            restart_needed_callback()
            return None
        alert_shown_callback()
        return None
    _report_kext_install_event('failed_password')
    failed_callback()


def _show_kext_prefs():
    TRACE('Opening system security & privacy preferences')
    _report_kext_install_event('open_preferences')
    open_security_pane_general()


def _get_kext_approval(approved_callback = None, timeout_callback = None, restart_required_callback = None):
    TRACE('Polling for kext approval...')
    _poll_kext_approval(approved_callback, timeout_callback, restart_required_callback, approved = False, time_lapsed = 0)

_poll_kext_approval = (lambda approved_callback, timeout_callback = None, restart_required_callback = None, approved = on_ui_thread(delay = _ACCESS_POLL_INTERVAL), time_lapsed = ('approved_callback', 'Callable[[], None]', 'timeout_callback', 'Callable[[], None]', 'restart_required_callback', 'Optional[Callable[[], None]]', 'approved', 'bool', 'time_lapsed', 'float', 'return', 'None'): if approved:
if KextManager.is_kext_loaded():
TRACE('Kext approved and loaded!')_report_kext_install_event('install_success')approved_callback()Noneif None > 120:
_report_kext_install_event('load_timeout')timeout_callback()None_poll_kext_approval(approved_callback, timeout_callback, restart_required_callback, True, time_lapsed + _ACCESS_POLL_INTERVAL)Noneif KextManager.is_kext_approved():
TRACE('Kext approved but not yet loaded! Waiting...')if restart_required_callback:
TRACE('Cannot load kext until next restart.')_report_kext_install_event('reboot_required')restart_required_callback()None_poll_kext_approval(approved_callback, timeout_callback, restart_required_callback, True, 0)Noneif None > _ACCESS_POLL_TIMEOUT:
_report_kext_install_event('approval_timeout')timeout_callback()None_poll_kext_approval(approved_callback, timeout_callback, restart_required_callback, False, time_lapsed + _ACCESS_POLL_INTERVAL))()

def KextUIState():
    '''KextUIState'''
    pass

KextUIState = <NODE:27>(KextUIState, 'KextUIState', NamedTuple('KextUIState', [
    ('uikit', BaseUIKit),
    ('state_machine', InfiniteStateMachine),
    ('done_callback', Optional[Callable[([], None)]]),
    ('abort_callback', Optional[Callable[([], None)]]),
    ('first_panel', KextScreenType),
    ('fresh_link', bool)]))

def _get_first_panel(state_machine = None):
    if _kext_is_installed(state_machine):
        return KextScreenType.DONE
    if _kext_is_waiting(state_machine):
        return KextScreenType.PREFS
    return None.ALERT

_launch_flow = (lambda state = None: pass# WARNING: Decompyle incomplete
)()

def _handle_premature_close(state = None):
    pass
# WARNING: Decompyle incomplete


def _kext_prompt_reboot_required(state = None):
    pass
# WARNING: Decompyle incomplete


def _kext_is_installed(state_machine = None):
    return InfiniteState.EXPOSED in state_machine.get_state().values()


def _kext_is_waiting(state_machine = None):
    return InfiniteState.KEXT_WAITING_APPROVAL in state_machine.get_state().values()


def _kext_is_pending_reboot(state_machine = None):
