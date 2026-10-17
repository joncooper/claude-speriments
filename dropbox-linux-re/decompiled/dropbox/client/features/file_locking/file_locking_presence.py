# Source Generated with Decompyle++
# File: file_locking_presence.pyc (Python 3.11)

from typing import List
from dropbox.client.features.file_locking.file_locking_controller import FileLockingAccessor
from dropbox.client.features.octave.gating import EXCEL_AID, POWERPOINT_AID, SKETCH_AID, SUPPORTED_AIDS, WORD_AID
from dropbox.foundation.context.user import UserContext
from dropbox.harmony.models.types import ApplicationID, DocumentSessionID
from dropbox.harmony.presence.document_presence_reporter import DocumentPresenceReporter
from dropbox.harmony.window_tracking.supported_applications import harmony_supported_apps
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.server_path import MRCasedServerPath
MAC_AIDS = SUPPORTED_AIDS | {
    EXCEL_AID,
    POWERPOINT_AID,
    WORD_AID,
    SKETCH_AID}

class FileLockingPresenceReporter(DocumentPresenceReporter):
    pass
# WARNING: Decompyle incomplete

