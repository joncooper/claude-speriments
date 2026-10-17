# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from enum import Enum
from typing import NamedTuple

class NavigationContentType(Enum):
    LOCAL_VIEW = 0
    LEGACY_VIEW = 1
    SERVER_VIEW = 3


class NavigationWindowType(Enum):
    STANDALONE = 0
    TRAY = 1

NavigationVisibilityConfig = NamedTuple('NavigationVisibilityConfig', [
    ('visible', bool),
    ('autoclose_timeout_secs', int)])
