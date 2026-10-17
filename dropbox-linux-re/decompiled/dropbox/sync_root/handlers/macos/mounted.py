# Source Generated with Decompyle++
# File: mounted.pyc (Python 3.11)

import errno
import os
from pathlib import Path
from typing import Callable, List, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.mac.system_preferences import open_security_pane_privacy, SecurityPaneServiceType
from dropbox.mac.version import CATALINA, MAC_VERSION
from dropbox.overrides import report_exception
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.handlers.interface import _SyncRootHandler
from dropbox.sync_root.handlers.macos.mac_handler import _MacRootHandler
from dropbox.sync_root.helpers import check_dropbox_path_exists
from dropbox.sync_root.interface import SyncRootType
from dropbox.sync_root.types import RemovalMode, SyncRootCreationResult, SyncRootHydrationPolicy, SyncRootRepairAction
from dropbox.trace import TRACE

class _MacMountedRootHandler(_MacRootHandler):
    pass
# WARNING: Decompyle incomplete

