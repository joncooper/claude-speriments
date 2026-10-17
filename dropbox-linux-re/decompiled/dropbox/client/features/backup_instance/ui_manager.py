# Source Generated with Decompyle++
# File: ui_manager.pyc (Python 3.11)

from typing import Dict, Optional
from build_number import BUILD_KEY
from build_number.platform import IS_MAC
from dropbox.client.features.backup_instance.backup_instance_logging import BackupInstanceLogger
from dropbox.client.features.backup_instance.constants import BackupInstanceStrings, BI_ROOT_INVALID_HC_ARTICLE_URL
from dropbox.client.features.backup_instance.types import BackupInstanceActionSurface, BackupInstanceEvent
from dropbox.client.features.backup_instance.utils import BI_TRACE
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.notifications.legacy_notifications import BackupInstanceRootInvalidErrorStickyNotification
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.url_info import dropbox_url_info

class BackupInstanceUIManager(Actor):
    pass
# WARNING: Decompyle incomplete

