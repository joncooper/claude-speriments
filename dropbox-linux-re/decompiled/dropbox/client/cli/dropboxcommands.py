# Source Generated with Decompyle++
# File: dropboxcommands.pyc (Python 3.11)

import os
from json import dumps as _dumps
from typing import Any, Callable, Dict, List, Mapping, Optional, Set, Text
from six import iteritems, iterkeys
from build_number import is_frozen
from dropbox.client.cli.commandserver import CommandArgType, CommandRetType, CommandServer, CommandType, IllegalArgumentException
from dropbox.client.client_shmodel import SharedLinkException
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.client.multiaccount.role import Roles
from dropbox.client.shell.linux import named_pipe_inqueue, named_pipe_outqueue
from dropbox.client.tray.sync_history import RECENTLY_CHANGED_FILES_CAP, SyncHistoryModel
from dropbox.client.util import get_contents_root, get_repo_root_unfrozen
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.model.types import FileId
from dropbox.preferences import AUTO_PROXY, HTTP, MANUAL_PROXY, NO_PROXY, OPT_P2P, SOCKS4, SOCKS5
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.local_path import InvalidDropboxPathException, LocalPathProperties, NonSyncingLocalPathException
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
MYPY = False
MSG_INIT = 0
MSG_FILE_STATUS = 1
MSG_RESERVED = 2
MSG_CONTEXT_OPTIONS = 3
MSG_CONTEXT_ACTION = 4
MSG_TOOLBAR_OPTIONS = 6
MSG_TOOLBAR_ACTION = 7
MSG_TRACE = 8
MSG_VERSION = 9
_SERVER_COMMANDS: 'Dict[Text, CommandType]' = { }

def __server_command(fn = None):
    name = Text(fn.__name__)
# WARNING: Decompyle incomplete


def add_commands(fn = None):
    for name, val in iteritems(_SERVER_COMMANDS):
        fn(Text(name), val)
        return None


def _get_user_context_for_primary_account(cs = None):
    pass
# WARNING: Decompyle incomplete


def _json_document(value = None):
    document = _dumps(value, ensure_ascii = False, separators = (',', ':'))
    if '\n' in document or '\r' in document:
        raise ValueError('Commandserver JSON responses must be single-line')
    return document


def _get_tag_info(nucleus_wrapper = None, local_path = None):
    location_props = nucleus_wrapper.lookup_properties_by_local_path(local_path).block().result()
# WARNING: Decompyle incomplete


def _args_to_enum(dmap, args, key):
    val = args[key].lower()
    
    try:
        return dmap[val]
    except KeyError:
        raise IllegalArgumentException(f'''Invalid value for `{key!s}` - options are {list(iterkeys(dmap))!r}''')


PROXY_MODE_MAP = {
    'none': NO_PROXY,
    'auto': AUTO_PROXY,
    'manual': MANUAL_PROXY }
PROXY_TYPE_MAP = {
    'http': HTTP,
    'socks4': SOCKS4,
    'socks5': SOCKS5 }
set_proxy_settings = (lambda cs = None, conn = None, args = __server_command: _args = iteritems(args)()mode = _args_to_enum(PROXY_MODE_MAP, _args, 'mode')prefs = {
'proxy_mode': mode }if prefs:
local_config = cs.app.config_manager.local_config(None)local_config.update_preferences(prefs)get_proxy_settings(cs, conn, { }))()
get_proxy_settings = (lambda cs = None, conn = None, args = __server_command: inverse_proxy_mode_map = iteritems(PROXY_MODE_MAP)()inverse_proxy_type_map = iteritems(PROXY_TYPE_MAP)()local_config = cs.app.config_manager.local_config(None)mode = local_config['proxy_mode']ret = {
'mode': inverse_proxy_mode_map[mode] }if mode == MANUAL_PROXY:
ret.update({
'type': inverse_proxy_type_map[local_config['proxy_type']],
'host': local_config['proxy_server'],
'port': local_config['proxy_port'] })username = local_config['proxy_username']if username:
ret['username'] = usernameiteritems(ret)())()
DOWNLOAD_MODE_MAP = {
    'unlimited': 0,
    'manual': 2 }
