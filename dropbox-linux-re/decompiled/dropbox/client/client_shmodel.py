# Source Generated with Decompyle++
# File: client_shmodel.pyc (Python 3.11)

import json
import re
import uuid
from enum import Enum
from functools import partial
from time import time as _time
from typing import Any, Callable, cast, Dict, Optional, Text
from urllib.parse import unquote
from apex.metrics import Metric
from six.moves.urllib import parse as urlparse
from build_number.features import feature_enabled
from dropbox.api.v2.datatypes.sharing import AlphaCreateSharedLinkWithSettingsArg, AlphaSharedLinkSettings, CreateSharedLinkWithSettingsArg, ListSharedLinksArg, PendingUploadMode, RequestedLinkAccessLevel, SharedLinkSettings
from dropbox.assertions import assert_
from dropbox.async_timers import async_timers
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.features.notification_dialog.utils import launch_copy_link_share_view
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.tray.events import TrayEventReporter
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client_api.apiv2.generated.sharing import Sharing
from dropbox.client_api.connection.exceptions import APIv2EndpointError
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.client_api.exceptions import HTTP409Error, is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import report
from dropbox.event_names import ASSISTANT_CLIENT_TRAY_EVENTS
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.functions import snippet
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, ServerPath
from dropbox.shared.util import safe_navigate
from dropbox.sharing.capture_pap_logger import log_to_pap_for_eligible_events
from dropbox.sharing.sharing_logger import ShareDesktopTiburonEvent
from dropbox.sharing.utils.link_util import get_link_type_from_url
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.sync_engine_boundary.types.sync_queue import SyncPriority
from dropbox.threading import Lock
from dropbox.threadutils import SafeValue
from dropbox.tiburon_log import log_tiburon_event, log_tiburon_event_with_server_path, redact_shared_link_url
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
CLIENT_SHMODEL_UI_TIMEOUT = 30
COPY_DROPBOX_LINK_STORMCROW = 'desktop-copy-link-notification'
MEV_NOTIFICATION_COPY_LINK_WHITELIST = [
    NotificationDialogEntryPoint.FINDER_CONTEXT_MENU]
_AMP_NAMESPACE = 'desktop_client_shmodel'

class ClientShmodelStrings(UIStrings):
    shmodel_working_caption = UI("Copied link on '%(file)s'")
    screenshots_shmodel_working_caption = UI('Sharing Screenshot')
    screenrecordings_shmodel_working_caption = UI('Sharing Screen Recording')
    shmodel_browse_taking_long = UI("We'll open the link in your web browser in just a moment")
    shmodel_clipboard_taking_long = UI("We'll copy the link to your clipboard in just a moment")
    shmodel_clipboard_finished = UI("A link to '%(file)s' was copied to your clipboard.")
    screenshots_shmodel_clipboard_finished = UI('A link to your screenshot was copied to your clipboard.')
    screenrecordings_shmodel_clipboard_finished = UI('A link to your screen recording was copied to your clipboard.')
    screenshots_shmodel_working_caption_pending = UI('Link copied. Screenshot is almost ready.')
    screenshots_shmodel_clipboard_finished_pending = UI('The screenshot will be viewable once it finishes uploading.')
    screenrecordings_shmodel_working_caption_pending = UI('Link copied. Screen recording is almost ready.')
    screenrecordings_shmodel_clipboard_finished_pending = UI('The screen recording will be viewable once it finishes uploading.')
    screenshots_open_in_finder = UI('Show in Finder')
    screenshots_open_in_explorer = UI('Show in Explorer')
    screenshots_open_in_dropbox = UI('Show in Dropbox')
    shmodel_error_caption = UI("Couldn't copy link")
    shmodel_error_summary = UI('We’ve interrupted your sharing activity. For details or to contact support, read our help center article.')
    shmodel_error_generic = UI("Something went wrong. We're working to fix it.")
    shmodel_error_timeout = UI('The server took too long to respond.  Please try again later.')
    shmodel_error_connection = UI('Check your internet connection and try again.')
    shmodel_error_not_yet_uploaded = UI("The file isn't uploaded yet")
    shmodel_error_deleted_or_moved = UI('The file was deleted or moved')
    shmodel_error_links_disabled = UI('Your shared links are disabled. Please contact Dropbox Support for assistance.')
    shmodel_error_over_quota = UI("You're out of Dropbox space!")
    snapshot_working_caption = UI('Sharing snapshot')
    snapshot_clipboard_finished = UI("A link to your snapshot of '%(file)s' has been copied to your clipboard.")
    snapshot_finished = UI('A link to your snapshot has been copied to your clipboard.')


