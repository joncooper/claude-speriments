# Source Generated with Decompyle++
# File: document_presence_reporter.pyc (Python 3.11)

from typing import List, Optional
from dropbox.client.features.harmony_gating import desktop_presence_reporting_enabled
from dropbox.client.features.presence.model.presence_tracker import PresenceTracker
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.signals import SignalConnection
from dropbox.harmony.models.types import ApplicationID, DocumentSessionID
from dropbox.harmony.window_tracking.document_session_manager import DocumentSessionManager
from dropbox.harmony.window_tracking.supported_applications import presence_supported_apps
from dropbox.platform import IS_MAC, IS_WINDOWS

class DocumentPresenceReporter(Actor):
    pass
# WARNING: Decompyle incomplete

