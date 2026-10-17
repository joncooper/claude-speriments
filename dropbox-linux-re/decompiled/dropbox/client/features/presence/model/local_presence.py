# Source Generated with Decompyle++
# File: local_presence.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, List, Optional, Tuple
import six
from dropbox.client.bolt.types import BoltToken
from dropbox.client.features.presence.model.beacon import BeaconTransmitter
from dropbox.client.features.presence.model.presence_context_mixin import PresenceContextMixin
from dropbox.client.features.presence.model.types import PresenceStatus
from dropbox.client.presence.model import BeaconContextInfo
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_1, async_queued_method_3
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures.basic import flatten_future, Future, ResolvedFuture
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import SignalConnection
from dropbox.functions import lrudict
from dropbox.harmony.utility.constants import BEACON_AUTH_KEY, PRESENCE_APP_ID
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.bolt.types import BoltUniqueID
    FileObjID = BoltUniqueID

class LocalPresence(PresenceContextMixin, SingletonActor):
    pass
# WARNING: Decompyle incomplete

