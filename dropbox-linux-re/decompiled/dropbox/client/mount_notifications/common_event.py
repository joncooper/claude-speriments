# Source Generated with Decompyle++
# File: common_event.pyc (Python 3.11)

from enum import Enum
from typing import Text

class MountChangeKind(Enum):
    UNMOUNT = 1
    UNKNOWN = 2


class CommonEvent:
    
    def __init__(self = None, device_path = None, event_kind = None):
        self.device_path = device_path
        self.event_kind = event_kind


