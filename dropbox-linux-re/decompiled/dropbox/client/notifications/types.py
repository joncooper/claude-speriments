# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import List, NewType, Optional
NotificationTok = NewType('NotificationTok', str)

class NotificationType(Enum):
    OTHER = 0
    COMMENT = 1
    MENTION = 2
    SHARE = 3
    TASK_ASSIGNED = 4
    TASK_COMPLETED = 5
    REQUEST_UNLOCK = 6


class NotificationImageType(Enum):
    SYSTEM = 0
    AVATAR = 1
    THUMBNAIL = 2

NotificationAvatarIcon = <NODE:12>()
NotificationSystemIcon = <NODE:12>()
NotificationRemoteIcon = <NODE:12>()
NotificationIcon = <NODE:12>()
NotificationAction = <NODE:12>()
NotificationTask = <NODE:12>()

class UserNotificationStatus(IntEnum):
    UNREAD = 0
    READ = 1
    INVISIBLE = 2


class UserNotificationSeenState(IntEnum):
    UNDEFINED = 0
    UNSEEN = 1
    SEEN = 2

NotificationActor = <NODE:12>()
NotificationRawType = <NODE:12>()
NotificationSourceObject = <NODE:12>()
NotificationThumbnail = <NODE:12>()
NotificationInfo = <NODE:12>()
StickyNotificationInfo = <NODE:12>()
