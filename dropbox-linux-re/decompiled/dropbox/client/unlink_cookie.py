# Source Generated with Decompyle++
# File: unlink_cookie.pyc (Python 3.11)

import base64
import errno
import json
import os
import random as insecure_random
import re
import time
from contextlib import contextmanager
from datetime import datetime
from hashlib import md5
from pprint import pformat
from typing import Any, cast, Dict, IO, Iterator, List, Optional, Set, Text, Tuple, Union
from six import iterkeys, string_types
from build_number import VERSION
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.config import ConfigDict, DBConfig, HIDDEN_FILEID_SET_KEY, UC_NUCLEUS_SE_KEY, UC_NUCLEUS_SE_VALUE
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.constants import AppDataPaths
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY, FILE_PROVIDER_ROOT_CONVERSION_FAILURE_TIME
from dropbox.client.mapreduce import BAD_UNLINK_COOKIE_KEY, DBKeyStore, KeystoreMissingItem
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_remove
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.functions import make_bytes, make_unicode, synchronized
from dropbox.infinite.constants import InfinitePolicySource
from dropbox.legacy_crypto import aes_decrypt, aes_encrypt, RSACipher
from dropbox.legacy_crypto.dropboxy import PUBLIC_KEY_TUPLE
from dropbox.native_threading.python3 import NativeRecursiveMutex
from dropbox.nucleus.migration_constants import SyncEngineState
from dropbox.nucleus.migration_state import SyncEngineStateManager
from dropbox.platform import IS_WINDOWS
from dropbox.preferences import FP_DOWNGRADE, INFINITE_OPTIN_TS, OPT_INSTALLER_TAG, OPT_LANG
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.trace import TRACE

class CorruptCookieError(Exception):
    pass


class UnsafeHostDbError(Exception):
    pass

_unique_host_ints: 'Optional[Set[int]]' = None
_salt = b's1d3fl4pz'
_COOKIE_NAME = 'unlink.db'
_cookie_lock = NativeRecursiveMutex()
_DROPBOX_INFO_FILENAME = 'info.json'
_HOSTDB_NAME = 'host.db'
_HOSTDBX_NAME = 'host.dbx'
HOST_SECRET_KEYNAME = 'host_secret'
UNLINK_COOKIE_PREFS = [
    OPT_LANG,
    OPT_INSTALLER_TAG]

def _write_host_dbx(host_int = None, dropbox_location = None, appdata_path = None):
    pass
# WARNING: Decompyle incomplete


def _write_safe_host_db(dropbox_location = None, appdata_path = None):
    
    try:
        f = open(os.path.join(appdata_path, _HOSTDB_NAME), 'wb')
        f.write(b'\n'.join([
            b'0000000000000000000000000000000000000000',
            base64.b64encode(dropbox_location.encode('utf8'))]))
        
        try:
            None(None, None)
            return None
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            report_exception(component = DesktopComponent.DATABASES)
                            return None





hold_cookie_lock_testonly = (lambda : pass# WARNING: Decompyle incomplete
)()

def get_insecure_unique_host_ints():
    pass
# WARNING: Decompyle incomplete


def _get_insecure_info_json_host_ints(appdata_path = None):
    
    try:
        f = open(os.path.join(appdata_path, _DROPBOX_INFO_FILENAME), 'r')
        info_json = json.load(f)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        return info_json.values()()
                    except Exception:
                        return 





write_dropbox_info = (lambda account_manager = None, appdata_path = synchronized: pass# WARNING: Decompyle incomplete
)()()

def _read_safe_host_db(appdata_path = None, check_for_host_int = None):
    
    try:
        f = open(os.path.join(appdata_path, _HOSTDB_NAME), 'rb')
        for i, line in enumerate(f):
            if check_for_host_int and i == 0 and line != b'%s\n' % b'0000000000000000000000000000000000000000':
                raise UnsafeHostDbError()
            if i == 1:
                
                
                try:
                    None(None, None)
                    return 
                    continue
                    
                    try:
                        None(None, None)
                    with None:
                        if not None, None, base64.b64decode(line).decode('utf8'):
                            
                            try:
                                
                                try:
                                    pass
                                except IOError:
                                    if e.errno != errno.ENOENT:
                                        report_exception(component = DesktopComponent.DATABASES)
                                    None = None
                                    del e
                                except UnsafeHostDbError:
                                    raise 
                                    except Exception:
                                        report_exception(component = DesktopComponent.DATABASES)
                                    return None






CookieDict = Dict[(Text, Any)]