class ClientShmodelOrigin(Enum):
    UNKNOWN = 'unknown'
    TRAY_RECENTLY_CHANGED = 'tray-recently-changed'
    CONTEXT_MENU = 'context-menu'
    SCREENSHOTS = 'screenshots'
    SCREENRECORDINGS = 'screenrecordings'
    HARMONY = 'harmony'
    OFFICE_ADDIN = 'office_addin'
    APOLLO = 'apollo'
    TRAY_SUGGESTED_FILE = 'tray-suggested-file'

CaptureSharedLinkTypes = {
    ClientShmodelOrigin.SCREENRECORDINGS: 'recording',
    ClientShmodelOrigin.SCREENSHOTS: 'screenshot' }

class _ClientSharingThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

ClientSharingThread = db_thread(_ClientSharingThreadImpl)
on_sharing_thread_returns_none = ClientSharingThread.on_queue_returns_none

class _ClientSharingNetworkThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

ClientSharingNetworkThread = db_thread(_ClientSharingNetworkThreadImpl)
on_sharing_network_thread = ClientSharingNetworkThread.on_queue

class SharedLinkException(Exception):
    pass


class ClientShmodel(object):
    
    def __init__(self = None, app = None):
        self.app = app
        self._active_request = None
        self._active_request_lock = Lock()
        self._thread = ClientSharingThread()
        self._network_thread = ClientSharingNetworkThread()

    
    def start(self):
        
        try:
            self._thread.start()
        except RuntimeError:
            pass

        
        try:
            self._network_thread.start()
            return None
        except RuntimeError:
            return None


    
    def shmodel_to_clipboard_async(self, account, server_path, is_dir, origin, local_path, file_id, success_callback, error_callback, title = None, is_capture_link = None, source = None, is_from_user_action = (None, None, None, None, None, None, False, None, True, False), is_from_screenshots_without_loud_notification = ('account', 'AccountInterface', 'server_path', 'ServerPath', 'is_dir', 'bool', 'origin', 'Optional[ClientShmodelOrigin]', 'local_path', 'Optional[LocalPath]', 'file_id', 'Optional[Text]', 'success_callback', 'Optional[Callable[[str], None]]', 'error_callback', 'Optional[Callable[[str], None]]', 'title', 'Optional[str]', 'is_capture_link', 'Optional[bool]', 'source', 'Optional[NotificationDialogEntryPoint]', 'is_from_user_action', 'Optional[bool]', 'is_from_screenshots_without_loud_notification', 'Optional[bool]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _report_link_match_to_amp(self = None, matched = None):
        
        try:
            metric_reporter = self.app.app_model.machine_context.metrics_reporter
            metric_reporter.create_stats(Metric(_AMP_NAMESPACE, 'copy_shared_link'), {
                'matched': str(matched) }).record(1)
            return None
        except Exception:
            return None


    
    def shmodel_from_localpath_async(self = None, account = None, local_path = None, origin = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_user_context_for_account(self = None, account = None):
        account_models = self.app.app_model.account_manager.account_models_all if feature_enabled('multi-team-accounts-prod') else self.app.app_model.account_manager.account_models
        account = cast(Account, account)
        account_model = account_models.get(account)
    # WARNING: Decompyle incomplete

    
    def _new_request(self = None):
        self._active_request_lock
        self._active_request = object()
        None(None, None)
        return 
        with None:
            if not None, self._active_request:
                pass

    
    def _deactivate_request(self = None, request = None):
        self._active_request_lock
        if request is self._active_request:
            self._active_request = None
            None(None, None)
            return True
        None(None, None)
        return False
        with None:
            if not None:
                pass

    
    def _bubble_success(self, local_path, server_path, link, origin, msg, is_non_rel_link, account, title = None, file_id = None, source = None, is_from_screenshots_without_loud_notification = (None, None, None, None, False, False), used_pending_upload_fallback = ('local_path', 'Optional[LocalPath]', 'server_path', 'ServerPath', 'link', 'Text', 'origin', 'ClientShmodelOrigin', 'msg', 'Optional[Text]', 'is_non_rel_link', 'bool', 'account', 'Optional[AccountInterface]', 'title', 'Optional[str]', 'file_id', 'Optional[Text]', 'source', 'Optional[NotificationDialogEntryPoint]', 'is_from_screenshots_without_loud_notification', 'Optional[bool]', 'used_pending_upload_fallback', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _open_help_article(self = None):
        if self.app.desktop_login:
            self.app.desktop_login.login_and_redirect('https://help.dropbox.com/share/banned-links')
            return None

    
    def _bubble_error(self = None, server_path = None, error = None, error_msg = (None,), account = ('server_path', 'ServerPath', 'error', 'str', 'error_msg', 'Optional[Text]', 'account', 'Optional[AccountInterface]', 'return', 'None')):
        TRACE('shmodel error: %r -> %s', Text(server_path), error)
        caption = ClientShmodelStrings.shmodel_error_caption
        surface_action = None
        if error_msg:
            message = ClientShmodelStrings.shmodel_error_summary
            surface_action = self._open_help_article
        else:
            
            try:
                message = ClientShmodelStrings[error]
            except KeyError:
                report_bad_assumption('Got unrecognized error: %r', error, full_stack = True)
                message = ClientShmodelStrings.shmodel_error_generic

            bubble = None
            if error == 'shmodel_error_over_quota':
                bubble = LoudNotification(LoudNotificationType.SHMODEL_ERROR, message, caption, self.app.bubble_context, surface_action = partial(self.app.desktop_login.login_and_redirect, 'c/getspace'), account = account, bypass_silent_mode = True)
            elif surface_action:
                bubble = LoudNotification(LoudNotificationType.SHMODEL_ERROR, message, caption, self.app.bubble_context, account = account, surface_action = surface_action, bypass_silent_mode = True)
            else:
                bubble = LoudNotification(LoudNotificationType.SHMODEL_ERROR, message, caption, account = account, bypass_silent_mode = True)
        self.app.ui_kit.show_bubble(bubble)

    
    def _user_clicked_shmodel_bubble(self = None, link = None, is_non_rel_link = None):
        if is_non_rel_link:
            self.app.dropbox_url_info.launch_full_url(link)
            return None
        url_toks = urlparse.urlsplit(link)
        link_rel = urlparse.urlunsplit(('', '') + url_toks[2:]).lstrip('/')
        self.app.desktop_login.login_and_redirect(link_rel)

    _get_shared_link_with_settings_async = (lambda self = None, account = None, server_path = on_sharing_network_thread, is_dir = (None, None), pending_upload = ('account', 'AccountInterface', 'server_path', 'ServerPath', 'is_dir', 'Optional[bool]', 'pending_upload', 'Optional[bool]', 'return', 'Dict[Text, Any]'): self._get_shared_link_with_settings_async_helper(account, server_path, is_dir, pending_upload))()
    
    def _get_shared_link_with_settings_async_helper(self = None, account = None, server_path = None, is_dir = (None, None), pending_upload = ('account', 'AccountInterface', 'server_path', 'ServerPath', 'is_dir', 'Optional[bool]', 'pending_upload', 'Optional[bool]', 'return', 'Dict[Text, Any]')):
        pass
    # WARNING: Decompyle incomplete

    _get_capture_link_async = (lambda self = None, account = None, server_path = on_sharing_network_thread, capture_type = ('account', 'AccountInterface', 'server_path', 'ServerPath', 'capture_type', 'Text', 'return', 'Dict[Text, Any]'): self._get_capture_link_async_helper(account, server_path, capture_type))()
    
    def _get_capture_link_async_helper(self = None, account = None, server_path = None, capture_type = ('account', 'AccountInterface', 'server_path', 'ServerPath', 'capture_type', 'Text', 'return', 'Dict[Text, Any]')):
        raise APIv2EndpointError('Capture API is deprecated', code = 404, error = b'capture_api_deprecated')

    _get_existing_shared_link_by_fileid_async = (lambda self = None, account = None, file_id = on_sharing_network_thread: if not file_id.startswith('id:'):
file_id = f'''id:{file_id}'''try:
list_shared_links_fut = Sharing.list_shared_links(self.app.conn, HostKeyAuth(account.host_secret), ListSharedLinksArg(path = file_id, direct_only = True))list_shared_links_fut.block()ret = list_shared_links_fut.result()for link_metadata in ret.links:
existing_url = getattr(link_metadata, 'url', None)if existing_url:
None, {
'url': existing_url }{
'url': None }except Exception:
if is_transient_error(e):
del eNonereport_exception(severity = Severity.WARN, component = DesktopComponent.SHARING)del eNoneNone = del e)()
    _will_use_pending_upload_fallback = (lambda location_props = None: 