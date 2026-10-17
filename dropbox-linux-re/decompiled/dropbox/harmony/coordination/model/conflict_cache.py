# Source Generated with Decompyle++
# File: conflict_cache.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Tuple
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import StandardSignal
from dropbox.functions import lrudict
from dropbox.harmony.coordination.model.types import CoordinationUpdate
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE

class ConflictCache(SingletonActor):
    pass
# WARNING: Decompyle incomplete

