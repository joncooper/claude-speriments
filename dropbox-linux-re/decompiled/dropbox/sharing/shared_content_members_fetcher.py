# Source Generated with Decompyle++
# File: shared_content_members_fetcher.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import time
from collections import defaultdict
from functools import partial
from typing import Any, Callable, Dict, List, Optional, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_1, async_queued_method_3, async_queued_method_4
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.futures.future_collection import FutureCollection, SingleFutureCollection
from dropbox.foundation.signals import StandardSignal
from dropbox.shared.util import safe_navigate
from dropbox.sharing.constants.content import Content, ContentType
from dropbox.sharing.constants.network_response import NetworkResponse
from dropbox.sharing.constants.shared_content_member import AccessType, MemberAction, MemberType, SharedContentMember
from dropbox.sharing.sharing_logger import ShareDesktopTiburonEvent, SharingLogger
from dropbox.sharing.utils.date_util import convert_time_last_seen_to_seconds
from dropbox.sharing.utils.network_util import make_api_request, RequestError
ACTION_BY_ACCESS_TYPE = {
    AccessType.VIEWER_NO_COMMENT: MemberAction.make_viewer_no_comment,
    AccessType.COMMENTER: MemberAction.make_viewer,
    AccessType.EDITOR: MemberAction.make_editor,
    AccessType.OWNER: MemberAction.make_owner }
FOLDER_MEMBER_ACTION_WHITELIST = [
    MemberAction.make_editor,
    MemberAction.make_owner,
    MemberAction.make_viewer,
    MemberAction.make_viewer_no_comment,
    MemberAction.remove,
    MemberAction.leave_a_copy]
FILE_MEMBER_ACTION_WHITELIST = [
    MemberAction.make_editor,
    MemberAction.make_viewer,
    MemberAction.make_viewer_no_comment,
    MemberAction.remove,
    MemberAction.leave_a_copy]
GET_ACCOUNT_BATCH_LIMIT = 300
LIST_FOLDER_MEMBERS_LIMIT = 1000
LIST_FILE_MEMBERS_LIMIT = 100
MEMBER_ACTION_UI_PRIORITY = {
    'make_editor': 0,
    'make_viewer': 1,
    'make_viewer_no_comment': 2,
    'make_owner': 3,
    'remove': 4 }
DEFAULT_LOW_MEMBER_ACTION_UI_PRIORITY = 100

def get_initials_from_name(name = None):
    first_letters = name.split(' ')()
    return ''.join(first_letters[:2]).upper()


def get_member_sort_priority(member = None):
    if member.type == MemberType.group:
        return 0
    if None.type == MemberType.me:
        return 1
# WARNING: Decompyle incomplete


def get_member_actions(member_info_dict = None):
    actions = []
    permissions = member_info_dict.get('permissions')
# WARNING: Decompyle incomplete


def sort_members(members = None):
    return sorted(members, key = (lambda member: (get_member_sort_priority(member), convert_time_last_seen_to_seconds(member.time_last_seen) if member.time_last_seen else 0, member.name.lower() if member.name else '')))


def process_groups(group_membership_infos = None, is_unshared_folder = None):
    processed_members = []
# WARNING: Decompyle incomplete


def process_invitees(invitee_membership_infos = None, is_unshared_folder = None):
    processed_members = []
# WARNING: Decompyle incomplete


def is_invalid_file(request_error = None):
    if request_error.network_response:
        if request_error.network_response.data:
            pass
    return safe_navigate(request_error.network_response.data, 'error', 'access_error', '.tag') == 'invalid_file'


class SharedContentMembersFetcher(Actor):
    pass
# WARNING: Decompyle incomplete

