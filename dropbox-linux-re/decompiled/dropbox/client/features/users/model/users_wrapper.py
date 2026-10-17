# Source Generated with Decompyle++
# File: users_wrapper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Dict, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.users import UserCache, UserInfo
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.foundation.transitional.connection_pool import make_delayed_network_call
from dropbox.model.types import FileId
from dropbox.threading import Lock

class UserCacheWrapper(Singleton):
    pass
# WARNING: Decompyle incomplete

