# Source Generated with Decompyle++
# File: file_opener.pyc (Python 3.11)

from typing import Iterable, List, Sequence, Text, Tuple
from dropbox.client.cloud_docs.constants import CloudDocsOpenFailureReason, CloudDocsOpenMiscFailure, CloudDocsValidationErrorCode
from dropbox.client.cloud_docs.dialogs import CloudDocsErrorDialog, get_open_failure_dialogs
from dropbox.client.cloud_docs.events import report_cloud_docs_open_failure
from dropbox.client.cloud_docs.opener_utils import EXTENSION_TO_OPEN_INFO
from dropbox.client.cloud_docs.strings import CloudDocsErrorStrings
from dropbox.client.cloud_docs.user_scoped_file_opener import UserScopedCloudDocsFileOpener
from dropbox.client.cloud_docs.utils import nucleus_wrapper_for_path, user_context_for_path
from dropbox.client.file_activation.constants import FileActivationError
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.file_activation.interface import ExtensionHandler
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.foundation.raii2 import destroying
from dropbox.trace import TRACE

class CloudDocsFileOpener(ExtensionHandler):
    
    def handle_open(self = None, files = None):
        if not files:
            return None
        failures = None.open_cloud_docs(files)
        if failures:
            TRACE('!! Failed to open Cloud Docs! %r', failures)
            failure_dialogs = get_open_failure_dialogs(failures)
            for dialog in failure_dialogs:
                self.display_error_dialog(dialog)
                return None
                return None

    
    def handle_error(self = None, errors = None):
        failures = []
        for filename, error, open_info in errors:
            if error == FileActivationError.SHORT_PATH_CONVERSION:
                failures.append((filename, CloudDocsOpenMiscFailure.SHORT_PATH))
                nucleus_wrapper = nucleus_wrapper_for_path(self._account_manager, self._sync_engine_adapter, filename)
                report_cloud_docs_open_failure(nucleus_wrapper, filename, CloudDocsOpenMiscFailure.SHORT_PATH, open_info)
                None(None, None)
            else:
                with None:
                    if not None:
                        pass
            TRACE('!! Failed to open Cloud Docs! %r', failures)
            failure_dialogs = get_open_failure_dialogs(failures)
            for dialog in failure_dialogs:
                self.display_error_dialog(dialog)
                return None

    handled_extensions = (lambda cls = None: EXTENSION_TO_OPEN_INFO.keys())()
    
    def display_error_dialog(self = None, dialog = None):
        self._ui_kit.show_native_non_blocking_dialog(caption = dialog.title, message = dialog.caption, buttons = [
            CloudDocsErrorStrings.confirm_button], dialog_source_type = DialogSourceTypes.OTHER)

    
    def open_cloud_docs(self = None, files = None):
        open_failures = []
        for file_name, open_info in files:
            context = user_context_for_path(self._account_manager, self._sync_engine_adapter, file_name)
            file_opener = destroying(UserScopedCloudDocsFileOpener(context = context))
            err_code = file_opener.open_cloud_doc(file_name, open_info)
            if err_code:
                open_failures.append((file_name, err_code))
            None(None, None)
        with None:
            if not None:
                pass
        continue
        return open_failures


