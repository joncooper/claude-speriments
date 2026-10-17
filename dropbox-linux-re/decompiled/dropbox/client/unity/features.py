# Source Generated with Decompyle++
# File: features.pyc (Python 3.11)

from typing import Any, Callable, Dict, List, Optional, Text, Tuple
from six import iterkeys
from six.moves.urllib import parse as urlparse
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.interface import AccountManagerInterface as LegacyAccountManagerInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.gandalf import Gandalf
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client.unity.connection import INSECURE_WEB_PERMISSION, SECURE_LOCAL_PERMISSION, SECURE_PERMISSION, UnityServer
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.foundation.futures.basic import ResolvedFuture
from dropbox.foundation.native_file_opener.bridge_gen.file_open_bridge_result import FileOpenBridgeResult
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.native_file_opener.bridge_gen.file_open_path import FileOpenPath
from dropbox.foundation.native_file_opener.bridge_gen.file_open_type import FileOpenType
from dropbox.foundation.native_file_opener.bridge_gen.path_open_properties import PathOpenProperties
from dropbox.foundation.native_file_opener.impl import ContextBoundNativeFileOpener
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.functions import EitherStr, file_extension, md5_hash
from dropbox.i18n import trans
from dropbox.model.types import FileId
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.exceptions import NamespaceNotMountedError, UnmountedPathError
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
if IS_WINDOWS:
    from dropbox.win32.version import WIN8, WINDOWS_VERSION
on_background_thread_future = make_on_thread_future_decorator(on_background_thread, 'on_background_thread_future')

class UnityFeatures(object):
    _LOGIN_COMPLETE_REDIRECT_URL = 'login_complete'
    
    def __init__(self, unity_server, account, desktop_login, gandalf, ui_kit = None, legacy_account_manager = None, account_manager = None, sync_engine_adapter = ('unity_server', 'UnityServer', 'account', 'Account', 'desktop_login', 'DesktopLogin', 'gandalf', 'Gandalf', 'ui_kit', 'BaseUIKit', 'legacy_account_manager', 'LegacyAccountManagerInterface', 'account_manager', 'AccountManager', 'sync_engine_adapter', 'SyncEngineAdapter', 'return', 'None')):
        self._unity_server = unity_server
        self._account = account
        self._desktop_login = desktop_login
        self._gandalf = gandalf
        self._ui_kit = ui_kit
        self._legacy_account_manager = legacy_account_manager
        self._account_manager = account_manager
        self._sync_engine_adapter = sync_engine_adapter
        unity_server.add_feature_handler('check_file', self._check_file, asynchronous = True)
        unity_server.add_feature_handler('check_file_batch', self._check_file_batch, asynchronous = True)
        unity_server.add_feature_handler('continue_as_user', self._continue_as_user, allowed_permissions = [
            INSECURE_WEB_PERMISSION])
        unity_server.add_feature_handler('continue_as_user_direct', self._continue_as_user_direct, allowed_permissions = [
            INSECURE_WEB_PERMISSION])
        unity_server.add_feature_handler('continue_as_user_oauth_webview', self._continue_as_user_oauth_webview, allowed_permissions = [
            INSECURE_WEB_PERMISSION])
        unity_server.add_feature_handler('web_destiny_info', self._web_destiny_info, allowed_permissions = [
            INSECURE_WEB_PERMISSION])
        unity_server.add_feature_handler('file_browser_display_name', self._file_browser_display_name)
        unity_server.add_feature_handler('open_file', self._open_file, asynchronous = True)
        unity_server.add_feature_handler('show_shared_content_dialog', self._show_shared_content_dialog, allowed_permissions = [
            SECURE_LOCAL_PERMISSION])
        unity_server.add_feature_handler('has_chime', self._has_chime)
        unity_server.add_feature_handler('can_open_apollo', self._can_open_apollo, allowed_permissions = [
            SECURE_PERMISSION,
            INSECURE_WEB_PERMISSION])
        unity_server.add_feature_handler('open_apollo_main_window', self._open_apollo_main_window, allowed_permissions = [
            SECURE_PERMISSION,
            INSECURE_WEB_PERMISSION])

    
    def _get_account_by_user_id(self = None, user_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_user_context(self = None, account = None):
        account_model = self._account_manager.account_models.get(account)
    # WARNING: Decompyle incomplete

    
    def _convert_path_props_to_dict(self = None, path_props = None):
        return {
            'is_locally_available': path_props.local_path is not None,
            'can_open_directly': path_props.file_open_type == FileOpenType.FILE,
            'open_application_identifier': path_props.app_for_file,
            'open_application_name': path_props.app_display_name,
            'path_is_dir': path_props.file_open_type == FileOpenType.DIR }

    
    def _with_native_file_opener(self = None, user_context = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_file(self = None, server_path = None, user_id = None, on_complete = ('server_path', 'Text', 'user_id', 'int', 'on_complete', 'Callable[[Dict[Text, Any]], None]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_file_batch(self = None, server_paths = None, user_id = None, on_complete = ('server_paths', 'List[Text]', 'user_id', 'int', 'on_complete', 'Callable[[Dict[Text, Dict[Text, Any]]], None]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _continue_as_user(self, browser, refresh_token):
        if not self._gandalf_variant_allows_destiny():
            return None
        None._unity_server.logger.report_event('continue_as_user', refresh_token = refresh_token)
        query_params = '?' + urlparse.urlencode({
            'refresh_token': refresh_token })
        self._desktop_login.login_and_redirect(self._LOGIN_COMPLETE_REDIRECT_URL + query_params, browser, account = self._account)

    
    def _continue_as_user_oauth_webview(self = None, app_id = None, url = None):
        if not self._gandalf_variant_allows_destiny():
            return None
        None._unity_server.logger.report_event('continue_as_user_oauth_webview')
        query = [
            ('response_type', 'token'),
            ('client_id', app_id),
            ('redirect_uri', url),
            ('disable_signup', 'true')]
        query_pieces = query()
        path = dropbox_url_info.construct_url_path(path = '1/oauth2/authorize', query_pieces = query_pieces)
        return {
            'url': self._desktop_login.create_file_url_for_redirect(path) }

    
    def _continue_as_user_direct(self):
        if not self._gandalf_variant_allows_destiny() and self._gandalf.allows('desktop-web-destiny-direct', account = self._account) or self._unity_server.is_flash_policy_server_secure():
            return None
        None._unity_server.logger.report_event('continue_as_user_direct')
        return self._desktop_login.get_login_credentials()()

    
    def _web_destiny_info(self):
