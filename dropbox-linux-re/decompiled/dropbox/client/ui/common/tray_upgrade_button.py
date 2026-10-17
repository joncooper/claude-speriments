# Source Generated with Decompyle++
# File: tray_upgrade_button.pyc (Python 3.11)

from typing import Optional
from dropbox.client.status.interface import ClientStatusInterface
from dropbox.client.status.label import StatusLabel
from dropbox.client.status.wrapper import StatusControllerWrapper
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.foundation.account_manager import AccountUpdate
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals import Signal, StandardSignal
UPGRADE_URI = 'upgrade?oqa=client_eh'
UPGRADE_URI_UNLINKED = 'upgrade?oqa=client_eh_unlinked'
UPGRADE_URI_PAIRED = 'upgrade?oqa=client_eh_paired'

class TrayUpgradeButtonController(Destroyable):
    pass
# WARNING: Decompyle incomplete

