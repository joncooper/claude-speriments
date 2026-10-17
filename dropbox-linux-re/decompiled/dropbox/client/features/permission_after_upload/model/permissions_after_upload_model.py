# Source Generated with Decompyle++
# File: permissions_after_upload_model.pyc (Python 3.11)

import os
import time
import unicodedata
from typing import Optional, Text
from six.moves.urllib import parse as urlparse
from dropbox.api.v2.datatypes.megaphone_bluenote import NotificationRequest
from dropbox.client.features.permission_after_upload.gating import permissions_after_upload_variant
from dropbox.client_api.apiv2.generated.megaphone_bluenote import MegaphoneBluenote
from dropbox.client_api.connection.exceptions import APIv2EndpointError
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FutureHelpers
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.trace import TRACE
BLUENOTE_AFTER_SYNC_SET_PERMISSIONS = 20004690

class PermissionsAfterUploadModel(SingletonActor):
    pass
# WARNING: Decompyle incomplete

