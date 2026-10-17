# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

from enum import auto, Enum
from typing import Optional
from dropbox.client.analytics import log_pap_event
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeInterval
from dropbox.event import report
from dropbox.pap.events.tray.click_tray_menu_pb2 import Click_TrayMenu

class SnoozeSyncEvent(Enum):
    SNOOZE_TIME_EXPIRED = auto()
    SET_SNOOZE_TIME = auto()
    TURN_OFF_SNOOZE = auto()


def report_event(event = None, time_interval = None):
    report('snooze-sync', event = event.name.lower(), time_interval = str(time_interval))
    log_pap_event(Click_TrayMenu(snooze_event = event.name.lower(), time_interval = str(time_interval)))

