# Source Generated with Decompyle++
# File: webdebugger.pyc (Python 3.11)

from typing import Dict, Optional
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.integration_test import SyncEverythingIntegrationTest
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.webdebugger.server import WebDebugger
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class SyncEverythingWebDebugger(Singleton):
    pass
# WARNING: Decompyle incomplete

