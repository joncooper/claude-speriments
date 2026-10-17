# Source Generated with Decompyle++
# File: visibility_inputs.pyc (Python 3.11)

import os
from typing import Any, Dict, List, NamedTuple, Optional, Text, Tuple
from build_number import is_full_msix
from build_number.platform import IS_WINDOWS
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.cloud_docs.extension_constants import CLOUD_ENHANCED_EXTS
from dropbox.client.cloud_docs.file_validator import is_cloud_docs_extension, is_shortcut as is_clouddocs_shortcut
from dropbox.client.cloud_docs.gating import is_cloud_docs_enabled
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.computer_backup.computer_backup_state import KnownCBFolder
from dropbox.client.features.copy_to_dropbox.constants import ExternalContextMenuSharingStormcrowVariants
from dropbox.client.features.copy_to_dropbox.utils import get_copy_to_dropbox_variant
from dropbox.client.features.external_drive_backup.cu_edb_chooser import EDBContextMenuGating
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.file_locking.constants import DESKTOP_FILE_LOCKING_STORMCROW
from dropbox.client.features.file_locking.file_locking_controller import FileLockingAccessor
from dropbox.client.features.file_locking.file_locking_predicates import file_locking_supported_nucleus, is_local_shortcut
from dropbox.client.features.file_requests.models.create_file_request import file_request_creation_enabled
from dropbox.client.features.hellosign.constants import HELLOSIGN_EXTS
from dropbox.client.features.hellosign.gating import is_open_with_self_sign_enabled, is_shell_open_with_hellosign_enabled
from dropbox.client.features.ignore_sync.constants import CONTEXT_MENU_IGNORE_FEATURE
from dropbox.client.features.reel.constants import REPLAY_EXTS
from dropbox.client.features.reel.gating import add_to_replay_from_desktop_enabled, is_review_in_replay_context_menu_enabled
from dropbox.client.features.rewinds.gating import is_rewind_context_menu_enabled
from dropbox.client.features.send_and_track.constants import SEND_AND_TRACK_EXTS
from dropbox.client.features.send_and_track.gating import is_open_with_send_and_track_enabled
from dropbox.client.features.sync.sync_prioritization.sync_prioritization import DESKTOP_SYNC_PRIORITIZATION_CONTEXT_MENU
from dropbox.client.features.sync_and_storage.utils import manage_space_enabled
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.features.sync_everything.v3.fs_utils import is_in_active_backup
from dropbox.client.features.transfer.add_to_transfer import transfer_desktop_creation_enabled
from dropbox.client.gandalf import Gandalf
from dropbox.client.move_to_dropbox import should_disable_move_to_dropbox
from dropbox.client.per_node_metadata.actions import get_pre_setup_actions
from dropbox.client.ui.common.constants import DROPBOX_SUPPORTED_EDITABLE_EXTS
from dropbox.client.util import check_move_blocked
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.functions import file_extension
from dropbox.infinite import InfiniteAllowedContextMenus
from dropbox.preferences import DESKTOP_CUSTOMIZABLE_CONTEXT_MENU_STORMCROW_ENABLED
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockState, FileLockStatus
from dropbox.sync_engine_boundary.types.local_props import DeviceAnchorInactiveReason, FileSyncStatus
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.remote_props import DirectoryProperties, FolderPolicyStatus, MountProperties, RemoteLocationProperties
MYPY = False
if MYPY:
    from dropbox.fsutil import FileSystem
    from dropbox.infinite.state_machine import InfiniteStateMachine

class ContextMenuUserProps(NamedTuple):
    is_customizable_context_menu_enabled: 'bool' = 'ContextMenuUserProps'


class ContextMenuMountProps(NamedTuple):
    is_in_encrypted_folder: 'bool' = 'ContextMenuMountProps'


class ContextMenuDbxPathProps(NamedTuple):
    is_ignore_root: 'bool' = 'ContextMenuDbxPathProps'

ContextMenuExtPathProps = NamedTuple('ContextMenuExtPathProps', [
    ('account', AccountInterface),
    ('move_blocked', bool),
    ('is_dir', bool),
    ('transfer_allow_add_files', bool),
    ('is_device_folder_symlink', bool),
    ('is_in_backup_known_folder', bool),
    ('is_edb_drive_backup_eligible', bool),
    ('is_cb_already_backup', bool),
    ('external_context_menu_sharing_variant', ExternalContextMenuSharingStormcrowVariants)])

