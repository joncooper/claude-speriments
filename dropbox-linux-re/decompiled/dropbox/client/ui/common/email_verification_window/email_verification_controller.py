# Source Generated with Decompyle++
# File: email_verification_controller.pyc (Python 3.11)

from typing import Any, Callable, Dict, Optional, Text
from build_number.features import feature_enabled
from async_request_controller import AsyncRequestController
from constants import ButtonTextDict, DialogTextDict
from sharing_strings import SharingStrings
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.meta_engine_apis.email_verification_api import EmailVerificationAPI
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.platform import IS_MAC
from dropbox.shared.util import safe_navigate
from dropbox.sharing.sharing_logger import ShareDesktopTiburonEvent
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class EmailVerificationController(AsyncRequestController):
    pass
# WARNING: Decompyle incomplete

