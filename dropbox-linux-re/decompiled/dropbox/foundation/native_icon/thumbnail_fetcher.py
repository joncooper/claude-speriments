# Source Generated with Decompyle++
# File: thumbnail_fetcher.pyc (Python 3.11)

import base64
from typing import Any, Callable, cast, Dict, Optional, Tuple
from apex.metrics import Metric, MetricsReporter
from dropbox import fsutil
from dropbox.client_api.exceptions import DropboxResponseClientError, DropboxResponseServerError, HTTP429Error, is_transient_error
from dropbox.client_api.thumbnailer import ThumbnailSize
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.native_icon.thumbnailer_wrapper import ThumbnailerWrapper
from dropbox.foundation.native_icon.util import create_metrics_reporter
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.scheme_handler.interface import CUSTOM_SCHEME_HANDLER_AMP_NAMESPACE
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_path import InvalidDropboxFilenameException
from dropbox.trace import TRACE
THUMBNAIL_FETCH_METRIC = 'native_file_icon/smart_sync_thumbnail_fetch'
NETWORK_RESULT_TAG_NAME = 'network_result'
THUMBNAIL_RESULT_TAG_NAME = 'thumbnail_result'
NETWORK_FAILURE_TAG_VALUE = 'network_failure'
UNSUPPORTED_EXTENSION_TAG_VALUE = 'unsupported_extension'
MISSING_ENTRIES_TAG_VALUE = 'response_missing_entries_failure'
WRONG_ENTRY_COUNT_TAG_VALUE = 'wrong_entry_count_failure'
NOT_PRESENT_TAG_VALUE = 'not_present_on_server_failure'
DECODE_FAILURE_TAG_VALUE = 'decode_failure'
SUCCESS_TAG_VALUE = 'success'
INVALID_FILENAME_TAG_VALUE = 'invalid_dropbox_filename'

class SmartSyncThumbnailFetcher(Destroyable):
    pass
# WARNING: Decompyle incomplete

