# Source Generated with Decompyle++
# File: account.pyc (Python 3.11)

import os
import uuid
from typing import Any, Dict, Optional, Set, Tuple
from build_number.features import feature_enabled
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface, AccountStringProtocol
from dropbox.client.authentication.types import AccountDataSource, AccountId
from dropbox.client.multiaccount.constants import MAX_TEAM_NAME_LEN, Role
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import sanitize_filename
from dropbox.functions import snippet
from dropbox.i18n import trans
from dropbox.model.types import FileId, NsId
from dropbox.proto.sync.root_pb2 import RootLayout
from dropbox.repr_utils import easy_repr
from dropbox.shared.quota_info import QuotaInfo
from dropbox.shared.util import parse_quota_info_from_list
from dropbox.trace import TRACE
LINK_ORIGIN_MANUAL_ADD_ACCOUNT = 'manual_add_account'

class Account(AccountInterface):
    
    def __init__(self = None):
        self.host_int = None
        self.host_secret = None
        self.paired_host_secret = None
        self.ui_flags = { }
        self._account_id = None
        self.uid = None
        self._paired_account_id = None
        self.paired_uid = None
        self.link_origin = None
        self.root_ns_id = None
        self.root_ns_fileid = None
        self.home_ns_id = None
        self.home_ns_fileid = None
        self.home_ns_path = None
        self.root_layout = RootLayout.UNKNOWN_ROOT
        self.email = None
        self.email_verified = False
        self.role = None
        self.subscription_type = None
        self.is_msl_team = False
        self.is_user_msl_on = False
        self.is_primary = False
        self.quota_info = None
        self.sync_space_used = 0
        self.root_mount_path = None
        self.user_display_name = None
        self.user_first_name = None
        self.host_display_name = None
        self.preauth = (None, False)
        self.team = None
        self.team_id = None
        self.linked = False
        self.is_fresh_link = False
        self.post_list_init_done = False
        self.disable_multiaccount_link = False
        self.handle_register_time = None
        self.link_sources = set()
        self.client_uuid = str(uuid.uuid4())

    most_recent_link_source = (lambda self = None: if AccountDataSource.SERVER in self.link_sources:
AccountDataSource.SERVERif None.DISK in self.link_sources:
AccountDataSource.DISK)()
    performing_initial_link_flow = (lambda self = None: not (self.link_sources))()
    finished_all_link_flows = (lambda self = None: AccountDataSource.SERVER in self.link_sources)()
    is_dfb_user = (lambda self = None: 