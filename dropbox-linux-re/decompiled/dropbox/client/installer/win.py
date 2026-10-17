# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

from __future__ import absolute_import, annotations
import abc
import ctypes
import errno
import filecmp
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from contextlib import contextmanager
from enum import Enum, IntEnum
from os.path import exists as _exists
from typing import Any, Iterator, List, Optional, Text, Tuple, TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import _win32typing
import psutil
import pywintypes
import win32api
import win32con
import win32event
import win32security
import winerror
from apex.util import process_architecture
from pynt.constants import KEY_ALL_ACCESS, KEY_READ, KEY_WOW64_32KEY, KEY_WOW64_64KEY, KEY_WRITE, REG_VALUE_TYPE, WOW64_ACCESS_TYPE
from pynt.helpers.registry import enum_registry_subkeys, enum_registry_values, registry_key, safe_delete_regvalue, safe_read_registry_value, set_registry_value
from six.moves.winreg import CreateKeyEx, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, REG_DWORD, REG_EXPAND_SZ, REG_SZ, SetValueEx
from win32com.shell import shellcon
from build_number import assert_full_msix_no_registry_writes, BRANCH, BUILD_KEY, dropbox_version, is_frozen, is_full_msix, VERSION
from build_number.constants import OFFICE_ADDIN_VERSION, WINDOWS_SHELL_EXT_VERSION
from build_number.features import feature_enabled
from lib.wininfinitedrivers.driver_installation import IncompatibleDriverArchitectureError, IncompatibleDriverSignatureError, InfiniteDriverInstaller, InsufficientDriverInstallationPrivilegesError, OmahaFailedToConnectError, OmahaInterfaceMismatchError
from dropbox.client.constants.win import DEFAULT_BINARY_PATH, DEFAULT_KILL_PROCESS_BY_NAME_TIMEOUT_MS, DROPBOX_UNINSTALL_KEY, DROPBOX_UPDATER_CLIENT_STATE_KEY, DROPBOX_UPDATER_CLIENTS_KEY, KillProcessByNameResult
from dropbox.client.features.desktop_client_url_scheme.win_registry_entries import desktop_client_url_scheme_registry_entries
from dropbox.client.file_activation.installer import install_file_type_associations, uninstall_file_type_associations
from dropbox.client.installer.errors import InstallerErrorCode, InstallerStrings
from dropbox.client.installer.install_event import InstallEventReporter
from dropbox.client.installer.install_work_item import InstallWorkItem, InstallWorkItemType, run_all_work_items
from dropbox.client.installer.win_installer_metadata import InstallerMetadata
from dropbox.client.installer.win_installer_restart import remove_installer_restart_flag, remove_installer_restart_stormcrow_flag
from dropbox.client.installer.win_installer_sparse_msix import clean_sparse_msix_registry, create_sparse_msix_registry_key, get_sparse_msix_policy_values, get_sparse_package_dir, is_full_msix_to_sparse_msix_rollback, is_sparse_msix_registered, is_sparse_msix_required, MSIX_ROLLBACK_ARG, register_sparse_package, should_disable_sparse_msix_provisioning, should_register_sparse_msix, SPARSE_MSIX_POLICY_HRESULT, unregister_sparse_package
from dropbox.client.installer.win_recovery import install_elevation_service, uninstall_elevation_service
from dropbox.client.photodownloader.win.installer import install_photo_uploader_per_machine_or_user, is_photo_uploader_installed_per_machine_or_user, uninstall_photo_uploader_per_machine_or_user
from dropbox.client.shortcut.windows import remove_all_start_menu_shortcuts, setup_shortcuts
from dropbox.client.startup.win import restart_explorer
from dropbox.client.url_schemes.client_url_scheme_handler import DesktopClientURLSchemeHandler
from dropbox.client.util import hard_exit
from dropbox.client.util.win import get_executable_dir, get_omaha_user_id, kill_process_by_name
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import report
from dropbox.event_names import CENTENNIAL_GET_PACKAGE_NAME_FAILURE, CENTENNIAL_OUT_OF_STORE_APP_EXISTS_DURING_STORE_APP_INSTALL, CLEANUP_PREVIOUS_INSTALLS_FAILURE, CLEANUP_PREVIOUS_INSTALLS_SUCCESS, ELEVATION_SERVICE_INSTALL_TIMEOUT, ELEVATION_SERVICE_UNINSTALL_TIMEOUT, INSTALL_ACTION_EVENT, INSTALL_ATTEMPT, INSTALL_FAILURE, INSTALL_FILES, INSTALL_SUCCESS, MSIX_SPARSE_REGISTRATION_FAILURE, MSIX_SPARSE_REGISTRATION_SUCCESS, MSIX_SPARSE_ROLLBACK_DETECTED, MSIX_SPARSE_ROLLBACK_FAILURE, MSIX_SPARSE_ROLLBACK_SUCCESS, MSIX_SPARSE_UNREGISTRATION_FAILURE, MSIX_SPARSE_UNREGISTRATION_SUCCESS, OEM_UNINSTALL_APP_ATTEMPT, OEM_UNINSTALL_APP_FAILURE, OEM_UNINSTALL_APP_SUCCESS, SYS_REDIRECT_DISABLE_ATTEMPT, SYS_REDIRECT_DISABLE_FAILURE, SYS_REDIRECT_DISABLE_RECOVER_ATTEMPT, SYS_REDIRECT_DISABLE_RECOVER_FAILURE, SYS_REDIRECT_DISABLE_RECOVER_NOOP, SYS_REDIRECT_DISABLE_RECOVER_SUCCESS, SYS_REDIRECT_DISABLE_SUCCESS, UNIVERSAL_UNINSTALL_APP_NOT_FOUND, UNIVERSAL_UNINSTALL_CHECK, UNIVERSAL_UNINSTALL_FAIL, UNIVERSAL_UNINSTALL_INVALID, UNIVERSAL_UNINSTALL_SUCCESS, UNIVERSAL_UNINSTALL_VALID
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_remove
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.util import report_infinite_event
from dropbox.install_type import get_dropbox_install_type, InstallType
from dropbox.install_type.win import DROPBOX_CLIENT_INSTALL_KEY, DROPBOX_ROOT_KEY, WINDOWS_CLASSES_KEY
from dropbox.trace import TRACE
from dropbox.win32.internal import get_registry, get_user_folder_path, is_admin, RegistryWowFlag
from dropbox.win32.version import get_app_version, WIN10, WINDOWS_VERSION
if WINDOWS_VERSION.version_number() >= WIN10.version_number():
    import _bowbow
else:
    _bowbow = None

def _winerror_repr(e = None):
    return f'''{hex(e.winerror & 0xFFFFFFFF)}: {e.strerror}'''