UPLOAD_MODE_MAP = {
    'unlimited': 0,
    'auto': 1,
    'manual': 2 }
get_bandwidth_limits = (lambda cs = None, conn = None, args = __server_command: inverse_download_mode_map = iteritems(DOWNLOAD_MODE_MAP)()inverse_upload_mode_map = iteritems(UPLOAD_MODE_MAP)()local_config = cs.app.config_manager.local_config(None)ret = {
'download_mode': inverse_download_mode_map.get(local_config['throttle_download_style']),
'upload_mode': inverse_upload_mode_map.get(local_config['throttle_upload_style']),
'download_limit': int(local_config['throttle_download_speed']),
'upload_limit': int(local_config['throttle_upload_speed']) }iteritems(ret)())()
set_bandwidth_limits = (lambda cs = None, conn = None, args = __server_command: _args = iteritems(args)()prefs = { }if 'download_mode' in _args:
dl_mode = _args_to_enum(DOWNLOAD_MODE_MAP, _args, 'download_mode')prefs['throttle_download_style'] = dl_modeif 'download_limit' in _args:
prefs['throttle_download_speed'] = float(_args['download_limit'])if 'upload_mode' in _args:
ul_mode = _args_to_enum(UPLOAD_MODE_MAP, _args, 'upload_mode')prefs['throttle_upload_style'] = ul_modeif 'upload_limit' in _args:
prefs['throttle_upload_speed'] = float(_args['upload_limit'])if prefs:
local_config = cs.app.config_manager.local_config(None)local_config.update_preferences(prefs)get_bandwidth_limits(cs, conn, { }))()
get_shared_link = (lambda cs = None, conn = None, args = __server_command: if 'path' not in args:
raise IllegalArgumentException("Missing 'path' argument")if len(args['path']) != 1:
raise IllegalArgumentException("The 'path' parameter requires single argument")path = args['path'][0]if not os.path.exists(path):
raise IllegalArgumentException(f'''The path "{path!s}" does not exist''')sv_resp = cs.app.client_shmodel.shmodel_from_localpath_async(cs.app.account_manager.primary, path, None)link = sv_resp.wait(timeout = 20)# WARNING: Decompyle incomplete
)()
get_folder_tag = (lambda cs = None, conn = None, args = __server_command: if 'path' not in args:
raise IllegalArgumentException("Missing 'path' argument")if len(args['path']) != 1:
raise IllegalArgumentException("The 'path' parameter requires single argument")path = args['path'][0]if not os.path.isdir(path):
raise IllegalArgumentException("The 'path' argument is not a directory")ret = {
'tag': [
''] }# WARNING: Decompyle incomplete
)()
is_out_of_date = (lambda cs = None, conn = None, args = __server_command: if 'version' not in args:
raise IllegalArgumentException("Missing 'version' argument")if len(args['version']) != 1:
raise IllegalArgumentException("The 'version' parameter requires single argument")version = args['version'][0]vers = version.split('.', 3)if len(vers) != 3:
raise IllegalArgumentException("The 'version' parameter isn't valid"){
'outofdate': [
'true'] })()
nautilus_dropbox_version = (lambda cs = None, conn = None, args = __server_command: if 'version' not in args:
raise IllegalArgumentException("Missing 'version' argument")if len(args['version']) != 1:
raise IllegalArgumentException("The 'version' parameter requires single argument")version = args['version'][0]vers = version.split('.', 3)if len(vers) != 3:
raise IllegalArgumentException("The 'version' parameter isn't valid"){ })()
icon_overlay_init = (lambda cs = None, conn = None, args = __server_command: named_pipe_inqueue.put((None, MSG_INIT))named_pipe_outqueue.get(){ })()
icon_overlay_file_status = (lambda cs = None, conn = None, args = __server_command: if 'path' not in args:
raise IllegalArgumentException("Missing 'path' argument")if len(args['path']) != 1:
raise IllegalArgumentException("The 'path' parameter requires single argument")path = args['path'][0]if not os.path.exists(path):
raise IllegalArgumentException("The 'path' argument does not exist")named_pipe_inqueue.put((path, MSG_FILE_STATUS))status = named_pipe_outqueue.get(){
'status': [
status] })()
icon_overlay_context_options = (lambda cs = None, conn = None, args = __server_command: if 'paths' not in args:
raise IllegalArgumentException("Missin 'paths' argument")paths = args['paths']for path in paths:
if not os.path.exists(path):
raise IllegalArgumentException(f'''The path "{path!s}" does not exist''')for path in paths[0:-1]:
named_pipe_inqueue.put((path + '|', MSG_CONTEXT_OPTIONS))named_pipe_outqueue.get()if len(paths) > 0:
named_pipe_inqueue.put((paths[len(paths) - 1], MSG_CONTEXT_OPTIONS))options = named_pipe_outqueue.get(){
'options': options.split('|') })()
icon_overlay_context_action = (lambda cs = None, conn = None, args = __server_command: if 'verb' not in args:
raise IllegalArgumentException("Missing 'verb' argument")if 'paths' not in args:
raise IllegalArgumentException("Missing 'paths' argument")if len(args['verb']) != 1:
raise IllegalArgumentException("'verb' parameter requires single argument ")verb = args['verb'][0]paths = args['paths']for path in paths:
if not os.path.exists(path):
raise IllegalArgumentException(f'''The path "{path!s}" does not exist''')for path in paths[0:-1]:
named_pipe_inqueue.put((path + '|', MSG_CONTEXT_OPTIONS))named_pipe_outqueue.get()named_pipe_inqueue.put((paths[len(paths) - 1], MSG_CONTEXT_OPTIONS))named_pipe_outqueue.get()named_pipe_inqueue.put((verb, MSG_CONTEXT_ACTION))named_pipe_outqueue.get(){ })()
get_quota = (lambda cs = None, conn = None, args = __server_command: if args:
raise IllegalArgumentException('get_quota takes no arguments')primary_user_context = _get_user_context_for_primary_account(cs)# WARNING: Decompyle incomplete
)()
get_recently_changed = (lambda cs = None, conn = None, args = __server_command: if args:
raise IllegalArgumentException('get_recently_changed takes no arguments')primary_user_context = _get_user_context_for_primary_account(cs)# WARNING: Decompyle incomplete
)()
get_dropbox_status = (lambda cs = None, conn = None, args = __server_command: if args:
raise IllegalArgumentException('get_dropbox_status takes no arguments')statuses = []fully_deprecated = False# WARNING: Decompyle incomplete
)()
soft_exit = (lambda cs = None, conn = None, args = __server_command: cs.app.soft_exit(ExitCode.SUCCESS, reason = 'Linux: soft exit command'){ })()
tray_action_open_dropbox = (lambda cs = None, conn = None, args = __server_command: cs.app.tray_menu_controller.file_opener_menu.open_dropbox(){ })()
tray_action_open_tray_login = (lambda cs = None, conn = None, args = __server_command: cs.app.tray_menu_controller.static_menu.open_tray_login(){ })()
tray_action_hard_exit = (lambda cs = None, conn = None, args = __server_command: cs.app.soft_exit(ExitCode.SUCCESS, reason = 'Linux: tray exit command'){ })()
tray_action_soft_resync = (lambda cs = None, conn = None, args = __server_command: cs.app.tray_menu_controller.debug_controller.soft_resync(){ })()
tray_action_launch_auth_page = (lambda cs = None, conn = None, args = __server_command: { })()
tray_action_open_prefs = (lambda cs = None, conn = None, args = __server_command: cs.app.ui_kit.enter_preferences(){ })()
tray_action_open_shell = (lambda cs = None, conn = None, args = __server_command: try:
raise Exception('not uh uh')except Exception:
report_exception(component = DesktopComponent.PREFERENCES_UI){ })()
needs_link = (lambda cs = None, conn = None, args = __server_command: if cs.app.account_manager and cs.app.account_manager.primary:
account = cs.app.account_manager.primaryelse:
raise IllegalArgumentException('No client link url available yet!')if account.linked:
{ }try:
ret = cs.app.conn.cli_link_nonce_gen(account, None){
'link_url': (ret['nonce_uri'],) }except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.PREFERENCES_UI)raise IllegalArgumentException('No client link url available yet!'))()
tag2emblem: 'Dict[Text, List[Text]]' = {
    FolderTag.CAMERA_UPLOADS: [],
    FolderTag.SANDBOX: [
        'dropbox-app'],
    FolderTag.FAMILY_SHARED_FOLDER: [
        'shared'],
    FolderTag.TEAM_FOLDER_READ_ONLY: [
        'shared'],
    FolderTag.TEAM_FOLDER: [
        'shared'],
    FolderTag.SHARED_VIEW_NAME_ONLY: [
        'shared'],
    FolderTag.SHARED_READ_ONLY: [
        'shared'],
    FolderTag.SHARED: [
        'shared'] }
