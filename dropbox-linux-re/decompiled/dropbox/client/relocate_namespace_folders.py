# Source Generated with Decompyle++
# File: relocate_namespace_folders.pyc (Python 3.11)

import itertools
import json
import os
from enum import Enum
from typing import Any, Callable, cast, Dict, Iterable, Iterator, List, NamedTuple, Optional, Set, Text, Tuple, Union
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountDataSource
from dropbox.client.constants import DEFAULT_DROPBOX_PATH
from dropbox.client.databases import clear_appdata_without_unlink
from dropbox.client.features.sync_everything.v3.config_utils import write_sync_everything_cdm_flag_if_needed
from dropbox.client.features.sync_everything.v3.open_handle_utils import has_only_explorer_handle_to_sync_everything
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.client.folder_tagger.folder_tagger import FolderTagger
from dropbox.client.high_trace import force_flush, send_trace_log
from dropbox.client.nucleus_cdm_relocation import NucleusCdmRelocationMigration, RelocationParameters
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.unlink_cookie import write_unlink_cookie_no_sync_engine
from dropbox.client.util import create_hidden_symlink, hard_exit, switch_sidebar_link
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dirtraverse import DirectoryModifiedError
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_bytes, make_unicode, split_extension
from dropbox.i18n import trans
from dropbox.infinite import is_user_running_cloud_files
from dropbox.model.types import FileId, NsId
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.read_only import set_read_only_recursive_helper
from dropbox.shared.relocation_stats import OPERATION_META_FILE, RemoveSyncedContentStats
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_engine_boundary.file_system_exceptions import DirectoryNotEmptyError, FileExistsError, FileNotFoundError, PermissionDeniedError
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.helpers import folder_conflicts_with_icloud
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE
if IS_WINDOWS:
    import ntpath
    from winenumhandles.api import get_open_handle_details, get_proc_description, get_proc_path
    from dropbox.client.util.win import kill_process_by_name
MYPY = False
if MYPY:
    from winenumhandles.api import OpenHandleDetails
    from dropbox.client.configuration.interface import LocalConfigurationInterface
    from dropbox.client.main import DropboxApplication
    from dropbox.shared.local_path import LocalPath
    OperationArgsTypeRaw = Union[(Tuple[(int, int)], Tuple[(int, Text)], Tuple[(int, Text, Text)], Tuple[(int, int, Text, Text, Text)], Tuple[(int, int, Text, Text, Text, Text)], Tuple[(int, int, Text, int)], Tuple[(int, int, Text, int, Optional[Tuple[(Text, FileId)]])])]
    FileSystem = Any

def report_cdm_skipping_update_account_info(name = None):
    DropboxArranger.log_cdm_move_attempt('skipping_cdm_update_account_{}'.format(name))


def report_mismatched_root_and_home_when_apply_changes():
    DropboxArranger.log_cdm_move_attempt('mismatched_root_should_never_happen')


def report_missing_config_root():
    DropboxArranger.log_cdm_move_attempt('missing_config_root_when_applying_changes')


class PersistedOperationType(Enum):
    OPERATION_INVALID = 0
    MOVE_FOLDER = 1
    DELETE_FOLDER = 2
    WRITE_ROOT_DOTDROPBOX = 3
    DECONFLICT_FOLDER = 4
    REMOVE_SYNC_DATABASE = 5
    RENAME_DROPBOX = 6
    SEC_ONLY_FAST_PATCH_SYNC_DATABASE = 7
    UPDATE_SIDEBAR = 8
    CHECK_OPEN_HANDLES = 9
    PRESERVE_FOLDER = 10
    SEC_ONLY_REMOVE_SYNCED_CONTENT = 11
    NUCLEUS_SPECIFIC_UPDATES = 12
    WRITE_NUCLEUS_MIGRATION_PARAMETERS = 13
    WRITE_NUCLEUS_TMF_FILEID = 14

if MYPY:
    OperationArgsType = Union[(Tuple[(PersistedOperationType, int)], Tuple[(PersistedOperationType, LocalPath)], Tuple[(PersistedOperationType, Text)], Tuple[(PersistedOperationType, LocalPath, Text)], Tuple[(PersistedOperationType, LocalPath, LocalPath)], Tuple[(PersistedOperationType, int, LocalPath, LocalPath, LocalPath)], Tuple[(PersistedOperationType, int, int, LocalPath, LocalPath, LocalPath)], Tuple[(PersistedOperationType, int, Text, int)], Tuple[(PersistedOperationType, int, Text, int, Optional[Tuple[(LocalPath, FileId)]])])]

class FatalType(Enum):
    COMMON = 'fatal_failure'
    RETRY_EXHAUSTED = 'retry_exhausted'


class FatalArrangementException(Exception):
    pass
# WARNING: Decompyle incomplete


class RetryArrangementException(Exception):
    pass


class TemporaryArrangementException(Exception):
    pass
# WARNING: Decompyle incomplete


def _flush_log_queue():
    force_flush()
    send_trace_log()


def _get_db_ns_rel_path(path = None, dropbox_localpath = None):
    text_path = '/'
    if path != dropbox_localpath:
        text_path = path.to_dropbox_ns_relative_path(dropbox_localpath)
    return Text(text_path)

FileInUseDetails = NamedTuple('FileInUseDetails', [
    ('proc_descs', List[Text]),
    ('detailed_text', Text),
    ('contains_explorer', bool)])
EXPLORER_SUFFIX = '\\explorer.exe'

