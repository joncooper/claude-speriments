# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional
from dropbox.foundation.stormcrow.user import UserStormcrow
PERMISSIONS_AFTER_UPLOAD_STORMCROW = 'desktop-core-team-space-sharing-modal'

def permissions_after_upload_enabled(user_stormcrow = None):
    return user_stormcrow.allows(PERMISSIONS_AFTER_UPLOAD_STORMCROW)


def permissions_after_upload_variant(user_stormcrow = None):
    return user_stormcrow.get_variant(PERMISSIONS_AFTER_UPLOAD_STORMCROW)

