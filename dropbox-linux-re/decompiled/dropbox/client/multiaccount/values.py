# Source Generated with Decompyle++
# File: values.pyc (Python 3.11)

from __future__ import absolute_import
from dropbox.client.multiaccount.constants import MAX_TEAM_NAME_LEN
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ui.common.strings import AccountString, UIStrings
from dropbox.exception.reporting import report_bad_assumption
from dropbox.i18n import trans
from dropbox.shared.util import undefined

class MultiaccountStrings(UIStrings):
    linking = AccountString('Linking <Personal> Dropbox...')
    unlinking = AccountString('Unlinking <Personal> Dropbox...')
    link = AccountString('Link <Personal> Dropbox...')
    location = AccountString('<Personal> Dropbox Location')
    sel_sync = AccountString('<Personal> Dropbox Selective Sync')
    dropbox = AccountString('<Personal> Dropbox')
    unlink = AccountString('Unlink <Personal> Dropbox...')
    screenshots = AccountString('Save screenshots to your <personal> Dropbox')
    type_colon = AccountString('<Personal>:')


class MultiaccountValue(object):
    
    def __init__(self, personal, business, primary, secondary):
        self.personal = personal
        self.business = business
        self.primary = primary
        self.secondary = secondary

    
    def get_by_role(self, role):
        return self.personal if role == Roles.PERSONAL else self.business



class MultiaccountValues(object):
    
    def multiaccount_value(self, personal, business, primary, secondary = (undefined, undefined, undefined, undefined)):
        account = self.app.account_manager.primary
        if account:
            secondary_role = Roles.BUSINESS if account.role == Roles.PERSONAL else Roles.PERSONAL
        if primary is not undefined and secondary is not undefined:
            if secondary_role == Roles.BUSINESS:
                business = secondary
                personal = primary
            elif secondary_role == Roles.PERSONAL:
                business = primary
                personal = secondary
            elif personal is not undefined and business is not undefined:
                if secondary_role == Roles.BUSINESS:
                    secondary = business
                    primary = personal
                elif secondary_role == Roles.PERSONAL:
                    secondary = personal
                    primary = business
        multiaccount_values = (personal, business, primary, secondary)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(multiaccount_values()):
            report_bad_assumption('Incomplete data passed in to multiaccount_value: %s', multiaccount_values)
            return None
    # WARNING: Decompyle incomplete

    
    def multiaccount_value_ex(self, string, max_len = (MAX_TEAM_NAME_LEN,)):
        team = ''
        if self.app.account_manager.primary:
            team = self.app.account_manager.primary.team
        return self.multiaccount_value(personal = string.personal, business = string.maybe_team(team, max_len = max_len))

    account_labels_plain = (lambda self: self.account_labels_with_options())()
    
    def account_labels_with_options(self, lower_plain_names, use_team = (False, True)):
