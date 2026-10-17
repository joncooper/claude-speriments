# Source Generated with Decompyle++
# File: fp_helpers.pyc (Python 3.11)

import errno
import os
from typing import Callable, Optional, Tuple
from FileProvider import NSFileProviderDomain, NSFileProviderErrorProviderNotFound, NSFileProviderManager, NSFileProviderManagerDisconnectionOptionsTemporary
from FinderSync import FIFinderSyncController
from Foundation import NSBundle, NSError, NSUserDefaults, NSXPCConnection
from constants import SyncRootConstants
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.mac.internal import autoreleasepool, MacError
from dropbox.mac.version import MAC_VERSION, SONOMA_14_1
from dropbox.trace import TRACE
# WARNING: Decompyle incomplete