def _cookie_dict_from_config(config = None):
    GROUPS = [
        [
            'host_id',
            'email',
            'root_ns',
            'dropbox_path'],
        [
            'home_ns_path'],
        [
            'home_ns'],
        [
            OPT_LANG],
        [
            OPT_INSTALLER_TAG],
        [
            'libraries_moved'],
        [
            HIDDEN_FILEID_SET_KEY],
        [
            FP_DOWNGRADE],
        [
            SyncRootConstants.CONFIG_KEY_FP_DOMAIN_ID,
            SyncRootConstants.CONFIG_KEY_SYNC_ROOT_TYPE],
        [
            InfinitePolicySource.USER_CHOICE.value],
        [
            FILE_PROVIDER_ROOT_CONVERSION_FAILURE_TIME],
        [
            FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY]]
    cookie_dict = { }
    for group in GROUPS:
        temp_dict = { }
        for key in group:
            if key == 'dropbox_path':
                tkey = 'path'
            elif key == 'host_id':
                tkey = HOST_SECRET_KEYNAME
            else:
                tkey = key
            value = config[key]
            if key == HIDDEN_FILEID_SET_KEY:
                value = cast(List[str], json.loads(value))
            elif key == FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY and isinstance(value, datetime):
                value = value.isoformat()
            temp_dict[tkey] = value
        except KeyError:
            TRACE("Don't have the complete unlink cookie group for %r", group)
            continue
        cookie_dict.update(temp_dict)
        return cookie_dict


def _write_multiple_cookie_dicts(cookie_dict, keystore = None, appdata_path = None, write_to_global_appdata_path = None, overrides = ('cookie_dict', 'CookieDict', 'keystore', 'Optional[DBKeyStore]', 'appdata_path', 'Text', 'write_to_global_appdata_path', 'bool', 'overrides', 'CookieDict', 'return', 'CookieDict')):
    if write_to_global_appdata_path:
        pass
    write_to_global = appdata_path != AppDataPaths.dropbox_appdata_path
    if write_to_global:
        cookie_dict_copy = dict.copy(cookie_dict)
        
        try:
            del cookie_dict_copy[HOST_SECRET_KEYNAME]
        except KeyError:
            pass

        augmented_overrides = dict.copy(overrides)
        
        try:
            del augmented_overrides[HOST_SECRET_KEYNAME]
        except KeyError:
            pass

        toret = _write_cookie_dict(cookie_dict, keystore, appdata_path, overrides)
        if write_to_global:
            TRACE('Writing a copy of the unlink cookie to global appdata.')
            _write_cookie_dict(cookie_dict_copy, None, AppDataPaths.dropbox_appdata_path, augmented_overrides)
    return toret


def _make_cookie_dict(overrides = None):
    return overrides


def write_unlink_cookie(local_config = None, account = None, nucleus_migration_overrides = None, **overrides):
    keystore = local_config.keystore
    appdata_path = local_config.appdata_path
    config = local_config.config_dict
    cookie_dict = _cookie_dict_from_config(config)
    None(None, None)
# WARNING: Decompyle incomplete


def write_unlink_cookie_no_sync_engine(local_config = None, write_config = None, write_host_secret = None, write_to_global_appdata = (False, False, True), **overrides):
    _cookie_lock
    appdata_path = local_config.appdata_path
    config_dict = local_config.config_dict if write_config else None
    keystore = local_config.keystore if write_host_secret else None
    TRACE("!! Can't write unlink cookie because we have no sync engine, just adding local overrides")
    cookie_dict = read_unlink_cookie(appdata_path, keystore)
    if not cookie_dict:
        TRACE("!! Don't have a sync engine, nor is there an old cookie; aborting writing any unlink cookie")
        None(None, None)
        return None
    hidden_fileid_set = None.get(HIDDEN_FILEID_SET_KEY)
# WARNING: Decompyle incomplete

UNLINK_COOKIE_VERSION = 2

def _generate_timestamp():
    return b'%08x' % int(time.time())


def _read_dict_from_file(appdata_path = None):
    pass
# WARNING: Decompyle incomplete


def _atomic_write(dest = None, contents = None):
    tmp = f'''{dest}-{insecure_random.getrandbits(32):x}'''
    
    try:
        f = open(tmp, 'wb')
        f.write(contents)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        os.replace(tmp, dest)
                        if os.path.exists(tmp):
                            os.remove(tmp)
                            return None
                        return None
                    except:
                        if os.path.exists(tmp):
                            os.remove(tmp)






def _write_dict_to_file(cookie_dict = None, timestamp = None, appdata_path = None):
    TRACE('Writing unlink cookie: %r', cookie_dict)
    data = make_bytes(json.dumps(cookie_dict))
    encrypted = aes_encrypt(md5(_salt).digest(), md5(timestamp).digest(), data)
