# Source Generated with Decompyle++
# File: users.pyc (Python 3.11)

from typing import Any, Callable, Dict, List, NamedTuple, Optional, Text, Tuple, TypeVar
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client_api.exceptions import HTTP409Error, HTTP429Error, TransientNetworkError
from dropbox.foundation.futures import Future
from dropbox.foundation.transitional.connection_pool import make_delayed_network_call
from dropbox.functions import lrudict
from dropbox.harmony.utility.threading import UserCacheThread
from dropbox.model.types import FileId
from dropbox.shared.util import safe_navigate
from dropbox.threading import Lock
from dropbox.trace import TRACE

class UserInfo(NamedTuple):
    display_name: 'Text' = 'UserInfo'
    is_paired: 'Optional[bool]' = None
    is_account_primary: 'Optional[bool]' = None
    is_teammate: 'Optional[bool]' = None
    is_email_verified: 'Optional[bool]' = None
    is_business_domain: 'Optional[bool]' = None
    shared_usage: 'Optional[int]' = None
    extra: 'Optional[Dict[Text, Any]]' = None
    raw_response: 'Optional[Dict[Text, Any]]' = None

_OptUserInfo = TypeVar('_OptUserInfo', UserInfo, Optional[UserInfo])

class UserCacheRefreshError(Exception):
    pass


class UserCache(object):
    CACHE_SIZE = 1024
    
    def __init__(self = None, conn = None, account_manager = None):
        self._lock = Lock()
        self._conn = conn
        self._account_manager = account_manager
        self._cache = lrudict(cache_size = self.CACHE_SIZE)
        self._dbid_by_uid = lrudict(cache_size = self.CACHE_SIZE)
        self._full_account_user_info_cache = lrudict(cache_size = self.CACHE_SIZE)
        self._init_user_cache_thread()

    
    def _init_user_cache_thread(self = None):
        UserCacheThread().start()

    
    def __getitem__(self = None, uid = None):
        self._lock
        dbid = self._dbid_by_uid[uid]
    # WARNING: Decompyle incomplete

    
    def _locked_get_uid(self = None, uid = None, default = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get(self = None, uid = None, default = None):
        self._lock
        (_, user) = self._locked_get_uid(uid, default = default)
        None(None, None)
        return 
        with None:
            if not None, user:
                pass

    
    def get_dbid(self = None, dbid = None, default = None):
        self._lock
        None(None, None)
        return 
        with None:
            if not None, self._cache.get(dbid, default = default):
                pass

    get_dbid_remote = (lambda self = None, dbid = None, account = UserCacheThread.on_queue_nonblocking: result = self._get_dbid_remote_batch([
dbid], account)result[dbid])()
    
    def get_dbid_remote_future(self = None, dbid = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    get_account_remote = (lambda self = None, account = None: self._get_account_remote(account))()
    get_file_modifier_remote = (lambda self = None, account = None, uid = UserCacheThread.on_queue_nonblocking, fileid = ('account', 'AccountInterface', 'uid', 'int', 'fileid', 'FileId', 'return', 'Optional[UserInfo]'): self._get_file_modifier_remote(account, uid, fileid))()
    get_file_modifier_remote_with_callback = (lambda self, account = None, uid = None, fileid = UserCacheThread.on_queue_returns_none(), callback = ('account', 'AccountInterface', 'uid', 'int', 'fileid', 'FileId', 'callback', 'Callable[[Optional[UserInfo]], Any]', 'return', 'None'): try:
result = self._get_file_modifier_remote(account, uid, fileid)callback(result)Noneexcept (TransientNetworkError, UserCacheRefreshError):
e = NoneTRACE('Ignoring exception `%r` in get_file_modifier_remote_with_callback', e)callback(None)e = Nonedel eNonee = Nonedel e)()
    get_dbid_remote_batch = (lambda self = None, dbid_list = None, account = UserCacheThread.on_queue_nonblocking: self._get_dbid_remote_batch(dbid_list, account))()
    
    def _get_dbid_remote_batch(self = None, dbid_list = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_account_remote(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_full_account_response(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_file_modifier_remote(self = None, account = None, uid = None, fileid = ('account', 'AccountInterface', 'uid', 'int', 'fileid', 'FileId', 'return', 'Optional[UserInfo]')):
        self._lock
        (cache_hit, user) = self._locked_get_uid(uid, default = None)
        None(None, None)

    
    def _do_api_v2_get_account_batch(self = None, dbids = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _do_get_current_account(self = None, account = None):
        TRACE('Making get_current_account request to metaserver for: uid=%s', account.uid)
    # WARNING: Decompyle incomplete

    
    def _do_get_file_modifier(self = None, account = None, uid = None, fileid = ('account', 'AccountInterface', 'uid', 'int', 'fileid', 'FileId', 'return', 'Optional[UserInfo]')):
        TRACE('Making get_file_modifier_account request to metaserver for: uid=%s, fileid=%s', uid, fileid)
    # WARNING: Decompyle incomplete

    
    def _locked_insert_valid_user_by_dbid(self = None, user_info = None, uid = None):
        dbid = user_info['account_id']
        display_name = user_info['name']['display_name']
        first_name = user_info['name']['given_name']
        last_name = user_info['name']['surname']
        initials = user_info['name']['abbreviated_name']
        is_paired = user_info.get('is_paired', None)
        is_account_primary = user_info.get('is_account_primary', None)
        is_teammate = user_info.get('is_teammate', None)
        is_email_verified = user_info.get('email_verified', None)
        suggest_members_enabled = safe_navigate(user_info, 'team', 'team_user_permissions', 'suggest_members_enabled')
        encoded_team_id = safe_navigate(user_info, 'team', 'id')
        is_business_domain = user_info.get('is_business_domain', None)
        shared_usage = safe_navigate(user_info, 'quota_info', 'shared')
        extra = { }
        if encoded_team_id and suggest_members_enabled:
            extra['encoded_team_id'] = encoded_team_id
            extra['suggest_members_enabled'] = suggest_members_enabled
        if last_name:
            short_name = f'''{first_name!s} {last_name[0]!s}.'''
        else:
            short_name = first_name
    # WARNING: Decompyle incomplete

    
    def _locked_insert_negative_uid_lookup(self = None, uid = None):
        self._dbid_by_uid[uid] = None


