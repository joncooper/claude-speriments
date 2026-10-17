# Source Generated with Decompyle++
# File: os_consent_flow.pyc (Python 3.11)

from uuid import uuid4
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.apollo_alerts.model.apollo_alerts import AlertResult, ApolloAlerts
from dropbox.client.features.os_consent.os_consent_logging import OSConsentEvent, report_os_consent_flow_event
from dropbox.client.features.os_consent.os_consent_strings import OSConsentUIStrings
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.sync_root.accessor import RootManagerAccessor

class OSConsentFlow(Actor):
    pass
# WARNING: Decompyle incomplete

