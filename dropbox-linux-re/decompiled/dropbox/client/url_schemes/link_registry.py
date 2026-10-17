# Source Generated with Decompyle++
# File: link_registry.pyc (Python 3.11)

from typing import Callable, List, Mapping
from dropbox.client.features.account_pairing.pair_deep_link_controller import PairDeepLinkController
from dropbox.client.features.desktop_client_url_scheme.desktop_folder_deep_link_controller import DesktopFolderDeepLinkController
from dropbox.client.features.sync_everything.v3.sync_everything_deep_link_controller import SyncEverythingDeepLinkController
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.legacy_views.parameters.bridge_gen.preferences_pane_params import PreferencesPaneParams
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.navigation_service.manifest_registry import PREFERENCES_PANE
MYPY = False
if MYPY:
    from dropbox.app.machine_ui_dispatcher import AttemptLinkFunc
    LinkHandler = Callable[([
        str,
        Mapping[(str, List[str])],
        NavigationServiceInterface,
        MachineContext,
        AttemptLinkFunc], None)]

def prefs_link_handler(_path, query = None, navigation_service = None, _machine_context = None, _attempt_link = ('_path', 'str', 'query', 'Mapping[str, List[str]]', 'navigation_service', 'NavigationServiceInterface', '_machine_context', 'MachineContext', 'return', 'None')):
