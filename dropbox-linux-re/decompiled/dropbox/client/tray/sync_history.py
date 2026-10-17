# Source Generated with Decompyle++
# File: sync_history.pyc (Python 3.11)

from collections import OrderedDict
from itertools import chain
from time import time as _time
from typing import Any, cast, Dict, List, Optional, Sequence
from dropbox.client.features.home_feed.shared.model.sync_history_db import DBSyncEventType, Direction, FileEventType, SyncHistoryDB, SyncHistoryRecord
from dropbox.client.features.home_feed.shared.util.signals import ThrottledSignal
from dropbox.client.features.sync_everything.constants import CONFIG_KEY_SYNC_EVERYTHING_DEVICE_STATE
from dropbox.client.features.sync_everything.v3.config_utils import se_active_device_name
from dropbox.client.features.sync_everything.v3.fs_utils import is_in_active_backup
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.tray.sync_history_types import ItemSyncStatus, SyncQueueAccountRole, SyncQueueItem, SyncQueueItemType, SyncQueueUserAction, SyncType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FutureHelpers
from dropbox.foundation.paths.bridge_gen.types import LocalPath as BridgeLocalPath, RRServerPath as BridgeRRServerPath
from dropbox.model.types import FileId
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedForFile, SyncCompletedSummary
from dropbox.trace import TRACE
SYNCED_FILES_CAP = 50
RECENTLY_CHANGED_FILES_CAP = 30
SE_EVENT_TYPE_TO_SQI_USER_ACTION = {
    SyncEventType.MOVE: SyncQueueUserAction.MOVE,
    SyncEventType.DELETE: SyncQueueUserAction.DELETE,
    SyncEventType.EDIT: SyncQueueUserAction.EDIT,
    SyncEventType.ADD: SyncQueueUserAction.ADD }
SE_SYNC_DIRECTION_TO_SQI_SYNC_TYPE = {
    SyncDirection.DOWN: SyncType.DOWNLOAD,
    SyncDirection.UP: SyncType.UPLOAD }
SE_ROLE_TO_SQI_ROLE: 'Dict[Optional[Role], SyncQueueAccountRole]' = {
    Roles.PERSONAL: SyncQueueAccountRole.PERSONAL,
    Roles.BUSINESS: SyncQueueAccountRole.BUSINESS }
SQI_USER_ACTION_TO_DB_FILE_EVENT_TYPE = {
    SyncQueueUserAction.MOVE: FileEventType.MOVE,
    SyncQueueUserAction.DELETE: FileEventType.DELETE,
    SyncQueueUserAction.EDIT: FileEventType.EDIT,
    SyncQueueUserAction.ADD: FileEventType.ADD }
SQI_SYNC_TYPE_TO_DB_SYNC_DIRECTION = {
    SyncType.DOWNLOAD: Direction.DOWN,
    SyncType.UPLOAD: Direction.UP }
DB_FILE_EVENT_TYPE_TO_SQI_USER_ACTION = {
    FileEventType.MOVE: SyncQueueUserAction.MOVE,
    FileEventType.DELETE: SyncQueueUserAction.DELETE,
    FileEventType.EDIT: SyncQueueUserAction.EDIT,
    FileEventType.ADD: SyncQueueUserAction.ADD }
DB_SYNC_DIRECTION_TO_SQI_SYNC_TYPE = {
    Direction.DOWN: SyncType.DOWNLOAD,
    Direction.UP: SyncType.UPLOAD }
SYNC_HISTORY_UPDATE_THROTTLE_SECS = 1
SYNC_HISTORY_DB_UPDATE_THROTTLE_SECS = 60

class SyncHistoryModel(Actor, UserSingleton):
    pass
# WARNING: Decompyle incomplete

