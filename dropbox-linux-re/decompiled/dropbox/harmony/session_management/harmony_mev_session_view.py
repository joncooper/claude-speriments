# Source Generated with Decompyle++
# File: harmony_mev_session_view.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.client.fenix.journeys.harmony.utils import get_harmony_document_session_view
from dropbox.client.fenix.types.harmony import DocumentSessionUpdateType, DocumentSessionView
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_1
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface
from dropbox.harmony.models.types import DocumentSession, DocumentSessionID, WindowID
from dropbox.harmony.session_management.harmony_mev_session_vm import HarmonyMEVSessionVM
from dropbox.harmony.session_management.harmony_session_update_tracker import HarmonySessionUpdateTracker, HarmonyUpdateInfo
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from dropbox.harmony.win.ignored_windows import IgnoredWindows

class HarmonyMEVSessionView(Actor):
    pass
# WARNING: Decompyle incomplete

