# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from build_number.features import feature_enabled
from dropbox.client.features.file_view_logging.gating import desktop_pass_view_logging_enabled
from dropbox.client.features.octave.gating import desktop_octave_enabled, desktop_octave_expanded
from dropbox.client.gandalf import Gandalf
from dropbox.foundation.stormcrow import MachineStormcrowInterface, NoStormcrowDataError
from dropbox.foundation.stormcrow.machine import MachineStormcrow
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.platform import IS_LINUX, IS_MAC
DESKTOP_HARMONY_STORMCROW = 'desktop-badge-test'
DESKTOP_HARMONY_TIPS_STORMCROW = 'desktop-harmony-tips'
DESKTOP_HARMONY_PASS_STORMCROW = 'desktop-harmony-pass'
DESKTOP_HARMONY_QT_AVATAR = 'desktop-harmony-qt-avatar'
DESKTOP_HARMONY_BADGE_USE_QWIDGET = 'desktop-harmony-badge-use-qwidget'
FEATURE_PRESENCE_REPORTING = 'desktop-presence-reporter'
FEATURE_DISABLE_EDITOR_TRACKING = 'desktop-harmony-disable-editor-tracking'

def desktop_harmony_is_supported():
    if IS_LINUX:
        return False


def desktop_harmony_is_allowed(stormcrow = None):
    if stormcrow.allows(DESKTOP_HARMONY_STORMCROW):
        pass
    return stormcrow.get_variant(DESKTOP_HARMONY_STORMCROW) == 'SHOW_BADGE'


def desktop_harmony_tips_is_allowed(stormcrow = None):
    return stormcrow.allows(DESKTOP_HARMONY_TIPS_STORMCROW)


def desktop_harmony_is_allowed_any_account(gandalf = None):
    pass
# WARNING: Decompyle incomplete


def desktop_harmony_polaris_enabled(stormcrow = None):
    return stormcrow.allows_any_account(DESKTOP_HARMONY_STORMCROW)


def desktop_harmony_octave_enabled(stormcrow = None):
    
    try:
        if not desktop_octave_enabled(stormcrow):
            return desktop_octave_expanded(stormcrow)
        except NoStormcrowDataError:
            return False



def desktop_harmony_polaris_file_view_logging_enabled(stormcrow = None):
