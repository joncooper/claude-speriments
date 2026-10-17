# Source Generated with Decompyle++
# File: nav_service.pyc (Python 3.11)

import os
from typing import Dict, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_app.bridge_gen.backup_app_nav_params import BackupAppNavParams
from dropbox.client.features.backup_quota_exempt_picker.bridge_gen.backup_quota_exempt_picker_nav_params import BackupQuotaExemptPickerNavParams
from dropbox.client.features.backup_restorations_onboarding.bridge_gen.backup_restorations_onboarding_nav_params import BackupRestorationsOnboardingNavParams
from dropbox.client.features.backup_restorations_onboarding.bridge_gen.eligible_backups import EligibleBackups
from dropbox.client.features.backup_sku_onboarding.bridge_gen.backup_sku_onboarding_nav_params import BackupSkuOnboardingNavParams
from dropbox.client.features.backup_unlimited_storage_modal.view_model.bridge_gen.backup_unlimited_storage_modal_nav_params import BackupUnlimitedStorageModalNavParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_unlimited_storage_modal_actions import BackupUnlimitedStorageModalActions
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything_carousel.bridge_gen.sync_everything_carousel_nav_params import SyncEverythingCarouselNavParams
from dropbox.client.features.sync_everything_preferences.bridge_gen.sync_everything_preferences_nav_params import SyncEverythingPreferencesNavParams
from dropbox.client.features.users.bridge_gen.role import Role
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.manifest_registry import BACKUP_APP, BACKUP_QUOTA_EXEMPT_PICKER, BACKUP_RESTORATIONS_ONBOARDING, BACKUP_SKU_ONBOARDING, BACKUP_UNLIMITED_STORAGE_MODAL, BACKUP_UNLIMITED_STORAGE_MODAL_LARGE, SYNC_EVERYTHING_CAROUSEL, SYNC_EVERYTHING_PREFERENCES

def show_sync_everything_onboarding(navigation_service, source = None, ignored_paths = None, session_logging_id = None, default_role = (None, None, None), folders = ('navigation_service', 'NavigationServiceInterface', 'source', 'Source', 'ignored_paths', 'Dict[Text, List[Text]]', 'session_logging_id', 'Optional[str]', 'default_role', 'Optional[Role]', 'folders', 'Optional[Dict[Text, Text]]', 'return', 'None')):
    return navigation_service.navigate(SYNC_EVERYTHING_CAROUSEL, view_key = 'sync_everything', parameter = SyncEverythingCarouselNavParams(source = source, session_logging_id = session_logging_id, default_role = default_role, ignored_paths = ignored_paths, folders = folders)).ground(component = DesktopComponent.SYNC_EVERYTHING)


def show_sync_everything_preferences(navigation_service = None, source = None, session_logging_id = None):
    return navigation_service.navigate(SYNC_EVERYTHING_PREFERENCES, parameter = SyncEverythingPreferencesNavParams(source = source, session_logging_id = session_logging_id)).ground(component = DesktopComponent.SYNC_EVERYTHING)


def show_backup_sku_onboarding(navigation_service, account = None, backups = None, source = None, session_logging_id = ('navigation_service', 'NavigationServiceInterface', 'account', 'AccountInterface', 'backups', 'List[BackupInfo]', 'source', 'Source', 'session_logging_id', 'str', 'return', 'None')):
    return navigation_service.navigate_user_bound(BACKUP_SKU_ONBOARDING, account, parameter = BackupSkuOnboardingNavParams(backups = backups, source = source, session_logging_id = session_logging_id)).ground(component = DesktopComponent.SYNC_EVERYTHING)


def show_backup_app(navigation_service, session_logging_id, eligible_roles, source, account_id, current_host_id, host_id, action, initial_message, web_source, initial_selected_id, ignored_paths, folders = None, updating_dbx_ignore_folders = None, root_path = None, fq_paths = (None, None, None, None, None, None, None, None, None, None, None, None, None), parent_id = ('navigation_service', 'NavigationServiceInterface', 'session_logging_id', 'str', 'eligible_roles', 'Dict[str, str]', 'source', 'Source', 'account_id', 'Optional[str]', 'current_host_id', 'Optional[str]', 'host_id', 'Optional[str]', 'action', 'Optional[str]', 'initial_message', 'Optional[str]', 'web_source', 'Optional[str]', 'initial_selected_id', 'Optional[str]', 'ignored_paths', 'Optional[Dict[str, List[str]]]', 'folders', 'Optional[Dict[str, str]]', 'updating_dbx_ignore_folders', 'Optional[List[str]]', 'root_path', 'Optional[str]', 'fq_paths', 'Optional[List[str]]', 'parent_id', 'Optional[int]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def show_backup_sku_modal(navigation_service = None, account = None, source = None, session_logging_id = ('navigation_service', 'NavigationServiceInterface', 'account', 'AccountInterface', 'source', 'Source', 'session_logging_id', 'str', 'return', 'None')):
    return navigation_service.navigate_user_bound(BACKUP_QUOTA_EXEMPT_PICKER, account, parameter = BackupQuotaExemptPickerNavParams(source = source, session_logging_id = session_logging_id)).ground(component = DesktopComponent.SYNC_EVERYTHING)


def show_backup_restorations_onboarding(navigation_service, session_logging_id = None, eligible_roles = None, eligible_backups = None, source = (False,), show_cb_onboarding_restoration = ('navigation_service', 'NavigationServiceInterface', 'session_logging_id', 'str', 'eligible_roles', 'Dict[str, str]', 'eligible_backups', 'List[EligibleBackups]', 'source', 'Source', 'show_cb_onboarding_restoration', 'bool', 'return', 'None')):
    return navigation_service.navigate(BACKUP_RESTORATIONS_ONBOARDING, view_key = 'backup_restorations_onboarding', parameter = BackupRestorationsOnboardingNavParams(session_logging_id = session_logging_id, eligible_roles = eligible_roles, eligible_backups = eligible_backups, source = source, show_cb_onboarding_restoration = show_cb_onboarding_restoration, home_path = os.path.expanduser('~'))).ground(component = DesktopComponent.SYNC_EVERYTHING)


def show_backup_unlimited_storage_modal(navigation_service, session_logging_id, action, device_name = None, role = None, selected_backup = None, is_large = ('navigation_service', 'NavigationServiceInterface', 'session_logging_id', 'str', 'action', 'BackupUnlimitedStorageModalActions', 'device_name', 'str', 'role', 'Role', 'selected_backup', 'BackupInfo', 'is_large', 'bool', 'return', 'None')):
    return navigation_service.navigate(BACKUP_UNLIMITED_STORAGE_MODAL_LARGE if is_large else BACKUP_UNLIMITED_STORAGE_MODAL, view_key = 'backup_unlimited_storage_modal_large' if is_large else 'backup_unlimited_modal_storage', parameter = BackupUnlimitedStorageModalNavParams(session_logging_id = session_logging_id, action = action, device_name = device_name, role = role, selected_backup = selected_backup), load_policy = NavigationLoadPolicy.CREATE_ALWAYS).ground(component = DesktopComponent.SYNC_EVERYTHING)

