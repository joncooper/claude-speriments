# Source Generated with Decompyle++
# File: disk_space_manager_factory.pyc (Python 3.11)

from _disk_space_manager_impl import DiskSpaceManagerImpl
from disk_space_manager import DebugDiskSpaceManager
from disk_space_sticky_factory import DiskSpaceStickyFactory
from notification_manager import BubbleManager, StickyManager
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.notification_adapter import UserNotificationControllerAdapter
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.url_info import DropboxURLInfo
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DiskSpaceManagerFactory(object):
    create = (lambda dropbox_app = None: pass# WARNING: Decompyle incomplete
)()

