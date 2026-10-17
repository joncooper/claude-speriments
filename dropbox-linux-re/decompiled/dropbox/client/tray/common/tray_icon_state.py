# Source Generated with Decompyle++
# File: tray_icon_state.pyc (Python 3.11)

from enum import IntEnum
from typing import NamedTuple, Optional, Tuple
from dropbox.client.status.label import StatusLabel

class TrayIconStatus(IntEnum):
    IDLE = 0
    BUSY = 1
    CONNECTING = 2
    BROKEN = 3
    CAM = 4
    PAUSED = 5
    RESUME = 6
    NEEDS_ATTENTION = 7
    QUITTING = 8


def get_icon_for_label(label = None):
    if label == StatusLabel.LABEL_IMPORTING:
        return TrayIconStatus.CAM
    if None in (StatusLabel.LABEL_LOW_DISK_SPACE, StatusLabel.LABEL_CANT_WATCH, StatusLabel.LABEL_CANT_UNMOUNT_NAMESPACE, StatusLabel.LABEL_CANT_MOUNT, StatusLabel.LABEL_NO_ROOT_PERMISSION):
        return TrayIconStatus.BROKEN
    if None == StatusLabel.LABEL_PAUSED:
        return TrayIconStatus.PAUSED
    if None in (StatusLabel.LABEL_CONNECTING, StatusLabel.LABEL_PRELINK):
        return TrayIconStatus.CONNECTING
    if None == StatusLabel.LABEL_BLANK:
        return TrayIconStatus.IDLE
    return None.BUSY


class TrayIconState(NamedTuple):
    label: 'Optional[str]' = 'TrayIconState'
    default = (lambda : DEFAULT_ICON_STATE)()

DEFAULT_ICON_STATE = TrayIconState(status = TrayIconStatus.IDLE, tooltip = None, badge_count = 0, snoozed = False, label = StatusLabel.LABEL_BLANK.value)
