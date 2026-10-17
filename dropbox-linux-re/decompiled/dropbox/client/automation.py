# Source Generated with Decompyle++
# File: automation.pyc (Python 3.11)

import hashlib
import json
import os
import socket
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
from six import iteritems
from build_number import dropbox_version
from dropbox.client.configuration.local_configuration import LocalConfiguration
from dropbox.client.relocate_namespace_folders import DropboxArranger
from dropbox.client.screenshots.controller import ScreenshotsController
from dropbox.client.setup_wizard.setup_wizard_controller import SetupWizardController
from dropbox.client.util import hard_exit
from dropbox.client_api.exceptions import HTTP500Error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.environment import is_integration_tests
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import retry, RetryException
from dropbox.harmony.utility.constants import CONFIG_KEY_HARMONY_ONBOARDING, HarmonyInteractionStates
from dropbox.platform import IS_MAC
from dropbox.preferences import OPT_SCREENSHOTS
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_boundary.hidden import HiddenSet
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
if IS_MAC:
    from dropbox.client.util.mac import privileged_defaults_string_for_key
    
    def _env_var_to_defaults_key(value = None):
