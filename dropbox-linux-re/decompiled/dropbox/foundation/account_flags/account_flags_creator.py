# Source Generated with Decompyle++
# File: account_flags_creator.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.foundation.account_flags.bridge_gen.account_flags import AccountFlags

def create_account_flags(account = None):
    can_comment_on_files = not account.ui_flags.get('team_commenting_disabled', False)
    is_team_admin = account.ui_flags.get('is_team_admin', False)
    return AccountFlags(can_comment_on_files = can_comment_on_files, is_team_admin = is_team_admin)

