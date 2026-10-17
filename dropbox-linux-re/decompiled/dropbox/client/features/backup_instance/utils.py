# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import hashlib
import os
from os import listdir
from os.path import exists
from typing import Any, Optional, Sequence
from apex.metrics import MetricsReporter
from build_number import BUILD_KEY
from build_number.platform import IS_MAC
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_instance.backup_instance_logging import BackupInstanceLogger
from dropbox.client.features.backup_instance.backup_root_description import BackupRootDescriptionNS
from dropbox.client.features.backup_instance.constants import APPLE_TIME_MACHINE_EXCLUDE_ATTR_NAME, APPLE_TIME_MACHINE_EXCLUDE_ATTR_VALUE, BI_SYNC_FOLDER
from dropbox.client.features.backup_instance.types import BackupInstanceEvent, RootValidationResult
from dropbox.client.folder_tagger.folder_tagger import FolderTagger
from dropbox.client.gandalf import Gandalf
from dropbox.client.periodic import PeriodicScheduler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_rmtree_with_retry
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.fsutil import FileSystem
from dropbox.metrics.constants import LOOKUP_FILEID_BATCH_ENABLED_TAG, SYNC_ENGINE_GENERATION_TAG, SYNC_ROOT_TYPE_TAG
from dropbox.model.types import NsId
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import BOUNDARY_FUTURE_COMPLETION_THREAD_POOL, LOOKUP_BY_FILEID_BATCH_ENABLED_STORMCROW
from dropbox.sync_engine_boundary.monitored_thread_pool import MonitoredThreadPoolExecutor
from dropbox.sync_engine_boundary.utils import backup_mode_args_to_engine_generation
from dropbox.sync_root.types import SyncRootType
from dropbox.trace import TRACE, WARNING
if IS_MAC:
    from dropbox.xattrs import xattr

def BI_TRACE(fmt = None, session_id = None, *args):
    real_fmt = '[{}] {}'.format(session_id if session_id else 'BKUP', fmt)
# WARNING: Decompyle incomplete


def BI_WARN(fmt = None, session_id = None, *args):
    real_fmt = '[{}] {}'.format(session_id if session_id else 'BKUP', fmt)
# WARNING: Decompyle incomplete


def _build_local_root_path(root = None, fs = None, attempt = None):
    root_path_base = os.path.expanduser('~')
    hasher = hashlib.sha256()
    hasher.update(bytes(str(int(root.ns_id)), encoding = 'ascii'))
    hashed_nsid = hasher.hexdigest()
    intermediate_folder = hashed_nsid if attempt == 0 else f'''{hashed_nsid}_{attempt}'''
    return fs.make_path(root_path_base).join('.{}_bi'.format(BUILD_KEY.lower())).join(intermediate_folder).join('DropboxBackup')


def local_backup_root_location(user_context = None, root = None, fs = None):
    return _build_local_root_path(root, fs, attempt = 0)


def compute_new_local_backup_root_location(user_context = None, root = None, fs = None, acceptable_validation_results = (None,), session_id = ('user_context', 'UserContext', 'root', 'BackupRootDescriptionNS', 'fs', 'FileSystem', 'acceptable_validation_results', 'Sequence[RootValidationResult]', 'session_id', 'Optional[str]', 'return', 'LocalPath')):
    pass
# WARNING: Decompyle incomplete


def has_local_bkup_root_parent(fs = None):
    root_path_base = os.path.expanduser('~')
    local_root_parent_dir = fs.make_path(root_path_base).join('.{}_bi'.format(BUILD_KEY.lower()))
    return fsutil.exists(fs, local_root_parent_dir)


def wipe_nucleus_db(user_context = None):
    local_config = user_context.local_config.get_local_configuration_interface()
    metadata_directory = os.path.join(local_config.appdata_path, BI_SYNC_FOLDER)
    if exists(metadata_directory):
        if safe_rmtree_with_retry(metadata_directory):
            BI_TRACE('Successfully deleted previous sync appdata at %r', metadata_directory)
            return None
        BI_TRACE('Exception while deleting previous sync appdata %r', metadata_directory)
        raise AssertionError('Cannot delete old appdata/sync folder')


def remove_folder(fs = None, path = None):
    return fsutil.rmtree(fs, path, ignore_errors = True)


def contains_only_trivial_entries(path = None):
    trivial_entries = {
        'icon\r',
        '.ds_store',
        '.localized',
        'desktop.ini',
        '.dropbox.cache'}
    for dir_ent in listdir(path.to_unicode()):
        if dir_ent.lower() not in trivial_entries:
            BI_TRACE('found nontrivial entry in root (%r): %r', None, path, dir_ent)
            return False
        return True


def validate_root_path(root_path = None, expected_ns_id = None, fs = None):
    if not fsutil.exists(fs, root_path):
        BI_WARN('proposed root path %r does not exist', None, root_path)
        return RootValidationResult.MISSING_FOLDER
    if not fsutil.is_directory(fs, root_path):
        BI_WARN('proposed root path %r is not a directory', None, root_path)
        return RootValidationResult.NOT_A_DIR
# WARNING: Decompyle incomplete


def build_sync_engine_boundary_threadpool(account, gandalf = None, periodic_scheduler = None, metrics_reporter = None, root_type = (None,), backup_mode_args = ('account', 'AccountInterface', 'gandalf', 'Gandalf', 'periodic_scheduler', 'PeriodicScheduler', 'metrics_reporter', 'MetricsReporter', 'root_type', 'SyncRootType', 'backup_mode_args', 'Optional[BackupModeArgs]', 'return', 'MonitoredThreadPoolExecutor')):
    pass
# WARNING: Decompyle incomplete


def is_regular_engine_on_fp(user_context = None):
    
    try:
        nucleus_wrapper = destroying(NucleusWrapper.from_context(user_context))
        
        try:
            None(None, None)
            return 
            with None:
                if not None, nucleus_wrapper().is_file_provider():
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)
                            return False






def best_effort_user_has_backup_root(user_context = None):
    return user_context.local_config.bi_local_backup_root_info is not None


def apply_time_machine_ignore_xattr_if_missing(path = None):
    if not IS_MAC:
        return None
    attrs = xattr.from_path(path.to_unicode())
# WARNING: Decompyle incomplete

