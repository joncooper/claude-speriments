# Source Generated with Decompyle++
# File: poll_runner.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, Optional
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import get_jittered_seconds
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method, async_queued_method_0_1
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.threading import Lock
from dropbox.trace import TRACE
SECONDS_PER_HOUR = 3600

class PollRunner(Actor):
    pass
# WARNING: Decompyle incomplete


class PollRunnerWithBackoff(PollRunner):
    pass
# WARNING: Decompyle incomplete


class PollRunnerWithModifiedOneOffExecution(PollRunner):
    pass
# WARNING: Decompyle incomplete

