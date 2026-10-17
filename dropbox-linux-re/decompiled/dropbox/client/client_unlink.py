# Source Generated with Decompyle++
# File: client_unlink.pyc (Python 3.11)

from typing import TYPE_CHECKING
from dropbox.client.unlink_handlers import UnlinkReason
if TYPE_CHECKING:
    from dropbox.client.main import DropboxApplication

class ClientUnlink:
    
    def __init__(self = None, app = None):
        self.app = app

    
    def unlink(self = None):
        self.app.restart_and_unlink(prompt_relink = True, reason_code = UnlinkReason.USER_REQUESTED)


