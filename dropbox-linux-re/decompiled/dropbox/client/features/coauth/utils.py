# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import List
from build_number import IS_WINDOWS
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.coauth.constants import COAUTH_ACCOUNT_KEY_ROOT_PATH_FIELD_NAME, COAUTH_ACCOUNT_KEY_WOPI_SERVICE_ID_FIELD_NAME, COAUTH_ACCOUNT_KEY_WOPI_SERVICE_ID_FIELD_VALUE, COAUTH_ACCOUNT_KEY_WOPI_USER_ID_FIELD_NAME, COAUTH_CLSID_KEY, COAUTH_DROPBOX_CLSID, COAUTH_GLOBAL_KEY, COAUTH_GLOBAL_KEY_HANDLER_FIELD_NAME, COAUTH_GLOBAL_KEY_HASH_ALGORITHM_FIELD_NAME, COAUTH_GLOBAL_KEY_HASH_ALGORITHM_FIELD_VALUE
from dropbox.event import report
from dropbox.foundation.context.machine import MachineContext
from dropbox.trace import TRACE
if IS_WINDOWS:
    from winreg import HKEY_CURRENT_USER, KEY_READ, KEY_WRITE, REG_SZ
    from pynt.helpers.registry import create_registry_key, enum_registry_subkeys, registry_key, safe_delete_regkey, set_registry_value

def _get_coauth_account_key(account = None):
    return f'''{COAUTH_GLOBAL_KEY}\\{account.uid}'''


def create_coauth_registry_key_for_account_if_needed(account = None, root_mount_path = None):
    TRACE('[CoauthController] create_coauth_registry_key_for_account_if_needed for account %s. root mount path: %s', account, root_mount_path)
    account_key = _get_coauth_account_key(account)
    (coauth_account_key, is_new_key_created, _) = create_registry_key(HKEY_CURRENT_USER, account_key)
    if is_new_key_created:
        TRACE('[CoauthController] created new coauth account key for account %s, root_mount_path %s', account, root_mount_path)
    else:
        TRACE('[CoauthController] using existing account key')
    set_registry_value(coauth_account_key, COAUTH_ACCOUNT_KEY_ROOT_PATH_FIELD_NAME, REG_SZ, root_mount_path)
    set_registry_value(coauth_account_key, COAUTH_ACCOUNT_KEY_WOPI_SERVICE_ID_FIELD_NAME, REG_SZ, COAUTH_ACCOUNT_KEY_WOPI_SERVICE_ID_FIELD_VALUE)
    set_registry_value(coauth_account_key, COAUTH_ACCOUNT_KEY_WOPI_USER_ID_FIELD_NAME, REG_SZ, str(account.uid))
    None(None, None)
    return None
    with None:
        if not None:
            pass


def create_coauth_registry_keys_global_if_needed():
    TRACE('[CoauthController] create_coauth_registry_keys_global_if_needed')
    (coauth_global_key, is_new_key_created, _) = create_registry_key(HKEY_CURRENT_USER, COAUTH_GLOBAL_KEY)
    if is_new_key_created:
        TRACE('[CoauthController] created new coauth global key')
    else:
        TRACE('[CoauthController] using existing global key')
    set_registry_value(coauth_global_key, COAUTH_GLOBAL_KEY_HANDLER_FIELD_NAME, REG_SZ, COAUTH_DROPBOX_CLSID)
    set_registry_value(coauth_global_key, COAUTH_GLOBAL_KEY_HASH_ALGORITHM_FIELD_NAME, REG_SZ, COAUTH_GLOBAL_KEY_HASH_ALGORITHM_FIELD_VALUE)
    None(None, None)


def destroy_coauth_registry_key_for_account(account = None):
    TRACE('[CoauthController] destroy_coauth_registry_key_for_account if present for account %s.', account)
    account_key = _get_coauth_account_key(account)
    safe_delete_regkey(HKEY_CURRENT_USER, account_key)


def destroy_coauth_global_registry_key():
    TRACE('[CoauthController] destroy_coauth_global_registry_key if present')
    safe_delete_regkey(HKEY_CURRENT_USER, COAUTH_GLOBAL_KEY)
    safe_delete_regkey(HKEY_CURRENT_USER, COAUTH_CLSID_KEY)


def remove_dangling_account_keys_if_any(machine_context = None):
    TRACE('[CoauthController] remove_dangling_account_keys_if_any')
    active_user_ids = machine_context.account_manager.account_models.keys()()
    remove_unknown_account_keys_if_any(active_user_ids)


def remove_unknown_account_keys_if_any(known_user_ids = None):
    TRACE('[CoauthController] remove_unknown_account_keys_if_any; known_user_ids=%r', known_user_ids)
    keys_to_remove = []
    global_key = registry_key(HKEY_CURRENT_USER, COAUTH_GLOBAL_KEY, permission = KEY_WRITE | KEY_READ)
    if not global_key:
        TRACE('[CoauthController] no global key exists so no account sub-keys to delete')
        None(None, None)
        return None
    for account_key_str in enum_registry_subkeys(global_key):
        if account_key_str not in known_user_ids:
            keys_to_remove.append(account_key_str)
        None(None, None)
    with None:
        if not None:
            pass
    if keys_to_remove:
        TRACE('[CoauthController] removing dangling account keys %s', keys_to_remove)
    else:
        TRACE('[CoauthController] no dangling account keys to remove')
    for account_key_str in keys_to_remove:
        account_key = f'''{COAUTH_GLOBAL_KEY}\\{account_key_str}'''
        safe_delete_regkey(HKEY_CURRENT_USER, account_key)
        report('coauth-events', event_name = 'remove_dangling_account_key', extra = dict(account_key = account_key_str))
        return None


def update_registry_key_root_path(account = None, new_dropbox_path = None):
    TRACE('[CoauthController] update_registry_key_root_path')
    account_key_name = _get_coauth_account_key(account)
    account_key = registry_key(HKEY_CURRENT_USER, account_key_name, permission = KEY_WRITE | KEY_READ)
    if account_key:
        TRACE('[CoauthController] updating registry key value for dropbox path with value: %s', new_dropbox_path)
        set_registry_value(account_key, COAUTH_ACCOUNT_KEY_ROOT_PATH_FIELD_NAME, REG_SZ, new_dropbox_path)
    else:
        TRACE('[CoauthController] no account key to update')
    None(None, None)
    return None
    with None:
        if not None:
            pass

