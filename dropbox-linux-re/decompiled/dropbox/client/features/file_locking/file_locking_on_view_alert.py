# Source Generated with Decompyle++
# File: file_locking_on_view_alert.pyc (Python 3.11)

from datetime import datetime as _datetime, timezone
from typing import Callable, Optional, Text
from dropbox.client.features.file_locking.base_file_locking_alert import AlertButton, BaseFileLockingAlert
from dropbox.client.features.file_locking.file_locking_metrics_logger import FileLockingLogger
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client.users import UserInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.functions import file_extension
from dropbox.i18n import ago
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.shared.util import format_html
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockStatus

class _OnLockStrings(UIStrings):
    TITLE = UI('Editing is locked for this file')
    BODY_NAME = UI("<b>%(user_full_name)s</b> temporarily locked editing for this file %(ago)s. You can view it while it's locked, or ask them to unlock it.")
    BODY_NO_NAME = UI("This file was temporarily locked for editing %(ago)s. You can view it while it's locked, or ask to unlock it.")
    BODY_NAME_JUST_NOW = UI("<b>%(user_full_name)s</b> temporarily locked editing for this file just now. You can view it while it's locked, or ask them to unlock it.")
    BODY_NO_NAME_JUST_NOW = UI("This file was temporarily locked for editing just now. You can view it while it's locked, or ask to unlock it.")
    OK_BUTTON = UI('OK')
    REQUEST_UNLOCK_BUTTON = UI('Ask to unlock')
    LEARN_MORE_BUTTON = UI('How locking works')

_OnLockCallback = Callable[([
    bool], None)]

class FileLockingOnViewAlert(BaseFileLockingAlert):
    pass
# WARNING: Decompyle incomplete

