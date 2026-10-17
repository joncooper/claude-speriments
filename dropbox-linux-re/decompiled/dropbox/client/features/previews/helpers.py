# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from typing import Any, Dict, Optional, Text
from six.moves import urllib
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.features.previews.constants import PreviewActions, PreviewEntryPoint, PREVIEWS_UNSUPPORTED_EXTENSIONS
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.components.desktop_components import DesktopComponent
from dropbox.functions import file_extension
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.url_info import dropbox_url_info
DESKTOP_USE_UNIFIED_PREVIEW_ROUTES = 'desktop-use-unified-preview-routes'

def normalize_and_sign_url(url = None, account = None):
    parsed_url = urllib.parse.urlparse(url)
# WARNING: Decompyle incomplete


def report_preview_event(account = None, event_action = None, extra = None, source = (None, None, None), session_id = ('account', 'AccountInterface', 'event_action', 'PreviewActions', 'extra', 'Optional[Dict[str, Any]]', 'source', 'Optional[str]', 'session_id', 'Optional[str]', 'return', 'None')):
    event = NonUserLoggingEvent(event_name = event_action.value, feature_session_id = session_id if session_id else '', action_surface = 'preview_window', source = source if source else '', component = DesktopComponent.FILE_VIEWER, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(event, account)


def launch_preview(event_hub, account, session_id, source, login_and_redirect, local_path, local_path_props, is_server_path, server_path = None, file_id = None, use_unified_route = None, is_shared_link = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'session_id', 'Text', 'source', 'PreviewEntryPoint', 'login_and_redirect', 'Any', 'local_path', 'Optional[LocalPath]', 'local_path_props', 'Optional[LocalPathProperties]', 'is_server_path', 'Optional[bool]', 'server_path', 'Optional[str]', 'file_id', 'Optional[str]', 'use_unified_route', 'bool', 'is_shared_link', 'Optional[bool]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def launch_preview_with_local_path(event_hub, account, session_id, source, file_id, local_path = None, local_path_props = None, login_and_redirect = None, use_unified_route = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'session_id', 'Text', 'source', 'PreviewEntryPoint', 'file_id', 'str', 'local_path', 'LocalPath', 'local_path_props', 'LocalPathProperties', 'login_and_redirect', 'Any', 'use_unified_route', 'bool', 'return', 'None')):
    extension = file_extension(Text(local_path))
    (ns_id, rel_path) = local_path_props.mr_server_path().ns_rel()
    if use_unified_route:
        is_pdf_supported = extension == 'pdf'
        unsupported_extensions = list(PREVIEWS_UNSUPPORTED_EXTENSIONS)
        if is_pdf_supported:
            unsupported_extensions.remove('pdf')
    if extension in unsupported_extensions:
        return launch_preview_in_browser(login_and_redirect = login_and_redirect, account = account, session_id = session_id, extension = extension, ns_id = ns_id, rel_path = rel_path)
    None.launch_journey(UserJourneyNames.PREVIEW_FLOW, session_id, {
        'nsId': ns_id,
        'relativePath': rel_path,
        'sessionId': session_id,
        'localPath': Text(local_path),
        'extension': file_extension(Text(local_path)),
        'fileId': file_id,
        'account': convert_to_local_account(account),
        'rootRelativePath': local_path_props.rr_server_path().rel,
        'unifiedPreviewEnabled': use_unified_route,
        'source': source.value,
        'webserverHost': dropbox_url_info.webserver_host }).ground(component = DesktopComponent.FILE_VIEWER)
    extras = {
        'extension': extension }
    report_preview_event(account, PreviewActions.VIEW_LAUNCHED, extras, source.value, session_id)


def launch_preview_with_server_path(event_hub, account, session_id, source, file_id = None, server_path = None, login_and_redirect = None, use_unified_route = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'session_id', 'Text', 'source', 'PreviewEntryPoint', 'file_id', 'str', 'server_path', 'str', 'login_and_redirect', 'Any', 'use_unified_route', 'bool', 'return', 'None')):
    rr_server_path = RRCasedServerPath(server_path)
    (ns_id, rel_path) = rr_server_path.ns_rel()
    extension = file_extension(Text(server_path))
    if use_unified_route:
        is_pdf_supported = extension == 'pdf'
        unsupported_extensions = list(PREVIEWS_UNSUPPORTED_EXTENSIONS)
        if is_pdf_supported:
            unsupported_extensions.remove('pdf')
    if extension in unsupported_extensions:
        return launch_preview_in_browser(login_and_redirect = login_and_redirect, account = account, session_id = session_id, extension = extension, ns_id = ns_id, rel_path = rel_path)
    None.launch_journey(UserJourneyNames.PREVIEW_FLOW, session_id, {
        'nsId': ns_id,
        'relativePath': rel_path,
        'serverPath': Text(server_path),
        'extension': file_extension(Text(server_path)),
        'fileId': file_id,
        'account': convert_to_local_account(account),
        'rootRelativePath': rel_path,
        'unifiedPreviewEnabled': use_unified_route,
        'source': source.value,
        'webserverHost': dropbox_url_info.webserver_host }).ground(component = DesktopComponent.FILE_VIEWER)
    extras = {
        'extension': extension,
        'server_path': True }
    report_preview_event(account, PreviewActions.VIEW_LAUNCHED, extras, source.value, session_id)


def launch_preview_in_browser(login_and_redirect, account, session_id = None, extension = None, ns_id = None, rel_path = ('login_and_redirect', 'Any', 'account', 'AccountInterface', 'session_id', 'Text', 'extension', 'str', 'ns_id', 'Any', 'rel_path', 'Any', 'return', 'None')):
    uri = f'''c/{'browse'!s}{urllib.parse.quote(rel_path.encode('utf-8'))!s}?ns_id={ns_id!s}'''
    extras = {
        'extension': extension,
        'unsupported_file_extension': extension in PREVIEWS_UNSUPPORTED_EXTENSIONS }
    login_and_redirect(uri, account = account)
    report_preview_event(account, PreviewActions.VIEW_LAUNCHED, extras, 'browser', session_id)


def launch_shared_link_preview(event_hub, account, session_id, source = None, file_id = None, server_path = None, use_unified_route = ('event_hub', 'EventHub', 'account', 'AccountInterface', 'session_id', 'Text', 'source', 'PreviewEntryPoint', 'file_id', 'Optional[str]', 'server_path', 'str', 'use_unified_route', 'bool', 'return', 'None')):
    server_path_without_query_params = server_path.split('?')[0]
    event_hub.launch_journey(UserJourneyNames.PREVIEW_FLOW, session_id, {
        'relativePath': server_path,
        'serverPath': Text(server_path),
        'extension': file_extension(Text(server_path_without_query_params)),
        'fileId': file_id,
        'account': convert_to_local_account(account),
        'rootRelativePath': server_path,
        'unifiedPreviewEnabled': use_unified_route,
        'source': source.value,
        'webserverHost': dropbox_url_info.webserver_host }).ground(component = DesktopComponent.FILE_VIEWER)

