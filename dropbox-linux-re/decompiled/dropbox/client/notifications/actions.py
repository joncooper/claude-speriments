# Source Generated with Decompyle++
# File: actions.pyc (Python 3.11)

import inspect
import json
import os
import uuid
from functools import partial
from threading import Event
from typing import Any, Callable, cast, Dict, List, Optional, Text, Tuple, Union
from urllib.parse import urlparse
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.client_shmodel import ClientShmodel, ClientShmodelOrigin
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.file_locking.file_locking_controller import FileLockingAccessor
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.features.previews.helpers import launch_preview, PreviewEntryPoint
from dropbox.client.features.sharing_modal.util import launch_share_modal
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.fenix.journeys.app_shell.constants import Views as AppShellViews
from dropbox.client.fenix.journeys.app_shell.utils import get_open_in_dropbox_foreground_surface, is_url_allowed_for_foreground_surface, launch_appshell, OpenInDropboxForegroundSurface
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.actions_factory_interface import UserNotificationActionFactoryInterface
from dropbox.client.notifications.exceptions import UserNotificationActionNotAvailableError
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.client.ui.common.uikit import BaseUIKit, on_ui_thread_returns_none
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import DropboxResponseClientError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import CancelledFutureException, Future, FutureHelpers, IncompleteFutureException, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.native_file_opener.bridge_gen.file_open_bridge_result import FileOpenBridgeResult
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.native_file_opener.bridge_gen.file_open_path import FileOpenPath
from dropbox.foundation.native_file_opener.impl import ContextBoundNativeFileOpener
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.navigation_service.interface import MachineNavigationManifest, UserNavigationManifest
from dropbox.foundation.navigation_service.manifest_registry import get_manifest_by_name
from dropbox.foundation.paths.bridge_gen.types import RRServerPath
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.i18n import trans
from dropbox.metrics.pro_event_reporting import report_pro_event
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.exceptions import InvalidLocalPathError, NamespaceNotMountedError
from dropbox.sync_engine_boundary.types.local_props import LocalDirectoryProperties, LocalLocationProperties
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.remote_props import MountProperties
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.threadutils import is_main_thread
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
SHARED_FOLDER_FAQ_CANT_CREATE = 'https://help.dropbox.com/files-folders/share/shared-folder-faq#cantcreate'
ZOOM_CLIENT_PROTOCOL = 'zoommtg://'