CREATE_NO_WINDOW = 134217728
FIRST_SHELL_EXT_CLASS_GUID = '{FB314ED9-A251-47B7-93E1-CDD82E34AF8B}'
FIRST_SHELL_EXT_CLASS_REG_KEY = f'''{WINDOWS_CLASSES_KEY!s}\\CLSID\\{FIRST_SHELL_EXT_CLASS_GUID!s}\\InProcServer32'''
SHELL_TOAST_ACTIVATION_CLASS_GUID = '{E7A37920-253C-4FF1-B169-298A7CE6CAA9}'
APP_RUNNING_ARG = '/appwasrunning'
NO_APP_RUNNING_ARG = '/noappwasrunning'
USER_INITIATED_KILL_PROCESS_TIMEOUT_MS = 30000

class InstallerDataDistribution(TypedDict):
    msi: 'bool' = 'InstallerDataDistribution'


class InstallerData(TypedDict):
    distribution: 'InstallerDataDistribution' = 'InstallerData'


class InstallerResult(IntEnum):
    SUCCESS = 0
    FAILED_CUSTOM_ERROR = 1


def _pop_arg(argv, key):
    value = None
    for i, arg in enumerate(argv):
        if arg.startswith(key):
            value = arg[len(key):]
            del argv[i]
        
        return value


def _get_current_path(argv):
    if hasattr(sys, 'frozen'):
        return get_executable_dir()
    dev_executable_dir = _pop_arg(argv, '/ExecutableDir:')
# WARNING: Decompyle incomplete


def _file_equal(file1 = None, file2 = None):
    if not _exists(file1) or _exists(file2):
        return False
    
    try:
        return filecmp.cmp(file1, file2, shallow = False)
    except Exception:
        report_exception(component = DesktopComponent.INSTALLER)
        return False



class TreeWalk(object):
    
    def __init__(self = None, root_dir = None):
        self.root_dir = root_dir

    handle_dir = (lambda self = None, rel_path = None: True)()
    
    def handle_dir_post_walk(self = None, rel_path = None):
        pass

    handle_file = (lambda self = None, rel_path = None: pass)()
    
    def walk(self = None, rel_path = None):
        current_dir = os.path.join(self.root_dir, rel_path)
        if not _exists(current_dir):
            return None
        names = os.listdir(current_dir)
        for name in names:
            child_rel_path = os.path.join(rel_path, name) if rel_path else name
            child_path = os.path.join(self.root_dir, child_rel_path)
            if os.path.isdir(child_path):
                if self.handle_dir(child_rel_path):
                    self.walk(child_rel_path)
                    self.handle_dir_post_walk(child_rel_path)
                continue
            self.handle_file(child_rel_path)
            return None



class BackUpInstallDir(TreeWalk):
    pass
# WARNING: Decompyle incomplete


class CopyBinaries(TreeWalk):
    pass
# WARNING: Decompyle incomplete


class RecoverOldBinaries(TreeWalk):
    pass
# WARNING: Decompyle incomplete


class CleanUpFiles(TreeWalk):
    pass
# WARNING: Decompyle incomplete


class ValidateFilesFileNotFoundError(Exception):
    pass


class ValidateFiles(TreeWalk):
    pass
# WARNING: Decompyle incomplete

_INSTALL_MARKER_NAME = 'INSTALL_MARKER'
_OLD_BINARIES_DIR_NAME = 'OldBinaries'

def _create_install_marker(install_dir = None):
    
    try:
        marker = open(os.path.join(install_dir, _INSTALL_MARKER_NAME), 'w')
        marker.close()
        return None
    except OSError:
        TRACE('Could not create install marker in %s', install_dir)
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.INSTALLER)
        return None



def _remove_install_marker(install_dir = None):
    
    try:
        os.remove(os.path.join(install_dir, _INSTALL_MARKER_NAME))
        return None
    except OSError:
        e = None
        if e.errno == errno.ENOENT:
            TRACE("Could not remove install marker in %s because it doesn't exist", install_dir)
        else:
            TRACE('Could not remove install marker in %s', install_dir)
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.INSTALLER)
        e = None
        del e
        return None
        e = None
        del e



def _test_mock_point(name = None):
    pass


class AtomicInstallType(Enum):
    NORMAL = 'NORMAL'
    CLEAN = 'CLEAN'
    REPAIR = 'REPAIR'


def _should_clean_install(dest_dir = None):
    folders_to_check = [
        'QtGraphicalEffects',
        'QtQuick',
        'QtQuick.2']
    for folder in folders_to_check:
        if not _exists(os.path.join(dest_dir, folder)):
            continue
        for root, _, filenames in os.walk(os.path.join(dest_dir, folder)):
            if filenames:
                TRACE('Encountered unexpected file, going to do a clean install: %s', os.path.join(root, filenames[0]))
                return True
            return False


def _get_installed_dropbox_version(dest_dir = None):
    dest_dropbox = os.path.join(dest_dir, '{}.exe'.format(BUILD_KEY))
    installed_version = None
    if _exists(dest_dropbox):
        
        try:
            installed_version = get_app_version(dest_dropbox)
        except pywintypes.error:
            TRACE('Failed to read old version, assuming that this is not a repair')
            report_exception(severity = Severity.TRACE, component = DesktopComponent.INSTALLER)

        return installed_version


