# Source Generated with Decompyle++
# File: link_controller.pyc (Python 3.11)

from typing import Callable, Optional
from build_number.features import feature_enabled
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.auth_state import AuthState
from dropbox.client.authentication.interface import AccountManagerInterface, LinkControllerInterface
from dropbox.client.authentication.link_thread import LinkThread, on_link_thread_returns_none
from dropbox.client.authentication.register_host_helper import RegisterHostHelper
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.client.configuration.local_configuration import LocalConfiguration
from dropbox.client.features.smarter_smart_sync.helpers import set_custom_root_policy_and_update_ss_autoevict
from dropbox.client.fenix.account_cache import FenixAccountCache
from dropbox.client.installer_tag import InstallerTag
from dropbox.client.setup_wizard.account_link_state import LinkPreferences
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.status.label import StatusLabel
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.client_api.exceptions import TransientErrorType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.i18n import trans
from dropbox.infinite.preferences import InfinitePolicy
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class LinkController(LinkControllerInterface):
    
    def __init__(self, app, account_manager, config_manager = None, status_controller = None, installer_tag = None, register_host_helper = ('app', 'DropboxApplication', 'account_manager', 'AccountManagerInterface', 'config_manager', 'ConfigurationManagerInterface', 'status_controller', 'StatusControllerInterface', 'installer_tag', 'InstallerTag', 'register_host_helper', 'RegisterHostHelper', 'return', 'None')):
        self._app = app
        self._account_manager = account_manager
        self._config_manager = config_manager
        self._status_controller = status_controller
        self._installer_tag = installer_tag
        self._register_host_helper = register_host_helper
        self.secondary_setupwizard_progress = Handler()
        self._register_host_helper.add_error_callback(self._on_register_host_error)
        self._start_link_thread()

    
    def _start_link_thread(self = None):
        self._thread = LinkThread()
        self._thread.start()

    
    def _on_register_host_error(self = None, transient_error = None, error_count = None):
        silent_retry_error = transient_error in (TransientErrorType.HTTP_5XX, TransientErrorType.CONNECTION_DROPPED, TransientErrorType.HTTP_503)
        local_config = self._config_manager.local_config(None)
    # WARNING: Decompyle incomplete

    link_account = (lambda self = None, unlinked_account = None, done_callback = None, linked_on_server = on_link_thread_returns_none(), setup_wizard_ui_appeared_callback = (False, None), *, is_pairing, local_config = None, setup_link_callback = None, preauth_nonce = None, preauth_complete = None: pass# WARNING: Decompyle incomplete
)()