class UserNotificationActionFactory(UserNotificationActionFactoryInterface):
    MOUNT_SHARED_FOLDER_TIMEOUT = 5
    OPEN_SHARING_VIEW_NUCLEUS_TIMEOUT = 5
    ESV_SUPPORTED_URLS = [
        '.dropbox.com/scl/fi/',
        '.dropbox.com/preview']
    
    def __init__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_debug_grant_access_action(self = None, account = None, backup_url_path = None, path_lower = ('account', 'AccountInterface', 'backup_url_path', 'Text', 'path_lower', 'Text', 'return', 'None')):
        self._debug_grant_access_actions[(account.uid, backup_url_path)] = path_lower

    
    def init_dependencies(self, machine_context, conn, desktop_login, gandalf, sync_engine_adapter, ui_kit = None, folder_opener_controller = None, client_shmodel = None, navigation_service = ('machine_context', 'MachineContext', 'conn', 'DropboxConnection', 'desktop_login', 'DesktopLogin', 'gandalf', 'Gandalf', 'sync_engine_adapter', 'SyncEngineAdapter', 'ui_kit', 'BaseUIKit', 'folder_opener_controller', 'FolderOpenerController', 'client_shmodel', 'ClientShmodel', 'navigation_service', 'NavigationServiceInterface', 'return', 'None')):
        self._machine_context = machine_context
        self._conn = conn
        self._desktop_login = desktop_login
        self._gandalf = gandalf
        self._sync_engine_adapter = sync_engine_adapter
        self._ui_kit = ui_kit
        self._folder_opener_controller = folder_opener_controller
        self._client_shmodel = client_shmodel
        self._navigation_service = navigation_service

    
    def get_action(self = None, account = None, action_name = None, action_parameters = ('account', 'AccountInterface', 'action_name', 'Text', 'action_parameters', 'Optional[Dict[Text, Any]]', 'return', 'Callable[[], None]')):
        pass
    # WARNING: Decompyle incomplete

    
    def _is_esv_preview_allowed_for_link(self = None, account = None, link = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _open_link_in_previews(self = None, account = None, link = None):
        if self._gandalf:
            pass
        use_unified_route = self._gandalf.allows('desktop-use-unified-preview-routes', account)
        is_preview_url = '.dropbox.com/preview' in link
        source = PreviewEntryPoint.NOTIFICATION_HANDOFF if is_preview_url else PreviewEntryPoint.NOTIFICATION
    # WARNING: Decompyle incomplete

    
    def _open_file(self = None, account = None, server_path = None, backup_url_path = (None, True), open_natively = ('account', 'AccountInterface', 'server_path', 'str', 'backup_url_path', 'Optional[str]', 'open_natively', 'Optional[Union[bool, str]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    _maybe_highlight_file = (lambda self = None, account = None, server_path = GlobalPool.dispatched_as_4('_maybe_highlight_file'), backup_url_path = ('account', 'AccountInterface', 'server_path', 'str', 'backup_url_path', 'Optional[str]', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    
    def _open_folder(self = None, account = None, server_path = None, backup_url_path = (None, False), force_open_in_cb = ('account', 'AccountInterface', 'server_path', 'str', 'backup_url_path', 'Optional[Text]', 'force_open_in_cb', 'Optional[bool]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _open_preferences(self = None, account = None, view_name = None):
        TRACE('_open_preferences notification action')
    # WARNING: Decompyle incomplete

    
    def _on_tray_icon_click(self = None, account = None):
        TRACE('_on_tray_icon_click notification action')
    # WARNING: Decompyle incomplete

    
    def _open_in_foreground_surface(self = None, account = None, url_path = None, is_dir = (False,)):
        if not self._gandalf:
            return False
        surface = get_open_in_dropbox_foreground_surface(self._gandalf, account)
        if surface is OpenInDropboxForegroundSurface.OFF:
            return False
        if not is_url_allowed_for_foreground_surface(url_path, gandalf = self._gandalf, account = account):
            return False
        if None.startswith('http://') or url_path.startswith('https://'):
            parsed = urlparse(url_path)
            initial_path = parsed.path
            if parsed.query:
                initial_path = f'''{initial_path}?{parsed.query}'''
            else:
                initial_path = url_path
        if not initial_path.startswith('/'):
            initial_path = f'''/{initial_path}'''
        
        try:
            if surface is OpenInDropboxForegroundSurface.APP_SHELL:
                launch_appshell(account, initial_path, 'notification', is_dir = is_dir, target_view = AppShellViews.LIBRARY)
            return True
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.FOREGROUND_SURFACE)
            return False


    
    def _open_url(self, account, url_path = None, local_preview_file_id = None, file_name = None, comment_thread_id = (None, None, None, False), is_dir = ('account', 'AccountInterface', 'url_path', 'Text', 'local_preview_file_id', 'Optional[Text]', 'file_name', 'Optional[Text]', 'comment_thread_id', 'Optional[Text]', 'is_dir', 'bool', 'return', 'None')):
        TRACE('_open_url notification action')
        preview_esv_was_opened = self._open_link_in_previews(account, url_path)
        if preview_esv_was_opened:
            TRACE('_open_url notification action: opened url in ESV Previews')
            return None
        if None._open_in_foreground_surface(account, url_path, is_dir = is_dir):
            TRACE('_open_url notification action: opened in foreground surface')
            return None
    # WARNING: Decompyle incomplete

    
    def _open_cloud_doc(self, account, fileid = None, extension = None, url_query = None, url_path = ('account', 'AccountInterface', 'fileid', 'Text', 'extension', 'Text', 'url_query', 'Text', 'url_path', 'Text', 'return', 'None')):
        TRACE('_open_cloud_doc notification action: opening url')
    # WARNING: Decompyle incomplete

    
    def _open_standalone_server_view(self, account, url_path = None, backup_url_path = None, stormcrow_rule_name = None, width = (800, 600), height = ('account', 'AccountInterface', 'url_path', 'Text', 'backup_url_path', 'Text', 'stormcrow_rule_name', 'Text', 'width', 'int', 'height', 'int', 'return', 'None')):
        TRACE('_open_standalone_server_view notification action')
        if self._desktop_login:
            TRACE('_open_standalone_server_view notification action: opening url instead')
            self._desktop_login.login_and_redirect(backup_url_path, account = account)
            return None

    
    def _open_zoom(self = None, account = None, client_url_path = None, web_url_path = ('account', 'AccountInterface', 'client_url_path', 'str', 'web_url_path', 'str', 'return', 'None')):
        TRACE('_open_zoom notification action')
        if not dropbox_url_info.launch_custom_url(client_url_path):
            TRACE('_open_zoom notification action: opening on web')
            dropbox_url_info.launch_full_url(web_url_path)
            return None

    
    def _mount_shared_folder(self = None, account = None, ns_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _show_selsync(self, account):
        TRACE('_show_selsync notification action')
    # WARNING: Decompyle incomplete

    
    def _show_error_dialog(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _show_shared_content_insufficient_quota_dialog(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _show_ns_limit_too_many_mounts_error_dialog(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _copy_link(self = None, account = None, path = None):
        TRACE('_copy_link notification action')
        server_path = MRCasedServerPath(path)
        if not self._sync_engine_adapter:
            TRACE('_copy_link notification action: sync engine is not ready')
            return None
        nucleus = None._sync_engine_adapter.nucleus_api(account)
        if not nucleus:
            TRACE('_copy_link notification action: sync engine is not ready')
            return None
        file_id = None.mr_server_to_fileid(server_path).block().result()
        if not file_id:
            TRACE('_copy_link notification action: file id not found')
            return None
        local_props = None.lookup_local_properties_by_fileid(file_id).block().result()
        if not local_props:
            TRACE('_copy_link notification action: local file not found')
            return None
        is_dir = isinstance(local_props.file_type, LocalDirectoryProperties)
    # WARNING: Decompyle incomplete

    
    def _unlock(self = None, account = None, path = None):
        TRACE('_unlock notification action')
        server_path = MRCasedServerPath(path)
        if not self._sync_engine_adapter:
            TRACE('_unlock notification action: sync engine is not ready')
            return None
        nucleus = None._sync_engine_adapter.nucleus_api(account)
        if not nucleus:
            TRACE('notification notification action: sync engine is not ready')
            return None
        FileLockingAccessor.handle_context_menu_unlock(account, server_path)

    
    def _open_view(self, account = None, manifest_name = None, parameter_json = None, stormcrow_rule_name = (None, None, None), backup_url_path = ('account', 'AccountInterface', 'manifest_name', 'str', 'parameter_json', 'Optional[str]', 'stormcrow_rule_name', 'Optional[str]', 'backup_url_path', 'Optional[str]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_user_context(self = None, account = None):
