# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from time import monotonic as _time
from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.configuration.wrapper import LocalConfigurationWrapper
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import IncompleteFutureException
from dropbox.foundation.raii2.singleton import Destroyable
from dropbox.model.types import FileId
from dropbox.preferences import OPT_NOTIFS_SYNC_ADD, OPT_NOTIFS_SYNC_EDIT_DELETE
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.remote_props import FolderPolicyStatus
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedForFile
from dropbox.trace import TRACE
SYNC_NOTIFICATION_AMP_NAMESPACE = 'desktop_sync_notification'
NUCLEUS_TIMEOUT = 3
DROPBOX_SERVER_USER_ID = 81554767

class SyncNotificationSettings(Destroyable):
    pass
# WARNING: Decompyle incomplete


def get_time():
    return _time()

