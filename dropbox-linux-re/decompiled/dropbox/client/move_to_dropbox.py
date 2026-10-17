# Source Generated with Decompyle++
# File: move_to_dropbox.pyc (Python 3.11)

import collections
import os
from typing import DefaultDict, Iterator, List, Optional, Text, Tuple
from build_number.features import feature_enabled
from dropbox import fsutil
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.icon_overlay import IconOverlayStrings
from dropbox.event import report
from dropbox.i18n import format_bytes
from dropbox.platform import IS_MAC
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, SIERRA
MYPY = False
if MYPY:
    from dropbox.client import main
DESKTOP_MOVE_TO_DROPBOX_SIERRA = 'desktop-move-to-dropbox-sierra'

def is_in_any_dropbox(app = None, pathlist = None, secondary_fallback = None):
