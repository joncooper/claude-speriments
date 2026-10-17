# Source Generated with Decompyle++
# File: device_anchor_opener.pyc (Python 3.11)

from functools import partial
from typing import cast, Iterable, List, NamedTuple, Optional, Text, Tuple
from urllib import parse as urlparse
from dropbox.client.authentication.account import Account
from dropbox.client.features.backup_common.constants import EDB_ANCHOR_EXTENSION
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.file_activation.constants import FileActivationError
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.file_activation.interface import ExtensionHandler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, Severity, UnexpectedNoneError
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.trace import TRACE
DeviceAnchorInfoWithLocalProp = NamedTuple('DeviceAnchorInfoWithLocalProp', [
    ('local_path_properties', Optional[LocalPathProperties]),
    ('device_anchor_info', Optional[DeviceAnchorInfo])])

class DeviceAnchorOpener(ExtensionHandler):
    _get_device_anchor_info = (lambda self = None, user_context = FutureHelpers.flatten, properties = GlobalPool.dispatched_as_3('DeviceAnchorOpener._get_device_anchor_info'): pass# WARNING: Decompyle incomplete
)()()
    
    def handle_open(self = None, files = None):
        pass
    # WARNING: Decompyle incomplete

    _open_device_anchor = (lambda self = None, desktop_login_wrapper = None, anchor_info_result = GlobalPool.dispatched_as_3('DeviceAnchorOpener._open_device_anchor'): if not anchor_info_result and anchor_info_result.device_anchor_info or anchor_info_result.local_path_properties:
raise UnexpectedNoneError('DeviceAnchorOpener info is not passed to open the target')(ns_id, rel_path) = anchor_info_result.local_path_properties.mr_server_path().ns_rel()get_params = []get_params.append(('ns_id', f'''{ns_id!s}'''))stringified_get_params = (lambda .0: [ '%s=%s' % get_param for get_param in .0 ])(get_params())
        desktop_login_wrapper().login_and_redirect(f'''c/browse{urlparse.quote(rel_path.encode('utf-8'))!s}?{stringified_get_params!s}''')
)()
    
    def handle_error(self = None, errors = None):
        for filename, error, open_info in errors:
            TRACE('Opener error on file %r: %r, open info %r', filename, error, open_info)
            return None

    handled_extensions = (lambda cls = None: [
EDB_ANCHOR_EXTENSION])()

