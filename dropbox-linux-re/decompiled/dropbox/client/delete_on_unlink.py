# Source Generated with Decompyle++
# File: delete_on_unlink.pyc (Python 3.11)

import os
import stat
import subprocess
import time
import traceback
from tempfile import gettempdir, mkdtemp
from typing import Any, cast, Dict, List, Optional, Text, Tuple, Union
from apex.context import ApexContext
from build_number.features import feature_enabled
from dropbox import fsutil
from dropbox.client.authentication.account import Account
from dropbox.client.databases import clear_appdata_for_unlink
from dropbox.client.file_permissions import fix_perms_without_prompt_if_needed
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.unlink_cookie import get_host_secret_from_unlink_cookie, HOST_SECRET_KEYNAME, write_unlink_cookie_no_sync_engine
from dropbox.client.unlink_handlers import report_unlink_event, UnlinkReason
from dropbox.client.util import get_user_agent_dict, start_unlink_and_quit
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import DropboxResponseServerError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_str
from dropbox.i18n import safe_activate_translation, trans
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_engine_boundary.file_system_exceptions import DirectoryNotEmptyError, FileSystemError
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.helpers import destroy_root_from_config
from dropbox.sync_root.types import RemovalMode, SyncRootType
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
if IS_WINDOWS:
    from pynt.constants import ERROR_SHARING_VIOLATION
elif not IS_MAC and IS_LINUX:
    raise ImportError('Current platform not supported!')
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import LocalConfigurationInterface
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility
PathDataTuple = Tuple[(Text, Optional[Text], Optional[int], bool, Dict[(Text, Any)])]