def _atomically_install_files(reporter, source_dir, dest_dir = None, temp_dir = None, installed_version = None, installer_metadata = ('reporter', 'InstallEventReporter', 'source_dir', 'str', 'dest_dir', 'str', 'temp_dir', 'str', 'installed_version', 'Optional[str]', 'installer_metadata', 'InstallerMetadata', 'return', 'None')):
    os.makedirs(dest_dir, exist_ok = True)
    if _should_clean_install(dest_dir):
        install_type = AtomicInstallType.CLEAN
    elif installed_version == VERSION:
        install_type = AtomicInstallType.REPAIR
    else:
        install_type = AtomicInstallType.NORMAL
    versioned_dir_white_list = [
        'DropboxOfficeAddIn.%s.dll' % OFFICE_ADDIN_VERSION,
        'DropboxOfficeAddIn64.%s.dll' % OFFICE_ADDIN_VERSION] if install_type == AtomicInstallType.REPAIR else []
    white_list = [
        'Dropbox.exe.log',
        'DropboxOfficeAddIn.%s.dll' % OFFICE_ADDIN_VERSION,
        'DropboxOfficeAddIn64.%s.dll' % OFFICE_ADDIN_VERSION,
        'DropboxExt.%s.0.dll' % WINDOWS_SHELL_EXT_VERSION,
        'DropboxExt64.%s.0.dll' % WINDOWS_SHELL_EXT_VERSION,
        'DropboxExt64a.%s.0.dll' % WINDOWS_SHELL_EXT_VERSION]
    src_versioned_dir = os.path.join(source_dir, VERSION)
    dest_versioned_dir = os.path.join(dest_dir, VERSION)
    
    try:
        TRACE('Writing installer metadata to versioned source_dir for atomic install')
        installer_metadata.write_file(src_versioned_dir)
    except Exception:
        TRACE('Failed to write installer metadata to versioned source_dir for atomic install')
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.INSTALLER)
        raise 

    
    try:
        if install_type == AtomicInstallType.CLEAN:
            _create_install_marker(dest_dir)
            BackUpInstallDir(dest_dir, source_dir, temp_dir, white_list, ignore_list = [
                _INSTALL_MARKER_NAME]).walk()
            _remove_install_marker(dest_dir)
            _test_mock_point('dest_dir_cleaned')
        os.makedirs(dest_versioned_dir, exist_ok = True)
        CopyBinaries(install_dir = dest_versioned_dir, setup_dir = src_versioned_dir, white_list = versioned_dir_white_list, ignore_list = [], ignore_if_equal = install_type == AtomicInstallType.REPAIR).walk()
        _test_mock_point('versioned_directory_installed')
        package_source_dir = get_sparse_package_dir(source_dir)
        package_dest_dir = get_sparse_package_dir(dest_dir)
        os.makedirs(package_dest_dir, exist_ok = True)
        CopyBinaries(install_dir = package_dest_dir, setup_dir = package_source_dir, white_list = white_list, ignore_list = []).walk()
        expected_shell_extensions = [
            'DropboxExt.%s.0.dll' % WINDOWS_SHELL_EXT_VERSION]
        if process_architecture() == 'arm64':
            expected_shell_extensions.append('DropboxExt64a.%s.0.dll' % WINDOWS_SHELL_EXT_VERSION)
        else:
            expected_shell_extensions.append('DropboxExt64.%s.0.dll' % WINDOWS_SHELL_EXT_VERSION)
        for dropboxext in expected_shell_extensions:
            shutil.copy2(os.path.join(source_dir, dropboxext), os.path.join(dest_dir, dropboxext))
            
            try:
                continue
                except Exception:
                    TRACE('Could not copy dropbox extension: %s', dropboxext)
                    if not _exists(os.path.join(dest_dir, dropboxext)):
                        raise 
                    TRACE('Continuing because the dropbox ext already exists in the install directory.')
                    
                    try:
                        continue
                        
                        try:
                            install_work_items = [
                                InstallWorkItem(InstallWorkItemType.COPY, source_dir = source_dir, source_name = 'Dropbox.VisualElementsManifest.xml', dest_dir = dest_dir, temp_dir = temp_dir),
                                InstallWorkItem(InstallWorkItemType.COPY, source_dir = source_dir, source_name = 'resources.pri', dest_dir = dest_dir, temp_dir = temp_dir),
                                InstallWorkItem(InstallWorkItemType.COPY, source_dir = source_dir, source_name = f'''{BUILD_KEY}Uninstaller.exe''', dest_dir = dest_dir, temp_dir = temp_dir)]
                            if feature_enabled('dropboxctl'):
                                install_work_items.append(InstallWorkItem(InstallWorkItemType.COPY, source_dir = source_dir, source_name = f'''{BUILD_KEY.lower()}ctl.exe''', dest_dir = dest_dir, temp_dir = temp_dir))
                            install_work_items.extend([
                                InstallWorkItem(InstallWorkItemType.MOVE_IF_SOURCE_EXISTS, source_dir = dest_dir, source_name = 'qt.conf', dest_dir = dest_dir, dest_name = 'oldqt.conf'),
                                InstallWorkItem(InstallWorkItemType.COPY, source_dir = source_dir, source_name = '{}.exe'.format(BUILD_KEY), dest_dir = dest_dir, temp_dir = temp_dir, callback = (lambda : _test_mock_point('install_successful')))])
                            run_all_work_items(install_work_items)
                        except Exception:
                            TRACE('Failed to install, re-raising')
                            if install_type == AtomicInstallType.CLEAN:
                                _create_install_marker(dest_dir)
                                TRACE('Non-atomically recovering old files because this was a clean install')
                                recover = RecoverOldBinaries(dest_dir, temp_dir, ignore_list = [
                                    _INSTALL_MARKER_NAME])
                                recover.walk()
                                if not recover.failed:
                                    TRACE('Recovered all old files successfully, removing install marker')
                                    _remove_install_marker(dest_dir)
                                elif install_type == AtomicInstallType.NORMAL:
                                    TRACE('Removing installed version directory because this was a normal atomic install.')
                                    shutil.rmtree(dest_versioned_dir, ignore_errors = True)
                            raise 

                        timed_reporter = reporter.with_timer()
                        
                        try:
                            old_dropbox = os.path.join(dest_dir, 'old{}.exe'.format(BUILD_KEY))
                            if _exists(old_dropbox):
                                os.remove(old_dropbox)
                            CleanUpFiles(dest_dir, source_dir, ignore_list = [
                                VERSION,
                                'Dropbox.exe.log']).walk()
                        except Exception:
                            TRACE('Could not clean up left over install files, continuing')
                            timed_reporter.report(INSTALL_ACTION_EVENT, action = 'installer_could_not_remove_old_install_files')

                        if dropbox_version.is_internal_alpha():
                            ValidateFiles(dest_dir, source_dir, ignore_list = []).walk()
                            return None
                        return None





def _cleanup_previous_installs(dest_dir = None, installed_version = None):
    old_dropbox_path = os.path.join(dest_dir, 'old{}.exe'.format(BUILD_KEY))
    old_dropbox_exists = _exists(old_dropbox_path)
    if old_dropbox_exists:
        
        try:
            _test_mock_point('remove_old_dropbox')
            os.remove(old_dropbox_path)
            old_dropbox_exists = False
        except OSError:
            TRACE('Could not remove old dropbox')
            report_exception(severity = Severity.TRACE, component = DesktopComponent.INSTALLER)

        should_clean_old_version_dirs = False
        if not old_dropbox_exists:
            if installed_version:
                should_clean_old_version_dirs = True
            else:
                dropbox_exe_exists = _exists(os.path.join(dest_dir, '{}.exe'.format(BUILD_KEY)))
                should_clean_old_version_dirs = not dropbox_exe_exists
    if should_clean_old_version_dirs:
        for entry in os.listdir(dest_dir):
            m = re.match('\\d+\\.\\d+\\.\\d+', entry)
            if not m:
                continue
            if entry in (VERSION, installed_version):
                continue
            versioned_dir_path = os.path.join(dest_dir, entry)
            if not os.path.isdir(versioned_dir_path):
                continue
            shutil.rmtree(versioned_dir_path, ignore_errors = True)
            old_binaries_dir = _get_old_binaries_folder(dest_dir)
            if _exists(old_binaries_dir):
                failed_to_remove_dropbox_exe = False
                for root, _, filenames in os.walk(old_binaries_dir):
                    for filename in filenames:
                        if not filename.lower().endswith('{}.exe'.format(BUILD_KEY).lower()):
                            continue
                        _test_mock_point('remove_dropbox_in_old_binaries')
                        os.remove(os.path.join(root, filename))
                        except OSError:
                            failed_to_remove_dropbox_exe = True
                            TRACE('Could not remove dropbox in OldBinaries: %r', filename)
                            report_exception(severity = Severity.TRACE, component = DesktopComponent.INSTALLER)
                            continue
                        if not failed_to_remove_dropbox_exe:
                            shutil.rmtree(old_binaries_dir, ignore_errors = True)
                            return None
                        return None
                        return None


