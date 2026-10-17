# Source Generated with Decompyle++
# File: user_cache.pyc (Python 3.11)

from typing import Any, cast, Dict, List, Optional, Text, TypedDict
from build_number.features import feature_enabled
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.users import UserInfo as CachedUserInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2 import destroying
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
from dropbox.client.fenix.types.user_info import UserInfo

class FullAccountInfo(TypedDict):
    twofactor_info: 'Optional[Dict[str, Any]]' = 'FullAccountInfo'


def convert_raw_response_to_full_account_info(raw_response = None):
    pass
# WARNING: Decompyle incomplete


def convert_cached_user_to_user_info(cached_user_info = None):
    return UserInfo(account_id = cached_user_info.dbid, image_url = cached_user_info.image_url, first_name = cached_user_info.first_name, last_name = cached_user_info.last_name, initials = cached_user_info.initials, short_name = cached_user_info.short_name, display_name = cached_user_info.display_name, is_paired = cached_user_info.is_paired, is_account_primary = cached_user_info.is_account_primary, is_teammate = cached_user_info.is_teammate, is_email_verified = cached_user_info.is_email_verified, is_business_domain = cached_user_info.is_business_domain, shared_usage = cached_user_info.shared_usage)


class UserCacheService(Actor):
    pass
# WARNING: Decompyle incomplete

