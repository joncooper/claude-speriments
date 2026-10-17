# Source Generated with Decompyle++
# File: flush_low_disk_notif.pyc (Python 3.11)

from six import iteritems
from dropbox.infinite.constants import InfiniteLowDiskNotifType
from dropbox.infinite.infinite_disk_tracker import DISK_STATES_TO_NOTIFY, FlushNotificationCallback
from dropbox.infinite.state_machine import AccountToStateAndDiskUsage

def flush_low_disk_notif_if_eligible(account_to_state_and_disk_usage = None, flush_notification = None):
    should_flush = False
    notify_account = None
    notif_type = InfiniteLowDiskNotifType.NONE
# WARNING: Decompyle incomplete