def _get_file_in_use_detailed_text_win(fs = None, path = None, error_detail = None):
    pass
# WARNING: Decompyle incomplete


def _get_temporary_exception_alert_dialog_buttons():
    return [
        trans('Try Again')]

TemporaryArrangeErrorAlertDetails = NamedTuple('TemporaryArrangeErrorAlertDetails', [
    ('caption', Text),
    ('message', Text),
    ('detailed_text', Text),
    ('contains_explorer', bool)])

def _get_temporary_arrange_error_alert_details(team_name = None, fs = None, localpath = None, error_detail = ('team_name', 'Optional[Text]', 'fs', 'FileSystem', 'localpath', 'Optional[LocalPath]', 'error_detail', 'Text', 'return', 'TemporaryArrangeErrorAlertDetails')):
    caption = trans("Can't sync Dropbox account")
    app_list_text = ''
    detailed_text = None
    
    class FilesInUseProc(Enum):
        Apps = 1
        Explorer = 2
        ExplorerWithApps = 3

    proc_type = FilesInUseProc.Apps
    if IS_WINDOWS:
        
        try:
            file_in_use_details = _get_file_in_use_detailed_text_win(fs, localpath.to_unicode() if localpath else None, error_detail)
            detailed_text = file_in_use_details.detailed_text
            if file_in_use_details.contains_explorer:
                pass
            for app_name in file_in_use_details.proc_descs:
                app_list_text += trans('\n• %(app_name)s') % {
                    'app_name': app_name }
        except Exception:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)

        message = trans('Your account stopped syncing during an update because some files are being used by other applications')
        if app_list_text:
            message += trans(':\n%(app_list)s\n\n') % {
                'app_list': app_list_text }
        elif localpath:
            message += trans(':\n%(path)s\n\n') % {
                'path': localpath.to_unicode() }
    message += trans('\n\nYou can quit Dropbox to close this dialog, but you must open the Dropbox app again to sync your files.')
    if not IS_WINDOWS:
        error_detail_text = trans('▸ %(error_detail)s') % {
            'error_detail': error_detail }
        message += '\n\n' + error_detail_text
    return TemporaryArrangeErrorAlertDetails(caption, message, detailed_text, proc_type in (FilesInUseProc.Explorer, FilesInUseProc.ExplorerWithApps))


