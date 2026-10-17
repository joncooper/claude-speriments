# Source Generated with Decompyle++
# File: account_api_base.pyc (Python 3.11)

from typing import Dict, Callable, Optional
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.meta_engine_api import MetaEngineBaseClass
from dropbox.client.fenix.meta_engine_apis.base import serialize_protobuf_response, wrap_typed_handler
from abc import abstractmethod
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.client.fenix.generated_types.account_pb2 import AccountEvent, AppdataPath, BusinessBasicEligibility, GetAccountForRoleReply, GetAccountForRoleReq, GetAccountLinkedOrFromCacheReply, GetAccountLinkedOrFromCacheReq, GetActiveAccountReply, GetAppdataPathReq, GetBusinessBasicEligibilityReq, GetHomeMountPathReq, GetLocallyLinkedAccountsAllReply, GetLocallyLinkedAccountsReply, GetPlanInfoReq, GetQuotaInfoForAccountReq, GetServerLinkedAccountsReply, GetServerLinkedAccountsReq, HasKnownAccountsLinkedFiredReply, HomeMountPath, InitializeMinimalAuthenticatedServicesReq, PlanInfo, QuotaInfo, RegisterLocallyAuthenticatedAccountReq, SetActiveAccountReq
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class _AccountBaseClass(MetaEngineBaseClass):
    pass
# WARNING: Decompyle incomplete

