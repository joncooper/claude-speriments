# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Dict, NamedTuple
from dropbox.shared.util import safe_navigate

class PresenceStatus(Enum):
    Offline = ''
    Viewer = 'viewer'
    Modifier = 'modifier'

START_TS_KEY = 'start_ts'

class PresenceInfo(NamedTuple):
    platform: 'int' = 'PresenceInfo'
    is_editing = (lambda self = None: self.status == PresenceStatus.Modifier)()
    last_edited = (lambda self = None: 