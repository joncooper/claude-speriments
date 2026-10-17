# Source Generated with Decompyle++
# File: fp_shadow_migration.pyc (Python 3.11)

import uuid
from typing import Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.trace import TRACE
FP_SHADOW_MIGRATION_IN_PROGRESS_NOTIFICATION_THRESHOLD_MS = 1000
WINDOW_TITLE_BAR_HEIGHT = 28
MODAL_WINDOW_WIDTH = 600
DIALOG_WINDOW_WIDTH = 480

def _show_fp_shadow_migration_notification(account = None, notification_surface = None, width = None, height = (None,), unmigrated_files_path = ('account', 'AccountInterface', 'notification_surface', 'Text', 'width', 'int', 'height', 'int', 'unmigrated_files_path', 'Optional[Text]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def show_fp_shadow_migration_in_progress_notification(account = None):
    _show_fp_shadow_migration_notification(account, 'fp_shadow_migration_in_progress_notification', MODAL_WINDOW_WIDTH, 516 + WINDOW_TITLE_BAR_HEIGHT)


def show_fp_shadow_migration_complete_notification(account = None):
    _show_fp_shadow_migration_notification(account, 'fp_shadow_migration_complete_notification', MODAL_WINDOW_WIDTH, 576 + WINDOW_TITLE_BAR_HEIGHT)


def show_fp_shadow_migration_unmigrated_files_notification(account = None, unmigrated_files_path = None):
    _show_fp_shadow_migration_notification(account, 'fp_shadow_migration_unmigrated_files_notification', DIALOG_WINDOW_WIDTH, 374 + WINDOW_TITLE_BAR_HEIGHT, unmigrated_files_path = unmigrated_files_path)

