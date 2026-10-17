# Source Generated with Decompyle++
# File: event_hub.pyc (Python 3.11)

from typing import Any, Callable, Dict, Optional, Text
from apex.metrics import MetricsReporter
from dropbox.client.fenix.constants import EventHubEvents, UserJourneyNames
from dropbox.client.fenix.types.harmony import DocumentSessionUpdateType, DocumentSessionView
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import FutureHelpers
from dropbox.foundation.futures.basic import Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.trace import TRACE
InvocationHandlerFunc = Callable[([
    JSONDict], Future[JSONish])]

class EventHubAccessor:
    Instance: "Optional['EventHub']" = None


class EventHub(Actor):
    pass
# WARNING: Decompyle incomplete

