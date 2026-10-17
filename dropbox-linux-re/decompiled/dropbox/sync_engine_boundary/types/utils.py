# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import Dict, Mapping, Optional
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties, NonSyncingLocalPathException
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.sync_engine_boundary.types.remote_props import DirectoryProperties, MountProperties, RemoteLocationProperties

def is_remote_dir(remote_props = None):
    return isinstance(remote_props.file_type, (DirectoryProperties, MountProperties))


def is_local_dir(local_props = None):
    return isinstance(local_props.file_type, LocalLocationProperties)


def local_path_properties_to_fileid(local_path_to_props = None):
    local_path_to_fileid = { }
    for path, props in local_path_to_props.items():
        local_path_to_fileid[path] = props.fileid()
        except NonSyncingLocalPathException:
            local_path_to_fileid[path] = None
            continue
        return local_path_to_fileid

