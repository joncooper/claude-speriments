# Source Generated with Decompyle++
# File: global_presence.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from collections import Counter
from typing import Any, Counter as CounterType, Dict, List, Optional, Set, Tuple
from six import itervalues
from dropbox.client.bolt import BoltChannelId, BoltChannelState, BoltRevisionInfo
from dropbox.client.bolt.payloads import ThunderClient
from dropbox.client.bolt.types import BoltAppID, BoltChannelPayloads, BoltUniqueID
from dropbox.client.features.presence.model.presence_context_mixin import PresenceContextMixin
from dropbox.client.presence.model import BeaconAgent, BeaconContextInfo, BeaconInfo, BeaconSource, PresenceStatus
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import StandardSignal
from dropbox.harmony.utility.constants import BEACON_AUTH_KEY, PRESENCE_APP_ID
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.threading import Lock
from dropbox.trace import TRACE

class GlobalPresence(PresenceContextMixin, SingletonActor):
    pass
# WARNING: Decompyle incomplete


class _GlobalPresenceState(Destroyable):
    pass
# WARNING: Decompyle incomplete

