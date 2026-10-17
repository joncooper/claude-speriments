# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import os
from os import listdir
from os.path import exists, isdir
from typing import Dict, List, Mapping, Optional
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_auto_selsync.constants import TOP_LEVEL_NAMES_TO_IGNORE
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.types.remote_props import DirPnmBehaviors, RemoteLocationProperties
from dropbox.trace import TRACE

def does_path_exist(path = None):
    return exists(path)


def list_top_level_entries(path = None, only_dirs = None):
    
    try:
        top_level_objects = listdir(path)
    except FileNotFoundError:
        TRACE('Path does not exist %s', path)
        return 

    [] = []
    for object_name in top_level_objects:
        if not (object_name.lower().strip() in TOP_LEVEL_NAMES_TO_IGNORE or only_dirs) and isdir(os.path.join(path, object_name)):
            ignored_objects.append(object_name.strip())
            continue
        cleansed_top_level_entries.append(object_name)
        TRACE('Found cleansed_top_level_entries (only_dir: %r): %r ; Ignoring following objects: %r', only_dirs, ','.join(cleansed_top_level_entries), ','.join(ignored_objects))
        return cleansed_top_level_entries


def does_non_empty_directory_exist_by_path(path = None):
    if isdir(path):
        pass
    return len(list_top_level_entries(path, only_dirs = False)) > 0


def get_local_backups(root_entry_mapping = None):
    current_machine_uuid = UNSAFE_get_raw_machine_uuid()
    local_backups = { }
# WARNING: Decompyle incomplete

