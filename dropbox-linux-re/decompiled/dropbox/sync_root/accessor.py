# Source Generated with Decompyle++
# File: accessor.pyc (Python 3.11)

from typing import Callable, Dict, List, Optional
from build_number.features import is_test
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.apollo_alerts.model.apollo_alerts import AlertResult, ApolloAlerts
from dropbox.client.features.os_consent.os_consent_logging import OSConsentEvent, report_os_consent_event
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.sync_root.interface import SyncRootConsentInterface, SyncRootManagerInterface, SyncRootType
from dropbox.sync_root.poll import RootPermissionPollster
from dropbox.threading import Lock
from dropbox.trace import TRACE

class RootManagerAccessor(SyncRootConsentInterface, Singleton):
    pass
# WARNING: Decompyle incomplete


class _RootPermissionObserver(Actor):
    pass
# WARNING: Decompyle incomplete