def _copy_binaries(reporter = None, source_dir = None, dest_dir = None, installer_metadata = ('reporter', 'InstallEventReporter', 'source_dir', 'Text', 'dest_dir', 'Text', 'installer_metadata', 'InstallerMetadata', 'return', 'None')):
    TRACE('Copying binaries from %r to %r', source_dir, dest_dir)
    timed_reporter = reporter.with_timer()
    installed_version = _get_installed_dropbox_version(dest_dir)
    
    try:
        _cleanup_previous_installs(dest_dir, installed_version)
        timed_reporter.report(INSTALL_ACTION_EVENT, action = CLEANUP_PREVIOUS_INSTALLS_SUCCESS)
    except Exception:
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.INSTALLER)
        timed_reporter.report(INSTALL_ACTION_EVENT, action = CLEANUP_PREVIOUS_INSTALLS_FAILURE)
        if dropbox_version.is_internal_alpha():
            raise 

    timed_reporter = reporter.with_timer()
    temp_folder = old_binaries_temp_folder(dest_dir)
    _atomically_install_files(reporter, source_dir, dest_dir, temp_folder, installed_version, installer_metadata)
    timed_reporter.report(INSTALL_ACTION_EVENT, action = INSTALL_FILES)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _get_old_binaries_folder(dest_dir = None):
    parent_folder = os.path.dirname(dest_dir)
    return os.path.join(parent_folder, _OLD_BINARIES_DIR_NAME)

old_binaries_temp_folder = (lambda dest_dir = None: pass# WARNING: Decompyle incomplete
)()

def _delete_install_folder(inst_dir = None):
    inst_dir = os.path.normpath(inst_dir)
    if not inst_dir.endswith('%s\\bin' % BUILD_KEY) and inst_dir.endswith('%s\\Client' % BUILD_KEY):
        TRACE('Unexpected binary path %s', inst_dir)
        uninstaller_path = os.path.join(inst_dir, '%sUninstaller.exe' % BUILD_KEY)
        
        try:
            os.remove(uninstaller_path)
        except FileNotFoundError:
            pass
        except Exception:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.INSTALLER)

        return None
    old_dropbox_exe = os.path.join(inst_dir, 'old{}.exe'.format(BUILD_KEY))
    dropbox_exe = os.path.join(inst_dir, '{}.exe'.format(BUILD_KEY))
    
    try:
        os.remove(old_dropbox_exe)
        
        try:
            pass
        except FileNotFoundError:
            
            try:
                pass
            try:
                
                try:
                    os.remove(dropbox_exe)
                    
                    try:
                        pass
                    except FileNotFoundError:
                        
                        try:
                            pass
                        try:
                            shutil.rmtree(inst_dir, ignore_errors = True)
                            return None
                        except Exception:
                            report_exception(severity = Severity.TRACE, component = DesktopComponent.INSTALLER)
                            return None







RegistryEntry = Tuple[(Text, Optional[Text], REG_VALUE_TYPE, WOW64_ACCESS_TYPE, Any)]

def get_uninstall_registry_entries(per_machine = None, is_enterprise = None, inst_dir = None):
    install_type = 'MACHINE' if per_machine else 'USER'
    uninstaller_path = os.path.join(inst_dir, f'''{BUILD_KEY}Uninstaller.exe''')
    if is_enterprise:
        uninstaller_args = f'''/InstallType:{install_type} /S'''
    else:
        uninstaller_args = f'''/InstallType:{install_type}'''
    entries = [
        (DROPBOX_ROOT_KEY, 'InstallPath', REG_SZ, KEY_WOW64_32KEY, inst_dir),
        (DROPBOX_UPDATER_CLIENT_STATE_KEY, 'UninstallString', REG_EXPAND_SZ, KEY_WOW64_32KEY, uninstaller_path),
        (DROPBOX_UPDATER_CLIENT_STATE_KEY, 'UninstallArguments', REG_SZ, KEY_WOW64_32KEY, uninstaller_args)]
    if is_enterprise:
        entries.append((DROPBOX_UPDATER_CLIENT_STATE_KEY, 'msi', REG_DWORD, KEY_WOW64_32KEY, 1))
        return entries
    uninstall_string = f'''{uninstaller_path}" {uninstaller_args}'''
    exe_path = os.path.join(inst_dir, f'''{BUILD_KEY}.exe''') if inst_dir else ''
    entries += [
        (DROPBOX_UNINSTALL_KEY, 'UninstallString', REG_EXPAND_SZ, KEY_WOW64_32KEY, uninstall_string),
        (DROPBOX_UNINSTALL_KEY, 'InstallLocation', REG_EXPAND_SZ, KEY_WOW64_32KEY, Text(inst_dir)),
        (DROPBOX_UNINSTALL_KEY, 'DisplayName', REG_SZ, KEY_WOW64_32KEY, BUILD_KEY),
        (DROPBOX_UNINSTALL_KEY, 'UninstallPath', REG_EXPAND_SZ, KEY_WOW64_32KEY, uninstaller_path),
        (DROPBOX_UNINSTALL_KEY, 'Publisher', REG_SZ, KEY_WOW64_32KEY, 'Dropbox, Inc.'),
        (DROPBOX_UNINSTALL_KEY, 'VersionMajor', REG_DWORD, KEY_WOW64_32KEY, BRANCH[0]),
        (DROPBOX_UNINSTALL_KEY, 'VersionMinor', REG_DWORD, KEY_WOW64_32KEY, BRANCH[1]),
        (DROPBOX_UNINSTALL_KEY, 'DisplayIcon', REG_SZ, KEY_WOW64_32KEY, f'''{exe_path},0'''),
        (DROPBOX_UNINSTALL_KEY, 'DisplayVersion', REG_SZ, KEY_WOW64_32KEY, Text(VERSION)),
        (DROPBOX_UNINSTALL_KEY, 'URLInfoAbout', REG_SZ, KEY_WOW64_32KEY, 'https://www.dropbox.com'),
        (DROPBOX_UNINSTALL_KEY, 'HelpLink', REG_SZ, KEY_WOW64_32KEY, 'https://www.dropbox.com'),
        (DROPBOX_UNINSTALL_KEY, 'NoModify', REG_DWORD, KEY_WOW64_32KEY, 1),
        (DROPBOX_UNINSTALL_KEY, 'NoRepair', REG_DWORD, KEY_WOW64_32KEY, 1)]
    return entries


