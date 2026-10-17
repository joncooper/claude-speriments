# Source Generated with Decompyle++
# File: tray_utils.pyc (Python 3.11)

from typing import Optional
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict

def normalize_file_id(file_id = None):
    if file_id and file_id.startswith('id:'):
        return file_id[3:]


def parse_bool_arg(args = None, key = None):
    value = args.get(key)
# WARNING: Decompyle incomplete


def parse_optional_str_arg(args = None, key = None):
    value = args.get(key)
    return str(value) if value else None

