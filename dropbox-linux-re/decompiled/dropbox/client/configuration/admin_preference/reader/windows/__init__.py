# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from typing import Any, Dict, NamedTuple, Optional, Type
import win32event
from dropbox.client.configuration.admin_preference.reader import AdminPreferenceReader, AdminPreferenceSetting
from dropbox.client.configuration.admin_preference.reader.windows.registry_utils import RegistryReader, SimpleRegistryReader
from dropbox.event import report
from dropbox.exception.severity import Severity
from dropbox.preferences import OPT_DROPBOX_FOLDER_OPENER_APP, OPT_HARMONY, OPT_HARMONY_VISIBILITY, OPT_P2P, OPT_STARTUP
from dropbox.trace import TRACE
REGISTRY_MAIN_PATH = 'SOFTWARE\\Policies\\Dropbox'
LOCKED_BY_ADMIN_VALUE = 1
RegistryPreference = NamedTuple('RegistryPreference', [
    ('key_path', str),
    ('value_name', str),
    ('registry_reader', Type[RegistryReader])])
# WARNING: Decompyle incomplete
