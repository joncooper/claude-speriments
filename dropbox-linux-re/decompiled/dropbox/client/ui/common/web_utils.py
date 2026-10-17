# Source Generated with Decompyle++
# File: web_utils.pyc (Python 3.11)

from typing import List, Optional, Text
from six.moves.urllib import parse as urlparse
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def launch_share_on_web(local_path_prop = None, app = None, account = None):
    rr_server_path = local_path_prop.rr_server_path()
    (ns_id, rel_path) = rr_server_path.ns_rel()
    file_or_folder_path = urlparse.quote(rel_path.encode('utf-8'))
    browse_path = f'''/c/browse{file_or_folder_path}?ns_id={ns_id}'''
    full_url = app.dropbox_url_info.construct_url_path(browse_path, query_pieces = [
        'share=true'])
# WARNING: Decompyle incomplete


def _launch_transfer_with_props(props_list = None, account = None, app = None):
    file_ids = (lambda .0: pass# WARNING: Decompyle incomplete
)(props_list())
    role = Roles.to_server(account.role) if account.role else None
    browse_path = '/transfer'
    query_pieces = []
    if file_ids:
        query_pieces.append(f'''fileids={file_ids}''')
    if role:
        query_pieces.append(f'''role={role}''')
    full_url = app.dropbox_url_info.construct_url_path(browse_path, query_pieces = query_pieces)
# WARNING: Decompyle incomplete


def launch_transfer_on_web(path_list = None, app = None, account = None):
    pass
# WARNING: Decompyle incomplete

