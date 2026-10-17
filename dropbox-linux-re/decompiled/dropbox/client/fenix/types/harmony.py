# Source Generated with Decompyle++
# File: harmony.pyc (Python 3.11)

from enum import StrEnum
from typing import List, Optional, TypedDict
from dropbox.client.fenix.types.user_info import UserInfo

class Viewer(TypedDict):
    user: 'Optional[UserInfo]' = 'Viewer'


class CoordinationInfo(TypedDict):
    stage: 'str' = 'CoordinationInfo'


class LastRevision(TypedDict):
    revision_ts: 'int' = 'LastRevision'


class SharedContentMember(TypedDict):
    account_id: 'Optional[str]' = 'SharedContentMember'


class DocumentSessionView(TypedDict):
    viewed_members: 'List[SharedContentMember]' = 'DocumentSessionView'


class DocumentSessionUpdateType(StrEnum):
    STARTED = 'started'
    ENDED = 'ended'
    CHANGED = 'changed'
    ACTIVE_SESSION_CHANGED = 'active_session_changed'
    DISABLED_BADGE_REMOVED_ALL_SESSIONS = 'disabled_badge_removed_all_sessions'