status2emblem: 'Dict[Text, List[Text]]' = {
    'infinite': [
        'dropbox-infinite'],
    'mixed state': [
        'dropbox-mixedstate'],
    'ignored': [
        'dropbox-selsync'],
    'syncing': [
        'dropbox-syncing'],
    'unsyncable': [
        'dropbox-unsyncable'],
    'unwatched': [],
    'outside dropbox': [],
    'up to date': [
        'dropbox-uptodate'],
    'implicit local': [
        'dropbox-uptodate'] }
get_emblem_paths = (lambda cs = None, conn = None, args = __server_command: root = get_contents_root() if is_frozen() else get_repo_root_unfrozen(){
'path': (os.path.join(root, 'images/emblems'),) })()
get_emblems = (lambda cs = None, conn = None, args = __server_command: if 'path' not in args:
raise IllegalArgumentException("Missing 'path' argument")if len(args['path']) != 1:
raise IllegalArgumentException("The 'path' parameter requires single argument")path = args['path'][0]status = []tag = []named_pipe_inqueue.put((path, MSG_FILE_STATUS))try:
status = status2emblem[named_pipe_outqueue.get()]except Exception:
report_exception(component = DesktopComponent.PREFERENCES_UI)primary_user_context = _get_user_context_for_primary_account(cs)# WARNING: Decompyle incomplete
)()
test_update = (lambda cs = None, conn = None, args = __server_command: if 'path' not in args:
raise IllegalArgumentException("Missing 'path' argument")if len(args['path']) != 1:
raise IllegalArgumentException("The 'path' parameter requires single argument")path = args['path'][0]if not os.path.exists(path):
raise IllegalArgumentException("The 'path' parameter must exit")named_pipe_inqueue.put((path, 255)){ })()
get_ignore_set = (lambda cs = None, conn = None, args = __server_command: result = [
'']primary_user_context = _get_user_context_for_primary_account(cs)# WARNING: Decompyle incomplete
)()
ignore_set_remove = (lambda cs = None, conn = None, args = __server_command: pass# WARNING: Decompyle incomplete
)()
ignore_set_add = (lambda cs = None, conn = None, args = __server_command: pass# WARNING: Decompyle incomplete
)()
set_lan_sync = (lambda cs = None, conn = None, args = __server_command: if 'lansync' not in args:
raise IllegalArgumentException("Missing 'lansync' argument.")if len(args['lansync']) != 1:
raise IllegalArgumentException('This command requires must have one argument.')try:
new_state = {
'enabled': True,
'disabled': False }[args['lansync'][0]]except KeyError:
raise IllegalArgumentException("Only 'enabled' or 'disabled' is allowed as an argument")if cs.app:
try:
local_config = cs.app.config_manager.local_config(None)local_config.update_preferences({
OPT_P2P: new_state })except Exception:
report_exception(component = DesktopComponent.PREFERENCES_UI){ })()
