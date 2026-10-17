# Source Generated with Decompyle++
# File: open_handle_utils.pyc (Python 3.11)

import itertools
import os
from typing import List, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.sync_everything.v3.config_utils import se_active_device_state_raw
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from winenumhandles.api import get_proc_path, OpenHandleDetails
EXPLORER_SUFFIX = Text('\\explorer.exe')

def has_only_explorer_handle_to_sync_everything(primary_config = None, account = None, open_handle_details_list = None):
