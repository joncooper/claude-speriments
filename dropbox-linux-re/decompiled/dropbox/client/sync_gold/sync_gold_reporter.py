# Source Generated with Decompyle++
# File: sync_gold_reporter.pyc (Python 3.11)

from dataclasses import dataclass
from typing import Dict, Optional, Tuple
from build_number import is_frozen
from build_number.platform import IS_MAC
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY
from dropbox.client.hourly_refresh import HourlyRefreshController
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.client.features.file_provider_migration.config import FPMigrationStateStore
    from dropbox.client.features.file_provider_migration.implementation import FileProviderMigrationController, FileProviderMigrationControllerWrapper
    from dropbox.client.util.mac import get_app_path
    from dropbox.mac.version import MAC_VERSION, MONTEREY
    from dropbox.sync_root.handlers.macos.types import FileProviderDomainProperties
MacOSSyncGoldData = <NODE:12>()

class MacOSSyncGoldReporter(SingletonActor):
    pass
# WARNING: Decompyle incomplete

