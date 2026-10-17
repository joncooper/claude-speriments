# Source Generated with Decompyle++
# File: smarter_smart_sync_manager.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Dict, List, Optional
from build_number.features import feature_enabled
from dropbox.client.features.smarter_smart_sync.feature import SmarterSmartSyncFeature
from dropbox.client.features.smarter_smart_sync.smarter_smart_sync_controller import SmarterSmartSyncController
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_2
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2.arc import Arc
from dropbox.trace import TRACE
SmarterSmartSyncControllerArc = Arc[SmarterSmartSyncController]

class SmarterSmartSyncManager(Actor):
    pass
# WARNING: Decompyle incomplete

