# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import
import os
import unicodedata
from build_number import BUILD_KEY
MYPY = False
if MYPY:
    from typing import Text
DEFAULT_DROPBOX_FOLDER_NAME = BUILD_KEY
LOCAL_FORM = 'NFD'

def path_from_name(dropbox_folder_name):
    return unicodedata.normalize(LOCAL_FORM, os.path.expanduser('~/%s' % dropbox_folder_name))


class AppDataPaths(object):
    dropbox_appdata_path = unicodedata.normalize(LOCAL_FORM, os.path.expanduser('~/.%s' % BUILD_KEY.lower()))
    instance_config_path = os.path.join(dropbox_appdata_path, 'instance_db')

DEFAULT_DROPBOX_PATH = path_from_name(DEFAULT_DROPBOX_FOLDER_NAME)

def get_alt_install_path_base():
    return f'''~/Library/Application Support/Dropbox/{BUILD_KEY!s}.app'''


def get_alt_install_path():
    return os.path.expanduser(get_alt_install_path_base())


def get_omaha4_crashpad_usage_stats_folder_path():
    return os.path.expanduser(os.path.join('~/Library', 'Application Support', 'Dropbox', BUILD_KEY))

