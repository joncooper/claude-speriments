# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import uuid
from enum import Enum
from typing import Optional, Set
from urllib.parse import urlparse
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.eligibility_cache import FenixEligibilityCache, FenixEligibilityGates
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.fenix.journeys.app_shell.constants import ALLOWED_EXACT_PATHS, ALLOWED_PATH_PREFIXES, BLOCKED_PATH_PREFIXES, DROPBOX_DOMAIN, DROPBOXUSERCONTENT_DOMAIN, FOREGROUND_SURFACE_EXPERIMENT, GATED_SCL_PATH_PREFIXES, REJECTED_PATH_PATTERNS, Views
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.trace import TRACE
BRIDGE_V2_PRIMARY_GROWTHBOOK_STORMCROW = 'desktop-experience-webmpxp-2026-04-24-bridge-v2-web'
BRIDGE_V2_ENABLED_VARIANTS = ('ON', 'FORCED_ON')
SCL_NATIVE_NAVIGATION_GROWTHBOOK = 'desktop-experience-2026-09-17-app-shell-scl-native-navigation-enabled'

def is_bridge_v2_stormcrow_candidate(gandalf = None, account = None, component = None):
    return is_bridge_v2_stormcrow_candidate_or_none(gandalf, account, component) is True


def is_bridge_v2_stormcrow_candidate_or_none(gandalf = None, account = None, component = None):
    pass
# WARNING: Decompyle incomplete


def _normalize_path(pathname = None):
