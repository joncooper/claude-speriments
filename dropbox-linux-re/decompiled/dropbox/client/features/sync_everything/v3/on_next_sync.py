# Source Generated with Decompyle++
# File: on_next_sync.pyc (Python 3.11)

from typing import Optional
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function
from dropbox.client.features.sync_everything.v3.errors import RequestAssertion
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingErrorName, SyncEverythingLogger
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_progress import SyncedCursor, SyncPhase, SyncProgress

class OnNextSync(Actor):
    pass
# WARNING: Decompyle incomplete

