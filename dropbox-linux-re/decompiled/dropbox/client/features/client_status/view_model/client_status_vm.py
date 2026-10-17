# Source Generated with Decompyle++
# File: client_status_vm.pyc (Python 3.11)

from datetime import datetime
from typing import Optional
from dropbox.client.features.client_status.bridge_gen.bridge_interface_client_status_vm import ClientStatusVMBridgeInterface, ClientStatusVMObservableMixin
from dropbox.client.features.client_status.bridge_gen.client_status import ClientStatus
from dropbox.client.features.client_status.bridge_gen.client_status_tag import ClientStatusTag
from dropbox.client.features.client_status.view_model.conversion import bridge_client_status
from dropbox.client.features.do_not_disturb.models.bridge_gen.interval import Interval
from dropbox.client.features.do_not_disturb.models.do_not_disturb_model import interval_to_native
from dropbox.client.features.home_feed.shared.util.signals import ThrottledSignal
from dropbox.client.features.snooze_sync.snooze_sync_controller_wrapper import SnoozeSyncControllerWrapper
from dropbox.client.status.interface import ClientStatusInterface, PauseOrResume
from dropbox.client.status.wrapper import StatusControllerWrapper
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.threading import Lock
from dropbox.trace import TRACE
THROTTLE_UPDATE_SECONDS = 1

class ClientStatusVM(ClientStatusVMBridgeInterface, SingletonActor, ClientStatusVMObservableMixin):
    pass
# WARNING: Decompyle incomplete

