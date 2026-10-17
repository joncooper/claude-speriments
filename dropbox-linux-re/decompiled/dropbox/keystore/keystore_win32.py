# Source Generated with Decompyle++
# File: keystore_win32.pyc (Python 3.11)

from __future__ import absolute_import
import os
import winreg
from typing import Dict, List, Optional, Text, Tuple
from pynt.constants import HKEY_CURRENT_USER, REG_BINARY
from pynt.helpers.registry import create_registry_key, read_registry_value, set_registry_value
from build_number import BUILD_KEY, is_full_msix
from _exceptions import KeystoreMigrationMismatch, KeystoreMissingItem, KeystoreRegKeyError
from base import KeyStoreBase
from dropbox.client.constants.win import AppDataPaths
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_remove
from dropbox.trace import TRACE
UNENCRYPTED_KEY_NAME_SUFFIX = '-p'
_SUFFIX_LEN = len(UNENCRYPTED_KEY_NAME_SUFFIX)
KEYSTORE_MIGRATION_VERSION = 6
FORCE_MIGRATION_TEST_ONLY = False

def _get_migration_version_file(config = None):
    appdata_path = AppDataPaths.dropbox_appdata_path
    if config:
        return os.path.join(appdata_path, 'ksmigrated_config.dbx')
    return None.path.join(appdata_path, 'ksmigrated.dbx')


def _get_migration_variant_file():
    return os.path.join(AppDataPaths.dropbox_appdata_path, 'ksmigrated_variant.dbx')


def _get_migration_variant():
    return 'appdata_only'


def _should_migrate_keystore(migration_version_marker = None, migration_variant_marker = None):
    if FORCE_MIGRATION_TEST_ONLY:
        return (True, 'Forcing migration for testing')
    if None.path.exists(migration_version_marker):
        version_marker = open(migration_version_marker, 'r', encoding = 'utf-8')
        migration_version = version_marker.read()
        if int(migration_version) < KEYSTORE_MIGRATION_VERSION:
            None(None, None)
            return (True, 'Keystore Migration version has increased')
        if None.path.exists(migration_variant_marker):
            variant_marker = open(migration_variant_marker, 'r', encoding = 'utf-8')
            prev_variant = variant_marker.read()
            curr_variant = _get_migration_variant()
            if prev_variant != curr_variant:
                None(None, None)
                None(None, None)
                return 
            None(None, None)
            None(None, None)
            return (False, None)
        with None:
            if not None:
                pass
    else:
        None(None, None)
        return (False, None)
    None(None, None)
    return None
    with None:
        if not None:
            pass
    return None
    return (True, 'No migration marker found')


def _clear_previous_migration_files():
    appdata_path = AppDataPaths.dropbox_appdata_path
    for filename in os.listdir(appdata_path):
        if filename.startswith('ksmigrated'):
            safe_remove(os.path.join(appdata_path, filename))
        return None


def _migrate_registry_key_to_appdata(appdata_path = None, instance_id = None):
    instance_string = str(instance_id) if instance_id else ''
    
    try:
        software_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software')
        dropbox_key = winreg.OpenKey(software_key, BUILD_KEY)
        subkey_name = f'''ks{instance_string}'''
        subkey = winreg.OpenKey(dropbox_key, subkey_name)
    except FileNotFoundError:
        TRACE('Keystore Migration: No registry key to migrate for instance %s', instance_id)
        return None

    TRACE("Keystore Migration: Migrating %s under instance '%s'", subkey_name, instance_id)
    for i in range(0, winreg.QueryInfoKey(subkey)[1]):
        (value_name, value_data, _) = winreg.EnumValue(subkey, i)
        value_data = value_data[:-1]
        if value_name[-_SUFFIX_LEN:] != UNENCRYPTED_KEY_NAME_SUFFIX:
            continue
        value_name = value_name[:-_SUFFIX_LEN]
        if not os.path.isdir(appdata_path):
            os.makedirs(appdata_path)
        appdata_file = f'''ks_{value_name}{instance_string}'''
        key_cache_path = os.path.join(appdata_path, appdata_file)
        TRACE('Keystore Migration: Migrating value %s\\%s: to %s)', subkey_name, value_name, key_cache_path)
        key_cache_file = open(key_cache_path, 'wb')
        key_cache_file.write(value_data)
        None(None, None)
    with None:
        if not None:
            pass
    continue
    winreg.CloseKey(subkey)
    winreg.CloseKey(dropbox_key)
    winreg.CloseKey(software_key)


