# Source Generated with Decompyle++
# File: sync_error_resolver.pyc (Python 3.11)

import os
import sys
from typing import Any, Optional
from six.moves.urllib import parse as urlparse
from dropbox import fsutil
from dropbox.client.features.sync_error.model.common import ResolveDetailsReturn, show_permissions_denied_resolver_flow, SyncErrorDetail, SyncErrorType
from dropbox.client.features.sync_error.model.sync_error_logger import PermissionEvent, SyncErrorLogger
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.screenshots.controller import allow_dataless_recall, DatalessContext
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client.util import highlight_file, typed_exc_info
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import ResolvedFuture
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.native_file_opener.bridge_gen.file_open_path import FileOpenPath
from dropbox.foundation.native_file_opener.impl import ContextBoundNativeFileOpener
from dropbox.foundation.paths.bridge_gen.types import LocalPath as BridgeLocalPath
from dropbox.i18n import trans
from dropbox.overrides import report_exception
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncDirection
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
if IS_MAC:
    from macffi.CoreFoundation import CFError
    from macffi_native import lib
    from dropbox.client.constants.mac import DEFAULT_DROPBOX_PATH
    from dropbox.client.file_permissions.posix import fix_perm_on_directory
elif IS_WINDOWS:
    from dropbox.client.constants.win import DEFAULT_DROPBOX_PATH
    from dropbox.client.file_permissions.windows import show_dialog_to_fix_permissions_for_entire_dropbox
else:
    from dropbox.client.constants.linux import DEFAULT_DROPBOX_PATH

def parse_url(url = None):
    fragment = None
    if '#' in url:
        parts = url.split('#')
        url = parts[0]
        fragment = parts[1]
    url = dropbox_url_info.construct_full_url(url, fragment = fragment)
    return url


class SyncErrorResolver(Actor):
    pass
# WARNING: Decompyle incomplete

