# Source Generated with Decompyle++
# File: user_active_tracker.pyc (Python 3.11)

from time import time as _time
from typing import List
from dropbox.client.features.home_feed.shared.model.constants import AssistantFeature
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_rare_event
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.signals import RepeatedEventSignal
from dropbox.trace import TRACE

class UserActiveTracker(Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

