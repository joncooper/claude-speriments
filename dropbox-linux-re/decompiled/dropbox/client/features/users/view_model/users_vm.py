# Source Generated with Decompyle++
# File: users_vm.pyc (Python 3.11)

from typing import Dict, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.contacts.polaris.contacts_db_updater import ContactsDBUpdater
from dropbox.client.contacts.polaris.contacts_query_interface import ContactsQueryInterface
from dropbox.client.contacts.polaris.types import Contact, ContactType
from dropbox.client.features.offline.model.watcher import OfflineWatcher
from dropbox.client.features.quota_usage.manager import QuotaUsageManager
from dropbox.client.features.users.bridge_gen.bridge_interface_users_vm import UsersVMBridgeInterface, UsersVMObservableMixin
from dropbox.client.features.users.bridge_gen.contact_info import ContactInfo
from dropbox.client.features.users.bridge_gen.full_team import FullTeam
from dropbox.client.features.users.bridge_gen.quota_info import QuotaInfo
from dropbox.client.features.users.bridge_gen.role import Role
from dropbox.client.features.users.bridge_gen.team_user_permissions import TeamUserPermissions
from dropbox.client.features.users.bridge_gen.user_info import UserInfo
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.multiaccount.role import Roles
from dropbox.client.users import UserCacheRefreshError, UserInfo as CachedUserInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.wrappers.replaceable import Replaceable
from dropbox.foundation.signals import SignalConnection
from dropbox.sqlite3_helpers import Cursor
from dropbox.trace import TRACE

class UsersVM(UsersVMBridgeInterface, Actor, UsersVMObservableMixin):
    pass
# WARNING: Decompyle incomplete


def convert_team(user_info = None, account = None):
    team = None
    if user_info.extra and account.team:
        encoded_team_id = user_info.extra.get('encoded_team_id')
        suggest_members_enabled = user_info.extra.get('suggest_members_enabled')
        if encoded_team_id and suggest_members_enabled:
            team = FullTeam(id = str(encoded_team_id), name = account.team, team_user_permissions = TeamUserPermissions(suggest_members_enabled = bool(suggest_members_enabled)))
    return team


def convert_user(user_info = None, account = None, *, plan, has_unlimited_space):
    role = None
# WARNING: Decompyle incomplete

