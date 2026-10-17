# Source Generated with Decompyle++
# File: control_flow_helpers.pyc (Python 3.11)

from typing import Callable, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.os_consent.os_consent_logging import OSConsentEvent
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.status.label import StatusLabel
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2 import Destroyable, destroying
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.sync_root.interface import SyncRootConsentInterface
from dropbox.sync_root.poll import RootPermissionPollster
from dropbox.trace import TRACE
FP_REVOKED_CONSENT_RESTART_KILLSWITCH = 'desktop-fp-revoked-consent-restart-killswitch'

class RootConsentHelper(Destroyable):
    pass
# WARNING: Decompyle incomplete


def on_consent_changed(account = None, context = None, on_consent_revoked = None, on_consent_granted = (None, None, None), on_error = ('account', 'AccountInterface', 'context', 'MachineContext', 'on_consent_revoked', 'Optional[Callable[[], None]]', 'on_consent_granted', 'Optional[Callable[[], None]]', 'on_error', 'Optional[Callable[[Exception, ExcInfo], Future[None]]]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete

