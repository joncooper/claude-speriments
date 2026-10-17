# Source Generated with Decompyle++
# File: authentication_service.pyc (Python 3.11)

import base64
from typing import Any, cast, Dict, Optional, Text, TypedDict
from dropbox.build_common import get_build_number
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.linked_host_telemetry import get_linked_host_ids_for_telemetry
from dropbox.client.authentication.register_host_helper import RegisterHostHelper
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.fenix.account_cache import FenixAccountCache
from dropbox.client.fenix.types.account import AuthenticatedAccount, BaseAccount
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import assert_not_none
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2._scope import destroying
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class GenerateHostAuthenticationArgs(TypedDict):
    installer_tag: 'Optional[str]' = 'GenerateHostAuthenticationArgs'


class FenixRegisterHostResponse(TypedDict):
    raw_response: 'Dict[str, Any]' = 'FenixRegisterHostResponse'


class VerifiedHostAuthentication(TypedDict):
    register_host_response: 'FenixRegisterHostResponse' = 'VerifiedHostAuthentication'


class UnauthenticatedRegisterHostResponse(Exception):
    pass


class AuthenticationService(Actor):
    pass
# WARNING: Decompyle incomplete

