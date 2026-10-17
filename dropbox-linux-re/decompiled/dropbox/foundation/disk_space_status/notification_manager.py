# Source Generated with Decompyle++
# File: notification_manager.pyc (Python 3.11)

import uuid
from typing import Callable, Optional, Text
from disk_space_state import DiskSpaceState, DiskSpaceStateMachineState, LocalFolderSelsyncState
from disk_space_sticky_factory import DiskSpaceStickyFactory
from disk_space_threshold import DiskSpaceThreshold
from disk_space_variant import DiskSpaceVariant, FullDiskSpaceVariant, LowDiskSpaceVariant, ManageSpaceVariant
from logging import DiskSpaceLogger, DiskSpaceLoggerEvent
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.features.sync_and_storage.constants import SyncAndStorageEntryPoint
from dropbox.client.features.sync_and_storage.utils import launch_sync_and_storage_view
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.notifications.notification_adapter import UserNotificationControllerAdapter
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.ui.common.uikit import BaseUIKit, on_ui_thread_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.i18n import trans
from dropbox.url_info import DropboxURLInfo

class BubbleManager(object):
    _STATE_TO_BUBBLE_TYPE = {
        DiskSpaceState.FULL: LoudNotificationType.FULL_DISK_SPACE,
        DiskSpaceState.LOW: LoudNotificationType.LOW_DISK_SPACE }
    _SELSYNCABLE_STATE_TO_BUBBLE_SELSYNC_TYPE = {
        DiskSpaceState.FULL: LoudNotificationType.FULL_DISK_SPACE_SELSYNC,
        DiskSpaceState.LOW: LoudNotificationType.LOW_DISK_SPACE_SELSYNC }
    
    def __init__(self = None, ui_kit = None, bubble_context = None, url_info = ('ui_kit', 'BaseUIKit', 'bubble_context', 'BubbleContext', 'url_info', 'DropboxURLInfo', 'return', 'None')):
        self._ui_kit = ui_kit
        self._bubble_context = bubble_context
        self._url_info = url_info

    
    def remove_bubble(self = None, state = None, selsync_state = None):
        state_to_bubble_type = BubbleManager._SELSYNCABLE_STATE_TO_BUBBLE_SELSYNC_TYPE if selsync_state == LocalFolderSelsyncState.ABLE_TO_FREE else BubbleManager._STATE_TO_BUBBLE_TYPE
        if state not in state_to_bubble_type:
            return None
        bubble_type = None[state]
        on_ui_thread_future(self._ui_kit.hide_bubble)(LoudNotification.compute_id(bubble_type, '')).ground(component = DesktopComponent.SYNC_ERRORS)

    
    def show_bubble(self, state = None, variant = None, threshold = None, logger = ('state', 'DiskSpaceStateMachineState', 'variant', 'DiskSpaceVariant', 'threshold', 'DiskSpaceThreshold', 'logger', 'DiskSpaceLogger', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



class StickyManager(object):
    
    def __init__(self, get_account_manager = None, notification_controller = None, sticky_factory = None, url_info = ('get_account_manager', 'Callable[[], Optional[AccountManagerInterface]]', 'notification_controller', 'UserNotificationControllerAdapter', 'sticky_factory', 'DiskSpaceStickyFactory', 'url_info', 'DropboxURLInfo', 'return', 'None')):
        self._get_account_manager = get_account_manager
        self._notification_controller = notification_controller
        self._sticky_factory = sticky_factory
        self._url_info = url_info

    
    def remove_sticky_if_exist(self = None):
        account_manager = self._get_account_manager()
    # WARNING: Decompyle incomplete

    
    def add_sticky(self, state, variant = None, threshold = None, logger = None, on_dismiss = ('state', 'DiskSpaceStateMachineState', 'variant', 'DiskSpaceVariant', 'threshold', 'DiskSpaceThreshold', 'logger', 'DiskSpaceLogger', 'on_dismiss', 'Callable[[], None]', 'return', 'bool')):
        account_manager = self._get_account_manager()
    # WARNING: Decompyle incomplete

    _remove_sticky_helper = (lambda self = None, account = None: for sticky_key in DiskSpaceStickyFactory.ALL_STICKY_KEYS:
if self._notification_controller.has_sticky(account, sticky_key):
self._notification_controller.remove_sticky(account, sticky_key)None)()
    _add_sticky_helper = (lambda self, account, state, variant = None, threshold = None, logger = on_ui_thread_future, on_dismiss = ('account', 'AccountInterface', 'state', 'DiskSpaceStateMachineState', 'variant', 'DiskSpaceVariant', 'threshold', 'DiskSpaceThreshold', 'logger', 'DiskSpaceLogger', 'on_dismiss', 'Callable[[], None]', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()

