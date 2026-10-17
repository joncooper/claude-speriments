# Source Generated with Decompyle++
# File: seen_state_vm.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, Dict, List, NamedTuple, Optional, Text
from dropbox.client.features.presence_and_seen_state.util import get_seen_state_string
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_0, async_queued_method_1
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.signals import StandardSignal
from dropbox.shared.local_path import LocalPath
from dropbox.sharing.constants.content import Content, ContentType
from dropbox.sharing.shared_content_members_fetcher import SharedContentMember, SharedContentMembersFetcher, sort_members
from dropbox.sharing.utils.content_util import get_api_id_from_server_path
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
SeenStateData = NamedTuple('SeenStateData', [
    ('time_last_seen', Optional[Text]),
    ('seen_state_string', Optional[Text])])
MAX_SEEN_STATE_USERNAME_LENGTH = 20

def get_shared_content_members_fetcher(context = None, local_path = None, sort_function = None):
    pass
# WARNING: Decompyle incomplete


def seen_state_string_function(shared_content_member = None):
    time_seen = shared_content_member.time_last_seen
    return get_seen_state_string(time_seen)


def user_seen_state_string_function(shared_content_member = None):
    time_seen = shared_content_member.time_last_seen
# WARNING: Decompyle incomplete


class SeenStateVM(Actor):
    pass
# WARNING: Decompyle incomplete

