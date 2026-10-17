# Source Generated with Decompyle++
# File: file_locking_predicates.pyc (Python 3.11)

import os
from typing import Text
from dropbox.client.cloud_docs.file_validator import is_shortcut
from dropbox.client.features.file_locking.constants import FILE_LOCKING_SHORTCUT_EXTENSIONS
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockState
from dropbox.sync_engine_boundary.path_properties import PathProperties
from dropbox.sync_engine_boundary.types.remote_props import FileLikeProperties, RemoteLocationProperties
from dropbox.sync_engine_boundary.types.utils import is_remote_dir

def is_local_shortcut(local_path = None):
    return os.path.splitext(Text(local_path))[1] in FILE_LOCKING_SHORTCUT_EXTENSIONS


def file_locking_supported(local_path = None, props = None):
