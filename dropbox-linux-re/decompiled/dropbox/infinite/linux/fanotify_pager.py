# Source Generated with Decompyle++
# File: fanotify_pager.pyc (Python 3.11)

import errno
import os
import socket
import subprocess
import sys
import time
from typing import cast, Optional, Text
from build_number import dropbox_version
from lib.linuxinfinite.comm import FAN_ALLOW, FAN_DENY, FROM_CLIENT_RESPONSE, FROM_CLIENT_SHUTDOWN_REQUEST, FROM_CLIENT_STATE, FROM_CLIENT_VERSION, FromClientResponse, FromClientState, FromClientVersion, get_sock_msg, sendmsg, TO_CLIENT_LOG, TO_CLIENT_REQUEST, TO_CLIENT_VERSION, ToClientLog, ToClientRequest, ToClientVersion
from lib.linuxinfinite.common import ERROR_DESCRIPTION
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.functions import make_bytes
from dropbox.infinite.blacklist import InfiniteRecallBlacklist
from dropbox.infinite.pager import InfiniteRequest, PageFileRequest, Pager, PagerCommunicationError, PageResponse, PagerNotLoadedError, PagerRequestType
from dropbox.sync_engine_boundary.infinite.linux.xattr_placeholder_context import XattrPlaceholderContext
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
_UNUSED_CLIENT_USER_ID = -1

def _normalize_listener_returncode(returncode = None):
    pass
# WARNING: Decompyle incomplete


class FanotifyPager(Pager):
    pass
# WARNING: Decompyle incomplete

