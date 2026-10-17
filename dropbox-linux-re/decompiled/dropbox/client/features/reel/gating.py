# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
DESKTOP_ADD_TO_REPLAY_GATE = 'desktop-add-to-replay-gate'
DESKTOP_REPLAY_2_0_GATE = 'desktop-core-media-intel-2026-01-20-media-hub-enabled'

def add_to_replay_from_desktop_enabled(gandalf = None, account = None):
    return gandalf.allows(DESKTOP_ADD_TO_REPLAY_GATE, account)


def is_review_in_replay_context_menu_enabled(gandalf = None, account = None):
    return gandalf.allows(DESKTOP_REPLAY_2_0_GATE, account)

