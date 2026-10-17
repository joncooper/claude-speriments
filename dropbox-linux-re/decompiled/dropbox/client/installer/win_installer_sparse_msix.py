# Source Generated with Decompyle++
# File: win_installer_sparse_msix.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from contextlib import contextmanager
from typing import Any, Dict, Iterator, Optional
from pynt.constants import KEY_ALL_ACCESS, KEY_QUERY_VALUE, KEY_SET_VALUE, KEY_WOW64_32KEY, REG_DWORD
from pynt.helpers.registry import delete_registry_value, read_registry_value, registry_key, safe_delete_regkey, safe_delete_regvalue, set_registry_value
from six.moves.winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE
from build_number import BUILD_KEY, dropbox_version, is_full_msix
from build_number.features import feature_enabled
from dropbox.client.constants.win import DROPBOX_UPDATER_CLIENTS_KEY
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import INSTALL_ACTION_EVENT, MSIX_SPARSE_REGISTRATION_CURRENT_USER_COMPLETE, MSIX_SPARSE_REGISTRATION_CURRENT_USER_FAILURE, MSIX_SPARSE_REGISTRATION_CURRENT_USER_SUCCESS
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.install_type import get_dropbox_install_type, InstallType
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.trace import TRACE
from dropbox.win32.internal import get_registry, RegistryWowFlag
from dropbox.win32.version import WIN10, WIN10_VERSION_2109, WIN11_VERSION_2109, WINDOWS_VERSION
from dropbox.win32.win_cache import DROPBOX_REG_KEY
if WINDOWS_VERSION.version_number() >= WIN10.version_number():
    import _bowbow
else:
    _bowbow = None
REGISTER_SPARSE_MSIX_REGISTRY_KEY = 'RegisterSparseMSIX'
INSTALL_FLAGS_REGISTRY_KEY = 'Software\\' + BUILD_KEY + '\\InstallFlags'
SPARSE_MSIX_POLICY_REGISTRY_KEY = 'Software\\Policies\\Microsoft\\Windows\\Appx'
SPARSE_MSIX_POLICY_HRESULT = 0x80073CFF
DISABLE_PROVISION_SPARSE_MSIX_STORMCROW_FLAG = 'desktop-disable-sparse-msix-provision'
DISABLE_PROVISION_SPARSE_MSIX_REGISTRY_KEY = 'DisableProvisionSparseMSIX'
DISABLE_PROVISION_SPARSE_MSIX_ENABLED_VALUE = 1
FULL_MSIX_REGISTRY_KEY = 'PackageFamilyName'
MSIX_ROLLBACK_ARG = '/msixrollback'

class RegisterSparseMSIXRegistryError(Exception):
    pass


def get_sparse_msix_policy_values():
    
    try:
        return {
            'sparse_msix_allow_all_trusted_apps': get_registry('AllowAllTrustedApps', None, hive = HKEY_LOCAL_MACHINE, wow_flag = RegistryWowFlag.KEY_WOW64_64KEY, key = SPARSE_MSIX_POLICY_REGISTRY_KEY),
            'sparse_msix_block_non_admin_user_install': get_registry('BlockNonAdminUserInstall', None, hive = HKEY_LOCAL_MACHINE, wow_flag = RegistryWowFlag.KEY_WOW64_64KEY, key = SPARSE_MSIX_POLICY_REGISTRY_KEY) }
    except Exception:
        return 



def is_full_msix_to_sparse_msix_rollback(per_machine = None):
    hive = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USER
    package_family_name = get_registry('PackageFamilyName', None, hive, RegistryWowFlag.KEY_WOW64_32KEY, key = DROPBOX_UPDATER_CLIENTS_KEY)
    return bool(package_family_name)


def create_sparse_msix_registry_key(per_machine = None):
    if not _is_sparse_msix_supported():
        return None
    if not None:
        return None
    _bowbow.create_install_flags_key()


def clean_sparse_msix_registry(per_machine = None):
    if not _is_sparse_msix_supported():
        return None
    perms = None | KEY_WOW64_32KEY
    if not per_machine:
        safe_delete_regvalue(HKEY_CURRENT_USER, DROPBOX_REG_KEY, REGISTER_SPARSE_MSIX_REGISTRY_KEY, permission = perms)
        return None
    safe_delete_regkey(HKEY_LOCAL_MACHINE, INSTALL_FLAGS_REGISTRY_KEY, permission = perms)


def should_register_sparse_msix():
