# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Optional, Text
from build_number import is_full_msix
from build_number.features import feature_enabled
from _exceptions import KeystoreItemUnexpectedlyMissing, KeystoreMissingItem, KeystoreRegKeyError
from base import KeyStoreBase
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE

def get_keystore(appdata_path = None, instance_id = None):
    if IS_MAC:
        KeyStoreMac = KeyStoreMac
        import keystore_mac
        return KeyStoreMac(appdata_path, instance_id)
    if None:
        AppDataKeyStoreWin = AppDataKeyStoreWin
        import keystore_win32
        return AppDataKeyStoreWin(appdata_path, instance_id)
# WARNING: Decompyle incomplete

