# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

import base64
import json
import os
from json import JSONDecodeError
from typing import Any, cast, Dict, List, Optional, Text
from stone.backends.python_rsrc.stone_serializers import json_encode
from stone.backends.python_rsrc.stone_validators import ValidationError
from dropbox.api.v2.datatypes.ekms import AsymmetricEncryptionAlgorithm, AsymmetricEncryptionAlgorithm_validator
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.constants import AppDataPaths
from dropbox.client.features.encrypted_folder.client_key_pair import ClientKeyPair
from dropbox.client.features.encrypted_folder.constants import EncryptedFolderConstants
from dropbox.client.features.encrypted_folder.fingerprint import KeyFingerprint, TeamKeyFingerprint
from dropbox.client.features.encrypted_folder.key_crypto import generate_key_pair
from dropbox.client.features.encrypted_folder.strings import EncryptedFolderStrings
from dropbox.client.notifications.legacy_notifications import EncryptedFolderEnrollmentStickyNotification
from dropbox.client.ui.common.dialog_constants import IconType
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_assertion_error, report_bad_assumption, report_exception, report_unexpected_none
from dropbox.exception.severity import Severity
from dropbox.functions import retry, RetryException
from dropbox.i18n import trans
from dropbox.native_threading import NativeRecursiveMutex
from dropbox.proto.nucleus.published_event_pb2 import EncryptionErrorEvent
from dropbox.sqlite3_exceptions import DiskIOError
from dropbox.sync_engine_boundary.constants import SyncOperationFailureReason
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class EncryptedFolderManager:
    
    def __init__(self = None, app = None):
        self._app = app

    
    def setup_for_account(self = None, account = None, local_config = None):
        TRACE('[Encrypted Folder] Ensuring client key pair for account %s', account.account_id)
    # WARNING: Decompyle incomplete

    
    def register_sync_engine_callbacks(self = None, sync_engine = None, account = None, local_config = ('sync_engine', 'NucleusInterface', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface')):
        pass
    # WARNING: Decompyle incomplete

    load_client_key_pair = (lambda account = None, local_config = None: pass# WARNING: Decompyle incomplete
)()
    load_team_key_fingerprint = (lambda account = None, local_config = None: pass# WARNING: Decompyle incomplete
)()
    
    def _save_team_key_fingerprint(self = None, fingerprint_bytes = None, account = None, local_config = ('fingerprint_bytes', 'bytes', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface')):
        pass
    # WARNING: Decompyle incomplete

    
    def _show_sticky_notification(self = None, account = None, local_config = None, only_update_existing = (False,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _remove_sticky_notification(self = None, account = None):
        verification_sticky_key = EncryptedFolderEnrollmentStickyNotification.STICKY_KEY
        if self._app.notification_controller_adapter.has_sticky(account, verification_sticky_key):
            self._app.notification_controller_adapter.remove_sticky(account, verification_sticky_key)
            return None

    
    def display_key_fingerprints_dialog(self = None, account = None, local_config = None):
        if not self._app.ui_kit:
            report_bad_assumption('[Encrypted Folder] Cannot display key fingerprints dialog because UiKit is not available!')
            return None
        stored_team_key_fingerprint = _load_team_key_fingerprint(account, local_config)
        stored_client_key_fingerprint = _load_client_key_fingerprint(local_config)
    # WARNING: Decompyle incomplete

    
    def _show_team_key_verification_dialog(self = None, account = None, local_config = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _show_team_key_mismatch_dialog(self = None, account = None, local_config = None):
        pass
    # WARNING: Decompyle incomplete


_load_with_retries = (lambda local_config = None, config_key_name = None: try:
local_config.config_dict.get(config_key_name)except DiskIOError:
err = Noneraise RetryException(inner = err), errerr = Nonedel err)()
_save_with_retries = (lambda local_config = None, config_key_name = None, item = retry(3, 1), allow_overwrite = ('local_config', 'LocalConfigurationInterface', 'config_key_name', 'str', 'item', 'Any', 'allow_overwrite', 'bool'): pass# WARNING: Decompyle incomplete
)()

def _load_client_key_pair(local_config = None):
    pass
# WARNING: Decompyle incomplete


def _save_client_key_pair(client_key_pair = None, local_config = None):
    pass
# WARNING: Decompyle incomplete


def _load_client_key_fingerprint(local_config = None):
    pass
# WARNING: Decompyle incomplete


def _ensure_client_key_fingerprint(client_key_pair = None, local_config = None):
    pass
# WARNING: Decompyle incomplete


def _save_client_key_fingerprint(fingerprint = None, local_config = None):
    pass
# WARNING: Decompyle incomplete


def _migrate_secp256k1_to_asymmetric_encryption_algorithm(serialized_client_key_pair = None, local_config = None):
    
    try:
        key_pair_dict = json.loads(serialized_client_key_pair)
        algorithm = AsymmetricEncryptionAlgorithm(key_pair_dict['algorithm'])
        TRACE('[Encrypted Folder] Applying migration from string identifier to client key pair')
        key_pair_dict['algorithm'] = json_encode(AsymmetricEncryptionAlgorithm_validator, algorithm)
        serialized_migrated_key_pair = json.dumps(key_pair_dict)
        config = local_config.config_dict
        config[EncryptedFolderConstants.CLIENT_KEY_PAIR_CONFIG_KEYNAME] = serialized_migrated_key_pair
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        return ClientKeyPair.deserialize(serialized_migrated_key_pair)
                    except (JSONDecodeError, ValidationError, KeyError, AssertionError):
                        TRACE('[Encrypted Folder] Could not parse serialized client key pair for migration! Resetting.')
                        config = local_config.config_dict
                        config[EncryptedFolderConstants.CLIENT_KEY_PAIR_CONFIG_KEYNAME] = None
                        None(None, None)
                    except:
                        with None:
                            if not None:
                                pass

                    return None




_fingerprints_file_lock = NativeRecursiveMutex()
_write_fingerprints_file = (lambda fingerprint_dict = None: json_dict = json.dumps(fingerprint_dict)TRACE('[Encrypted Folder] Writing fingerprint dict to fingerprint database: %s', json_dict)encoded_json = base64.b64encode(json_dict.encode('utf8'))fingerprints_file_path = os.path.join(AppDataPaths.dropbox_appdata_path, EncryptedFolderConstants.TEAM_KEY_FINGERPRINT_FILE)try:
_fingerprints_file_lockfile = open(fingerprints_file_path, 'wb')file.write(encoded_json)None(None, None)with None:
if not None:
passtry:
None(None, None)Nonewith None:
if not None:
try:
try:
Noneexcept (IOError, OSError):
err = Noneraise RetryException(inner = err), errerr = Nonedel err)()
_read_fingerprints_file = (lambda : fingerprints_file_path = os.path.join(AppDataPaths.dropbox_appdata_path, EncryptedFolderConstants.TEAM_KEY_FINGERPRINT_FILE)encoded_bytes = b''try:
_fingerprints_file_lockfile = open(fingerprints_file_path, 'rb')read = file.read()if not read:
passelse:
encoded_bytes += readNone(None, None)with None:
if not None:
passtry:
None(None, None)with None:
if not None:
try:
try:
passexcept FileNotFoundError:
Noneexcept (IOError, OSError):
err = Noneraise RetryException(inner = err), errerr = Nonedel errtry:
decoded = base64.decodebytes(encoded_bytes)if len(decoded) > 0:
json.loads(decoded)except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.DATABASES)None)()

def _load_team_key_fingerprint(account = None, local_config = None):
    pass
# WARNING: Decompyle incomplete


def _write_team_key_fingerprint(team_key_fingerprint = None, account = None, local_config = None):
    pass
# WARNING: Decompyle incomplete


def _delete_team_key_fingerprint(account = None, local_config = None):
    pass
# WARNING: Decompyle incomplete