def get_updater_registration_entries(launch_cmd = None):
    return [
        (DROPBOX_UPDATER_CLIENTS_KEY, 'name', REG_SZ, KEY_WOW64_32KEY, BUILD_KEY),
        (DROPBOX_UPDATER_CLIENTS_KEY, 'pv', REG_SZ, KEY_WOW64_32KEY, VERSION),
        (DROPBOX_UPDATER_CLIENT_STATE_KEY, 'InstallerResult', REG_DWORD, KEY_WOW64_32KEY, InstallerResult.SUCCESS),
        (DROPBOX_UPDATER_CLIENT_STATE_KEY, 'InstallerError', REG_DWORD, KEY_WOW64_32KEY, 0),
        (DROPBOX_UPDATER_CLIENT_STATE_KEY, 'InstallerSuccessLaunchCmdLine', REG_SZ, KEY_WOW64_32KEY, launch_cmd),
        (DROPBOX_UPDATER_CLIENT_STATE_KEY, 'usagestats', REG_DWORD, KEY_WOW64_32KEY, 1)]


def get_dropbox_entries(per_machine = None, inst_dir = None):
    exe_path = os.path.join(inst_dir, f'''{BUILD_KEY}.exe''') if inst_dir else ''
    clsid_toast_activator = 'Software\\Classes\\CLSID\\' + SHELL_TOAST_ACTIVATION_CLASS_GUID
    entries = [
        (DROPBOX_CLIENT_INSTALL_KEY, 'Version', REG_SZ, KEY_WOW64_32KEY, VERSION),
        (clsid_toast_activator + '\\LocalServer32', None, REG_SZ, KEY_WOW64_32KEY, exe_path)]
    if per_machine:
        entries.append(('Software\\Microsoft\\Windows\\CurrentVersion\\Run', Text(BUILD_KEY), REG_SZ, KEY_WOW64_32KEY, '"%s" /systemstartup' % exe_path))
    return entries


def get_msi_registry_entries(product_code = None):
    packed_product_code = pack_enterprise_product_code(product_code)
    entries = []
    wow64_accesses = (KEY_WOW64_32KEY, KEY_WOW64_64KEY)
    for wow64_access in wow64_accesses:
        entries.append((f'''Software\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products\\{packed_product_code}\\InstallProperties''', 'DisplayVersion', REG_SZ, wow64_access, VERSION))
        entries.append((f'''Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{product_code}''', 'DisplayVersion', REG_SZ, wow64_access, VERSION))
        return entries


def _get_registry_entries(per_machine = None, is_enterprise = None, inst_dir = None, launch_cmd = (True,), include_updater_entries = ('per_machine', 'bool', 'is_enterprise', 'bool', 'inst_dir', 'Text', 'launch_cmd', 'Optional[Text]', 'include_updater_entries', 'bool', 'return', 'List[RegistryEntry]')):
    entries = get_dropbox_entries(per_machine, inst_dir)
    if include_updater_entries:
        entries += get_updater_registration_entries(launch_cmd)
    entries += get_uninstall_registry_entries(per_machine, is_enterprise, inst_dir)
    return entries


def _set_reg_entries(per_machine = None, entries = None):
    hkey = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USER
# WARNING: Decompyle incomplete


def _is_omaha4(argv = None):
    is_omaha4 = '/Omaha4' in argv
    TRACE('Is Omaha 4 install?: %r', is_omaha4)
    return is_omaha4


def _is_per_machine(argv = None):
    install_type = _pop_arg(argv, '/InstallType:')
    TRACE('Install type: %r', install_type)
# WARNING: Decompyle incomplete


def _get_channel_id(argv = None):
    channel_id = _pop_arg(argv, '/ChannelId:')
    TRACE('Channel id: %r', channel_id)
    if not channel_id:
        return None
    if None == 'internal-alpha':
        return 'internal_alpha'


def _is_auto_update(argv = None):
    is_auto_update = _pop_arg(argv, '/IsAutoUpdate:')
    TRACE('IsAutoUpdate: %r', is_auto_update)
    return is_auto_update == 'YES'


def pop_installer_data(argv = None):
    installer_data_path = _pop_arg(argv, '/InstallerData:')
    if not installer_data_path:
        TRACE('No installer data found')
        return {
            'distribution': {
                'msi': False } }
    
    try:
        file = open(installer_data_path, 'r', encoding = 'utf-8-sig')
        installer_data = json.load(file)
        TRACE('Installer data found: %s', installer_data)
        
        try:
            None(None, None)
            return 
            with None:
                if not None, installer_data:
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            TRACE('Failed to load installer data: %s (%r)', installer_data_path, ex)
                            del ex
                            return None
                            None = 
                            del ex






def _should_kill_all_processes(argv = None):
    kill_all_processes = _pop_arg(argv, '/KillEveryone:')
# WARNING: Decompyle incomplete


def is_per_user_windows_install(argv = None):
    return not _is_per_machine(argv)


def _get_install_dir(argv = None):
    inst_dir = _pop_arg(argv, '/InstallDir:')
    TRACE('Install dir: %r', inst_dir)
# WARNING: Decompyle incomplete


def _get_contents_root(install_dir = None):
    return os.path.join(install_dir, VERSION)


def _kill_other_instances(kill_others_users_process = None, force_kill = None, user_initiated = None):
    TRACE("Going to kill all Dropbox processes; kill other users's Dropbox: %r", kill_others_users_process)
    timeout = USER_INITIATED_KILL_PROCESS_TIMEOUT_MS if user_initiated else DEFAULT_KILL_PROCESS_BY_NAME_TIMEOUT_MS
    ret = kill_process_by_name('%s.exe' % BUILD_KEY, other_users = kill_others_users_process, send_signal = True, force_kill = force_kill, timeout = timeout)
    return ret


def _check_kill_all_dropbox_processes(should_kill_all_processes = None, per_machine = None, force_kill = None, user_initiated = ('should_kill_all_processes', 'bool', 'per_machine', 'bool', 'force_kill', 'bool', 'user_initiated', 'bool', 'return', 'KillProcessByNameResult')):
    if should_kill_all_processes:
        return _kill_other_instances(per_machine, force_kill = force_kill, user_initiated = user_initiated)
    return KillProcessByNameResult(False, 0)

