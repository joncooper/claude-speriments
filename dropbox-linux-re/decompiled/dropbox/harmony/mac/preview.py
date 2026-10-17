# Source Generated with Decompyle++
# File: preview.pyc (Python 3.11)

from __future__ import absolute_import
import re
from typing import Optional, Tuple
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1
from dropbox.harmony.mac.accessibility import AccessibilityPlugin
from dropbox.harmony.models.types import ApplicationVersion, WindowID
from dropbox.harmony.utility.exceptions import SEVERITY_CRITICAL, StateNotAvailableError

class PreviewMultipleFilesNotSupportedException(StateNotAvailableError):
    pass
# WARNING: Decompyle incomplete


class PreviewPlugin(AccessibilityPlugin):
    APPLICATION_IDENTIFIER = 'com.apple.Preview'
    STORMCROW_RULE = 'desktop-harmony-enable-preview-app'
    get_active_file = (lambda self = None, validate_wid = None: (window, wid) = self._get_focused_window()path = self._get_window_path(window)title = self._get_window_title(window)if self.detect_multiple_files_in_same_window(title):
raise PreviewMultipleFilesNotSupportedException(title = title)(wid, path))()
    detect_multiple_files_in_same_window = (lambda title = None: pattern = '^.*\\([0-9]+ documents, [0-9]+ total pages\\)$'True if re.match(pattern, title) else False)()
    supports_version = (lambda cls = None, version = None: True)()

