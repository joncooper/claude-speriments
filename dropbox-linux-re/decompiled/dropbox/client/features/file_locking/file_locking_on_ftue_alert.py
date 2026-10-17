# Source Generated with Decompyle++
# File: file_locking_on_ftue_alert.pyc (Python 3.11)

import webbrowser
from typing import Callable, Optional, Text
from dropbox.client.features.coauth.constants import COAUTH_ACCOUNT_KEY_WOPI_SERVICE_ID_FIELD_VALUE
from dropbox.client.features.file_locking.base_file_locking_alert import AlertButton, BaseFileLockingAlert
from dropbox.client.features.file_locking.file_locking_metrics_logger import FileLockingLogger
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import file_extension
from dropbox.model.types import FileId
from dropbox.platform import IS_MAC
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.shared.util import format_html
from dropbox.url_info import dropbox_url_info

class _OnLockStrings(UIStrings):
    TITLE = UI('Lock editing so only you can make changes?')
    BODY = UI('<b>%(filename)s</b> is shared with other people. To make sure no one else edits it while you do, lock editing.')
    CHECK_BOX_LABEL = UI("Don't ask me this again")
    LOCK_BUTTON = UI('Lock')
    CANCEL_BUTTON = UI('Leave unlocked')
    LEARN_MORE_BUTTON = UI('How locking works')
    COAUTH_TITLE = UI('Allow co-authoring?')
    COAUTH_BODY = UI('Work real-time with your team on <b>%(filename)s</b> without conflicted copies. Alternatively, you can lock the file to prevent other edits while you are working on the file. ')
    COAUTH_LEARN_MORE_BUTTON = UI('How it works')
    COAUTH_LOCK_BUTTON = LOCK_BUTTON
    COAUTH_CO_AUTHOR_BUTTON = UI('Co-author')

COAUTH_HELP_URL = 'https://dropbox.com/help/view-edit/collaborate-on-microsoft-office'
ADD_PLACE_URL = 'ms-office-storage-host:asp|d|{service_id}|o|0|a|Web'.format(service_id = COAUTH_ACCOUNT_KEY_WOPI_SERVICE_ID_FIELD_VALUE)

class FileLockingOnFTUEAlert(BaseFileLockingAlert):
    pass
# WARNING: Decompyle incomplete


class CoauthFileLockingOnFTUEAlert(BaseFileLockingAlert):
    pass
# WARNING: Decompyle incomplete

