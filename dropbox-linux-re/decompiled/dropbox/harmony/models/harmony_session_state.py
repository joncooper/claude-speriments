# Source Generated with Decompyle++
# File: harmony_session_state.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Any, List, NamedTuple, Optional, Text
from dropbox.client.users import UserInfo
from dropbox.harmony.coordination.model.types import CoordinationInfo
from dropbox.harmony.models.harmony_user import HarmonyUser
from dropbox.harmony.models.types import WindowID
from dropbox.sync_engine_boundary.types import Revision
from dropbox.sharing.shared_content_members_fetcher import SharedContentMember

class FlyoutState(Enum):
    NoFlyout = 0
    Info = 1
    Coordination = 2
    OriginalCopy = 3

ConflictedCopyState = NamedTuple('ConflictedCopyState', [
    ('caption', Text),
    ('message', Text),
    ('icon', Text)])
OriginalCopyState = NamedTuple('OriginalCopyState', [
    ('caption', Text),
    ('message', Text),
    ('footnote', Text),
    ('icon', Text)])
LastRevisionState = NamedTuple('LastRevisionState', [
    ('caption', Text),
    ('message', Text),
    ('file_history_message', Text)])
LastRevisionSnapshot = NamedTuple('LastRevisionSnapshot', [
    ('revision', Optional[Revision]),
    ('editor', Optional[UserInfo]),
    ('state', Optional[LastRevisionState])])
SeenStateInfo = NamedTuple('SeenStateInfo', [
    ('viewed_members', List[SharedContentMember])])

class BadgeVersion:
    MEV = 'mev'

_HarmonyMEVSessionState = NamedTuple('_HarmonyMEVSessionState', [
    ('visible', bool),
    ('flyout', FlyoutState),
    ('wid', Optional[WindowID]),
    ('is_saved', bool),
    ('coordination_info', Optional[CoordinationInfo]),
    ('viewers', List[HarmonyUser]),
    ('original_copy', Optional[OriginalCopyState]),
    ('conflicted_copy', Optional[ConflictedCopyState]),
    ('last_revision', Optional[LastRevisionSnapshot]),
    ('seen_states', SeenStateInfo),
    ('badge_version', Optional[str])])

class HarmonyMEVSessionState(_HarmonyMEVSessionState):
    pass
# WARNING: Decompyle incomplete