class DeleteOnUnlink(object):
    NO_DELETE = 0
    DELETE_REQUESTED = 1
    RETRY_DELETE = 2
    DELETEDATA_TRUE = 'deletedata_true'
    UNLINK_MESSAGE_KEY = 'unlink_message'
    
    class ServerState(object):
        DELETE_IN_PROGRESS = 3
        DELETE_COMPLETED = 4
        DELETE_FAILED = 5

    RETRY_INTERVAL_SEC = 300
    
    def __init__(self = None, app = None):
        self.app = app
        self.restart = True

    
    def start_delete(self, apex_context = None, local_config = None, unlink_message = None, restart_message = ('apex_context', 'ApexContext', 'local_config', 'LocalConfigurationInterface', 'unlink_message', 'Optional[Text]', 'restart_message', 'Optional[Text]', 'return', 'None')):
        self._persist_state(local_config, delete_stage = DeleteOnUnlink.DELETE_REQUESTED, restart_message = restart_message, unlink_message = unlink_message)
        self._report_to_server(apex_context, local_config, finished = False)
        self.app.restart()

    
    def show_unlink_message_dialog(self = None):
        if not feature_enabled('multiaccount'):
            return False
        instance_config = None.app.instance_config
        unlink_msg = instance_config.get_shared_config(DeleteOnUnlink.UNLINK_MESSAGE_KEY)
        if unlink_msg:
            dialog_future = self.app.ui_kit.show_native_blocking_dialog(caption = trans('Dropbox folder deleted'), message = unlink_msg, buttons = [
                trans(MiscStrings.ok_button)], dialog_source_type = DialogSourceTypes.OTHER)
            dialog_future.block()
            instance_config.set_shared_config(DeleteOnUnlink.UNLINK_MESSAGE_KEY, None)
            return True

    
    def connect_and_check_for_delete(self = None, apex_context = None, local_config = None, is_primary = ('apex_context', 'ApexContext', 'local_config', 'LocalConfigurationInterface', 'is_primary', 'bool', 'return', 'None')):
        if self._get_stage(local_config) == DeleteOnUnlink.NO_DELETE and local_config.unlink_cookie and HOST_SECRET_KEYNAME in local_config.unlink_cookie:
            
            try:
                (conn, account) = self._create_connection(apex_context, local_config)
                
                try:
                    ret = conn.check_for_unlink(account)
                    
                    try:
                        if ret.get('deletedata') == DeleteOnUnlink.DELETEDATA_TRUE:
                            self._persist_state(local_config, delete_stage = DeleteOnUnlink.DELETE_REQUESTED, restart_message = ret.get('restart_message'), unlink_message = ret.get('unlink_message'))
                        else:
                            except (IOError, DropboxResponseServerError):
                                TRACE('Could not check if linked with server; retrying in 60 seconds')
                                time.sleep(60)
                                
                                try:
                                    pass
                                try:
                                    continue
                                except Exception:
                                    report_exception(component = DesktopComponent.ACCOUNT_MANAGEMENT)

                                self.restart = False
                                self.check_for_delete(apex_context, local_config, is_primary)
                                return None




    
    def check_for_delete(self = None, apex_context = None, local_config = None, is_primary = ('apex_context', 'ApexContext', 'local_config', 'LocalConfigurationInterface', 'is_primary', 'bool', 'return', 'None')):
        if self._get_stage(local_config) != DeleteOnUnlink.NO_DELETE:
            TRACE('Delete on unlink detected: %r', local_config.unlink_cookie.get('delete_stage'))
            
            try:
                self._delete_data(apex_context, local_config, is_primary)
                return None
            except Exception:
                report_exception(severity = Severity.CRITICAL, component = DesktopComponent.ACCOUNT_MANAGEMENT)
                self._delete_dbs_and_restart(local_config, is_primary)
            except Exception:
                report_exception(component = DesktopComponent.ACCOUNT_MANAGEMENT)
            except:
                return None

            return None
        TRACE('No delete on unlink in progress')

    
    def on_second_instance_exit(self = None, exit_code = None):
        local_config = self.app.config_manager.local_config(None)
        if self._get_stage(local_config) != DeleteOnUnlink.RETRY_DELETE:
            return None
        if None or self.app.system_startup or local_config.unlink_cookie:
            restart_message = local_config.unlink_cookie.get('restart_message')
            if restart_message:
                import win32api
                win32api.MessageBox(None, restart_message, 'Dropbox', 4096)
                return None
            return None
        return None
        return None

    
    def _get_stage(self = None, local_config = None):
        if not local_config.unlink_cookie:
            return DeleteOnUnlink.NO_DELETE
        return None.unlink_cookie.get('delete_stage', DeleteOnUnlink.NO_DELETE)

    
    def _delete_data(self = None, apex_context = None, local_config = None, is_primary = ('apex_context', 'ApexContext', 'local_config', 'LocalConfigurationInterface', 'is_primary', 'bool', 'return', 'None')):
        fs = SyncEngineFactory.make_default_file_system()
        paths_to_delete = []
    # WARNING: Decompyle incomplete

    
    def _delete_dbs_and_restart(self = None, local_config = None, is_primary = None):
        if feature_enabled('multi-team-accounts-prod'):
            if not not is_primary:
                pass
            multi_account = self.app.instance_config.get_linked_account_count() > 1
        elif not not is_primary:
            multi_account = local_config.has_secondary_creds
            clear_appdata_for_unlink(database_dir = local_config.appdata_path, clear_unlink_cookie = True)
            if local_config.unlink_cookie:
                unlink_msg = cast(Optional[Text], local_config.unlink_cookie.get('unlink_message'))
                if multi_account and unlink_msg:
                    self.app.instance_config.set_shared_config(DeleteOnUnlink.UNLINK_MESSAGE_KEY, unlink_msg)
        report_unlink_event(reason_code = UnlinkReason.REMOTE_UNLINK, is_primary = is_primary)
        if not self.restart:
            return None
        if not is_primary:
            if is_primary:
                start_unlink_and_quit('/unlinkr', self.app.dialog_controller)
                return None
            None.app.restart([
                '/unlinksecondary'])
            return None
        if None:
            if IS_WINDOWS:
                unlink_msg = '"' + unlink_msg.replace('"', '\\"') + '"'
            self.app.restart([
                make_str('/unlinkmessage'),
                make_str(unlink_msg)])
            return None
        None.app.restart()

    
    def _persist_state(self = None, local_config = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _report_to_server(self = None, apex_context = None, local_config = None, paths_to_delete = ([], True), finished = ('apex_context', 'ApexContext', 'local_config', 'LocalConfigurationInterface', 'paths_to_delete', 'List[PathDataTuple]', 'finished', 'bool', 'return', 'None')):
        if not finished:
            delete_state = DeleteOnUnlink.ServerState.DELETE_IN_PROGRESS
        elif len(paths_to_delete) == 0:
            delete_state = DeleteOnUnlink.ServerState.DELETE_COMPLETED
        else:
            delete_state = DeleteOnUnlink.ServerState.DELETE_FAILED
        TRACE('Reporting delete on unlink state to the server')
        (conn, account) = self._create_connection(apex_context, local_config)
        
        try:
            conn.record_unlink_state(account, delete_state, paths_to_delete)
            TRACE('Unlink state reported to server')
            return None
        except (IOError, DropboxResponseServerError):
            TRACE('Could not report unlink_state to server; retrying in 60 seconds')
            time.sleep(60)
        except Exception:
            TRACE('Could not report unlink_state to server; giving up')
            return None

        continue

    
    def _create_connection(self = None, apex_context = None, local_config = None):
        conn = DropboxConnection(hosts = dropbox_url_info.api_hosts, user_agent_dict = get_user_agent_dict(), legacy_usage_skip_metrics = True, apex_context = apex_context)
        mock_account = Account()
    # WARNING: Decompyle incomplete



def _run_command_and_get_output_wrapping_failures(args = None, encoding = None, errors = None, **kwargs):
    pass
# WARNING: Decompyle incomplete

_get_extra_info_for_failed_path = (lambda fs = None, path = None, formatted_exc = handle_exceptions: extra_path_info = { }if formatted_exc:
extra_path_info['exception_traceback'] = formatted_exctry:
path_attrs = fs.indexing_attributes(path, resolve_link = False)extra_path_info['indexing_attributes'] = dict(type = path_attrs.type, is_read_only = path_attrs.is_read_only)except FileSystemError:
e = Noneextra_path_info['indexing_attributes'] = str(e)e = Nonedel eexcept Exception:
exc2 = Noneextra_path_info['indexing_attributes'] = str(exc2)TRACE('Caught unexpected exception %s in call to indexing_attributes for path %s', exc2, path)report_exception(component = DesktopComponent.ACCOUNT_MANAGEMENT)exc2 = Nonedel exc2except:
exc2 = Nonedel exc2if IS_WINDOWS:
import win32apisystem_path = win32api.GetSystemDirectory()extra_path_info['attrib'] = _run_command_and_get_output_wrapping_failures([
os.path.join(system_path, 'attrib.exe'),
path], encoding = 'oem')extra_path_info['icacls'] = _run_command_and_get_output_wrapping_failures([
os.path.join(system_path, 'icacls.exe'),
path], encoding = 'oem')elif IS_MAC:
extra_path_info['ls'] = _run_command_and_get_output_wrapping_failures([
'ls',
'-lOed',
path])elif IS_LINUX:
extra_path_info['ls'] = _run_command_and_get_output_wrapping_failures([
'ls',
'-ld',
path])extra_path_info['lsattr'] = _run_command_and_get_output_wrapping_failures([
'lsattr',
'-ld',
path])extra_path_info['getfacl'] = _run_command_and_get_output_wrapping_failures([
'getfacl',
path])extra_path_info)()

def _move_to_tmp(path = None):
    
    try:
        move_to_temp = _find_mount_point(gettempdir()) == _find_mount_point(path)
    except OSError:
        e = None
        TRACE("Could not check if '%r' and TEMP are on the same drive: %r", path, e)
        move_to_temp = False
        e = None
        del e
    except:
        e = None
        del e

    if move_to_temp:
        new_name = 'dbfldr'
        new_dir = mkdtemp(prefix = '')
    else:
        safe_activate_translation()
        new_name = trans('Deleted Dropbox')
        new_dir = mkdtemp(dir = os.path.dirname(path), prefix = new_name + ' - ')
    
    try:
        os.chmod(path, stat.S_IREAD | stat.S_IWRITE | stat.S_IXUSR)
        os.rename(path, os.path.join(new_dir, new_name))
        path = new_dir
        TRACE('Moved the Dropbox folder to %r', new_dir)
    except OSError:
        e = None
        TRACE('Could not move the Dropbox folder to %r, error=%r, traceback=%s', new_dir, e, traceback.format_exc())
        os.rmdir(new_dir)
        e = None
        del e
    except:
        e = None
        del e

    return path


def delete_failed_paths(fs = None, paths_to_delete = None):
    failures = []
# WARNING: Decompyle incomplete


def _rmrf(fs = None, root_path = None):
    pass
# WARNING: Decompyle incomplete


def _find_mount_point(path = None):
    path = os.path.abspath(path)
# WARNING: Decompyle incomplete