_remove_firewall_exception = (lambda binary_dir = None, use_rule_name_only = None: TRACE('Remove firewall rule: %r with path: %r', BUILD_KEY, binary_dir)netsh_exe_unicode = os.path.join(get_user_folder_path(shellcon.CSIDL_SYSTEM), 'netsh.exe')program_arg_unicode = 'program=%s' % os.path.join(binary_dir, '%s.exe' % BUILD_KEY)netsh_exe = netsh_exe_unicodeprogram_arg = program_arg_unicodeproc_args = [
netsh_exe,
'advfirewall',
'firewall',
'delete',
'rule',
'name=%s' % BUILD_KEY]if not use_rule_name_only:
proc_args.append(program_arg)proc = subprocess.Popen(proc_args, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, creationflags = CREATE_NO_WINDOW)(stdout, stderr) = proc.communicate()TRACE('Firewall exception request stdout:\n%r', stdout)TRACE('Firewall exception request stderr:\n%r', stderr)if proc.returncode != 0 or proc.returncode != 1:
report_bad_assumption('Unable to delete the firewall exception rule')NoneNone)()
_add_firewall_exception = (lambda inst_dir = None: TRACE('Add %s\\%s.exe into firewall exception list', inst_dir, BUILD_KEY)netsh_exe_unicode = os.path.join(get_user_folder_path(shellcon.CSIDL_SYSTEM), 'netsh.exe')program_path_unicode = 'program=%s' % os.path.join(inst_dir, '%s.exe' % BUILD_KEY)netsh_exe = netsh_exe_unicodeprogram_path = program_path_unicodefor protocol, port_range in (('tcp', '17500-17510'), ('udp', '17500')):
proc_args = [
netsh_exe,
'advfirewall',
'firewall',
'add',
'rule',
'name=%s' % BUILD_KEY,
'dir=in',
'action=allow',
program_path,
'enable=yes',
'profile=Any',
f'''protocol={protocol}''',
f'''localport={port_range}''']proc = subprocess.Popen(proc_args, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, creationflags = CREATE_NO_WINDOW)(stdout, stderr) = proc.communicate()TRACE('Firewall exception request stdout:\n%r', stdout)TRACE('Firewall exception request stderr:\n%r', stderr)if proc.returncode != 0:
TRACE('!! Unable to add the firewall exception rule')None)()

def _compose_launch_cmd(inst_dir, need_restart_explorer = None, is_update = None, is_auto_update = None, dropbox_process_killed = (False, False, False, False, False), is_msix_rollback = ('inst_dir', 'Text', 'need_restart_explorer', 'bool', 'is_update', 'bool', 'is_auto_update', 'bool', 'dropbox_process_killed', 'bool', 'is_msix_rollback', 'bool', 'return', 'Text')):
    launch_args = [
        '"%s"' % os.path.join(inst_dir, '%s.exe' % BUILD_KEY)]
    if is_auto_update:
        launch_args.append('/firstrunupdate')
    elif is_update:
        launch_args.append('/firstrunupdatemanual')
    else:
        launch_args.append('/firstrun')
    if need_restart_explorer:
        launch_args.append('1')
    else:
        launch_args.append('0')
    if dropbox_process_killed:
        launch_args.append(APP_RUNNING_ARG)
    else:
        launch_args.append(NO_APP_RUNNING_ARG)
    if is_msix_rollback:
        launch_args.append(MSIX_ROLLBACK_ARG)
    return ' '.join(launch_args)


def _dropbox_exists(inst_dir = None):
    exe_path = os.path.join(inst_dir, '%s.exe' % BUILD_KEY)
    return _exists(exe_path)


def is_enterprise_managed(per_machine = None, installer_data = None):
    if not per_machine:
        return False
# WARNING: Decompyle incomplete


def get_enterprise_product_code(per_machine = None):
    if not per_machine:
        return None
    
    try:
        key = registry_key(HKEY_LOCAL_MACHINE, DROPBOX_UPDATER_CLIENT_STATE_KEY, permission = KEY_READ | KEY_WOW64_32KEY)
        if key:
            for name in enum_registry_values(key):
                if name.startswith('EnterpriseProduct'):
                    
                    
                    try:
                        None(None, None)
                        return 
                        continue
                        
                        try:
                            None(None, None)
                        with None:
                            if not None, None, name[len('EnterpriseProduct'):]:
                                
                                try:
                                    
                                    try:
                                        pass
                                    except Exception:
                                        report_exception(severity = Severity.WARN, component = DesktopComponent.INSTALLER)

                                    return None






def pack_enterprise_product_code(product_code = None):
    parts = [
        product_code[1:9],
        product_code[10:14],
        product_code[15:19],
        product_code[20:22],
        product_code[22:24],
        product_code[25:27],
        product_code[27:29],
        product_code[29:31],
        product_code[31:33],
        product_code[33:35],
        product_code[35:37]]
    packed = ''
    for part in parts:
        packed += part[::-1]
        return packed.upper()


