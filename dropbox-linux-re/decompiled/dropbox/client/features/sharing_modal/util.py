# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import uuid
from typing import List, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.event_hub import EventHub, UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.components.desktop_components import DesktopComponent

def launch_share_modal(event_hub = None, account = None, file_id = None, share_modal_initial_screen = (None, None), prefill_emails = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'file_id', 'str', 'share_modal_initial_screen', 'Optional[str]', 'prefill_emails', 'Optional[List[str]]', 'return', 'None')):
    event_hub.launch_journey(UserJourneyNames.EDISON_SHARING_FLOW, str(uuid.uuid4()), {
        'account': convert_to_local_account(account),
        'file_id': file_id,
        'share_modal_initial_screen': share_modal_initial_screen,
        'prefill_emails': prefill_emails }).ground(component = DesktopComponent.SHARING)

