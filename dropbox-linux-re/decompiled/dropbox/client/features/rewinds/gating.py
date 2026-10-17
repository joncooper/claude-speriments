# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
REWINDS_GANDALF_FEATURE = 'desktop-cash-feature-folder-rewind'
REWINDS_UPSELL_GANDALF_FEATURE = 'desktop-context-menu-rewind-upsell'

def is_rewind_context_menu_enabled(gandalf = None, account = None):
    if not account:
        return False
    if None.allows(REWINDS_GANDALF_FEATURE, account):
        return True
    if None.allows(REWINDS_UPSELL_GANDALF_FEATURE, account):
        return True

