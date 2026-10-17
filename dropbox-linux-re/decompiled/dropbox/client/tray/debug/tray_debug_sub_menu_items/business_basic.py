# Source Generated with Decompyle++
# File: business_basic.pyc (Python 3.11)

import functools
import uuid
from typing import Sequence, TYPE_CHECKING
from dropbox.client.authentication.account import Account
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
from dropbox.components.desktop_components import DesktopComponent
if TYPE_CHECKING:
    from dropbox.client.main import DropboxApplication
_PLAN_USAGE_URL = 'account/plan'
_UPGRADE_URL = 'plans'

def launch_business_basic_sharing_onboarding(app = None, account = None):
    pass
# WARNING: Decompyle incomplete


def launch_business_basic_sharing_onboarding_for_active_account(app = None):
    pass
# WARNING: Decompyle incomplete


def get_business_basic_subitems(app = None):
    return [
        MenuItem('Sharing onboarding', functools.partial(launch_business_basic_sharing_onboarding_for_active_account, app))]

