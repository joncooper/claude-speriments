# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import annotations
from enum import Enum
from typing import NamedTuple
from dropbox.foundation.types.rect import Size
WindowWillCreateResult = NamedTuple('WindowWillCreateResult', [
    ('size', Size)])

class WindowManagerDelegateType(Enum):
    DEFAULT = 0
    SETUP_WIZARD = 1
    STUB = 2
    box = (lambda cls = None, obj = None: obj.value)()

