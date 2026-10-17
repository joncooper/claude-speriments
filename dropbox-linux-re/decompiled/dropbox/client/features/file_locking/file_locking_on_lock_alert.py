# Source Generated with Decompyle++
# File: file_locking_on_lock_alert.pyc (Python 3.11)

from typing import Callable, Optional, Text
from dropbox.client.features.file_locking.base_file_locking_alert import AlertButton, BaseFileLockingAlert
from dropbox.client.features.file_locking.file_locking_metrics_logger import FileLockingLogger
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.functions import file_extension
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.shared.util import format_html

class _OnLockStrings(UIStrings):
    TITLE = UI('Lock editing for this file?')
    BODY = UI('Only you can make changes to <b>%(filename)s</b> while editing is locked. Anyone else with access to the file can still view it.')
    CHECK_BOX_LABEL = UI("Don't ask me this again")
    LOCK_BUTTON = UI('Lock')
    CANCEL_BUTTON = UI('Cancel')
    LEARN_MORE_BUTTON = UI('How locking works')

_OnLockCallback = Callable[([
    bool], None)]

class FileLockingOnLockAlert(BaseFileLockingAlert):
    pass
# WARNING: Decompyle incomplete

