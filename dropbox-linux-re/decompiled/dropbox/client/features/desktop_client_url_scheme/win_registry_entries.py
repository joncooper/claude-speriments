# Source Generated with Decompyle++
# File: win_registry_entries.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List, Optional, Text, Tuple
from pynt.constants import REG_VALUE_TYPE, WOW64_ACCESS_TYPE
from dropbox.client.features.foundation.custom_url_scheme_handler.registrar_win import url_scheme_registry_entries
from dropbox.client.url_schemes.client_url_scheme_handler import DesktopClientURLSchemeHandler

def desktop_client_url_scheme_registry_entries(exe_path = None):
    return url_scheme_registry_entries(exe_path, DesktopClientURLSchemeHandler.scheme, exe_path)

