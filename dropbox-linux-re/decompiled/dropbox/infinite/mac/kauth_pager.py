# Source Generated with Decompyle++
# File: kauth_pager.pyc (Python 3.11)

import os
import sys
from typing import cast, Dict, Union
from macinfinite.common import process_path
from macinfinite.kern_control import KernControl, KextAccessRequest, KextMoveRequest, REQUEST_TYPE_CANCEL_ACCESS, REQUEST_TYPE_CANCEL_MOVE, REQUEST_TYPE_LOG_ACCESS, REQUEST_TYPE_REQUEST_ACCESS, REQUEST_TYPE_REQUEST_EXTERNAL_ACCESS, REQUEST_TYPE_REQUEST_MOVE, RESPONSE_ALLOW_FILE_ACCESS, RESPONSE_ALLOW_PLACEHOLDER_ACCESS, RESPONSE_DENY_ACCESS
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.infinite.blacklist import InfiniteRecallBlacklist
from dropbox.infinite.mac.util import check_unsigned_run_box_access_error
from dropbox.infinite.pager import CancelMoveRequest, CancelPageRequest, InfiniteRequest, MoveFileRequest, PageFileRequest, PageFolderRequest, Pager, PagerCommunicationError, PageResponse, PagerMissingElevationError, PagerNotLoadedError, PagerRequestType
from dropbox.sync_engine_boundary.infinite.mac.xattr_placeholder_context import XattrPlaceholderContext
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False

class KauthPager(Pager):
    pass
# WARNING: Decompyle incomplete


def _convert_page_response(user_response = None):
    if user_response == PageResponse.CANCEL:
        return RESPONSE_DENY_ACCESS
    if None == PageResponse.CONTINUE:
        return RESPONSE_ALLOW_FILE_ACCESS
    if None == PageResponse.CONTINUE_STILL_PLACEHOLDER:
        return RESPONSE_ALLOW_PLACEHOLDER_ACCESS


def _request_thread_id(request = None):
    return request.thread_id

