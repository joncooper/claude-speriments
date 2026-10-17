# Source Generated with Decompyle++
# File: file_presence.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Dict, List, Optional, Set, Text, Tuple
from six import iteritems
from dropbox.client.features.presence.model.file_presence import FilePresence
from dropbox.client.features.presence.model.types import PresenceInfo, PresenceStatus
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.presence.model import BeaconAgent, BeaconInfo
from dropbox.client.users import UserInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.signals import StandardSignal
from dropbox.harmony.models.harmony_user import HarmonyUser
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.trace import TRACE

class FilePresenceVM(Actor):
    pass
# WARNING: Decompyle incomplete

