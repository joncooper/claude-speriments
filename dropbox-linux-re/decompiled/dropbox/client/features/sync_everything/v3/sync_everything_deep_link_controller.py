# Source Generated with Decompyle++
# File: sync_everything_deep_link_controller.pyc (Python 3.11)

from typing import List, Mapping
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_accounts, get_sync_everything_preferences_user_contexts
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.constants import ACTION_SURFACE_MAP
from dropbox.client.multiaccount.role import Roles
from dropbox.foundation.context.machine import MachineContext
MYPY = False
if MYPY:
    from dropbox.client.main import AttemptLinkFunc

class SyncEverythingDeepLinkController:
    open_sync_everything_onboarding = (lambda _path, _query = None, _navigation_service = None, machine_context = staticmethod, attempt_link = ('machine_context', 'MachineContext', 'attempt_link', 'AttemptLinkFunc', 'return', 'None'): session_id = random_session_id()if len(machine_context.account_manager.linked_accounts) == 0:
SyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, None, SyncEverythingEvent.deep_link_show_setup_wizard, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER])attempt_link(None, None, False)Noneeligible_accounts = get_sync_everything_preferences_accounts(machine_context)if len(eligible_accounts) > 0:
onboarding_account = eligible_accounts[0]user_context = machine_context.account_manager.account_models[onboarding_account].user_contextSyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, onboarding_account, SyncEverythingEvent.deep_link_open_onboarding, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER])ComputerBackupManagerWrapper.on_deep_link(user_context, machine_context)NoneSyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, None, SyncEverythingEvent.deep_link_not_eligible, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER]))()
    open_backup_sku_onboarding = (lambda _path, _query = None, _navigation_service = None, machine_context = staticmethod, attempt_link = ('machine_context', 'MachineContext', 'attempt_link', 'AttemptLinkFunc', 'return', 'None'): session_id = random_session_id()if len(machine_context.account_manager.linked_accounts) == 0:
SyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, None, SyncEverythingEvent.deep_link_sku_show_setup_wizard, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER])attempt_link(None, None, False)Noneeligible_accounts = get_sync_everything_preferences_accounts(machine_context)if len(eligible_accounts) > 0:
onboarding_account = eligible_accounts[0]for account in eligible_accounts:
if account.role == Roles.PERSONAL:
onboarding_account = accountuser_context = machine_context.account_manager.account_models[onboarding_account].user_contextComputerBackupManagerWrapper.on_backup_sku_deep_link(user_context, machine_context, session_id)NoneSyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, None, SyncEverythingEvent.deep_link_sku_not_eligible, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER])None)()
    open_backup_app = (lambda _path, query = None, _navigation_service = None, machine_context = staticmethod, attempt_link = ('query', 'Mapping[str, List[str]]', 'machine_context', 'MachineContext', 'attempt_link', 'AttemptLinkFunc', 'return', 'None'): session_id = random_session_id()if not query.get('account_id', [
''])[0]:
account_id = Noneif not query.get('host_id', [
''])[0]:
host_id = Noneif not query.get('drive_uuid', [
''])[0]:
drive_uuid = Noneif not query.get('action', [
''])[0]:
action = Noneif not query.get('source', [
''])[0]:
web_source = Noneif not query.get('fq_paths', []):
fq_paths = Nonebackup_app_params = BackupAppParams(ignored_paths = { }, account_id = account_id, host_id = host_id, drive_uuid = drive_uuid, action = action, web_source = web_source, fq_paths = fq_paths)if len(machine_context.account_manager.linked_accounts) == 0:
SyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, None, SyncEverythingEvent.deep_link_backup_app_show_setup_wizard, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER])attempt_link(None, None, False)Noneeligible_user_contexts = get_sync_everything_preferences_user_contexts(machine_context)if len(eligible_user_contexts) > 0:
user_context = eligible_user_contexts[0]for eligible_user_context in eligible_user_contexts:
if eligible_user_context.account.role == Roles.PERSONAL:
user_context = eligible_user_contextComputerBackupManagerWrapper.on_backup_app_deep_link(user_context, machine_context, session_id, backup_app_params)NoneSyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, None, SyncEverythingEvent.deep_link_backup_app_not_eligible, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER])None)()
    open_backup_restoration = (lambda _path, query = None, _navigation_service = None, machine_context = staticmethod, attempt_link = ('query', 'Mapping[str, List[str]]', 'machine_context', 'MachineContext', 'attempt_link', 'AttemptLinkFunc', 'return', 'None'): session_id = random_session_id()if not query.get('backup_id', [
''])[0]:
backup_id = Noneaction_surface = ActionSurface.PROTOCOL_HANDLERsource = Source.PROTOCOL_HANDLERif len(machine_context.account_manager.linked_accounts) == 0:
SyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, None, SyncEverythingEvent.deep_link_backup_restoration_show_setup_wizard, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER])attempt_link(None, None, False)Noneeligible_user_contexts = get_sync_everything_preferences_user_contexts(machine_context)if len(eligible_user_contexts) > 0 and backup_id:
user_context = eligible_user_contexts[0]for eligible_user_context in eligible_user_contexts:
if eligible_user_context.account.role == Roles.PERSONAL:
user_context = eligible_user_contextComputerBackupManagerWrapper.on_backup_restoration_deep_link(user_context, machine_context, session_id, backup_id, action_surface, source)NoneSyncEverythingLogger.report_ui_event(machine_context.metrics_reporter, None, SyncEverythingEvent.deep_link_backup_restoration_not_eligible, session_id, ACTION_SURFACE_MAP[ActionSurface.PROTOCOL_HANDLER])None)()

