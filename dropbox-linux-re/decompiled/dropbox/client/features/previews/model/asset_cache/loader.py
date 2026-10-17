# Source Generated with Decompyle++
# File: loader.pyc (Python 3.11)

import json
import time
from enum import Enum
from io import BytesIO
from typing import Any, Dict, List, Optional, Text, Tuple, Union
from dropbox.client.features.previews.helpers import normalize_and_sign_url
from dropbox.client.features.previews.model.asset_cache.manager import AssetCacheManager
from dropbox.client_api.connection_util import ConnectionResponse
from dropbox.client_api.exceptions import DropboxResponseClientError, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.threading import Lock
CONN_NAME = 'previews-dbx-server'
CACHE_CONTROL = 'cache-control'
NO_CACHE = 'no-cache'
NO_STORE = 'no-store'

class AssetLoaderCacheOutcome(Enum):
    HIT = 'HIT'
    MISS = 'MISS'
    SKIP = 'SKIP'
    BAN = 'BAN'

ResponseOrError = Union[(ConnectionResponse, DropboxResponseClientError, TransientNetworkError)]
AssetResponse = Tuple[(AssetLoaderCacheOutcome, ConnectionResponse)]

class PreviewsAssetLoader(SingletonActor):
    pass
# WARNING: Decompyle incomplete

