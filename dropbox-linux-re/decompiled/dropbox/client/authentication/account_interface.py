# Source Generated with Decompyle++
# File: account_interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Set, Tuple
from typing_extensions import Protocol
from dropbox.client.authentication.types import AccountDataSource, AccountId
from dropbox.client.multiaccount.constants import MAX_TEAM_NAME_LEN, Role
from dropbox.model.types import FileId, NsId
from dropbox.proto.sync.root_pb2 import RootLayout
from dropbox.shared.quota_info import QuotaInfo

class AccountStringProtocol(Protocol):
    personal = (lambda self = None: pass)()
    business = (lambda self = None: pass)()
    with_name = (lambda self = None: pass)()
    single = (lambda self = None: pass)()
    
    def maybe_team(self = None, team_name_ = None, max_len = None, **kw):
        pass



class AccountInterface(ABC):
    client_uuid: 'str' = 'AccountInterface'
    most_recent_link_source = (lambda self = None: pass)()()
    performing_initial_link_flow = (lambda self = None: pass)()()
    finished_all_link_flows = (lambda self = None: pass)()()
    is_dfb_user = (lambda self = None: pass)()()
    is_admin = (lambda self = None: pass)()()
    is_reseller_user = (lambda self = None: pass)()()
    account_id = (lambda self = None: pass)()()
    paired_account_id = (lambda self = None: pass)()()
    folder_name = (lambda self = None: pass)()()
    home_mount_path = (lambda self = None: pass)()()
    has_tmf = (lambda self = None: pass)()()
    is_tmr_member = (lambda self = None: pass)()()
    is_paired = (lambda self = None: pass)()()
    account_labels_plain = (lambda self = None: pass)()()
    update_from_server_data = (lambda self = None, register_host_response = None: pass)()
    update_msl_indications_from_server_response = (lambda self = None, response = None: pass)()
    get_email = (lambda self = None: pass)()
    safe_team_name = (lambda self = None, max_len = None: pass)()
    render_string = (lambda self = None, string = None, max_len = abstractmethod, flip_role = (MAX_TEAM_NAME_LEN, False, False), assume_paired = ('string', 'AccountStringProtocol', 'max_len', 'int', 'flip_role', 'bool', 'assume_paired', 'bool', 'kw', 'Any', 'return', 'str'): pass)()
    update_team_name = (lambda self = None, team_name = None: pass)()
    __repr__ = (lambda self = None: pass)()