class DisableFileSystemRedirection:
    _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
    _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
    
    def __init__(self = None, reporter = None):
        self._reporter = reporter

    
    def __enter__(self = None):
        timed_reporter = self._reporter.with_timer()
        
        try:
            self._reporter.report(INSTALL_ACTION_EVENT, action = SYS_REDIRECT_DISABLE_ATTEMPT)
            self.old_value = ctypes.c_long()
            self.success = self._disable(ctypes.byref(self.old_value))
            report_action = SYS_REDIRECT_DISABLE_SUCCESS if self.success else SYS_REDIRECT_DISABLE_FAILURE
            timed_reporter.report(INSTALL_ACTION_EVENT, action = report_action)
            return None
        except Exception:
            timed_reporter.report(INSTALL_ACTION_EVENT, action = SYS_REDIRECT_DISABLE_FAILURE)
            TRACE('Disabling Windows system redirect failed')
            report_exception(severity = Severity.DEBUG, component = DesktopComponent.INSTALLER)
            return None


    
    def __exit__(self = None, ignored = None, value = None, traceback = ('ignored', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        timed_reporter = self._reporter.with_timer()
        
        try:
            self._reporter.report(INSTALL_ACTION_EVENT, action = SYS_REDIRECT_DISABLE_RECOVER_ATTEMPT)
            if self.success:
                revert_success = self._revert(self.old_value)
                report_action = SYS_REDIRECT_DISABLE_RECOVER_SUCCESS if revert_success else SYS_REDIRECT_DISABLE_RECOVER_FAILURE
                timed_reporter.report(INSTALL_ACTION_EVENT, action = report_action)
                return None
            None.report(INSTALL_ACTION_EVENT, action = SYS_REDIRECT_DISABLE_RECOVER_NOOP)
            return None
        except Exception:
            timed_reporter.report(INSTALL_ACTION_EVENT, action = SYS_REDIRECT_DISABLE_RECOVER_FAILURE)
            TRACE("Reverting 'Windows system redirect disable' failed")
            report_exception(severity = Severity.DEBUG, component = DesktopComponent.INSTALLER)
            return None




def _uninstall_dropbox_universal(reporter = None):
    TRACE('[Dropbox Universal] unintall dropbox universal started.')
    timed_reporter = reporter.with_timer()
    
    try:
        reporter.report(INSTALL_ACTION_EVENT, action = UNIVERSAL_UNINSTALL_CHECK)
        win_dir = win32api.GetWindowsDirectory()
        universal_path = os.path.join(os.environ['LOCALAPPDATA'], 'Packages', 'C27EB4BA.DROPBOX_xbfy0k16fey96')
        if not os.path.exists(universal_path):
            timed_reporter.report(INSTALL_ACTION_EVENT, action = UNIVERSAL_UNINSTALL_APP_NOT_FOUND)
            return None
        metadata_path = None.path.join(os.environ['LOCALAPPDATA'], 'Packages', 'C27EB4BA.DROPBOX_xbfy0k16fey96', 'LocalCache', '.for_dbx')
        metadata_exists = os.path.exists(metadata_path)
        can_be_uninstalled = not metadata_exists
        if metadata_exists:
            
            try:
                f = open(metadata_path)
                uwp_dic = json.load(f)
                if uwp_dic.get('can_be_uninstalled') and uwp_dic['can_be_uninstalled'].lower() == 'true':
                    can_be_uninstalled = True
                    
                    try:
                        None(None, None)
                    with None:
                        if not None:
                            
                            try:
                                
                                try:
                                    
                                    try:
                                        pass
                                    except Exception:
                                        TRACE('[Dropbox Universal] Failed to read from metadata file.')
                                        report_exception(severity = Severity.DEBUG, component = DesktopComponent.INSTALLER)
                                        
                                        try:
                                            pass
                                        try:
                                            if can_be_uninstalled:
                                                TRACE('[Dropbox Universal] Deleting Dropbox Universal.')
                                                timed_reporter.report(INSTALL_ACTION_EVENT, action = UNIVERSAL_UNINSTALL_VALID)
                                                powershell_path = os.path.join(win_dir, 'System32', 'WindowsPowerShell', 'v1.0', 'powershell')
                                                uninstall_universal = subprocess.Popen([
                                                    powershell_path,
                                                    'Get-AppxPackage C27EB4BA.DROPBOX | Remove-AppxPackage'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, creationflags = CREATE_NO_WINDOW)
                                                uninstall_universal.communicate()
                                                timed_reporter.report(INSTALL_ACTION_EVENT, action = UNIVERSAL_UNINSTALL_SUCCESS)
                                                return None
                                            None.report(INSTALL_ACTION_EVENT, action = UNIVERSAL_UNINSTALL_INVALID)
                                            TRACE('[Dropbox Universal] Metadata file was found to prevent deletion. Not deleting Dropbpox Universal.')
                                            return None
                                        except Exception:
                                            TRACE('[Dropbox Universal] Failed to delete Dropbox Universal.')
                                            report_exception(severity = Severity.DEBUG, component = DesktopComponent.INSTALLER)
                                            timed_reporter.report(INSTALL_ACTION_EVENT, action = UNIVERSAL_UNINSTALL_FAIL)
                                            return None









def _uninstall_oem(reporter = None, per_machine = None):
    TRACE('[DropboxOEM UWP] un-installation start.')
    cmd = 'Get-AppxPackage C27EB4BA.DropboxOEM | Remove-AppxPackage'
    if per_machine:
        cmd += '; Get-AppxProvisionedPackage -Online | Where-Object DisplayName -In "C27EB4BA.DropboxOEM" | Remove-ProvisionedAppxPackage -Online'
    timed_reporter = reporter.with_timer()
    
    try:
        reporter.report(INSTALL_ACTION_EVENT, action = OEM_UNINSTALL_APP_ATTEMPT)
        win_dir = win32api.GetWindowsDirectory()
        powershell_path = os.path.join(win_dir, 'System32', 'WindowsPowerShell', 'v1.0', 'powershell')
        subprocess.Popen([
            powershell_path,
            cmd], stdin = subprocess.DEVNULL, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL, creationflags = CREATE_NO_WINDOW)
        TRACE('[DropboxOEM UWP] triggered async un-installation of DropboxOEM.')
        timed_reporter.report(INSTALL_ACTION_EVENT, action = OEM_UNINSTALL_APP_SUCCESS)
        return None
    except Exception:
        TRACE('[DropboxOEM UWP] un-installation of DropboxOEM app failed.')
        timed_reporter.report(INSTALL_ACTION_EVENT, action = OEM_UNINSTALL_APP_FAILURE)
        report_exception(severity = Severity.DEBUG, component = DesktopComponent.INSTALLER)
        return None



def _install_dropbox(reporter, setup_dir, inst_dir, per_machine, is_enterprise = None, is_auto_update = None, dropbox_process_killed = None, installer_metadata = ('reporter', 'InstallEventReporter', 'setup_dir', 'Text', 'inst_dir', 'Text', 'per_machine', 'bool', 'is_enterprise', 'bool', 'is_auto_update', 'bool', 'dropbox_process_killed', 'bool', 'installer_metadata', 'InstallerMetadata', 'return', 'Optional[str]')):
    TRACE('Installing Dropbox at folder: %r, per_machine: %r', inst_dir, per_machine)
# WARNING: Decompyle incomplete

_diagnose_installation_error = (lambda per_machine = None, inst_dir = None: try:
disk_usage = shutil.disk_usage(inst_dir)if disk_usage.free < 1048576000:
_set_install_error(per_machine, InstallerErrorCode.DISK_FULL, InstallerStrings.disk_full_error)Noneexcept Exception:
pass_set_install_error(per_machine, InstallerErrorCode.UNKNOWN, InstallerStrings.unknown_error % dict(inst_dir = inst_dir)))()
_set_install_error = (lambda per_machine = None, error_code = None, ui_message = handle_exceptions: entries = [
(DROPBOX_UPDATER_CLIENT_STATE_KEY, 'InstallerResult', REG_DWORD, KEY_WOW64_32KEY, InstallerResult.FAILED_CUSTOM_ERROR),
(DROPBOX_UPDATER_CLIENT_STATE_KEY, 'InstallerError', REG_DWORD, KEY_WOW64_32KEY, error_code),
(DROPBOX_UPDATER_CLIENT_STATE_KEY, 'InstallerResultUIString', REG_SZ, KEY_WOW64_32KEY, ui_message)]_set_reg_entries(per_machine, entries))()

def _try_update_driver_with_timeout(setup_dir = None):
    pass
# WARNING: Decompyle incomplete


def _get_installer_mutex_name():
    return 'Global\\' + BUILD_KEY + '_INSTALLING'


def _create_install_mutex_security_attributes():
    desc = win32security.SECURITY_DESCRIPTOR()
    desc.Initialize()
    desc.SetSecurityDescriptorDacl(True, None, False)
    sec_attrs = win32security.SECURITY_ATTRIBUTES()
    sec_attrs.SECURITY_DESCRIPTOR = desc
    sec_attrs.bInheritHandle = False
    return sec_attrs

_MUTEX: 'Optional[pywintypes.HANDLEType]' = None

def _limit_to_one_instance_during_install():
    global _MUTEX
    installer_mutex_name = _get_installer_mutex_name()
    
    try:
        sec_attrs = _create_install_mutex_security_attributes()
    except pywintypes.error:
        TRACE('Could not create SECURITY_ATTRIBUTES for install exception, continuing with the default SECURITY_ATTRIBUTES')
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.INSTALLER)
        sec_attrs = None

    mutex = win32event.CreateMutex(sec_attrs, 0, installer_mutex_name)
    last_error = win32api.GetLastError()
    if last_error == winerror.ERROR_ALREADY_EXISTS:
        TRACE('_limit_to_one_instance_during_install: quitting because another install process is running')
        hard_exit(ExitCode.FAILURE, reason = 'another install process is running')
        return None
    if None and last_error:
        report_rare_event('_limit_to_one_instance_during_install: error creating mutex. error code: %s', last_error)
    _MUTEX = mutex


def _is_centennial_app_installed(reporter = None, per_machine = None):
    TRACE('Checking if centennial Dropbox is installed %s', 'per machine' if per_machine else 'per user')
    if not _bowbow:
        TRACE('Skipping centennial Dropbox install check because _bowbow is None')
        return False
    timed_reporter = None.with_timer()
    
    try:
        TRACE('Getting centennial Dropbox package full name for %s', 'per machine' if per_machine else 'per user')
        package_name = _bowbow.get_centennial_dropbox_package_full_name(per_machine)
    except WindowsError:
        e = None
        timed_reporter.report(INSTALL_ACTION_EVENT, action = CENTENNIAL_GET_PACKAGE_NAME_FAILURE, stderr = _winerror_repr(e))
        report_exception(severity = Severity.WARN, component = DesktopComponent.INSTALLER)
        TRACE('Failed to get package full name from _bowbow. Assuming no packaged app version exists')
        e = None
        del e
        return False
        e = None
        del e

    if not package_name:
        return False


def _try_write_installer_metadata(channel_id = None, per_machine = None):
    
    try:
        InstallerMetadata(channel_id = channel_id).write_file_to_app_data(per_machine)
        return None
    except Exception:
        e = None
        TRACE('Failed to write installer metadata for channel_id=%r: %s', channel_id, e)
        e = None
        del e
        return None
        e = None
        del e



def install(reporter = None, argv = None):
    TRACE('Install args: %r', argv)
    per_machine = _is_per_machine(argv)
    inst_dir = _get_install_dir(argv)
    setup_dir = _get_current_path(argv)
    is_omaha4 = _is_omaha4(argv)
    channel_id = _get_channel_id(argv)
    is_auto_update = _is_auto_update(argv)
    installer_data = pop_installer_data(argv)
    should_kill_all_processes = _should_kill_all_processes(argv)
    hkey = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USER
    reporter.extend_extra_metadata({
        'per_machine': per_machine,
        'is_auto_update': is_auto_update,
        'is_omaha4': is_omaha4,
        'updater_id': get_omaha_user_id(hkey),
        'channel_id': channel_id })
    reporter.report(INSTALL_ACTION_EVENT, action = INSTALL_ATTEMPT)
    timed_reporter = reporter.with_timer()
    success = _install(reporter, per_machine, inst_dir, setup_dir, is_omaha4, is_auto_update, should_kill_all_processes, installer_data, channel_id)
    timed_reporter.report(INSTALL_ACTION_EVENT, action = INSTALL_SUCCESS if success else INSTALL_FAILURE)
    return success


def _install(reporter, per_machine, inst_dir, setup_dir, is_omaha4, is_auto_update = None, should_kill_all_processes = None, installer_data = None, channel_id = ('reporter', 'InstallEventReporter', 'per_machine', 'bool', 'inst_dir', 'Text', 'setup_dir', 'Text', 'is_omaha4', 'bool', 'is_auto_update', 'bool', 'should_kill_all_processes', 'bool', 'installer_data', 'InstallerData', 'channel_id', 'Optional[str]', 'return', 'bool')):
    pass
# WARNING: Decompyle incomplete

_remove_user_startup_shortcut = (lambda : TRACE('Remove user startup shortcut')dropbox_startup_shortcut = os.path.join(get_user_folder_path(shellcon.CSIDL_STARTUP), '%s.lnk' % BUILD_KEY)safe_remove(dropbox_startup_shortcut))()
_remove_user_desktop_shortcuts = (lambda : TRACE('Remove user desktop, sidebar and sendto shortcuts')dropbox_desktop_shortcut = os.path.join(get_user_folder_path(shellcon.CSIDL_DESKTOP), '%s.lnk' % BUILD_KEY)safe_remove(dropbox_desktop_shortcut)dropbox_sendto_shortcut = os.path.join(get_user_folder_path(shellcon.CSIDL_SENDTO), '%s.lnk' % BUILD_KEY)safe_remove(dropbox_sendto_shortcut)dropbox_sidebar_shortcut = os.path.join(os.path.join(get_user_folder_path(shellcon.CSIDL_PROFILE, 'Links')), '%s.lnk' % BUILD_KEY)safe_remove(dropbox_sidebar_shortcut))()

def update_reg_entries(per_machine = None, entries = None):
    hkey = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USER
    for key_name, value_name, value_type, wow64_access, value in entries:
        TRACE('Updating value for %s of key %s\\%s to %s', value_name, hkey, key_name, value)
        key = registry_key(hkey, key_name, permission = KEY_WRITE | wow64_access)
        if key:
            set_registry_value(key, value_name, value_type, value)
        None(None, None)
    with None:
        if not None:
            pass
    continue
    except Exception:
        ex = None
        TRACE('Unable to update to registry entry: %r', ex)
        ex = None
        del ex
        continue
        ex = None
        del ex

_remove_reg_entries = (lambda per_machine = None, entries = None: hkey = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USERfor key_name, value_name, _, wow64_access, _ in entries:
TRACE('Removing value %s from key %s\\%s', value_name, hkey, key_name)safe_delete_regvalue(hkey, key_name, value_name, delete_key = True, permission = KEY_ALL_ACCESS | wow64_access)None)()
_remove_full_msix_reg_entries = (lambda per_machine = None, remove_omaha_entries = None: if not remove_omaha_entries:
Noneomaha_msix_migration_reg_entries = [
(None, 'MSIXMigrationStatus', REG_SZ, KEY_WOW64_32KEY, ''),
(DROPBOX_UPDATER_CLIENT_STATE_KEY, 'MSIXMigrationRetryCount', REG_DWORD, KEY_WOW64_32KEY, 0),
(DROPBOX_UPDATER_CLIENTS_KEY, 'PackageFamilyName', REG_SZ, KEY_WOW64_32KEY, '')]_remove_reg_entries(per_machine, omaha_msix_migration_reg_entries))()
_cleanup_dropbox = (lambda per_machine, is_enterprise = None, inst_dir = None, keep_user_desktop_shortcut = handle_exceptions, keep_sparse_package = (False, False, False), is_msix_migration = ('per_machine', 'bool', 'is_enterprise', 'bool', 'inst_dir', 'Text', 'keep_user_desktop_shortcut', 'bool', 'keep_sparse_package', 'bool', 'is_msix_migration', 'bool', 'return', 'None'): 