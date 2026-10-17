# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import uuid
from typing import List, Optional, TypedDict
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.sprig.logging import report_update_primary_account_event, SprigTriggerPoints
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.managed_electron_view import ManagedElectronView, ManagedElectronViewDefinition, ManagedElectronViewResult
from dropbox.foundation.platform_version import PLATFORM_VERSION
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
RPC_NAME_TRACK_EVENT = 'sprig_track_event'
RPC_NAME_SPRIG_SET_USER_ATTRIBUTES = 'sprig_set_user_attributes'
RPC_NAME_DESTROY_WINDOW = 'sprig_destroy_window'
SPRIG_VIEW_NAME = 'sprigView'

def SprigUserAttributes():
    '''SprigUserAttributes'''
    desktopDashDualPopVariant: 'str' = 'SprigUserAttributes'

SprigUserAttributes = <NODE:27>(SprigUserAttributes, 'SprigUserAttributes', TypedDict, total = False)

class SprigController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

