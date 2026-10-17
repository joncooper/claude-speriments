# Source Generated with Decompyle++
# File: tray_do_not_disturb_menu.pyc (Python 3.11)

from collections import OrderedDict
from datetime import datetime
from typing import Callable, List, Optional, Union
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeInterval
from dropbox.client.notifications.loud_notifications.do_not_disturb.controller_wrapper import DoNotDisturbControllerWrapper
from dropbox.client.notifications.loud_notifications.do_not_disturb.model import DNDTimeIntervalsStringMapping
from dropbox.client.tray.events import track_click, TrayEventName, TrayEventTrigger
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem, Separator, SubMenu
from dropbox.client.ui.common.tray_menu_options import TrayOption, TrayOptionStrings
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.i18n import format_time

class TrayDoNotDisturbMenu(Destroyable):
    pass
# WARNING: Decompyle incomplete