class ContextMenuLocalConfig:
    DEPENDENT_FIELDS_WITH_DEFAULTS = {
        'move_to_dropbox': True }
    
    def __init__(self = None, config_dict = None):
        self._config_dict = config_dict

    from_local_config = (lambda cls = None, local_config = None: config_dict = { }for field, default in cls.DEPENDENT_FIELDS_WITH_DEFAULTS.items():
config_dict[field] = local_config.config_dict.get(field, default)cls(config_dict))()
    pref_regex = (lambda cls = None: '(%s)' % '|'.join(cls.DEPENDENT_FIELDS_WITH_DEFAULTS.keys()))()
    move_to_dropbox = (lambda self = None: self._config_dict['move_to_dropbox'])()


def get_target_ns_id(location_props = None):
    pass
# WARNING: Decompyle incomplete


def build_context_menu_dbx_path_props(user_context, local_path = None, location_props = None, machine_context = None, sync_engine_adapter = (False,), allow_missing_local_props = ('user_context', 'UserContext', 'local_path', 'LocalPath', 'location_props', 'LocationProperties', 'machine_context', 'MachineContext', 'sync_engine_adapter', 'SyncEngineAdapter', 'allow_missing_local_props', 'bool', 'return', 'ContextMenuDbxPathProps')):
    local_props = location_props.local_properties
# WARNING: Decompyle incomplete


def build_context_menu_mount_props(account = None, remote_props = None):
    
    try:
        if account.quota_info is not None:
            pass
        is_over_quota = account.quota_info.over_any_quota()
    except AssertionError:
        is_over_quota = False

    return ContextMenuMountProps(is_over_quota = is_over_quota, is_in_team_folder = remote_props.is_in_team_folder, is_view_name_only = remote_props.is_view_name_only, is_read_only = remote_props.is_read_only, is_in_shared_folder = remote_props.is_in_shared_folder, is_in_encrypted_folder = remote_props.is_in_encrypted_folder)


def _get_computer_backup_context_menu_props(path, pathlist = None, account_manager = None, machine_context = None, file_system = ('path', 'LocalPath', 'pathlist', 'List[Text]', 'account_manager', 'AccountManagerInterface', 'machine_context', 'MachineContext', 'file_system', 'FileSystem', 'return', 'Tuple[Dict[Account, bool], Dict[Account, bool], Dict[Account, bool]]')):
    pass
# WARNING: Decompyle incomplete


def _get_edb_context_menu_props(path = None, account_manager = None, machine_context = None):
    is_edb_drive_backup_eligible = account_manager.linked_accounts()
    if IS_WINDOWS and ExternalDriveBackupFeature.event_onboarding_allowed_for_any_user(machine_context) and len(path.split()) == 2 and path.split()[0] != 'C:':
        selected_context = None
        for model in machine_context.account_manager.account_models.values():
            if ExternalDriveBackupFeature.event_onboarding_allowed_for_user(model.user_context):
                selected_context = model.user_context
                (lambda .0: pass# WARNING: Decompyle incomplete
)
            
            if selected_context:
                is_edb_drive_backup_eligible[selected_context.account] = EDBContextMenuGating.is_drive_allowed_edb_context_menu(selected_context, path.split()[0] + '\\')
    return is_edb_drive_backup_eligible


def build_context_menu_ext_path_props(account_manager, gandalf, file_system = None, machine_context = None, pathlist = None, is_dir = ('account_manager', 'AccountManagerInterface', 'gandalf', 'Gandalf', 'file_system', 'FileSystem', 'machine_context', 'MachineContext', 'pathlist', 'List[Text]', 'is_dir', 'bool', 'return', 'List[ContextMenuExtPathProps]')):
    pass
# WARNING: Decompyle incomplete


def build_context_menu_user_props(account = None, gandalf = None, infinite_state_machine = None, context_menu_config = ('account', 'Optional[AccountInterface]', 'gandalf', 'Gandalf', 'infinite_state_machine', 'Optional[InfiniteStateMachine]', 'context_menu_config', 'ContextMenuLocalConfig', 'return', 'ContextMenuUserProps')):
    if account is not None:
        if gandalf.allows(DESKTOP_FILE_LOCKING_STORMCROW, account = account):
            file_locking_enabled = FileLockingAccessor.context_menu_supported(account)
            if account:
                file_locking_team_policy_enabled = not FileLockingAccessor.is_disabled_by_team_policy(account)
                is_team_folder_context_menu_enabled = account is not None
                sync_prioritization_enabled = gandalf.allows(DESKTOP_SYNC_PRIORITIZATION_CONTEXT_MENU, account = account)
                if account and infinite_state_machine:
                    infinite_allowed_menus = infinite_state_machine.get_allowed_context_menu_items(account)
                else:
                    infinite_allowed_menus = InfiniteAllowedContextMenus.RECALL_OR_UPSELL
# WARNING: Decompyle incomplete

