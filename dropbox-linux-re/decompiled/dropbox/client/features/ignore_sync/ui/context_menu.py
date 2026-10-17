# Source Generated with Decompyle++
# File: context_menu.pyc (Python 3.11)

from typing import Optional
from dropbox.client.features.ignore_sync.constants import SUPPRESS_SYNC_IGNORE_CONFIRMATION_DIALOG
from dropbox.client.features.ignore_sync.context_menu_logging import EventContext, IgnoreSyncEventType, report_ignore_sync_event, report_ignore_sync_event_from_context
from dropbox.client.features.ignore_sync.ui.strings import get_ignore_sync_error_reason_string, IgnoreSyncConfirmation, IgnoreSyncError
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import SetPathIgnoredStateErrorReason
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.config import ConfigDict
    from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
    from dropbox.foundation.context.user import UserContext
    from dropbox.shared.local_path import LocalPath

def _show_ignore_path_failure_alert(user_context, legacy_ui_launcher = None, path = None, error_reason = None, event_context = ('user_context', 'UserContext', 'legacy_ui_launcher', 'LegacyUILauncher', 'path', 'LocalPath', 'error_reason', 'SetPathIgnoredStateErrorReason', 'event_context', 'EventContext', 'return', 'None')):
    if error_reason in (SetPathIgnoredStateErrorReason.IS_CLOUD_DOC, SetPathIgnoredStateErrorReason.HAS_CLOUD_DOCS, SetPathIgnoredStateErrorReason.HAS_PLACEHOLDERS_AND_CLOUD_DOCS):
        report_ignore_sync_event_from_context(event_context, IgnoreSyncEventType.IGNORE_FAILED_CLOUD_FILES)
    if error_reason in (SetPathIgnoredStateErrorReason.IS_PLACEHOLDER, SetPathIgnoredStateErrorReason.HAS_PLACEHOLDERS, SetPathIgnoredStateErrorReason.HAS_PLACEHOLDERS_AND_CLOUD_DOCS):
        report_ignore_sync_event_from_context(event_context, IgnoreSyncEventType.IGNORE_FAILED_PLACEHOLDERS)
    error_reason_str = get_ignore_sync_error_reason_string(error_reason)
    legacy_ui_launcher.show_non_blocking_dialog(IgnoreSyncError.headline % {
        'name': path.basename }, error_reason_str, [
        IgnoreSyncError.acknowledge], use_electron = False)


def _set_path_ignored(user_context, legacy_ui_launcher = None, config_dict = None, path = None, event_context = ('user_context', 'UserContext', 'legacy_ui_launcher', 'LegacyUILauncher', 'config_dict', 'ConfigDict', 'path', 'LocalPath', 'event_context', 'EventContext', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def ignore_path(user_context, legacy_ui_launcher = None, config_dict = None, path = None, event_context = ('user_context', 'UserContext', 'legacy_ui_launcher', 'LegacyUILauncher', 'config_dict', 'ConfigDict', 'path', 'LocalPath', 'event_context', 'EventContext', 'return', 'None')):
    _set_path_ignored(user_context, legacy_ui_launcher, config_dict, path, event_context)


def unignore_path(user_context = None, path = None):
    pass
# WARNING: Decompyle incomplete


def show_ignore_path_cloud_doc_failure(user_context = None, legacy_ui_launcher = None, path = None, event_context = ('user_context', 'UserContext', 'legacy_ui_launcher', 'LegacyUILauncher', 'path', 'LocalPath', 'event_context', 'EventContext', 'return', 'None')):
    _show_ignore_path_failure_alert(user_context, legacy_ui_launcher, path, SetPathIgnoredStateErrorReason.IS_CLOUD_DOC, event_context)


def show_ignore_path_infinite_failure(user_context, legacy_ui_launcher = None, path = None, is_dir = None, event_context = ('user_context', 'UserContext', 'legacy_ui_launcher', 'LegacyUILauncher', 'path', 'LocalPath', 'is_dir', 'bool', 'event_context', 'EventContext', 'return', 'None')):
    error_reason = SetPathIgnoredStateErrorReason.HAS_PLACEHOLDERS if is_dir else SetPathIgnoredStateErrorReason.IS_PLACEHOLDER
    _show_ignore_path_failure_alert(user_context, legacy_ui_launcher, path, error_reason, event_context)

