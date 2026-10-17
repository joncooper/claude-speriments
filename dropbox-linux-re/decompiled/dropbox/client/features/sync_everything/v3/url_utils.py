# Source Generated with Decompyle++
# File: url_utils.pyc (Python 3.11)

from typing import Dict, Optional
from urllib import parse as urlparse
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.multiaccount.role import Roles
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.model.types import FileId
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
_fileid_to_server_path = (lambda user_context = None, fileid = None: handle_response = (lambda remote_props = None: if not remote_props:
ResolvedFuture(None)ResolvedFuture(remote_props.rr_server_path))()
    if not fileid:
        return ResolvedFuture(None)
    nucleus_wrapper = destroying(NucleusWrapper.from_context(user_context))
    None(None, None)
    return 
    with None:
        if not None, nucleus_wrapper().lookup_remote_properties_by_fileid(fileid).then(handle_response):
            pass
)()
open_server_folder = (lambda user_context = None, server_path = None, client_route = future_function: account = user_context.account(ns_id, rel_path) = server_path.ns_rel()webpath = f'''c/{client_route!s}{urlparse.quote(rel_path)!s}?ns_id={ns_id!s}'''login_arc = destroying(DesktopLoginWrapper.from_context(user_context))login_arc().login_and_redirect(webpath, account = account)None(None, None)with None:
if not None, ResolvedFuture(None):
pass)()
open_client_route_on_server_by_device_name = (lambda user_context = None, client_route = None, device_name = future_function: account = user_context.accountif not account.home_ns_id:
report_bad_assumption('Account missing home namespace. Cannot open home path.')ResolvedFuture(None)server_path = RRCasedServerPath.from_ns_rel(account.home_ns_id, '/' + device_name)open_server_folder(user_context, server_path, client_route))()
open_account_plan_on_server = (lambda user_context = None: account = user_context.accountwebpath = '/account/plan'params = { }if account.role:
params['role'] = Roles.to_server(account.role)webpath += '?%s' % urlparse.urlencode(params)login_arc = destroying(DesktopLoginWrapper.from_context(user_context))login_arc().login_and_redirect(webpath, account = account)None(None, None)with None:
if not None, ResolvedFuture(None):
pass)()
open_backup_on_web_by_name = (lambda user_context = None, device_name = None, params = future_function: pass# WARNING: Decompyle incomplete
)()
open_backup_all_on_web = (lambda user_context = None, params = None: pass# WARNING: Decompyle incomplete
)()
