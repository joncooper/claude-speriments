# Source Generated with Decompyle++
# File: auth_error.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.multiaccount.ui_strings import MultiAccountStrings
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType
from dropbox.client.setup_wizard.setup_wizard_strings import SetupWizardStrings
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.client.util import hard_exit
from dropbox.client_api.exceptions import TransientErrorType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_exception
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.platform import IS_MAC
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def unicode_clean(_str):
    
    try:
        _str = Text(_str)
        
        try:
            pass
        except UnicodeError:
            _str = str(_str).decode('utf-8', 'ignore')
            
            try:
                pass
            try:
                pass
            except Exception:
                report_exception(component = DesktopComponent.AUTH)
                _str = ''

            return _str




def show_connection_error_dialog(app, transient_error, error_count):
    if IS_MAC:
        return None
    
    try:
        if error_count == 1 or transient_error == TransientErrorType.INVALID_SSL_CERT:
            app.ui_kit.show_bubble(LoudNotification(LoudNotificationType.SECURE_CONNECTION_ERROR, SetupWizardStrings.secure_connection_error, SetupWizardStrings.secure_connection_error_title, bypass_silent_mode = True))
            return None
        return None
        return None
    except Exception:
        report_exception(component = DesktopComponent.AUTH)
        return None



def show_unlink_failure_dialog(app = None, account = None):
    pass
# WARNING: Decompyle incomplete


def show_missing_dropbox_dialog(app = None, account = None):
    pass
# WARNING: Decompyle incomplete


def show_multiple_missing_dropbox_dialog(app = None, missing_dropbox_paths = None):
    pass
# WARNING: Decompyle incomplete


def show_single_missing_additional_dropbox_dialog(app = None, account = None):
    pass
# WARNING: Decompyle incomplete


def show_relink_confirmation_dialog(app = None):
    pass
# WARNING: Decompyle incomplete


def show_dropbox_drive_missing_dialog(app = None, account = None, drive_name = None):
    pass
# WARNING: Decompyle incomplete

show_unlink_because_unpaired_alert = (lambda app = None, account = None: pass# WARNING: Decompyle incomplete
)()
show_multiaccount_disabled_alert = (lambda app = None, account_manager = None: pass# WARNING: Decompyle incomplete
)()
