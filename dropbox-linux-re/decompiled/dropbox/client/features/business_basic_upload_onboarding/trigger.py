# Source Generated with Decompyle++
# File: trigger.pyc (Python 3.11)

import uuid
from typing import Optional
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary

class BusinessBasicUploadOnboardingTrigger(SingletonActor):
    pass
# WARNING: Decompyle incomplete

