# Source Generated with Decompyle++
# File: deals_win_client_info.pyc (Python 3.11)

from typing import Any
from pynt.constants import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, KEY_READ, KEY_WOW64_64KEY, REG_DWORD
from pynt.helpers.registry import create_registry_key, enum_registry_values, registry_key, set_registry_value

def get_hp_segment_registry_values():
    reg_key = registry_key(HKEY_LOCAL_MACHINE, 'SOFTWARE\\Hewlett-Packard\\CommonInfo\\Segment', KEY_READ | KEY_WOW64_64KEY)
    None(None, None)
    return 
    with None:
        if not None, list(enum_registry_values(reg_key)):
            pass


def get_deals_test_registry_values():
    reg_key = registry_key(HKEY_LOCAL_MACHINE, 'SOFTWARE\\Dropbox-Desktop\\Deals', KEY_READ | KEY_WOW64_64KEY)
    None(None, None)
    return 
    with None:
        if not None, list(enum_registry_values(reg_key)):
            pass


def create_deal_redeemed_registry_value():
    (key, _, _) = create_registry_key(HKEY_CURRENT_USER, 'SOFTWARE\\Dropbox-Desktop\\Deals')
    if key:
        set_registry_value(key, 'deal_redeemed', REG_DWORD, 1)
    else:
        raise Exception("Couldn't set key deal_redeemed in registry")
    None(None, None)
    return None
    with None:
        if not None:
            pass

