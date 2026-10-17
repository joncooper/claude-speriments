# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import NamedTuple, Optional, Text, Union
from dropbox.client.users import UserInfo
from dropbox.shared.local_path import LocalPath

class CoordinationStage(Enum):
    NoUpdate = 'no-update'
    Ready = 'ready'
    Pending = 'pending'
    Coordinating = 'coordinating'

CoordinationUpdate = NamedTuple('CoordinationUpdate', [
    ('user_id', int),
    ('timestamp', Union[(int, float)]),
    ('fileid', bytes),
    ('local_path', LocalPath),
    ('update_failed', bool)])
_CoordinationState = NamedTuple('_CoordinationState', [
    ('update', Optional[CoordinationUpdate]),
    ('stage', CoordinationStage)])
CoordinationInfo = NamedTuple('CoordinationInfo', [
    ('user', Optional[UserInfo]),
    ('stage', CoordinationStage),
    ('is_saved', bool)])

class CoordinationState(_CoordinationState):
    pass
# WARNING: Decompyle incomplete

