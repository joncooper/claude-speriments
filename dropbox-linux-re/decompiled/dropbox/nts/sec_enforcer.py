# Source Generated with Decompyle++
# File: sec_enforcer.pyc (Python 3.11)

from typing import Callable
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.nts import cert_pinning_disabled
from dropbox.nts.notifications import show_cert_pinning_disabled_bubble, show_cert_pinning_enabled_bubble, show_security_logout_bubble
from dropbox.trace import TRACE
NTS_NOTIFICATION_SHOWN = 'nts-notification-shown'
NTS_ACKNOWLEDGED_AT_LINK = 'nts-acknowledged-at-link'

def check_cert_pinning_and_unlink_account_if_needed(account = None, local_config = None, ui_kit = None, unlink_handler = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'ui_kit', 'BaseUIKit', 'unlink_handler', 'Callable[[UnlinkReason], None]', 'return', 'None')):
    TRACE('NTS: Checking cert pinning state for account %r', account)
    if not cert_pinning_disabled():
        TRACE('NTS: Cert pinning is enabled')
        show_link_nts_bubble_if_needed(account, local_config, ui_kit)
        return None
    if None.is_fresh_link:
        TRACE('NTS: Not trying to unlink account because it was freshly linked, setting acknowledgement flag')
        local_config.config_dict[NTS_ACKNOWLEDGED_AT_LINK] = True
        show_link_nts_bubble_if_needed(account, local_config, ui_kit)
        return None
    if None.config_dict.get(NTS_ACKNOWLEDGED_AT_LINK, False):
        TRACE('NTS: Account was linked when cert pinning was already disabled, keeping account logged in')
        return None
    TRACE('NTS: Unlinking account because cert pinning was just disabled')
    local_config.config_dict[NTS_ACKNOWLEDGED_AT_LINK] = False
    show_security_logout_bubble(ui_kit)
    unlink_handler(UnlinkReason.CERT_PINNING_DISABLED)


def show_link_nts_bubble_if_needed(account = None, local_config = None, ui_kit = None):
    notif_shown = local_config.config_dict.get(NTS_NOTIFICATION_SHOWN, False)
    if not cert_pinning_disabled() and notif_shown:
        TRACE('NTS: Showing cert pinning disabled bubble')
        show_cert_pinning_disabled_bubble(ui_kit)
        local_config.config_dict[NTS_NOTIFICATION_SHOWN] = True
    if cert_pinning_disabled() or notif_shown:
        TRACE('NTS: Showing cert pinning re-enabled bubble')
        show_cert_pinning_enabled_bubble(ui_kit)
        local_config.config_dict[NTS_NOTIFICATION_SHOWN] = False
        return None
    return None

