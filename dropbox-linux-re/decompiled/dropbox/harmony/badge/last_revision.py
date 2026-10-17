# Source Generated with Decompyle++
# File: last_revision.pyc (Python 3.11)

import math
from typing import cast, NamedTuple, Optional, Text
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.ui.common.harmony import HarmonyStrings
from dropbox.client.users import UserInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.signals import StandardSignal
from dropbox.foundation.signals.event import EventSignal
from dropbox.harmony.models.harmony_session_state import LastRevisionSnapshot, LastRevisionState
from dropbox.harmony.utility.constants import DROPBOX_SERVER_USER_ID
from dropbox.i18n import ago
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath, MRLowerServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper, SyncEngineWrapper
from dropbox.sync_engine_boundary.types import Revision
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.trace import TRACE

class LastRevision(Actor):
    pass
# WARNING: Decompyle incomplete

