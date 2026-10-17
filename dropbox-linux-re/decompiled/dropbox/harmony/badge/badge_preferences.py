# Source Generated with Decompyle++
# File: badge_preferences.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Any
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals import StandardSignal
from dropbox.preferences import OPT_HARMONY, OPT_HARMONY_VISIBILITY

class BadgeVisibility(Enum):
    Never = 0
    Always = 1
    OthersPresent = 2


class BadgePreferences(Destroyable):
    pass
# WARNING: Decompyle incomplete

