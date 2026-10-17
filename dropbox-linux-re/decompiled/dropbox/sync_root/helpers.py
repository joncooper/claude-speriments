# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

import os
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Text, Tuple
from psutil import disk_partitions
from constants import SyncRootConstants
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.util import get_fs_type, get_volume_info, switch_sidebar_link
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions_ex_1
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fastwalk import fastwalk_with_exception_handling
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.read_only import set_read_only_recursive_helper
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError
from dropbox.sync_root.events.reporter import report_sync_root_event
from dropbox.sync_root.events.types import ExtraInfo, RootInfoExtraInfo, RootMergeInfo, SyncRootEvent, SyncRootEventType
from dropbox.sync_root.interface import SyncRootInfo, SyncRootManagerInterface, SyncRootType
from dropbox.sync_root.types import RemovalMode, SyncRootCreationResult, SyncRootDriveMissing, SyncRootHydrationPolicy, SyncRootMountMissing, SyncRootTypeReason, SyncRootUnsafeMerge
from dropbox.trace import TRACE
on_background_thread_future = make_on_thread_future_decorator(on_background_thread, 'on_background_thread_future')
_CREATE_ROOT_TIMEOUT_SECONDS = 60

def _create_mounted_root(fs = None, local_config = None, folder_path_raw = None):
    TRACE('[RootManager] Creating mounted root (via temporary mechanism)')
# WARNING: Decompyle incomplete


def create_root_for_account(root_manager, account_manager, fs, account, local_config, root_type = None, root_type_reason = None, root_parent_path = None, root_mount_path = (None, None, SyncRootHydrationPolicy.FULL), hydration_policy = ('root_manager', 'SyncRootManagerInterface', 'account_manager', 'AccountManagerInterface', 'fs', 'Any', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'root_type', 'SyncRootType', 'root_type_reason', 'SyncRootTypeReason', 'root_parent_path', 'Optional[str]', 'root_mount_path', 'Optional[str]', 'hydration_policy', 'SyncRootHydrationPolicy', 'return', 'None')):
    report_sync_root_event(SyncRootEvent(sync_root_type = root_type, event_type = SyncRootEventType.ROOT_TYPE_CHOSEN, extra_info = ExtraInfo(reason = root_type_reason.value)))
# WARNING: Decompyle incomplete


def _create_default_mounted_root_for_account(root_manager, account_manager = None, fs = None, account = None, local_config = ('root_manager', 'SyncRootManagerInterface', 'account_manager', 'AccountManagerInterface', 'fs', 'Any', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'return', 'None')):
    TRACE('[RootManager] _create_default_mounted_root_for_account')
    new_root_mount_path = account_manager.get_new_dropbox_location(account, local_config, use_cookie = False)
    new_root_display_name = account_manager.get_display_name_account_component(account)
    TRACE('[RootManager] _create_default_mounted_root_for_account: %r', new_root_mount_path)
    if os.path.exists(new_root_mount_path):
        raise SyncRootUnsafeMerge(new_root_mount_path)
    _create_mounted_root(fs, local_config, new_root_mount_path)
    root_manager.create_root(account, SyncRootType.MOUNTED, new_root_display_name).block(_CREATE_ROOT_TIMEOUT_SECONDS).result()


def _handle_incomplete_cdm_relocation_of_root_for_account(root_manager, account_manager, fs = None, account = None, local_config = None, show_archive_dialog_func = ('root_manager', 'SyncRootManagerInterface', 'account_manager', 'AccountManagerInterface', 'fs', 'Any', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'show_archive_dialog_func', 'Callable[[Optional[str], Optional[str]], None]', 'return', 'None')):
    incomplete_cdm_relocation = local_config.config_dict.get(SyncRootConstants.CONFIG_KEY_CDM_RELOCATE_INCOMPLETE, None)
    if not incomplete_cdm_relocation:
        TRACE('[RootManager] CDM_RELOCATE: No incomplete CDM relocation, aborting.')
        return None
    TRACE('[RootManager] CDM_RELOCATE: There is an incomplete relocation to handle (type %r)!', incomplete_cdm_relocation)
    
    try:
        relocating_root_type = SyncRootType(incomplete_cdm_relocation)
    except ValueError:
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SYNC_ENGINE)
        TRACE('!! [RootManager] CDM_RELOCATE: Invalid relocating_root_type %r, default to `MOUNTED`', incomplete_cdm_relocation)
        relocating_root_type = SyncRootType.MOUNTED

    if relocating_root_type == SyncRootType.MOUNTED:
        _create_default_mounted_root_for_account(root_manager, account_manager, fs, account, local_config)
# WARNING: Decompyle incomplete


def fp_upgrade_root_for_account(root_manager = None, account_manager = None, account = None, local_config = ('root_manager', 'SyncRootManagerInterface', 'account_manager', 'AccountManagerInterface', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'return', 'Future[Optional[SyncRootCreationResult]]')):
    TRACE('[RootManager] FP_UPGRADE: upgrade root for account %r', account)
    root_display_name = account_manager.generate_fp_domain_display_name(account)
    TRACE('[RootManager] FP_UPGRADE: importing data from existing root')
    root_mount_path = local_config.get_dropbox_path()
# WARNING: Decompyle incomplete


def _build_root_info_event(sync_root_info = None):
    default_value = 'unknown'
    root_fstype = default_value
    root_mount_path = default_value
    root_device = default_value
    mount_options = default_value
    is_internal = default_value
    is_encrypted = default_value
    media_size = default_value
    device_vendor = default_value
    device_model = default_value
    bus_name = default_value
