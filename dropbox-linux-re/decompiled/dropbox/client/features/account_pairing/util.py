# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from typing import Any, Optional, Text
from uuid import uuid4 as _uuid4
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import EXPERIMENT_EVENT

def show_account_pairing(checkpoint_token, account_email, user_id, pair_origin = None, first_account = None, second_account = None, duplicate_role = ('checkpoint_token', 'Text', 'account_email', 'Text', 'user_id', 'Text', 'pair_origin', 'Text', 'first_account', 'AccountInterface', 'second_account', 'Optional[AccountInterface]', 'duplicate_role', 'Optional[Role]', 'return', 'None')):
    paired_account_email = None
    if second_account:
        paired_account_email = second_account.email
# WARNING: Decompyle incomplete


def report_account_pairing_event(event_name = None, account = None, **extra_dict):
    extra_dict = sanitize_event_extra_dict(extra_dict)
    report(EXPERIMENT_EVENT, account = account, event = event_name, extra = extra_dict)

