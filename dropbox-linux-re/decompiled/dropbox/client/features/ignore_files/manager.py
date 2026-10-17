# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

from typing import Dict, Optional
from build_number.features import feature_enabled
from dropbox.client.authentication.types import AccountId
from dropbox.client.features.ignore_files.controller import IgnoreFilesController
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.stormcrow.machine import MachineStormcrow

class IgnoreFilesManager(SingletonActor):
    pass
# WARNING: Decompyle incomplete

