# Source Generated with Decompyle++
# File: bolt_client.pyc (Python 3.11)

from __future__ import annotations
from concurrent.futures import Future
from typing import Dict, Iterable, List, NamedTuple, Sequence, Set, Tuple
from dropbox.client.bolt.signalling import BoltClient
from dropbox.client.bolt.types import BoltAppID, BoltChannelId, BoltChannelState, BoltRevisionInfo
from dropbox.lock_ordering import NonRecursiveLock
SubscribeResult = NamedTuple('SubscribeResult', [
    ('updated', Sequence[BoltChannelState]),
    ('invalid', Sequence[BoltChannelId])])
_ChannelState = NamedTuple('_ChannelState', [
    ('futures', 'Set[_SubscribeFuture]'),
    ('revision_info', BoltRevisionInfo)])

class NucleusBoltClient:
    
    def __init__(self = None, bolt_client = None):
        self._client = bolt_client
        self._lock = NonRecursiveLock()
        self._channels = { }
        self._handled_apps = set()

    
    def subscribe(self = None, channel_states = None):
        states = tuple(channel_states)
        future = _SubscribeFuture(states, self)
        self._lock
        known_updated = []
    # WARNING: Decompyle incomplete

    
    def _register_app_handler_locked(self = None, app_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _unlink_future_locked(self = None, future = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _trigger_channel_locked(self = None, channel_id = None, updated = None, invalid = ((),)):
        pass
    # WARNING: Decompyle incomplete

    
    def _trigger_future_locked(self = None, future = None, updated = None, invalid = ((),)):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_bolt_update(self = None, updated = None, invalid = None):
        self._lock
        for state in updated:
            channel = self._channels.get(state.channel_id, None)
            if not channel:
                continue
            if state.revision_info.revision <= channel.revision_info.revision:
                continue
            self._trigger_channel_locked(state.channel_id, updated, invalid)
            for channel_id in invalid:
                if channel_id in self._channels:
                    self._trigger_channel_locked(channel_id, updated, invalid)
                None(None, None)
                return None
                with None:
                    if not None:
                        pass


MYPY = False

class _SubscribeFuture(BaseFuture):
    pass
# WARNING: Decompyle incomplete

