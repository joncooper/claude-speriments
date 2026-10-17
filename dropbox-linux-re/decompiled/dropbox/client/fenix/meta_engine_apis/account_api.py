# Source Generated with Decompyle++
# File: account_api.pyc (Python 3.11)

import json
from typing import List, Optional
from build_number.features import feature_enabled
from dropbox.api.v2.datatypes.users import GetLinkedUsersRequest, GetLinkedUsersResult
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountDataSource
from dropbox.client.fenix.account_cache import FenixAccountCache
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.account_pb2 import AccountEvent, AccountOrId, AppdataPath, BusinessBasicEligibility, GetAccountForRoleReply, GetAccountForRoleReq, GetAccountLinkedOrFromCacheReply, GetAccountLinkedOrFromCacheReq, GetActiveAccountReply, GetAppdataPathReq, GetBusinessBasicEligibilityReq, GetHomeMountPathReq, GetLocallyLinkedAccountsAllReply, GetLocallyLinkedAccountsReply, GetPlanInfoReq, GetQuotaInfoForAccountReq, GetServerLinkedAccountsReply, GetServerLinkedAccountsReq, HasKnownAccountsLinkedFiredReply, HomeMountPath, InitializeMinimalAuthenticatedServicesReq, KnownAccountsLinkedEvent, LocalAccountChangeEvent, LocalAccountChangeType, LocalAccountPairedEvent, PlanInfo, QuotaInfo, RegisterLocallyAuthenticatedAccountReq, ServerAccount as ProtoServerAccount, SetActiveAccountReq, TrayActiveAccountChangedEvent
from dropbox.client.fenix.generated_types.shared_pb2 import AccountRole
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.account_api_base import _AccountBaseClass
from dropbox.client.fenix.meta_engine_apis.meta_engine_utils import account_to_proto, proto_to_authenticated_account_dict
from dropbox.client.multiaccount.role import Roles
from dropbox.client.setup_wizard.account_link_state import LinkPreferences
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client_api.apiv2.generated.users import Users
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import assert_not_none
from dropbox.foundation.account_manager import AccountManager, AccountUpdate
from dropbox.foundation.account_manager.bridge_gen.account_update_type import AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FutureHelpers
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.selsync import FileIdSet
from dropbox.sync_root.types import SyncRootType, SyncRootTypeReason
from dropbox.trace import TRACE
GLOBAL_ACCOUNT_ID = ''
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def _lookup_account_from_cache_or_manager(account_or_id_req = None, account_manager = None, legacy_account_manager = None):
    account_or_id = account_or_id_req.account_or_id
    typed_account_id = None
    if account_or_id.HasField('account_id'):
        typed_account_id = account_or_id.account_id
    elif account_or_id.HasField('account'):
        typed_account_id = account_or_id.account.account_id
# WARNING: Decompyle incomplete


def _parse_sync_root_type(value = None):
    for member in SyncRootType:
        if member.value == value:
            
            return None, member
        return SyncRootType.MOUNTED


def _parse_sync_root_type_reason(value = None):
    for member in SyncRootTypeReason:
        if member.value == value:
            
            return None, member
        return SyncRootTypeReason.UNKNOWN


class AccountAPI(_AccountBaseClass):
    pass
# WARNING: Decompyle incomplete

