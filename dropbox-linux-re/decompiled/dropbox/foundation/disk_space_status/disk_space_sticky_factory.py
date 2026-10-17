# Source Generated with Decompyle++
# File: disk_space_sticky_factory.pyc (Python 3.11)

from typing import Callable, Optional, Text
from disk_space_state import DiskSpaceState, DiskSpaceStateMachineState
from disk_space_threshold import DiskSpaceThreshold
from disk_space_variant import DiskSpaceVariant, FullDiskSpaceVariant, LowDiskSpaceVariant, ManageSpaceVariant
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.notifications.legacy_notifications import HardDriveFullSelsyncV2StickyNotification, HardDriveFullStickyNotification, HardDriveFullV2StickyNotification, HardDriveLowSelsyncV2StickyNotification, HardDriveLowV2StickyNotification, HardDriveV2StickyNotificationBase, ManageSpaceHardDriveFullStickyNotification, ManageSpaceHardDriveLowStickyNotification, StickyNotification
from dropbox.client.notifications.strings import UserNotificationStrings
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DiskSpaceStickyFactory(object):
    ALL_STICKY_KEYS = [
        HardDriveFullV2StickyNotification.STICKY_KEY,
        HardDriveFullSelsyncV2StickyNotification.STICKY_KEY,
        HardDriveLowV2StickyNotification.STICKY_KEY,
        HardDriveLowSelsyncV2StickyNotification.STICKY_KEY,
        HardDriveFullStickyNotification.STICKY_KEY,
        ManageSpaceHardDriveLowStickyNotification.STICKY_KEY,
        ManageSpaceHardDriveFullStickyNotification.STICKY_KEY]
    V2_TYPE_MAPPINGS = {
        DiskSpaceState.FULL: HardDriveFullV2StickyNotification,
        DiskSpaceState.LOW: HardDriveLowV2StickyNotification }
    SELSYNC_V2_TYPE_MAPPINGS = {
        DiskSpaceState.FULL: HardDriveFullSelsyncV2StickyNotification,
        DiskSpaceState.LOW: HardDriveLowSelsyncV2StickyNotification }
    V2_TITLE_MAPPINGS = {
        DiskSpaceState.FULL: (lambda : UserNotificationStrings.hard_drive_v2_full_bubble_title),
        DiskSpaceState.LOW: (lambda : UserNotificationStrings.hard_drive_v2_low_bubble_title) }
    V2_MESSAGE_MAPPINGS = {
        DiskSpaceState.FULL: (lambda : UserNotificationStrings.hard_drive_v2_full_message),
        DiskSpaceState.LOW: (lambda : UserNotificationStrings.hard_drive_v2_low_message) }
    
    def __init__(self = None, dropbox_app = None):
        self._dropbox_app = dropbox_app

    
    def create_sticky(self, account, state, disk_space_variant, threshold = None, on_dismiss = None, on_action = None, on_open_help_center = ('account', 'AccountInterface', 'state', 'DiskSpaceStateMachineState', 'disk_space_variant', 'DiskSpaceVariant', 'threshold', 'DiskSpaceThreshold', 'on_dismiss', 'Callable[[], None]', 'on_action', 'Callable[[], None]', 'on_open_help_center', 'Callable[[], None]', 'return', 'Optional[StickyNotification]')):
        pass
    # WARNING: Decompyle incomplete


