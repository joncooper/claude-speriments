# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

import functools
import time
from abc import abstractmethod, abstractproperty
from os import path
from typing import Any, Callable, Dict, Iterable, List, Mapping, NamedTuple, Optional, Set, Text, Tuple, Union
from dropbox.client.background_worker import on_background_thread
from dropbox.client.cloud_docs.constants import CloudDocsValidationErrorCode
from dropbox.client.cloud_docs.file_validator import is_cloud_docs_extension
from dropbox.client.cloud_docs.user_scoped_file_opener import UserScopedCloudDocsFileOpener
from dropbox.client.file_activation.constants import FileOpenStage
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client.util import app_display_name_for_file, app_for_file, highlight_file, is_dir as is_path_dir, launch_app, launch_folder
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.native_file_opener.bridge_gen.app_info import AppInfo
from dropbox.foundation.native_file_opener.bridge_gen.app_info_list import AppInfoList
from dropbox.foundation.native_file_opener.bridge_gen.file_open_bridge_error import FileOpenBridgeError
from dropbox.foundation.native_file_opener.bridge_gen.file_open_error_code import FileOpenErrorCode
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.native_file_opener.open_with import get_associated_applications, open_with_application
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.foundation.signals import Signal
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.functions import file_extension
from dropbox.i18n import trans
from dropbox.model.types import FileId
from dropbox.platform import IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import RRCasedServerPath, ServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.remote_props import FolderPolicyStatus
from dropbox.trace import TRACE
on_background_thread_future = make_on_thread_future_decorator(on_background_thread, 'on_background_thread_future')

class OpenFileError(Exception):
    pass
# WARNING: Decompyle incomplete

OpenFileResult = NamedTuple('OpenFileResult', [
    ('error', Optional[FileOpenBridgeError]),
    ('can_open_directly', Optional[bool]),
    ('app_for_file', Optional[Text]),
    ('app_display_name', Optional[Text])])

class CoreNativeFileOpenerGandalfInterface(Destroyable):
    get_variant = (lambda self = None, feature = None: raise NotImplementedError)()
    on_changed = (lambda self = None: raise NotImplementedError)()

CoreNativeFileOpenerWhitelistFetcher = Callable[([], Dict[(Text, Any)])]

class CoreNativeFileOpener(Destroyable):
    pass
# WARNING: Decompyle incomplete

