# Source Generated with Decompyle++
# File: email_verification_api.pyc (Python 3.11)

import uuid
from typing import Dict, Text
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.email_verification_pb2 import DialogText, EmailVerificationDialogAction, EmailVerificationDialogResult, ShowEmailVerificationDialogRequest, ShowSharingErrorDialogRequest
from dropbox.client.fenix.meta_engine_apis.base import GLOBAL_ACCOUNT_ID
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.email_verification_api_base import _EmailVerificationBaseClass
from dropbox.client.ui.common.email_verification_window.constants import ButtonTextDict, DialogTextDict
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.basic import EasyFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class EmailVerificationAPI(_EmailVerificationBaseClass):
    pass
# WARNING: Decompyle incomplete

