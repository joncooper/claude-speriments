# Source Generated with Decompyle++
# File: browser_api.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.browser_pb2 import LoginAndRedirectReq, OpenUrlInBrowserReq
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.browser_api_base import _BrowserBaseClass
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.raii2._scope import destroying
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class BrowserAPI(_BrowserBaseClass):
    pass
# WARNING: Decompyle incomplete

