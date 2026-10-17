# Source Generated with Decompyle++
# File: bolt_client_wrapper.pyc (Python 3.11)

from typing import Callable, Dict, List, NamedTuple, Optional, Tuple
from dropbox.client.bolt import BoltChannelId, BoltChannelState
from dropbox.client.bolt.signalling import BoltClient
from dropbox.client.bolt.types import BoltAppID
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import StandardSignal
from dropbox.threading import Lock
AppSignal = StandardSignal[Tuple[(List[BoltChannelState], List[BoltChannelId])]]
_AppChangeHandler = NamedTuple('_AppChangeHandler', [
    ('signal', AppSignal),
    ('client_handler', Callable[([
        List[BoltChannelState],
        List[BoltChannelId]], None)])])

class BoltClientWrapper(SingletonActor):
    pass
# WARNING: Decompyle incomplete

