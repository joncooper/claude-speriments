# Source Generated with Decompyle++
# File: harmony_session_update_tracker.pyc (Python 3.11)

from typing import NamedTuple, Optional
from dropbox.client.fenix.types.harmony import DocumentSessionUpdateType, DocumentSessionView
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import StandardSignal
from dropbox.harmony.models.types import DocumentSessionID
HarmonyUpdateInfo = NamedTuple('HarmonyUpdateInfo', [
    ('document_session_id', Optional[DocumentSessionID]),
    ('document_session_view', Optional[DocumentSessionView]),
    ('update_type', DocumentSessionUpdateType)])

class HarmonySessionUpdateTracker(SingletonActor):
    pass
# WARNING: Decompyle incomplete

