# Source Generated with Decompyle++
# File: webdebugger.pyc (Python 3.11)

from typing import Dict, Optional
from dropbox.client.features.external_drive_backup.integration_test import ExternalDriveBackupIntegrationTest
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.webdebugger.server import WebDebugger
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class ExternalBackupWebDebugger(Singleton):
    pass
# WARNING: Decompyle incomplete

