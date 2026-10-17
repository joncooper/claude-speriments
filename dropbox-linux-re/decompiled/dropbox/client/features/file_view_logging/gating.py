# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from __future__ import absolute_import
from dropbox.client.features.file_view_logging.constants import DESKTOP_PASS_VIEW_LOGGING_STORMCROW
from dropbox.foundation.stormcrow import MachineStormcrowInterface

def desktop_pass_view_logging_enabled(stormcrow = None):
    return stormcrow.allows_any_account(DESKTOP_PASS_VIEW_LOGGING_STORMCROW)