# WARNING: Decompyle incomplete


def build_root_merge_event(sync_root_type, account = None, unlink_cookie = None, rejection_reason = None, tagged_root_ns = (None, None), tmf_fileid = ('sync_root_type', 'SyncRootType', 'account', 'AccountInterface', 'unlink_cookie', 'Dict[str, Any]', 'rejection_reason', 'Optional[str]', 'tagged_root_ns', 'Optional[int]', 'tmf_fileid', 'Optional[str]', 'return', 'SyncRootEvent')):
    extra_info = RootMergeInfo(fp_domain_id = unlink_cookie.get(SyncRootConstants.CONFIG_KEY_FP_DOMAIN_ID), reason = rejection_reason, unlink_cookie_root_ns_id = unlink_cookie.get('root_ns'), unlink_cookie_home_ns_id = unlink_cookie.get('home_ns'), unlink_sync_root_type = unlink_cookie.get(SyncRootConstants.CONFIG_KEY_SYNC_ROOT_TYPE), current_root_ns_id = account.root_ns_id, current_home_ns_id = account.home_ns_id)
# WARNING: Decompyle incomplete


def _record_root_info_event(sync_root_info = None):
    root_info_event = _build_root_info_event(sync_root_info)
    report_sync_root_event(root_info_event)


def get_root_for_account(root_manager, config_manager = None, account_manager = None, account = None, local_config = ('root_manager', 'SyncRootManagerInterface', 'config_manager', 'ConfigurationManagerInterface', 'account_manager', 'AccountManagerInterface', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'return', 'Optional[SyncRootInfo]')):
    was_config_corrupted = config_manager.corruptdb if account.is_primary else config_manager.corruptdb_secondary
    if not was_config_corrupted and account.is_fresh_link:
        _try_recover_root_from_cookie(account_manager, account, local_config)
    root_info = root_manager.get_root_info(account).block().result()
# WARNING: Decompyle incomplete


def collect_missing_dropbox_roots(account_manager, config_manager = None, account = None, local_config = None, known_missing = ('account_manager', 'AccountManagerInterface', 'config_manager', 'ConfigurationManagerInterface', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'known_missing', 'bool', 'return', 'Tuple[List[Text], bool, List[AccountInterface], Set[int]]')):
    pass
# WARNING: Decompyle incomplete


def check_mounted_root_for_account(fs = None, account = None, folder_path_raw = None):
    TRACE('[RootManager] Checking mounted root (via temporary mechanism)')
    if IS_WINDOWS:
        
        try:
            switch_sidebar_link(folder_path_raw, ignore_missing = True, windows_skip_desktop_shortcut = True)
            return None
        except Exception:
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SYNC_ENGINE)
            return None
            return None



def _restore_write_permissions_under_root(fs = None, root_mount_path = None):
    local_path = fs.make_path(root_mount_path)
    TRACE('Restoring write permissions under path %r', local_path)
    walker = fastwalk_with_exception_handling(fs, local_path, no_atime = True, follow_symlinks = False)
    dirpath = None
# WARNING: Decompyle incomplete


def _destroy_mounted_root(fs = None, local_config = None):
    TRACE('[RootManager] Destroying mounted root (via temporary mechanism)')
    root_mount_path = local_config.config_dict.pop('dropbox_path', None)
    TRACE('[RootManager] Current mount path is %r', root_mount_path)
# WARNING: Decompyle incomplete


def destroy_root_from_config(root_manager, fs = None, local_config = None, is_primary = None, mode = ('root_manager', 'SyncRootManagerInterface', 'fs', 'Any', 'local_config', 'LocalConfigurationInterface', 'is_primary', 'bool', 'mode', 'RemovalMode', 'return', 'None')):
    TRACE('[RootManager] destroy_root_from_config %r, primary? %r, mode? %r', local_config, is_primary, mode)
    config_dict = local_config.config_dict
# WARNING: Decompyle incomplete


def fp_get_valid_domain_id_from_unlink_cookie(account = None, local_config = None):
    unlink_cookie = local_config.unlink_cookie
    if not unlink_cookie:
        return None
    root_ns = None.get('root_ns')
    home_ns = unlink_cookie.get('home_ns')
# WARNING: Decompyle incomplete


def _try_recover_root_from_cookie(account_manager = None, account = None, local_config = None):
    TRACE('!! [RootManager] corruptdb: trying to recover state from unlink cookie!')
# WARNING: Decompyle incomplete


def _get_desktop_path():
    return os.path.expanduser('~/Desktop')


def _get_documents_path():
    return os.path.expanduser('~/Documents')

folder_is_multiroot_experiment = (lambda folder_path = None: pass# WARNING: Decompyle incomplete
)()

def _folder_is_in_desktop_or_documents(folder_path = None):
    desktop_directory = _get_desktop_path()
    documents_directory = _get_documents_path()
    if os.path.commonprefix([
        desktop_directory,
        folder_path]) == desktop_directory:
        return True
    if None.path.commonprefix([
        documents_directory,
        folder_path]) == documents_directory:
        return True


def _folder_is_not_named_dropbox(folder_path = None):
    return os.path.basename(folder_path) != 'Dropbox'

folder_conflicts_with_icloud = (lambda folder_path = None: pass# WARNING: Decompyle incomplete
)()

def check_dropbox_path_exists(dropbox_path_str = None):
    dropbox_path = Path(dropbox_path_str)
    if dropbox_path.exists():
        return None
# WARNING: Decompyle incomplete