class DropboxArranger(object):
    TEMP_FOLDER = '/.dropbox-temp-relocate3640a06ba127'
    
    def __init__(self, app, file_system, config, shell_touch = None, update_tray_status = None, new_dropbox_name = None, account = ('app', 'DropboxApplication', 'file_system', 'FileSystem', 'config', 'LocalConfigurationInterface', 'shell_touch', 'Callable[[Union[Text, LocalPath]], None]', 'update_tray_status', 'Callable[[], None]', 'new_dropbox_name', 'Text', 'account', 'AccountInterface', 'return', 'None')):
        self._app = app
        self._fs = file_system
        self._config = config
        self._folder_tagger = FolderTagger(self._fs, shell_touch = shell_touch)
        self._new_dropbox_name = new_dropbox_name
        self._account = account
        self._update_tray_status = update_tray_status

    get_meta_file_path = (lambda fs = None, config = None: dropbox_path = config.get_dropbox_path()dropbox_localpath = fs.make_path(dropbox_path)dropbox_localpath.join_nfc_components(Text(OPERATION_META_FILE)))()
    
    def write_required_operations_for_namespaces(self = None, root_ns_id = None, home_ns_id = None, home_ns_localpath = ('root_ns_id', 'int', 'home_ns_id', 'int', 'home_ns_localpath', 'LocalPath', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def report_num_operations_for_namespaces(self = None, root_ns_id = None, home_ns_id = None, home_ns_localpath = ('root_ns_id', 'int', 'home_ns_id', 'int', 'home_ns_localpath', 'LocalPath', 'return', 'None')):
        
        try:
            TRACE('CDM_RELOCATE: Report number of operation for the migration (Should be zero). Root ns %s. Home ns %s. Home path %s.', root_ns_id, home_ns_id, Text(home_ns_localpath))
            dropbox_path = self._config.get_dropbox_path()
            dropbox_localpath = self._fs.make_path(dropbox_path)
            if not fsutil.exists(self._fs, dropbox_localpath):
                return None
            operations = None._get_operation_list(dropbox_localpath, root_ns_id, home_ns_id, home_ns_localpath)
            operation_names = []
            if operations:
                for operation in operations:
                    operation_names.append(operation[0])
                    TRACE('CDM_RELOCATE: operations: %r', str(operation_names))
                    return None
                    except Exception:
                        report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)
                        return None


    
    def execute_pending_operations(self = None):
        TRACE('CDM_RELOCATE: attempting to execute pending operations')
        dropbox_path = self._config.get_dropbox_path()
        dropbox_localpath = self._fs.make_path(dropbox_path)
        relocate_localpath = dropbox_localpath.join_nfc_components(Text(OPERATION_META_FILE))
        if not fsutil.exists(self._fs, relocate_localpath):
            TRACE('CDM_RELOCATE: Not performing a relocate. No .dropbox-relocate file exists.')
            return None
        if None.DISK in self._account.link_sources:
            TRACE('CDM_RELOCATE: Restarting client because it finished starting up before a CDM relocate.')
            self._report_async_restart_error()
            self._app.restart()
            return None
        
        try:
            self._update_read_only(dropbox_localpath, False)
        except Exception:
            TRACE("CDM_RELOCATE: We couldn't make the root Read Only?  Something odd happened here.")

        retries = 0
        operations_found = False
        self._update_tray_status()
        
        try:
            relocate_file = self._fs.open(relocate_localpath)
            json_dict = json.loads(make_unicode(relocate_file.read()))
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            pass
                        except FileNotFoundError:
                            TRACE('CDM_RELOCATE: .dropbox-relocate not found.')
                            return None
                            except PermissionDeniedError:
                                self._report_permission_error()
                                raise 

                        operations = json_dict['operations']
                        if operations:
                            operations_found = True



    # WARNING: Decompyle incomplete

    
    def _write_relocate_file(self = None, local_path = None, json_dict = None):
        relocate_file = self._fs.open(local_path, 'w', hidden = True, system = True)
        relocate_file.write(make_bytes(json.dumps(json_dict)))
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _handle_temporary_exception(self = None, src_localpath = None, message = None):
        self._report_temporary()
        report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)
        alert_details = _get_temporary_arrange_error_alert_details(self._account.team, self._fs, src_localpath, message)
        TRACE('CDM_RELOCATE: AlertDialog message: %r, detailed_text:%r', alert_details.message, alert_details.detailed_text)
    # WARNING: Decompyle incomplete

    
    def _handle_fatal_exception(self = None, excp = None):
        fatal_type = FatalType.COMMON
        if isinstance(excp, FatalArrangementException):
            fatal_type = excp.fatal_type
        self._report_fatal(fatal_type)
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UNKNOWN)
        dropbox_path = self._config.get_dropbox_path()
        dropbox_localpath = self._fs.make_path(dropbox_path)
        new_path_suffix = trans('Old')
        new_local_path = fsutil.get_available_path(self._fs, dropbox_localpath, dropbox_localpath.dirname, dropbox_localpath.basename, new_path_suffix, use_existing_dir = False)
        team_name = self._account.team
        if team_name:
            message = trans('Dropbox has encountered problems joining %(team_name)s and will have to re-sync your files.\n\nYour old Dropbox files will be moved to "%(old_dropbox)s".') % {
                'old_dropbox': new_local_path.to_unicode(),
                'team_name': team_name }
        else:
            message = trans('Dropbox has encountered problems leaving your team and will have to re-sync your files.\n\nYour old Dropbox files will be moved to "%(old_dropbox)s".') % {
                'old_dropbox': new_local_path.to_unicode() }
        TRACE('CDM_RELOCATE: FatalException message - team_name: %r, new_local_path: %r', team_name, new_local_path)
        _flush_log_queue()
    # WARNING: Decompyle incomplete

    
    def _execute_check_open_handles(self = None, dropbox_path = None, rel_path = None):
        if IS_WINDOWS:
            src_localpath = dropbox_path.join_dropbox_ns_relative_path(rel_path)
            TRACE('CDM_RELOCATE: Checking if %r has any opened handles', src_localpath)
            
            try:
                open_handle_details_list = get_open_handle_details(src_localpath.to_unicode())
            except WindowsError:
                e = None
                TRACE('get_open_handle_details failed:%r', e)
                open_handle_details_list = []
                e = None
                del e
            except:
                e = None
                del e

            if open_handle_details_list:
                primary_account_config = self._app.config_manager.local_config(None)
                if has_only_explorer_handle_to_sync_everything(primary_account_config, self._account, open_handle_details_list):
                    TRACE('CDM_RELOCATE: [Sync Everything] found only Explorer handles to Desktop, ignoring')
                    return None
                TRACE('CDM_RELOCATE: Found %r opened handles. Raise exception', len(open_handle_details_list))
                raise TemporaryArrangementException(trans('Files are still opened in %(path)s') % {
                    'path': src_localpath.to_unicode() }, src_localpath = src_localpath)
            return None
        TRACE('CDM_RELOCATE: Not checking open handles on non-windows platforms')

    
    def _rearrange_item_lists(self = None, item_names = None):
        
        try:
            index = item_names.index('.dropbox')
            return item_names[:index] + item_names[index + 1:] + [
                item_names[index]]
        except ValueError:
            return 


    
    def _execute_preserve_folder(self = None, dropbox_path = None, src_relpath = None, dst_name = ('dropbox_path', 'LocalPath', 'src_relpath', 'Text', 'dst_name', 'Text', 'return', 'None')):
        src_localpath = dropbox_path.join_dropbox_ns_relative_path(src_relpath)
        dst_localpath = dropbox_path.join_nfc_components(dst_name)
        self.verbose_trace('attempt to preserve %r at %r', src_localpath, dst_localpath)
        if self._is_folder_empty(src_localpath):
            self.verbose_trace('%r is empty, delete it', src_localpath)
            self._delete_folder(src_localpath)
            return None
        if fsutil.exists(self._fs, dst_localpath):
            raise FatalArrangementException('CDM_RELOCATE: Cache folder %r already exists' % dst_localpath)
        self._move_folder(dropbox_path, src_localpath, dst_localpath)

    
    def _move_folder(self = None, dropbox_path = None, src_localpath = None, dst_localpath = ('dropbox_path', 'LocalPath', 'src_localpath', 'LocalPath', 'dst_localpath', 'LocalPath', 'return', 'None')):
        if src_localpath == dst_localpath:
            raise FatalArrangementException('CDM_RELOCATE: Cannot move a folder to itself.')
        if not fsutil.exists(self._fs, src_localpath, resolve_link = False):
            self.verbose_trace("src: %r doesn't exist - just return", src_localpath)
            return None
        None._update_read_only(src_localpath, False)
        if fsutil.exists(self._fs, dst_localpath, resolve_link = False) and fsutil.same_file_object(self._fs, src_localpath, dst_localpath):
            
            try:
                self.verbose_trace('- same file object. Simply renaming %r to %r', src_localpath, dst_localpath)
                self._fs.rename(src_localpath, dst_localpath)
                return None
            except PermissionDeniedError:
                raise TemporaryArrangementException(trans("Couldn't rename: %(path)s") % {
                    'path': src_localpath.to_unicode() }, src_localpath = src_localpath)
                except FileNotFoundError:
                    return None
                if not src_localpath.is_parent_of(dst_localpath) and dst_localpath.is_parent_of(src_localpath) and fsutil.exists(self._fs, dst_localpath, True):
                    self.verbose_trace('- simply renaming %r to %r', src_localpath, dst_localpath)
                    fsutil.makedirs(self._fs, dst_localpath.dirname)
                    
                    try:
                        self._fs.rename(src_localpath, dst_localpath)
                        return None
                    except FileExistsError:
                        raise RetryArrangementException("Couldn't rename folder wholesale since destination already exists. Will move piecewise.")
                        except PermissionDeniedError:
                            raise TemporaryArrangementException(trans("Couldn't rename: %(path)s") % {
                                'path': src_localpath.to_unicode() }, src_localpath = src_localpath)
                        except FileNotFoundError:
                            return None
                        fsutil.makedirs(self._fs, dst_localpath)
                        self.verbose_trace("-- Can't simply rename, moving items from %r to %r", src_localpath, dst_localpath)
                        
                        try:
                            item_names = fsutil.listdir(self._fs, src_localpath)
                        except DirectoryModifiedError:
                            raise RetryArrangementException('Tried to get the list of subitems to move, but something changed while iterating. Trying again')

                        item_names = self._rearrange_item_lists(item_names)
                        for item_name in item_names:
                            item_src = src_localpath.join_nfc_components(item_name)
                            item_dst = dst_localpath.join_nfc_components(item_name)
                            if dst_localpath.startswith(item_src):
                                continue
                            if item_src == dropbox_path.join_nfc_components(Text(OPERATION_META_FILE)):
                                continue
                            self.verbose_trace('-- moving %r to %r', item_src, item_dst)
                            self._deconflict_file_or_folder(item_dst)
                            self._safe_rename(item_src, item_dst)
                            except FileExistsError:
                                raise RetryArrangementException('Tried to move a subitem but it already existed. Going to deconflict parent again.')
                            except FileNotFoundError:
                                raise RetryArrangementException('Tried to move a subitem but it no longer existed. Continuing.')
                            except PermissionDeniedError:
                                report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)
                                raise TemporaryArrangementException(trans("Couldn't rename %(path)s") % {
                                    'path': item_src.to_unicode() }, src_localpath = item_src)
                            if dst_localpath.is_parent_of(src_localpath):
                                
                                try:
                                    fsutil.safe_rmdir(self._fs, src_localpath)
                                    return None
                                except FileNotFoundError:
                                    return None
                                    except DirectoryNotEmptyError:
                                        raise RetryArrangementException("Tried to remove folder after moving but it wasn't empty.")
                                    except PermissionDeniedError:
                                        raise TemporaryArrangementException(trans("Couldn't delete: %(path)s") % {
                                            'path': src_localpath.to_unicode() }, src_localpath = src_localpath)
                                    return None




    
    def _execute_folder_move(self = None, dropbox_path = None, src_relpath = None, dst_relpath = ('dropbox_path', 'LocalPath', 'src_relpath', 'Text', 'dst_relpath', 'Text', 'return', 'None')):
        self.verbose_trace('attempting to relocate %r to %r', src_relpath, dst_relpath)
        src_localpath = dropbox_path.join_dropbox_ns_relative_path(src_relpath)
        dst_localpath = dropbox_path.join_dropbox_ns_relative_path(dst_relpath)
        self._move_folder(dropbox_path, src_localpath, dst_localpath)

    
    def _execute_folder_delete(self = None, dropbox_path = None, src_path = None):
        self.verbose_trace('Attempting to delete %r', src_path)
        local_path = dropbox_path.join_dropbox_ns_relative_path(src_path)
        self._delete_folder(local_path)

    
    def _delete_folder(self = None, local_path = None):
        
        try:
            self._safe_remove_tree(local_path)
            return None
        except FileNotFoundError:
            return None
            except DirectoryNotEmptyError:
                raise RetryArrangementException("Couldn't remove non-empty folder %s" % local_path.to_unicode())
            except PermissionDeniedError:
                raise TemporaryArrangementException(trans("Couldn't delete: %(path)s") % {
                    'path': local_path.to_unicode() }, src_localpath = local_path)


    
    def _execute_write_dotdropbox(self = None, dropbox_path = None, root_ns_id = None):
        TRACE('Writing .dropbox file with root_ns_id:%r to %r', root_ns_id, dropbox_path)
        self._folder_tagger.tag_folder(dropbox_path, FolderTag.DROPBOX, to_ns = root_ns_id)

    
    def _is_folder_empty(self = None, item_localpath = None):
        if not fsutil.exists(self._fs, item_localpath):
            return True
        if not fsutil.is_directory(self._fs, item_localpath):
            return False
        return len(fsutil.listdir(self._fs, item_localpath)) == 0

    
    def _deconflict_file_or_folder(self = None, item_localpath = None):
        if not fsutil.exists(self._fs, item_localpath):
            return None
        None.verbose_trace('Need to deconflict %r', item_localpath)
        if fsutil.is_directory(self._fs, item_localpath):
            ext = ''
            base = item_localpath.basename
        else:
            (base, ext) = split_extension(item_localpath.basename)
        conflict_string = trans('Conflict')
        conflict_index = 0
        if conflict_index == 0:
            new_filename = item_localpath.basename
        elif conflict_index == 1:
            new_filename = f'''{base!s} ({conflict_string!s}){ext!s}'''
        elif conflict_index > 1:
            new_filename = f'''{base!s} ({conflict_string!s} {conflict_index!s}){ext!s}'''
        conflict_index = conflict_index + 1
        next_path = item_localpath.dirname.join_nfc_components(new_filename)
        if fsutil.exists(self._fs, next_path):
            continue
        
        try:
            self._safe_rename(item_localpath, next_path, use_shell_fallback = False)
        except FileExistsError:
            continue
            except FileNotFoundError:
                return None
            except PermissionDeniedError:
                raise TemporaryArrangementException(trans("Couldn't move: %(path)s") % {
                    'path': item_localpath.to_unicode() }, src_localpath = item_localpath)

        self.verbose_trace('- deconflicted %r to %r', item_localpath, next_path)

    
    def _execute_deconflict_folder(self = None, dropbox_path = None, folder_relpath = None):
        folder_localpath = dropbox_path.join_dropbox_ns_relative_path(folder_relpath)
        self._deconflict_file_or_folder(folder_localpath)

    
    def _remove_tag(self = None, dropbox_path = None, folder_relpath = None):
        folder_lp = dropbox_path.join_dropbox_ns_relative_path(folder_relpath)
        tag_lp = folder_lp.join_nfc_components('.dropbox')
        self.verbose_trace('Removing .dropbox tag in %r', tag_lp)
        fsutil.safe_remove(self._fs, tag_lp)

    
    def _remove_dropbox_cache_dir(self = None, dropbox_path = None, folder_relpath = None):
        folder_localpath = dropbox_path.join_dropbox_ns_relative_path(folder_relpath)
        cache_localpath = folder_localpath.join_nfc_components('.dropbox.cache')
        self.verbose_trace('About to remove .dropbox_cache %r', cache_localpath)
        
        try:
            self._safe_remove_tree(cache_localpath)
            return None
        except FileNotFoundError:
            return None
            except PermissionDeniedError:
                raise TemporaryArrangementException(trans("Couldn't remove: %(path)s") % {
                    'path': folder_localpath.to_unicode() }, src_localpath = folder_localpath)


    
    def _execute_write_nucleus_migration_parameters(self, pre_relocate_root_ns_id = None, pre_relocate_root_ns_fileid = None, post_relocate_root_ns_id = None, team_join_raw = ('pre_relocate_root_ns_id', 'NsId', 'pre_relocate_root_ns_fileid', 'FileId', 'post_relocate_root_ns_id', 'NsId', 'team_join_raw', 'Optional[Union[List, Tuple]]', 'return', 'None')):
        TRACE('CDM_RELOCATE: writing Nucleus migration parameters: pre_relocate_root_ns_id: %r, pre_relocate_root_ns_fileid: %r, post_relocate_root_ns_id: %r, team_join: %r, ', pre_relocate_root_ns_id, pre_relocate_root_ns_fileid, post_relocate_root_ns_id, team_join_raw)
        team_join = None
    # WARNING: Decompyle incomplete

    
    def _execute_write_nucleus_tmf_fileid(self = None, dropbox_path = None, home_ns_path = None, fileid = ('dropbox_path', 'LocalPath', 'home_ns_path', 'Text', 'fileid', 'FileId', 'return', 'None')):
        TRACE('CDM_RELOCATE: _execute_WRITE_NUCLEUS_TMF_FILEID, dropbox_path: %r, home_ns_path: %r, fileid: %r', dropbox_path, home_ns_path, fileid)
        tmf_lp = dropbox_path.join_dropbox_ns_relative_path(home_ns_path)
        TRACE('CDM_RELOCATE, writing fileid:%r to %r', fileid, tmf_lp)
        SyncEngineFactory.write_nucleus_fileid(tmf_lp, fileid, 1)

    
    def _execute_nucleus_specific_updates(self, dropbox_path, server_root_ns_id = None, folder_relpath = None, client_home_relpath = None, server_home_relpath = ('dropbox_path', 'LocalPath', 'server_root_ns_id', 'int', 'folder_relpath', 'Text', 'client_home_relpath', 'Text', 'server_home_relpath', 'Text', 'return', 'None')):
        TRACE('CDM_RELOCATE: _execute_nucleus_specific_updates. server_root_ns_id:%r, folder_relpath:%r, client_home_relpath:%r, server_home_relpath:%r', server_root_ns_id, folder_relpath, client_home_relpath, server_home_relpath)
        self._remove_tag(dropbox_path, folder_relpath)
        self._remove_dropbox_cache_dir(dropbox_path, folder_relpath)
        self._apply_changes_to_config(server_root_ns_id, folder_relpath, client_home_relpath, server_home_relpath)

    
    def _apply_changes_to_config(self, server_root_ns_id = None, folder_relpath = None, client_home_relpath = None, server_home_relpath = ('server_root_ns_id', 'int', 'folder_relpath', 'Text', 'client_home_relpath', 'Text', 'server_home_relpath', 'Text', 'return', 'None')):
        self._config.config_dict['root_ns'] = server_root_ns_id
        self._config.config_dict['home_ns_path'] = server_home_relpath
    # WARNING: Decompyle incomplete

    
    def _execute_delete_config(self, dropbox_path, server_root_ns_id = None, folder_relpath = None, client_home_relpath = None, server_home_relpath = ('dropbox_path', 'LocalPath', 'server_root_ns_id', 'int', 'folder_relpath', 'Text', 'client_home_relpath', 'Text', 'server_home_relpath', 'Text', 'return', 'None')):
        TRACE('CDM_RELOCATE: in execute_delete_config')
        self._remove_dropbox_cache_dir(dropbox_path, folder_relpath)
        clear_appdata_without_unlink(self._config.appdata_path)
        self._apply_changes_to_config(server_root_ns_id, folder_relpath, client_home_relpath, server_home_relpath)

    
    def _execute_rename_dropbox_folder(self = None, dropbox_path = None, desired_folder_name = None):
        TRACE('CDM_RELOCATE: Renaming dropbox folder to  %r', desired_folder_name)
        dropbox_parent = dropbox_path.dirname
        new_dropbox_path = dropbox_parent.join(desired_folder_name)
        if IS_MAC and folder_conflicts_with_icloud(Text(new_dropbox_path)):
            dropbox_parent = self._fs.make_path(DEFAULT_DROPBOX_PATH).dirname
            new_dropbox_path = dropbox_parent.join(desired_folder_name)
            TRACE('CDM_RELOCATE: Relocating dropbox folder to %r to avoid conflict with iCloud', new_dropbox_path)
            if not fsutil.on_same_device(self._fs, dropbox_path, dropbox_parent):
                raise FatalArrangementException('avoiding icloud conflict would move across volumes')
        did_rename_dropbox = False
        if self._is_path_valid_may_clobber_symlink(new_dropbox_path):
            did_rename_dropbox = self._rename_dropbox(dropbox_path, new_dropbox_path)
        if not did_rename_dropbox:
            self._report_dropbox_rename_fallback()
    # WARNING: Decompyle incomplete

    
    def _execute_update_sidebar_links(self = None, new_dropbox_path = None, old_dropbox_path = None):
        switch_sidebar_link(new_dropbox_path.to_unicode(), ignore_missing = True, old_dropbox_folder = old_dropbox_path)

    
    def _remove_symlink_at(self = None, path = None):
        if fsutil.is_symlink(self._fs, path):
            self.verbose_trace('Removing symlink at %r', path)
            if not fsutil.clobber_symlink_at(self._fs, path):
                fsutil.delete_broken_link(self._fs, path)
                return None
            return None

    
    def _is_path_valid_may_clobber_symlink(self = None, new_potential_dropbox_path = None):
        self._remove_symlink_at(new_potential_dropbox_path)
        return not fsutil.exists(self._fs, new_potential_dropbox_path)

    
    def _rename_dropbox(self = None, original_dropbox_path = None, new_dropbox_path = None):
        
        try:
            self._safe_rename(original_dropbox_path, new_dropbox_path)
            return True
        except PermissionDeniedError:
            raise TemporaryArrangementException(trans('Could not rename your Dropbox folder.'), src_localpath = original_dropbox_path)
            except FileExistsError:
                self.verbose_trace("The file name we just thought was usable, isn't.  Not a big deal, try another")
                return False
            except FileNotFoundError:
                self.verbose_trace('Somehow the dropbox was removed from underneath us.  This is bad.')
                raise FatalArrangementException('The dropbox was removed by some other process while trying to rename')


    
    def _execute_single_operation(self = None, dropbox_path = None, operation_typed = None):
        TRACE('CDM_RELOCATE: Relocating Dropbox subfolder. Operation %r', operation_typed)
        operation = operation_typed
        if operation[0] == PersistedOperationType.MOVE_FOLDER.value:
            self._execute_folder_move(dropbox_path, operation[1], operation[2])
        elif operation[0] == PersistedOperationType.DELETE_FOLDER.value:
            self._execute_folder_delete(dropbox_path, operation[1])
        elif operation[0] == PersistedOperationType.WRITE_ROOT_DOTDROPBOX.value:
            self._execute_write_dotdropbox(dropbox_path, operation[1])
        elif operation[0] == PersistedOperationType.DECONFLICT_FOLDER.value:
            self._execute_deconflict_folder(dropbox_path, operation[1])
        elif operation[0] == PersistedOperationType.REMOVE_SYNC_DATABASE.value:
            self._execute_delete_config(dropbox_path, operation[1], operation[2], operation[3], operation[4])
        elif operation[0] == PersistedOperationType.RENAME_DROPBOX.value:
            self._execute_rename_dropbox_folder(dropbox_path, operation[1])
        elif operation[0] == PersistedOperationType.UPDATE_SIDEBAR.value:
            return self._execute_update_sidebar_links(dropbox_path, operation[1])
        if operation[0] == PersistedOperationType.SEC_ONLY_FAST_PATCH_SYNC_DATABASE.value:
            raise FatalArrangementException('Can no longer execute FAST_PATCH_SYNC_DATABASE')
        if operation[0] == PersistedOperationType.NUCLEUS_SPECIFIC_UPDATES.value:
            self._execute_nucleus_specific_updates(dropbox_path, operation[1], operation[2], operation[3], operation[4])
        elif operation[0] == PersistedOperationType.WRITE_NUCLEUS_MIGRATION_PARAMETERS.value:
            self._execute_write_nucleus_migration_parameters(operation[1], operation[2], operation[3], operation[4])
        elif operation[0] == PersistedOperationType.WRITE_NUCLEUS_TMF_FILEID.value:
            self._execute_write_nucleus_tmf_fileid(dropbox_path, operation[1], operation[2])
        elif operation[0] == PersistedOperationType.CHECK_OPEN_HANDLES.value:
            self._execute_check_open_handles(dropbox_path, operation[1])
        elif operation[0] == PersistedOperationType.PRESERVE_FOLDER.value:
            self._execute_preserve_folder(dropbox_path, operation[1], operation[2])
        elif operation[0] == PersistedOperationType.SEC_ONLY_REMOVE_SYNCED_CONTENT.value:
            raise FatalArrangementException('Can no longer execute REMOVE_SYNCED_CONTENT')
        raise FatalArrangementException(f'''Got invalid relocation operation type {operation[0]!r}.''')

    
    def _normalize_operation_list(self = None, dropbox_local_path = None, operation_list = None):
        result = []
        for item_typed in operation_list:
            item = item_typed
            if item[0] == PersistedOperationType.MOVE_FOLDER:
                src = _get_db_ns_rel_path(item[1], dropbox_local_path)
                dst = _get_db_ns_rel_path(item[2], dropbox_local_path)
                result.append((PersistedOperationType.MOVE_FOLDER.value, src, dst))
                continue
            if item[0] == PersistedOperationType.RENAME_DROPBOX:
                result.append((PersistedOperationType.RENAME_DROPBOX.value, item[1]))
                continue
            if item[0] == PersistedOperationType.UPDATE_SIDEBAR:
                result.append((PersistedOperationType.UPDATE_SIDEBAR.value, Text(item[1])))
                continue
            if item[0] == PersistedOperationType.DELETE_FOLDER:
                src = _get_db_ns_rel_path(item[1], dropbox_local_path)
                result.append((PersistedOperationType.DELETE_FOLDER.value, src))
                continue
            if item[0] == PersistedOperationType.WRITE_ROOT_DOTDROPBOX:
                result.append((PersistedOperationType.WRITE_ROOT_DOTDROPBOX.value, item[1]))
                continue
            if item[0] == PersistedOperationType.DECONFLICT_FOLDER:
                if item[1] == dropbox_local_path:
                    raise FatalArrangementException('CDM_RELOCATE: Cannot deconflict root Dropbox.')
                result.append((PersistedOperationType.DECONFLICT_FOLDER.value, item[1].to_dropbox_ns_relative_path(dropbox_local_path)))
                continue
            if item[0] == PersistedOperationType.REMOVE_SYNC_DATABASE:
                dst = _get_db_ns_rel_path(item[2], dropbox_local_path)
                client_home_path = _get_db_ns_rel_path(item[3], dropbox_local_path)
                server_home_path = _get_db_ns_rel_path(item[4], dropbox_local_path)
                result.append((PersistedOperationType.REMOVE_SYNC_DATABASE.value, item[1], dst, client_home_path, server_home_path))
                continue
            if item[0] == PersistedOperationType.SEC_ONLY_FAST_PATCH_SYNC_DATABASE:
                raise FatalArrangementException('Can no longer execute FAST_PATCH_SYNC_DATABASE')
            if item[0] == PersistedOperationType.NUCLEUS_SPECIFIC_UPDATES:
                dst = _get_db_ns_rel_path(item[2], dropbox_local_path)
                client_home_path = _get_db_ns_rel_path(item[3], dropbox_local_path)
                server_home_path = _get_db_ns_rel_path(item[4], dropbox_local_path)
                result.append((PersistedOperationType.NUCLEUS_SPECIFIC_UPDATES.value, item[1], dst, client_home_path, server_home_path))
                continue
            if item[0] == PersistedOperationType.WRITE_NUCLEUS_MIGRATION_PARAMETERS:
                team_join = None
                if item[4]:
                    (home_lp, home_fileid) = item[4]
                    server_home_path = _get_db_ns_rel_path(home_lp, dropbox_local_path)
                    team_join = (server_home_path, home_fileid)
                result.append((PersistedOperationType.WRITE_NUCLEUS_MIGRATION_PARAMETERS.value, item[1], item[2], item[3], team_join))
                continue
            if item[0] == PersistedOperationType.WRITE_NUCLEUS_TMF_FILEID:
                home_path = _get_db_ns_rel_path(item[1], dropbox_local_path)
                result.append((PersistedOperationType.WRITE_NUCLEUS_TMF_FILEID.value, home_path, item[2]))
                continue
            if item[0] == PersistedOperationType.CHECK_OPEN_HANDLES:
                rel_path = _get_db_ns_rel_path(item[1], dropbox_local_path)
                result.append((PersistedOperationType.CHECK_OPEN_HANDLES.value, rel_path))
                continue
            if item[0] == PersistedOperationType.PRESERVE_FOLDER:
                rel_path = _get_db_ns_rel_path(item[1], dropbox_local_path)
                result.append((PersistedOperationType.PRESERVE_FOLDER.value, rel_path, item[2]))
                continue
            if item[0] == PersistedOperationType.SEC_ONLY_REMOVE_SYNCED_CONTENT:
                raise FatalArrangementException('Can no longer execute REMOVE_SYNCED_CONTENT')
            raise FatalArrangementException('CDM_RELOCATE: Unexpected operation type found: %r' % item)
            return result

    
    def _get_operation_list(self, dropbox_path = None, root_ns_id = None, home_ns_id = None, home_ns_path = ('dropbox_path', 'LocalPath', 'root_ns_id', 'int', 'home_ns_id', 'int', 'home_ns_path', 'LocalPath', 'return', 'List[OperationArgsType]')):
        client_home_ns_path_unicode = self._config.config_dict.get('home_ns_path', None)
        home_ns_path_exists = fsutil.exists(self._fs, home_ns_path)
        root_tag_ns = self._folder_tagger.get_folder_ns(dropbox_path)
    # WARNING: Decompyle incomplete

    
    def _safe_rename(self = None, cur_path = None, new_path = None, skip_restore = (False, True), use_shell_fallback = ('cur_path', 'LocalPath', 'new_path', 'LocalPath', 'skip_restore', 'bool', 'use_shell_fallback', 'bool', 'return', 'None')):
        if not IS_WINDOWS:
            will_set_read_only = self._fs.is_read_only(cur_path)
            path_to_read_only = cur_path
            
            try:
                if will_set_read_only:
                    self._update_read_only(cur_path, False)
                self._fs.rename(cur_path, new_path)
                path_to_read_only = new_path
                if will_set_read_only:
                    if not path_to_read_only == cur_path or skip_restore:
                        self._update_read_only(path_to_read_only, True)
                        return None
                    return None
                return None
            except:
                if will_set_read_only:
                    if not path_to_read_only == cur_path or skip_restore:
                        self._update_read_only(path_to_read_only, True)
                self._fs.rename(cur_path, new_path, use_shell_fallback = use_shell_fallback)
                return None


    
    def verbose_trace(self = None, string = None, *n, **kw):
        string = '[CDM_RELOCATE] ' + string
    # WARNING: Decompyle incomplete

    
    def _update_read_only(self = None, path = None, read_only = None):
        if self._fs.is_read_only(path) != read_only:
            self._set_read_only(path, read_only)
            return None

    
    def _set_read_only(self = None, path = None, read_only = None):
        self._fs.set_read_only(path, read_only)
        if read_only:
            fsutil.set_fs_bit_readonly(self._fs, path)
            return None
        fsutil.clear_fs_bits(self._fs, path)

    
    def _safe_remove_tree(self = None, path = None):
        set_read_only_recursive_helper(self._set_read_only, self._fs, path, False)
        fsutil.rmtree(self._fs, path, ignore_errors = False)

    
    def _report_fatal(self = None, fatal_type = None):
        self._log_cdm_move_attempt(fatal_type.value)

    
    def _report_temporary(self = None):
        self._log_cdm_move_attempt('temp_failure')

    
    def _report_permission_error(self = None):
        self._log_cdm_move_attempt('relocate_permission_error')

    
    def _report_removing_relocate_file(self = None):
        self._log_cdm_move_attempt('relocate_deleted')

    
    def _report_writing(self = None):
        self._log_cdm_move_attempt('relocate_written')

    
    def _report_success(self = None):
        self._log_cdm_move_attempt('success')

    
    def _report_async_restart_on_operation_file_write(self = None):
        self._log_cdm_move_attempt('async_restart_on_operation_file_write')

    
    def _report_async_restart_error(self = None):
        self._log_cdm_move_attempt('async_restart_error')

    
    def _report_non_cdm_dropbox_path_mismatch(self = None):
        self._log_cdm_move_attempt('non_cdm_dropbox_path_mismatch')

    
    def _report_config_nuked_on_non_empty_content_cdm(self = None):
        self._log_cdm_move_attempt('config_nuked_on_non_empty_content_cdm')

    
    def _report_config_nuked_on_non_empty_content_non_cdm(self = None):
        self._log_cdm_move_attempt('config_nuked_on_non_empty_content_non_cdm')

    
    def _report_fast_patch_error(self = None):
        self._log_cdm_move_attempt('fast_patch_error')

    
    def _report_fast_patch_root_not_found(self = None):
        self._log_cdm_move_attempt('fast_patch_root_not_found_in_cache')

    
    def _report_remove_synced_content_error(self = None):
        self._log_cdm_move_attempt('remove_synced_content_error')

    
    def _report_remove_synced_content_temp_error(self = None):
        self._log_cdm_move_attempt('remove_synced_content_temp_error')

    
    def _report_remove_synced_content_result(self = None, op_stats = None):
        self._log_cdm_move_attempt('remove_synced_content_result_%s' % op_stats.op_status.value)
    # WARNING: Decompyle incomplete

    
    def _report_dropbox_rename_fallback(self = None):
        self._log_cdm_move_attempt('rename_fallback')

    
    def _report_team_merge_skipped(self = None):
        self._log_cdm_move_attempt('team_merge_skipped')

    
    def _report_root_changed_during_relocation(self = None):
        self._log_cdm_move_attempt('nuc_root_changed_during_relocation')

    
    def _report_resume_in_progress_relocation(self = None):
        self._log_cdm_move_attempt('nuc_resume_in_progress_relocation')

    
    def _log_cdm_move_attempt(self = None, event_name = None, num_operations = None, operation_names = (None, None)):
        self.log_cdm_move_attempt(event_name, num_operations, operation_names)

    log_cdm_move_attempt = (lambda event_name = None, num_operations = None, operation_names = staticmethod: report('cdm-relocate-attempt', event_name = event_name, operation_count = num_operations, operation_names = operation_names, is_nucleus = True))()