# WARNING: Decompyle incomplete


def _write_cookie_dict(cookie_dict = None, keystore = None, appdata_path = None, overrides = ('cookie_dict', 'CookieDict', 'keystore', 'Optional[DBKeyStore]', 'appdata_path', 'Text', 'overrides', 'CookieDict', 'return', 'CookieDict')):
    cookie_dict.update(overrides)
    timestamp = _generate_timestamp()
    if cookie_dict.get(HOST_SECRET_KEYNAME):
        if keystore:
            pass_key = keystore.get_database_key()
            iv = md5(timestamp).digest()
            encrypted = aes_encrypt(pass_key, iv, make_bytes(cookie_dict[HOST_SECRET_KEYNAME]))
            cookie_dict[HOST_SECRET_KEYNAME] = make_unicode(base64.b64encode(encrypted))
        else:
            report_bad_assumption('cookie with host_id but no keystore')
            del cookie_dict[HOST_SECRET_KEYNAME]
    if FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY in cookie_dict:
        value = cookie_dict[FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY]
        if isinstance(value, datetime):
            cookie_dict[FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY] = value.isoformat()
    cookie_dict['cookie_version'] = UNLINK_COOKIE_VERSION
    cookie_dict['build_no'] = VERSION
    _write_dict_to_file(cookie_dict, timestamp, appdata_path)
    if 'path' in cookie_dict:
        cookie_path = cookie_dict['path']
        if not cookie_path or isinstance(cookie_path, string_types):
            report_bad_assumption('Bad cookie_path in cookie_dict %r' % cookie_path)
    return cookie_dict


def _ensure_safe_host_db(appdata_path = None):
    
    try:
        _read_safe_host_db(appdata_path, check_for_host_int = True)
        return None
    except UnsafeHostDbError:
        dropbox_location = _read_safe_host_db(appdata_path, check_for_host_int = False)
        safe_remove(os.path.join(appdata_path, _HOSTDB_NAME))
        TRACE('!! Found and removed unsafe (old) host db!')
        if dropbox_location:
            TRACE('!! Writing old location %s into new safe host db!', dropbox_location)
            _write_safe_host_db(dropbox_location, AppDataPaths.dropbox_appdata_path)
            return None
        return None
        except Exception:
            report_exception(component = DesktopComponent.DATABASES)
            return None


get_host_secret_from_unlink_cookie = (lambda appdata_path = None, instance_id = None: pass# WARNING: Decompyle incomplete
)()

def remove_unlink_cookie(appdata_path = None, remove_from_global_appdata_path = None):
    _cookie_lock
    cookie_path = os.path.join(appdata_path, _COOKIE_NAME)
    safe_remove(cookie_path)
    if remove_from_global_appdata_path:
        remove_from_global = appdata_path != AppDataPaths.dropbox_appdata_path
        if remove_from_global:
            cookie_path = os.path.join(AppDataPaths.dropbox_appdata_path, _COOKIE_NAME)
            safe_remove(cookie_path)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def read_unlink_cookie(appdata_path = None, keystore = None):
    _ensure_safe_host_db(appdata_path)
    unlink_cookie_tuple = None
    _cookie_lock
    unlink_cookie_tuple = _read_dict_from_file(appdata_path)
# WARNING: Decompyle incomplete


def ensure_unlink_cookie(local_config = None, account = None):
    keystore = local_config.keystore
    appdata_path = local_config.appdata_path
    _cookie_lock
    current_dict = read_unlink_cookie(appdata_path, keystore)
# WARNING: Decompyle incomplete


def _enforce_host_secret_keyname(uc_dict = None):
    if HOST_SECRET_KEYNAME == 'host_secret':
        bad_key = 'host_id'
    else:
        bad_key = 'host_secret'
    if bad_key in uc_dict:
        if HOST_SECRET_KEYNAME not in uc_dict:
            uc_dict[HOST_SECRET_KEYNAME] = uc_dict[bad_key]
        del uc_dict[bad_key]
    if HOST_SECRET_KEYNAME in uc_dict and bad_key in uc_dict:
        report_bad_assumption('Both host secret and host id in unlink cookie')
        del uc_dict[bad_key]
    return uc_dict


def unlink_cookie_is_valid(unlink_cookie = None, account = None):
    if not unlink_cookie:
        return True
    root_ns = None.get('root_ns')
    home_ns = unlink_cookie.get('home_ns')
    root_ns_missing = root_ns is None
    home_ns_missing = home_ns is None
# WARNING: Decompyle incomplete

