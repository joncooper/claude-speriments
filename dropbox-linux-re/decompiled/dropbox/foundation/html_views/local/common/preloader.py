# Source Generated with Decompyle++
# File: preloader.pyc (Python 3.11)

from time import monotonic
from typing import Callable, Deque, Generic, NamedTuple, Optional, Text, Tuple, TypeVar
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.futures.basic import flatten_future
from dropbox.trace import TRACE
_O = TypeVar('_O')
PreloadMetadata = NamedTuple('PreloadMetadata', [
    ('was_preloaded', bool),
    ('reason', Text),
    ('previous_object_id', Optional[Text]),
    ('seconds_since_previous', Optional[float])])
TryCreateMetadata = NamedTuple('TryCreateMetadata', [
    ('reason', Text),
    ('previous_object_id', Optional[Text]),
    ('seconds_since_previous', Optional[float])])

def ObjectPreloader():
    '''ObjectPreloader'''
    pass
# WARNING: Decompyle incomplete

ObjectPreloader = <NODE:27>(ObjectPreloader, 'ObjectPreloader', Actor, Generic[_O])
