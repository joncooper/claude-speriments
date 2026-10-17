# Source Generated with Decompyle++
# File: shared_content_member.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List, NamedTuple, Optional, Text

class AccessType:
    COMMENTER = 'viewer'
    EDITOR = 'editor'
    OWNER = 'owner'
    VIEWER_NO_COMMENT = 'viewer_no_comment'


class MemberType:
    group = 'group'
    me = 'me'
    user = 'user'
    invitee = 'invitee'


class MemberAction:
    make_owner = 'make_owner'
    make_editor = 'make_editor'
    make_viewer = 'make_viewer'
    make_viewer_no_comment = 'make_viewer_no_comment'
    leave_a_copy = 'leave_a_copy'
    remove_my_access = 'remove_my_access'
    remove = 'remove'

SharedContentMember = NamedTuple('SharedContentMember', [
    ('name', Optional[Text]),
    ('email', Optional[Text]),
    ('type', MemberType),
    ('same_team', bool),
    ('access_type', AccessType),
    ('inherited_access_type', AccessType),
    ('profile_photo_url', Optional[Text]),
    ('member_id', Text),
    ('member_actions', Optional[List[MemberAction]]),
    ('member_count', Optional[int]),
    ('initials', Optional[Text]),
    ('is_inherited', bool),
    ('time_last_seen', Optional[Text]),
    ('dbid', Optional[Text]),
    ('disabled', bool),
    ('group_management_type', Optional[Text])])
