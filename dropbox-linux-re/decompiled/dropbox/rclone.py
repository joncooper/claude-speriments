# Source Generated with Decompyle++
# File: rclone.pyc (Python 3.11)

import ctypes
import json
import os
import threading
from typing import Dict, Iterable, Optional, Text, TYPE_CHECKING
from build_number import BuildChannel, get_build_channel, is_frozen
from build_number.features import feature_enabled
from dropbox.client.util import get_contents_root, get_repo_root_unfrozen
from dropbox.client_typing import JSONable
from dropbox.platform import IS_LINUX
if TYPE_CHECKING:
    from apex.auth import OAuthClient
    from apex.context import ApexContext
    from dropbox.client.authentication.account_interface import AccountInterface
_LIBRCLONE_NAME = 'libdropbox_rclone.so'
_REDACTED = '[redacted]'
JSONDict = Dict[(Text, JSONable)]

def rclone_enabled():
    return feature_enabled('rclone')


class RcloneException(Exception):
    pass
# WARNING: Decompyle incomplete


class _RcloneRPCResult(ctypes.Structure):
    _fields_ = [
        ('Output', ctypes.c_void_p),
        ('Status', ctypes.c_int)]

_lock = threading.RLock()
_librclone: 'Optional[ctypes.CDLL]' = None
_initialized = False

def _find_librclone():
    if not IS_LINUX:
        raise RuntimeError('librclone is only packaged for Linux')
    if is_frozen() and os.environ.get('BAZEL_TEST'):
        return os.path.join(get_repo_root_unfrozen(), 'app', 'linux', _LIBRCLONE_NAME)
    return None.path.join(get_contents_root(), _LIBRCLONE_NAME)


def _load_librclone():
    _lock
    if not rclone_enabled():
        raise RuntimeError('rclone is disabled by the rclone feature')
# WARNING: Decompyle incomplete


def configure_logging(apex_context = None, *, debug_logging):
    _load_librclone().RcloneSetupLoggingForApex(ctypes.c_void_p(apex_context.raw_ptr()))
    log_level = 'NOTICE'
# WARNING: Decompyle incomplete


def _redact_secrets(value = None, secret_values = None):
    pass
# WARNING: Decompyle incomplete


def _sanitize_error_output(output = None, secret_values = None):
    pass
# WARNING: Decompyle incomplete


def _rpc(method = None, input_data = None, secret_values = None):
    librclone = _load_librclone()
# WARNING: Decompyle incomplete


def rpc(method = None, input_data = None):
    return _rpc(method, input_data)


def _retrieve_oauth_access_token(oauth_client = None, account = None):
    access_token = oauth_client.retrieve_access_token(str(account.account_id)).result()
    if not access_token:
        raise RuntimeError('Failed to retrieve OAuth access token for rclone')
    return access_token


def mount_dropbox(oauth_client = None, account = None, mount_point = None, *, remote_root, mount_options, vfs_options):
    access_token = _retrieve_oauth_access_token(oauth_client, account)
    token = {
        'access_token': access_token,
        'token_type': 'Bearer' }
    input_data = {
        'fs': {
            'type': 'dropbox',
            '_root': remote_root,
            'token': json.dumps(token) },
        'mountPoint': mount_point,
        'mountType': 'mount' }
# WARNING: Decompyle incomplete


def unmount(mount_point = None):
    _rpc('mount/unmount', {
        'mountPoint': mount_point })


def run_atexit_handlers():
    _lock
    librclone = _librclone if _initialized else None
    None(None, None)
# WARNING: Decompyle incomplete


def finalize():
    _lock
# WARNING: Decompyle incomplete

