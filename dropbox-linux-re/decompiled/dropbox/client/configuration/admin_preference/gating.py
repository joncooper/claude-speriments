# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from __future__ import absolute_import
from dropbox.foundation.stormcrow import MachineStormcrowInterface
DESKTOP_SETTINGS_PROPAGATION_STORMCROW = 'desktop-settings-propagation'

def desktop_settings_propagation_stormcrow_enabled(stormcrow = None):
    return stormcrow.allows_any_account(DESKTOP_SETTINGS_PROPAGATION_STORMCROW)

