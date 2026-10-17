# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

import time
from enum import Enum
from typing import Callable, Optional, Text, TypeVar
from dropbox.client.cloud_docs.extension_constants import CLOUD_DOC_EXTS, SHORTCUT_CLOUD_DOC_EXTS
from dropbox.client.features.desktop_logging.extension_whitelist import get_whitelisted_extension
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.futures.thread import ThreadPoolExecutor
from dropbox.foundation.native_icon.icon_db_access import IconDBAccess
from dropbox.foundation.native_icon.interface import ImageFormat
from dropbox.foundation.native_icon.loader import NativeIconLoaderFactory
from dropbox.foundation.native_icon.thumbnail_fetcher import SmartSyncThumbnailFetcher
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.functions import file_extension
from dropbox.sync_engine_boundary.exceptions import UnmountedPathError
from dropbox.trace import TRACE
_T = TypeVar('_T')
_A_WEEK_IN_SECONDS = 604800
DEFAULT_ICON_SIZE = 256
THUMBNAIL_SIZE = 256
ICON_SIZES = {
    16,
    32,
    64,
    128,
    DEFAULT_ICON_SIZE}

def get_icon_size_from_text(size_text = None):
    pass
# WARNING: Decompyle incomplete


class ImageType(Enum):
    THUMBNAIL = 't'
    ICON = 'i'


def format_path_key(path = None, image_type = None, image_format = None):
    return image_type.value + image_format.value + path


class NativeIconManager(Destroyable):
    pass
# WARNING: Decompyle incomplete

