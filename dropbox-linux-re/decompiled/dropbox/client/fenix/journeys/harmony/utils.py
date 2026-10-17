# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import math
from typing import Optional
from dropbox.client.fenix.types.harmony import CoordinationInfo, DocumentSessionView, LastRevision, SharedContentMember, Viewer
from dropbox.client.fenix.user_cache import convert_cached_user_to_user_info
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.harmony.models.harmony_session_state import CoordinationInfo as CoordinationInfoOriginal, HarmonyMEVSessionState, LastRevisionSnapshot
from dropbox.harmony.models.harmony_user import HarmonyUser
from dropbox.harmony.models.types import DocumentSession
from dropbox.sharing.shared_content_members_fetcher import SharedContentMember as SharedContentMemberOriginal
from dropbox.sharing.utils.date_util import convert_time_last_seen_to_seconds

def get_coordination_info(coordination_info = None):
    pass
# WARNING: Decompyle incomplete


def get_harmony_user_to_viewer(user = None):
    return Viewer(name = user.first_name, is_editing = user.is_editing, last_edited = user.last_edited, last_opened = user.last_opened, user = convert_cached_user_to_user_info(user.user_info))


def get_shared_content_member(viewed_member = None):
    time_last_seen_ago = convert_time_last_seen_to_seconds(viewed_member.time_last_seen) if viewed_member.time_last_seen else 0
    return SharedContentMember(name = viewed_member.name if viewed_member.name else '', initials = viewed_member.initials if viewed_member.initials else '', time_last_seen_ago = time_last_seen_ago, account_id = viewed_member.dbid)


def get_last_revision_from_snapshot(lv_snapshot = None):
    pass
# WARNING: Decompyle incomplete


def get_harmony_document_session_view(document_session = None, state = None):
    pass
# WARNING: Decompyle incomplete

