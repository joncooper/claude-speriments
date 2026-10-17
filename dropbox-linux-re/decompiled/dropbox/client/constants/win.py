# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

from __future__ import absolute_import
import os
from collections import namedtuple
from typing import NamedTuple, Text
from build_number import BUILD_KEY
from win32com.shell import shellcon
from dropbox.win32.internal import get_user_folder_path

def path_from_name(dropbox_folder_name):
    user_folder_path = get_user_folder_path(shellcon.CSIDL_PROFILE)
    return os.path.join(user_folder_path, dropbox_folder_name)


def get_omaha4_crashpad_usage_stats_folder_path():
    raise NotImplementedError

DEFAULT_DROPBOX_FOLDER_NAME = BUILD_KEY
DEFAULT_DROPBOX_PATH = path_from_name(DEFAULT_DROPBOX_FOLDER_NAME)
LOCAL_FORM = 'NFC'
LOCAL_APPDATA = get_user_folder_path(shellcon.CSIDL_LOCAL_APPDATA)
ROAMING_APPDATA = get_user_folder_path(shellcon.CSIDL_APPDATA)
DROPBOX_LOCAL_APPDATA = os.path.join(LOCAL_APPDATA, BUILD_KEY)
DROPBOX_ROAMING_APPDATA = os.path.join(ROAMING_APPDATA, BUILD_KEY)
DEFAULT_BINARY_PATH = DROPBOX_ROAMING_APPDATA
common_appdata_path = get_user_folder_path(shellcon.CSIDL_COMMON_APPDATA)

class AppDataPaths(object):
    dropbox_appdata_path = DROPBOX_LOCAL_APPDATA
    instance_config_path = os.path.join(dropbox_appdata_path, 'instance_db')

DROPBOX_OMAHA_GUID = '{CC46080E-4C33-4981-859A-BBA2F780F31E}'
DROPBOX_UPDATER_CLIENTS_KEY = f'''Software\\DropboxUpdate\\Update\\Clients\\{DROPBOX_OMAHA_GUID}'''
DROPBOX_UPDATER_CLIENT_STATE_KEY = f'''Software\\DropboxUpdate\\Update\\ClientState\\{DROPBOX_OMAHA_GUID}'''
DROPBOX_UNINSTALL_KEY = 'Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\%s' % BUILD_KEY
DROPBOX_OEM_LOE_KEY = 'SOFTWARE\\DropboxOEM'
COMPAT_MODE_FLAG_LOCATION = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers'
UNSUPPORTED_COMPAT_MODE_FLAGS = [
    'WIN2000',
    'WINXP',
    'WINXPSP2',
    'WINXPSP3',
    'VISTARTM',
    'VISTASP1',
    'VISTASP2',
    'WIN7RTM',
    'WINSRV03SP1',
    'WINSRV08SP1',
    'WIN8RTM']
KillProcessByNameResult = NamedTuple('KillProcessByNameResult', [
    ('success', bool),
    ('kill_count', int)])
DEFAULT_KILL_PROCESS_BY_NAME_TIMEOUT_MS = 600000
NAMED_PROCESS_EVENT_PREFIX = 'Global\\' + BUILD_KEY + 'Event'
WinProcessInfo = namedtuple('WinProcessInfo', [
    'handle',
    'name',
    'pid'])
