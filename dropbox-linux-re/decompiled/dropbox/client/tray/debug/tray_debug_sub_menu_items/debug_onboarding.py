# Source Generated with Decompyle++
# File: debug_onboarding.pyc (Python 3.11)

from typing import Optional, Sequence
from build_number import BUILD_KEY
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.module import Fenix
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
from dropbox.components.desktop_components import DesktopComponent
_DEBUG_ACCOUNT_INFO = {
    'dropboxPath': '/hello/abc',
    'contentStartsOnlineOnly': False,
    'fileProviderEnabled': False,
    'canChangeInfinite': False,
    'syncSpaceUsed': 1073741824,
    'freeSpace': 0x80000000 }

def launch_welcome_flow(fenix = None, account = None, show_auth = None, content_mitigation = (False, 'LARGE_DROPBOX')):
    session_id = 'debug_' + random_session_id()
# WARNING: Decompyle incomplete


def get_onboarding_subitems(fenix = None, account_manager = None):
    pass
# WARNING: Decompyle incomplete

