# Source Generated with Decompyle++
# File: sharing_logger.pyc (Python 3.11)

import hashlib
from enum import auto, Enum
from time import time as _time
from typing import Any, Callable, Text
from uuid import uuid4
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.foundation.futures.basic import Future
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.transitional.connection_pool import make_delayed_network_call
from dropbox.sharing.constants.content import Content
from dropbox.sharing.constants.network_response import NetworkResponse
from dropbox.sharing.utils.network_util import request_and_handle
from dropbox.tiburon_log import get_rlkey_sha1_from_url, get_scl_token_sha1_from_url, get_subpath_from_url, get_tkey_sha1_from_url, log_tiburon_event

class ShareDesktopTiburonEvent(Enum):
    BEGIN_SHARE_FLOW = auto()
    CLICK_INBAND_SHARE_BUTTON = auto()
    CLIENT_APIV2_ERROR = auto()
    COPY_CAPTURE_SHARED_LINK_ERROR = auto()
    COPY_CAPTURE_SHARED_LINK_SUCCESS = auto()
    COPY_CAPTURE_SHARED_LINK_OVERQUOTA = auto()
    COPY_LINK_FROM_SCREENSHOT_SAVED_TO_DBX_ERROR = auto()
    COPY_LINK_FROM_SCREENSHOT_SAVED_TO_DBX_SUCCESS = auto()
    COPY_LINK_FROM_SCREENSHOT_SAVED_TO_DBX_OVERQUOTA = auto()
    COPY_LINK_FROM_SCREENRECORDING_SAVED_TO_DBX_ERROR = auto()
    COPY_LINK_FROM_SCREENRECORDING_SAVED_TO_DBX_SUCCESS = auto()
    COPY_LINK_FROM_SCREENRECORDING_SAVED_TO_DBX_OVERQUOTA = auto()
    COPY_SHARED_LINK_ERROR = auto()
    COPY_SHARED_LINK_SUCCESS = auto()
    COPY_SHARED_LINK_OVERQUOTA = auto()
    DESKTOP_SERVER_ERROR = auto()
    DESKTOP_TRANSIENT_ERROR = auto()
    DESKTOP_UNKNOWN_ERROR = auto()
    INITIATE_COPY_CAPTURE_SHARED_LINK = auto()
    INITIATE_COPY_LINK_FROM_SCREENSHOT_SAVED_TO_DBX = auto()
    INITIATE_COPY_LINK_FROM_SCREENRECORDING_SAVED_TO_DBX = auto()
    INITIATE_COPY_SHARED_LINK = auto()
    LOCAL_VIEWS_SHARE_MODAL_OPEN = auto()
    LOCAL_VIEWS_SHARE_MODAL_OPEN_SUCCESS = auto()
    ON_GET_ACCOUNT_INFO_DONE = auto()
    TIBURON_SHARE_SHOWN_IN_CONTEXT_MENU = auto()
    TIBURON_VIEW_CONTEXT_MENU = auto()
    TIBURON_SHARING_NEW_PREDICATE_REGRESSION = auto()


class SharingLogger(Destroyable):
    pass
# WARNING: Decompyle incomplete

