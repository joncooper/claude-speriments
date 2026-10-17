# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from enum import Enum
from dropbox.enum_utils import auto, AutoNameEnum

class LoudNotificationActivationType(AutoNameEnum):
    BUTTON_ACTION = auto()
    SURFACE_ACTION = auto()
    BUTTON_DISMISS = auto()
    REPLY_ACTION = auto()


class ToastDismissedReason(Enum):
    UserCanceled = 0
    ApplicationHidden = 1
    TimedOut = 2

