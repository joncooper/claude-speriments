# Source Generated with Decompyle++
# File: registry.pyc (Python 3.11)

from typing import Optional
import win32con
from pynt.constants import KEY_READ, KEY_WOW64_32KEY
from pynt.helpers.registry import registry_key, safe_read_registry_value

def get_registry_dealcode():
    hkey = registry_key(win32con.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Dropbox\\DropboxOEM', permission = KEY_READ | KEY_WOW64_32KEY)
    if hkey:
        None(None, None)
        return 
    None(None, None)

