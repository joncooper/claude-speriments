# Source Generated with Decompyle++
# File: symlink_util.pyc (Python 3.11)

from __future__ import absolute_import
import os
import re
import stat
from typing import Any, Optional, Text, Tuple, Union
from dropbox.fileutils import is_case_insensitive_path
from dropbox.platform import IS_WINDOWS
from dropbox.shared.util import db_lower
from dropbox.trace import TRACE

def is_decodable(linkpath = None):
    return bool(re.search('[\\uD800-\\uDFFF]', linkpath) is None)


def compute_target_paths(file_system = None, curdir = None, link = None, dropbox_folder_path = ('file_system', 'Any', 'curdir', 'Text', 'link', 'Text', 'dropbox_folder_path', 'Text', 'return', 'Tuple[Text, Optional[Text]]')):
    separator = file_system.make_path(dropbox_folder_path).SEPARATOR
    if file_system.is_absolute_path(link):
        linkpath = Text(file_system.realpath(link))
    else:
        linkpath = Text(file_system.realpath(curdir + separator + link))
    folder_realpath = Text(file_system.realpath(dropbox_folder_path)) + separator
    target_root_relative_path = None
    if IS_WINDOWS:
        inside_dropbox = db_lower(linkpath).startswith(db_lower(folder_realpath))
    else:
        inside_dropbox = linkpath.startswith(folder_realpath)
    if inside_dropbox:
        target_root_relative_path = linkpath[len(folder_realpath) - 1:].replace(separator, '/')
    return (linkpath, target_root_relative_path)


def _iterate_up_to(rel, path, case_insensitive = (True,)):
    pass
# WARNING: Decompyle incomplete

if IS_WINDOWS:
    
    def should_recurse(path, rel, case_insensitive = ('/', True)):
        return True

    return None

def should_recurse(path, rel, case_insensitive = None):
    pass
# WARNING: Decompyle incomplete

