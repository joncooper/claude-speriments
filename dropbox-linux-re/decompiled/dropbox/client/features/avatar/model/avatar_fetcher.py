# Source Generated with Decompyle++
# File: avatar_fetcher.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import base64
import time
from functools import partial
from typing import List, Optional, Text
from avatar_db import AvatarDbActor, AvatarItem
from dropbox.client_api.exceptions import ClientInitiatedDisconnect, DropboxResponseClientError, DropboxResponseServerError, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.futures.future_collection import MultiFutureCollection
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import StandardSignal
from dropbox.foundation.transitional import make_delayed_network_call

class CachedAvatarFetcher(SingletonActor):
    pass
# WARNING: Decompyle incomplete

