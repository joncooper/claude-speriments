# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)

from enum import Enum
from typing import Any, cast, Iterable, Optional
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.multiaccount.role import Roles
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import NTS_EVENT
from dropbox.nts import cert_pinning_disabled, nts_team_id_preference

class NtsEventType(Enum):
    NTS_ACCOUNTS_LOADED_EVENT = 'accounts_loaded'


def report_nts_event(event_name = None, account = None, **extra_dict):
    pass
# WARNING: Decompyle incomplete


def report_nts_accounts_loaded_event(account_manager = None):
