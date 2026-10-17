# Source Generated with Decompyle++
# File: nav_service.pyc (Python 3.11)

import os
from typing import Dict, List, Optional, Text
from dropbox.client.features.computer_backup_custom_folder_picker.bridge_gen.computer_backup_custom_folder_picker_params import ComputerBackupCustomFolderPickerParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.users.bridge_gen.role import Role
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.manifest_registry import COMPUTER_BACKUP_CUSTOM_FOLDER_PICKER

def show_custom_folders_selector(navigation_service, role, session_id, source, backup_info, ignored_paths, anchor_folders_limit = None, selected_folders = None, preselected_path = None, unselected_paths = (None, None, None, None), remediation_flag = ('navigation_service', 'NavigationServiceInterface', 'role', 'Role', 'session_id', 'str', 'source', 'Source', 'backup_info', 'BackupInfo', 'ignored_paths', 'Dict[Text, List[Text]]', 'anchor_folders_limit', 'Optional[int]', 'selected_folders', 'Optional[Dict[Text, bool]]', 'preselected_path', 'Optional[str]', 'unselected_paths', 'Optional[List[str]]', 'remediation_flag', 'Optional[bool]', 'return', 'None')):
    return navigation_service.navigate(COMPUTER_BACKUP_CUSTOM_FOLDER_PICKER, view_key = 'computer_backup_custom_folder_picker', parameter = ComputerBackupCustomFolderPickerParams(session_logging_id = session_id, role = role, source = source, root_path = os.path.expanduser('~'), backup_info = backup_info, ignored_paths = ignored_paths, anchor_folders_limit = anchor_folders_limit, selected_folders = selected_folders, preselected_path = preselected_path, unselected_paths = unselected_paths, remediation_flag = remediation_flag), load_policy = NavigationLoadPolicy.ALLOW_REUSE).ground(component = DesktopComponent.BACKUP_ENGINE)

