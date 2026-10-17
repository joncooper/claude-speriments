# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from build_number import is_frozen
from build_number.features import feature_enabled
from dropbox.foundation.environment import is_integration_tests
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from linux import AppDataPaths, DEFAULT_DROPBOX_FOLDER_NAME, DEFAULT_DROPBOX_PATH, get_omaha4_crashpad_usage_stats_folder_path, LOCAL_FORM
elif IS_MAC:
    from mac import AppDataPaths, DEFAULT_DROPBOX_FOLDER_NAME, DEFAULT_DROPBOX_PATH, get_omaha4_crashpad_usage_stats_folder_path, LOCAL_FORM
elif IS_WINDOWS:
    from win import AppDataPaths, DEFAULT_DROPBOX_FOLDER_NAME, DEFAULT_DROPBOX_PATH, get_omaha4_crashpad_usage_stats_folder_path, LOCAL_FORM
if (is_frozen() and feature_enabled('connect-to-dev-vm') or is_integration_tests()) and os.environ.get('DROPBOX_HOST'):
    DROPBOX_API_APP_KEY = 'devboxdropboxdesktopappkey'
    DROPBOX_API_APP_SECRET = 'devboxdropboxdesktopappsecret'
    return None
from bazel_generated.api_keys import DROPBOX_API_APP_KEY, DROPBOX_API_APP_SECRET
