# Source Generated with Decompyle++
# File: coordination.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Optional
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.ui.common.harmony import HarmonyStrings
from dropbox.client.users import UserInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.signals import StandardSignal
from dropbox.harmony.coordination.model.coordination import Coordination
from dropbox.harmony.coordination.model.types import CoordinationInfo, CoordinationStage
from dropbox.harmony.presence.editor_tracking import EditorTrackingInterface
from dropbox.model.types import FileId
from dropbox.trace import TRACE

class CoordinationVM(Actor):
    pass
# WARNING: Decompyle incomplete

