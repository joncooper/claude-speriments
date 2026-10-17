# Source Generated with Decompyle++
# File: apollo_view_anchor.pyc (Python 3.11)

from typing import cast, Optional
from dropbox.client.features.account_switcher.account_switcher_vm import AccountSwitcherVM
from dropbox.client.features.account_switcher.bridge_gen.bridge_interface_account_switcher_vm import AccountSwitcherVMBridgeInterface
from dropbox.client.features.api_v2.api_v2 import ApiV2ClientUntyped
from dropbox.client.features.apollo_alerts.view_model.apollo_alerts_vm import ApolloAlertsVM
from dropbox.client.features.apollo_landing_surface.bridge_gen.bridge_interface_apollo_view_anchor import ApolloViewAnchorBridgeInterface
from dropbox.client.features.feature_flags.feature_flags_manager import FeatureFlagsManager
from dropbox.client.features.network_state.view_model.network_state_vm import NetworkStateVM
from dropbox.client.features.sync_everything.view_model.sync_everything_manager_view_model import SyncEverythingManagerViewModel
from dropbox.client.features.users.view_model.users_vm import UsersVM
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.html_views.common.bridge_gen.bridge_interface_view_anchor import ViewAnchorBridgeInterface
from dropbox.foundation.html_views.common.interface import ViewAnchorConfiguration, ViewAnchorInterface
from dropbox.foundation.native_file_opener.impl import ContextBoundNativeFileOpener
from dropbox.foundation.paths.user_folder_paths_wrapper import UserFolderPathsWrapper
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2.wrappers.lazy import Lazy

class ApolloViewAnchor(Actor, ApolloViewAnchorBridgeInterface, ViewAnchorInterface):
    pass
# WARNING: Decompyle incomplete


def cast_to_apollo_anchor(anchor = None):
    return anchor if isinstance(anchor, ApolloViewAnchor) else None

