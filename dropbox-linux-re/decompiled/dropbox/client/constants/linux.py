# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import
import os
import unicodedata
from build_number import BUILD_KEY
MYPY = False
if MYPY:
    from typing import Text
LOCAL_FORM = 'NFC'

def path_from_name(dropbox_folder_name):
    return unicodedata.normalize(LOCAL_FORM, os.path.expanduser('~/%s' % dropbox_folder_name))


class AppDataPaths(object):
    dropbox_appdata_path = unicodedata.normalize(LOCAL_FORM, os.path.expanduser('~/.%s' % BUILD_KEY.lower()))
    instance_config_path = os.path.join(dropbox_appdata_path, 'instance_db')


def get_omaha4_crashpad_usage_stats_folder_path():
    raise NotImplementedError

DEFAULT_DROPBOX_FOLDER_NAME = BUILD_KEY
DEFAULT_DROPBOX_PATH = path_from_name(DEFAULT_DROPBOX_FOLDER_NAME)
UPDATE_ROOT = os.path.expanduser('~/.dropbox-dist')
