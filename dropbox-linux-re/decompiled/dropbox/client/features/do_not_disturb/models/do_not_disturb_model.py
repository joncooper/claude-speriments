# Source Generated with Decompyle++
# File: do_not_disturb_model.pyc (Python 3.11)

from datetime import datetime
from typing import Optional
from dropbox.client.features.do_not_disturb.models.bridge_gen.bridge_interface_do_not_disturb_model import DoNotDisturbModelBridgeInterface, DoNotDisturbModelObservableMixin
from dropbox.client.features.do_not_disturb.models.bridge_gen.interval import Interval
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeInterval
from dropbox.client.notifications.loud_notifications.do_not_disturb.controller_wrapper import DoNotDisturbControllerWrapper
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.singleton import SingletonActor

def interval_to_native(interval = None):
    if interval == Interval.THIRTY_MINUTES:
        return SnoozeTimeInterval.THIRTY_MINUTES
    if None == Interval.ONE_HOUR:
        return SnoozeTimeInterval.ONE_HOUR
    if None == Interval.UNTIL_AFTERNOON:
        return SnoozeTimeInterval.UNTIL_AFTERNOON
    if None == Interval.UNTIL_END_OF_DAY:
        return SnoozeTimeInterval.UNTIL_END_OF_DAY
    if None == Interval.UNTIL_TOMORROW:
        return SnoozeTimeInterval.UNTIL_TOMORROW
    if None == Interval.INDEFINITELY:
        return SnoozeTimeInterval.INDEFINITELY
    return None.UNKNOWN


class DoNotDisturbModel(SingletonActor, DoNotDisturbModelBridgeInterface, DoNotDisturbModelObservableMixin):
    pass
# WARNING: Decompyle incomplete

