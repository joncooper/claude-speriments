# Source Generated with Decompyle++
# File: onboarding_legacy_service.pyc (Python 3.11)

from typing import Any, cast, Dict, Optional, Tuple
from apex.metrics import Metric
from build_number import BUILD_KEY
from dropbox import fsutil
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.fenix.account_cache import FenixAccountCache
from dropbox.client.fenix.types.account import AuthenticatedAccount
from dropbox.client.fenix.utils import fenix_api, get_account_linked_or_from_cache
from dropbox.client.setup_wizard.setup_wizard_constants import DESKTOP_WELCOME_FLOW_TABLE_NAME
from dropbox.client.setup_wizard.setup_wizard_controller import SMB_FUNNEL_AMP_NAMESPACE
from dropbox.client.setup_wizard.setup_wizard_metrics import SetupWizardMetrics
from dropbox.client.setup_wizard.setup_wizard_pap_logging import generate_validation_trace_id, log_setup_wizard_pap_event
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import EXPERIMENT_EVENT
from dropbox.exception.reporting import report_exception
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class OnboardingLegacyService(Actor):
    pass
# WARNING: Decompyle incomplete

