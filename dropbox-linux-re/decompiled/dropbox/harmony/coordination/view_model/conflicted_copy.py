# Source Generated with Decompyle++
# File: conflicted_copy.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import math
import os
import time
from typing import Optional, Tuple
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.ui.common.harmony import HarmonyStrings
from dropbox.client.users import UserInfo
from dropbox.client.util import launch_app
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_1
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.signals import StandardSignal
from dropbox.harmony.coordination.model.conflict_cache import ConflictCache
from dropbox.harmony.coordination.model.types import CoordinationUpdate
from dropbox.harmony.models.harmony_session_state import ConflictedCopyState, OriginalCopyState
from dropbox.i18n import ago
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE

class ConflictVM(Actor):
    pass
# WARNING: Decompyle incomplete

