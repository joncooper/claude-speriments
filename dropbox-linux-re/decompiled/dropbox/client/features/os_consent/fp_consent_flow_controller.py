# Source Generated with Decompyle++
# File: fp_consent_flow_controller.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.os_consent.os_consent_flow import OSConsentFlow
from dropbox.client.features.os_consent.os_consent_notifications import show_fp_consent_revoke_notification
from dropbox.client.high_trace import report_bad_assumption
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.local_time_getter import LocalTimeGetter
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import Destroyable
from dropbox.sync_root.interface import SyncRootManagerInterface, SyncRootType
FP_CONSENT_REVOKED_TIME = 'fp_consent_revoked_time'

class FPConsentFlowController(Destroyable):
    pass
# WARNING: Decompyle incomplete