def migrate_config_registry_to_appdata():
    
    try:
        migration_version_marker = _get_migration_version_file(config = True)
        migration_variant_marker = _get_migration_variant_file()
        (should_migrate, reason) = _should_migrate_keystore(migration_version_marker, migration_variant_marker)
        if should_migrate:
            TRACE('Keystore Migration: %s; migrating keystore for InstanceConfig again.', reason)
            _clear_previous_migration_files()
        else:
            TRACE('Keystore Migration: Migration for InstanceConfig already complete, skipping.')
            return True
        _migrate_registry_key_to_appdata(AppDataPaths.instance_config_path, None)
        version_marker = open(migration_version_marker, 'w', encoding = 'utf-8')
        version_marker.write(str(KEYSTORE_MIGRATION_VERSION))
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        variant_marker = open(migration_variant_marker, 'w', encoding = 'utf-8')
                        curr_variant = _get_migration_variant()
                        variant_marker.write(curr_variant)
                        
                        try:
                            None(None, None)
                        with None:
                            if not None:
                                
                                try:
                                    
                                    try:
                                        return True
                                    except PermissionError:
                                        return False
                                        TRACE('!! Keystore Migration: Migration for InstanceConfig failed')
                                        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.DATABASES)
                                        return False









def migrate_instances_registry_to_appdata(instances = None):
    
    try:
        migration_version_marker = _get_migration_version_file(config = False)
        migration_variant_marker = _get_migration_variant_file()
        (should_migrate, reason) = _should_migrate_keystore(migration_version_marker, migration_variant_marker)
        if should_migrate:
            TRACE('Keystore Migration: %s; migrating keystore for Dropbox instances again.', reason)
        else:
            TRACE('Keystore Migration: Migration for Dropbox instances already complete, skipping.')
            return True
        for appdata_path, instance_id in None:
            _migrate_registry_key_to_appdata(appdata_path, instance_id)
            version_marker = open(migration_version_marker, 'w', encoding = 'utf-8')
            version_marker.write(str(KEYSTORE_MIGRATION_VERSION))
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            variant_marker = open(migration_variant_marker, 'w', encoding = 'utf-8')
                            curr_variant = _get_migration_variant()
                            variant_marker.write(curr_variant)
                            
                            try:
                                None(None, None)
                            with None:
                                if not None:
                                    
                                    try:
                                        
                                        try:
                                            return True
                                        except PermissionError:
                                            return False
                                            TRACE('!! Keystore Migration: Migration for Dropbox instances failed')
                                            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.DATABASES)
                                            return False









def _remove_registry_keys():
    
    try:
        software_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software')
        dropbox_key = winreg.OpenKey(software_key, BUILD_KEY)
    except FileNotFoundError:
        TRACE('Keystore Migration: No registry keys to remove')
        return None

    next_idx = 0
    max_check = winreg.QueryInfoKey(dropbox_key)[0]
# WARNING: Decompyle incomplete


def remove_registry_keys(migration_successful = None):
    if not migration_successful:
        TRACE('Keystore Migration: Migration was unsuccessful, unable to remove registry keys')
        return None
    if is_full_msix():
        return None
    
    try:
        _remove_registry_keys()
        TRACE('KeyStore Migration: Registry cleanup successful')
        return None
    except PermissionError:
        TRACE('KeyStore Migration: Failed to remove registry keys due to permission errors')
        return None
        TRACE('KeyStore Migration: Failed to remove registry keys')
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.DATABASES)
        return None



class AppDataKeyStoreWin(KeyStoreBase):
    pass
# WARNING: Decompyle incomplete


class RegistryKeyStoreWin(KeyStoreBase):
    pass
# WARNING: Decompyle incomplete


class ComparisonKeyStore(KeyStoreBase):
    pass
# WARNING: Decompyle incomplete

