# Source Generated with Decompyle++
# File: editor_tracking.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractproperty
from typing import Optional
from dropbox.callbacks import create_weakref_callback
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.futures.basic import CancelledFutureException, flatten_future, IncompleteFutureException
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.raii2.arc import Arc, Weak
from dropbox.foundation.signals import StandardSignal
from dropbox.harmony.models.types import DocumentSession, DocumentSessionID
from dropbox.harmony.plugins.base import EditorStatusTracker, HarmonyPlugin
from dropbox.harmony.plugins.broker import PluginBroker
from dropbox.harmony.utility.exceptions import StateNotAvailableError
from dropbox.harmony.window_tracking.document_session_manager import DocumentSessionManager
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.sync_engine_adapter.wrapper import SyncEngineWrapper
from dropbox.trace import TRACE

class EditorTrackingInterface(Actor):
    state_change_signal = (lambda self = None: pass)()
    is_saved = (lambda self = None: pass)()


class EditorTrackingStub(Actor, EditorTrackingInterface):
    pass
# WARNING: Decompyle incomplete


class EditorTracking(Actor, EditorTrackingInterface):
    pass
# WARNING: Decompyle incomplete

