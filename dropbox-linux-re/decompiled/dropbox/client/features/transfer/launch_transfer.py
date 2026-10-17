# Source Generated with Decompyle++
# File: launch_transfer.pyc (Python 3.11)

from typing import List, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.transfer.constants import FileTransferEntryPoint
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.components.desktop_components import DesktopComponent

def launch_file_transfer_mev(event_hub, session_id = None, source = None, account = None, pathlist = ('event_hub', 'EventHub', 'session_id', 'Text', 'source', 'FileTransferEntryPoint', 'account', 'AccountInterface', 'pathlist', 'List[Text]', 'return', 'None')):
    event_hub.launch_journey(UserJourneyNames.FILE_TRANSFER_FLOW, session_id, {
        'pathlist': pathlist,
        'account': convert_to_local_account(account) }).ground(component = DesktopComponent.FILE_VIEWER)

