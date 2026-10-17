# Source Generated with Decompyle++
# File: multibox.pyc (Python 3.11)

import os
import pprint
import re
import shutil
from typing import Any, Dict, Text
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.auth_state import AuthState
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.constants import AppDataPaths
from dropbox.client.databases import clear_appdata_for_unlink
from dropbox.client.multiaccount.values import MultiaccountValues
from dropbox.client.unlink_cookie import read_unlink_cookie
from dropbox.client.unlink_handlers import report_unlink_event
from dropbox.client.util import launch_new_dropbox
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.fileutils import safe_remove
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE

class MultiBoxServer(MultiaccountValues):
    pass
# WARNING: Decompyle incomplete

