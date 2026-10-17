# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

from typing import List, Optional
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.shared.quota_info import QuotaInfo
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncOperationFailureReason
from dropbox.sync_engine_boundary.types.sync_failures import SyncOpFailed
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress

class QuotaUsageManager(Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

