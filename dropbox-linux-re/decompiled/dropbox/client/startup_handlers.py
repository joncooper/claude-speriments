# Source Generated with Decompyle++
# File: startup_handlers.pyc (Python 3.11)

import os
from typing import List, Optional, Text, Tuple, Union
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.config import ConfigDict
from dropbox.client.databases import clear_appdata_for_unlink
from dropbox.client.high_trace import force_flush as force_rtrace_flush
from dropbox.client.unlink_cookie import HOST_SECRET_KEYNAME, write_unlink_cookie_no_sync_engine
from dropbox.client.util import get_user_agent_dict, kill_other_instances, launch_new_dropbox
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.environment import is_playwright_tests
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.i18n import safe_activate_translation, trans
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.sync_root.helpers import destroy_root_from_config
from dropbox.sync_root.types import RemovalMode
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
if IS_WINDOWS:
    from dropbox.client.features.coauth.utils import destroy_coauth_global_registry_key, remove_unknown_account_keys_if_any
    from dropbox.client.installer.win import is_per_user_windows_install, remove_keystore_registry_entries
    from dropbox.client.ui.win32.dialogs import ProgressTaskDialog
if IS_MAC:
    from dropbox.client.ui.cocoa.cf_dialog import CFMacDialog
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility

class StartupHandlers(object):
    handler_map = {
        '/unlink': (lambda app, args: unlink_handler(app, '/unlink')),
        '/killdata': (lambda app, args: unlink_handler(app, '/killdata', args)),
        '/unlinkr': (lambda app, args: unlink_handler(app, '/unlinkr')) }
    run = (lambda cls = None, app = None, first_arg = classmethod, args = ('app', 'Union[DropboxApplication, DropboxApplicationUtility]', 'first_arg', 'Text', 'args', 'Optional[List[Text]]', 'return', 'Optional[ExitCode]'): if first_arg not in cls.handler_map:
report_bad_assumption('Unknown argument: %r' % first_arg)ExitCode.FATAL_EXCEPTIONcls.handler_map[first_arg](app, args))()


def unlink_handler(app = None, first_arg = None, args = None):
    will_reboot = first_arg == '/unlinkr'
    
    try:
        safe_activate_translation()
    except Exception:
        TRACE('!! Failed to activate translation! Uninstall/signout dialog strings will be untranslated')

    caption = trans('Signing out...')
    message = trans('Dropbox needs to restart to sign out')
    if will_reboot and IS_MAC:
        mac_dialog = CFMacDialog()
        mac_dialog.display_mac_notification(caption = caption, message = message)
    elif will_reboot and IS_WINDOWS:
        win_dialog = ProgressTaskDialog(caption = caption, message = message, marquee = True)
        win_dialog.show()
    (unlink_ret_code, param) = perform_unlink(app, first_arg, args)
    if will_reboot and IS_MAC:
        mac_dialog.destroy_mac_notification()
    elif will_reboot and IS_WINDOWS:
        win_dialog.close()
    if will_reboot and unlink_ret_code == ExitCode.SUCCESS:
        app.restart(param)
    return unlink_ret_code


def perform_unlink(app = None, first_arg = None, args = None):
    pass
# WARNING: Decompyle incomplete

