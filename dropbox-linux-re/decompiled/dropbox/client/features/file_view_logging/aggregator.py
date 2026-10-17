# Source Generated with Decompyle++
# File: aggregator.pyc (Python 3.11)

from collections import deque
from typing import Any, Deque, Dict, List, Text
from dropbox.client.features.file_locking.file_locking_controller import FileLockingAccessor
from dropbox.client.features.file_view_logging.constants import DESKTOP_PASS_VIEW_LOGGING_STORMCROW, FileView
from dropbox.client.features.poll_runner.poll_runner import PollRunnerWithBackoff
from dropbox.client.product_span import ProductSpan
from dropbox.client_api.exceptions import HTTP429Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import ConnectionBackoff
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_1
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.harmony.utility.constants import FileViewActionType, FileViewOriginType
from dropbox.trace import TRACE
SerializedFileView = Dict[(Text, Any)]

class FileViewAggregator(Actor):
    pass
# WARNING: Decompyle incomplete

