# Source Generated with Decompyle++
# File: pro_event_reporting.pyc (Python 3.11)

from typing import Dict, Optional, Union
from typing_extensions import Literal
from mypy_extensions import TypedDict
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.tray.tray_metrics.tray_metrics_helpers import report_tray_metrics_from_pro_event
from dropbox.event import report
EXTRAS_DICT = TypedDict('EXTRAS_DICT', {
    'action': Literal[('view', 'click', 'close', 'form_submit')],
    'button_text': str,
    'destination_url': str,
    'location': Literal[('top', 'left_bar', 'right_bar', 'footer', 'in_desktop_tray', 'in_menu', 'overlay', 'in_product')],
    'quota_status': Literal[('under', 'near', 'over')],
    'upsell_type': Literal[('modal', 'button', 'banner', 'in_menu', 'loud_notification', 'redirect')],
    'trigger': str,
    'style': str,
    'refer_friend_hidden': str }, total = False)

def report_pro_event(event = None, account = None, user_agent = None, request_id = (None, None, None, None), extra = ('event', 'str', 'account', 'Optional[AccountInterface]', 'user_agent', 'Optional[str]', 'request_id', 'Optional[str]', 'extra', 'Optional[EXTRAS_DICT]', 'return', 'None')):
    
    def get_active_user_id(account):
        active_user_id = account.uid if account else None
        return active_user_id

    
    def get_authed_user_ids(account):
        active_user_ids = [
            account.uid] if account else None
        return active_user_ids

    active_user_id = get_active_user_id(account)
    authed_user_ids = get_authed_user_ids(account)
    event_dictionary_extra = extra
    event_dictionary = {
        'event_name': event,
        'user_agent': user_agent,
        'request_id': request_id,
        'identity_gid': None,
        'active_user_id': active_user_id,
        'authed_user_ids': authed_user_ids,
        'extra': event_dictionary_extra }
# WARNING: Decompyle incomplete

