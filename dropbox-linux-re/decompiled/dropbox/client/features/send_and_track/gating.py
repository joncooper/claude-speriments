# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
OPEN_WITH_SEND_AND_TRACK_GATE = 'desktop-send-and-track-file-context-menu'

def is_open_with_send_and_track_enabled(gandalf = None, account = None):
    return gandalf.allows(OPEN_WITH_SEND_AND_TRACK_GATE, account)

