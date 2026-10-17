# Source Generated with Decompyle++
# File: cx_support_tool_api.pyc (Python 3.11)

from typing import List, Optional
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.cx_support_tool_pb2 import FetchEngineDebugInfoReply
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.cx_support_tool_api_base import _CxSupportToolBaseClass
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.proto.nucleus.app_service_pb2 import DebugInfo as DebugInfoProto
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.debug_info import DebugInfo
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def _debug_info_to_proto(debug_info = None):
