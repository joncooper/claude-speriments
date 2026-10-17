# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.i18n import trans
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs, LocalizedStrings

def localized_strings(account = None, backup_mode = None):
    strings = LocalizedStrings()
    conflict_str = trans("%(display_name)s's conflicted copy")
    strings.conflicted_copy_host = conflict_str % dict(display_name = account.host_display_name)
    strings.conflicted_copy_user = conflict_str % dict(display_name = account.user_display_name)
    conflict_str = trans("%(display_name)s's invalid files")
    strings.invalid_files_conflict = conflict_str % dict(display_name = account.host_display_name)
    strings.permissions_conflict = trans('view-only conflicts')
    strings.case_conflict = trans('Case Conflict')
    strings.whitespace_conflict = trans('Whitespace Conflict')
    strings.unicode_encoding_conflict = trans('Unicode Encoding Conflict')
    strings.selective_sync_conflict = trans('Selective Sync Conflict')
    strings.camera_uploads_old = trans('Old')
    strings.cycle_renamed = trans('renamed')
    strings.ignored_path_conflict = trans('Ignored Item Conflict')
    strings.shared_folder_conflict = trans('shared folder conflict')
    file_lock_conflict_str = trans("%(display_name)s's edits")
    strings.file_locking_conflict = file_lock_conflict_str % dict(display_name = account.user_display_name)
    strings.merge_into_dropbox_conflict = trans('New')
    strings.ext_to_dbx_breadcrumb_name = trans('My files in Dropbox')
    strings.dbx_to_ext_breadcrumb_name = trans('Files on my computer')
    strings.one_way_sync_conflict = trans('Backup Conflicts')
# WARNING: Decompyle incomplete

