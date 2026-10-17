# Source Generated with Decompyle++
# File: img_handler.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import random as insecure_random
from enum import Enum
from functools import partial
from typing import Dict, List, Optional, Text, Union
from apex.metrics import Metric
from build_number import BuildChannel, dropbox_version
from build_number.features import feature_enabled
from typing_extensions import Literal
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountManager, AccountUpdate, AccountUpdateType
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import CancelledFuture, CancelledFutureException, Future, ResolvedFuture
from dropbox.foundation.futures.thread import ThreadPoolExecutor
from dropbox.foundation.html_views.common.navigation_rules import LOCAL_VIEW_NATIVE_IMG_PATH_PREFIX
from dropbox.foundation.native_icon.manager import get_icon_size_from_text, NativeIconManager
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.foundation.scheme_handler.interface import CustomSchemeHandlerInterface
from dropbox.foundation.scheme_handler.types import CustomSchemeHandlerResult, CustomSchemeUrlRequest
from dropbox.foundation.scheme_handler.util import get_mime_type_for_ext
from dropbox.threading import Lock
from dropbox.trace import TRACE, WARNING
NATIVE_IMG_RELIABILITY_SAMPLE_RATE = {
    BuildChannel.stable: 0.0001,
    BuildChannel.beta: 0.01,
    BuildChannel.internal_alpha: 0.05 }.get(dropbox_version.channel, 0)
SHOULD_REPORT_NATIVE_IMG_RELIABILITY = insecure_random.random() < NATIVE_IMG_RELIABILITY_SAMPLE_RATE
NativeImgReliabilityEventName = Union[(Literal['native_img_requested'], Literal['native_img_cancelled'], Literal['native_img_error'], Literal['native_img_not_found'], Literal['native_img_succeeded'])]

class NativeImgType(Enum):
    FILE_ICON = 'file_icon'
    FILE_THUMBNAIL = 'file_thumbnail'
    UNKNOWN = 'unknown'


class LocalViewNativeImgHandler(Singleton, CustomSchemeHandlerInterface):
    pass
# WARNING: Decompyle incomplete

