# Source Generated with Decompyle++
# File: notification_controller.pyc (Python 3.11)

from typing import Callable, Optional, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.ignore_files.logger import IgnoreFilesNotificationLogger
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.notifications.legacy_notifications import IgnoreFilesSticky
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2._impl import Actor
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.stormcrow.utils import get_variant_as_int
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
IGNORE_FILES_SHOWN_KEY = 'ignore_files_notification_shown'
HELP_CENTER_LINK = 'https://help.dropbox.com/sync/how-to-prevent-files-from-syncing'
DEFAULT_MIN_FILE_COUNT = 0

def _get_nucleus_file_count(user_context = None):
    pass
# WARNING: Decompyle incomplete


class IgnoreFilesNotificationController(Actor):
    pass
# WARNING: Decompyle incomplete

