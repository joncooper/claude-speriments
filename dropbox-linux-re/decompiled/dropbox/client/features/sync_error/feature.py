# Source Generated with Decompyle++
# File: feature.pyc (Python 3.11)

from typing import Optional
from build_number.features import feature_enabled
from dropbox.client.gandalf import Gandalf
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.platform import IS_LINUX
SYNC_ERRORS_FEATURE_NAME = 'desktop-sync-errors'
SYNC_ERRORS_FEATURE_STORMCROW = 'desktop-sync-errors-enabled'
BI_SYNC_ERRORS_FEATURE_STORMCROW = 'desktop-backup-instance-sync-errors-enabled'

class SyncErrorsFeature:
    enabled = (lambda context = None: if feature_enabled(SYNC_ERRORS_FEATURE_NAME):
passcontext.stormcrow.allows(SYNC_ERRORS_FEATURE_STORMCROW))()
    should_display_menu_item = (lambda gandalf = None: 