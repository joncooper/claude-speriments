# Source Generated with Decompyle++
# File: _impl.pyc (Python 3.11)

from typing import Any, Dict, Iterable, List, NamedTuple, Optional, Set, Text, Tuple, Union
from dropbox.callbacks import create_weakref_callback
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.native_file_opener.bridge_gen.app_info import AppInfo
from dropbox.foundation.native_file_opener.bridge_gen.app_info_list import AppInfoList
from dropbox.foundation.native_file_opener.bridge_gen.bridge_interface_native_file_opener import NativeFileOpenerBridgeInterface
from dropbox.foundation.native_file_opener.bridge_gen.dangerously_bypass_whitelist import DangerouslyBypassWhitelist
from dropbox.foundation.native_file_opener.bridge_gen.file_open_bridge_error import FileOpenBridgeError
from dropbox.foundation.native_file_opener.bridge_gen.file_open_bridge_result import FileOpenBridgeResult
from dropbox.foundation.native_file_opener.bridge_gen.file_open_error_code import FileOpenErrorCode
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.native_file_opener.bridge_gen.file_open_path import FileOpenPath
from dropbox.foundation.native_file_opener.bridge_gen.file_open_type import FileOpenType
from dropbox.foundation.native_file_opener.bridge_gen.icon_info import IconInfo
from dropbox.foundation.native_file_opener.bridge_gen.path_open_properties import PathOpenProperties
from dropbox.foundation.native_file_opener.core import CoreNativeFileOpener, CoreNativeFileOpenerGandalfInterface, OpenFileResult
from dropbox.foundation.native_file_opener.dangerous_whitelist import DANGEROUS_NATIVE_OPEN_WHITELIST
from dropbox.foundation.native_file_opener.logger import log_pap_open_file, log_to_pap_for_open_events
from dropbox.foundation.native_file_opener.open_with import get_dropbox_icon, get_dropbox_paper_icon
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals import Signal
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.foundation.types.paths import FSPath, PathConverter
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import ServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper

class _CoreNativeFileOpenerUserStormcrowAdapter(CoreNativeFileOpenerGandalfInterface):
    pass
# WARNING: Decompyle incomplete

NativeFileOpenerFileInfo = NamedTuple('NativeFileOpenerFileInfo', [
    ('local_path', Optional[Text]),
    ('resolved_local_path', Optional[Text]),
    ('is_locally_available', bool),
    ('can_open_directly', bool),
    ('open_application_identifier', Optional[Text]),
    ('open_application_name', Optional[Text]),
    ('path_is_dir', bool),
    ('is_placeholder', bool),
    ('error_message', Optional[Text])])

class NativeFileOpener(Destroyable):
    pass
# WARNING: Decompyle incomplete


class ContextBoundNativeFileOpener(NativeFileOpenerBridgeInterface, Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

