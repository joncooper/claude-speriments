# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
SHELL_OPEN_WITH_HELLOSIGN_GATE = 'desktop-shell-open-with-hellosign'
OPEN_WITH_SELF_SIGN_GATE = 'desktop-open-with-self-sign'

def is_shell_open_with_hellosign_enabled(gandalf = None, account = None):
    return gandalf.allows(SHELL_OPEN_WITH_HELLOSIGN_GATE, account)


def is_open_with_self_sign_enabled(gandalf = None, account = None):
    return gandalf.allows(OPEN_WITH_SELF_SIGN_GATE, account)

