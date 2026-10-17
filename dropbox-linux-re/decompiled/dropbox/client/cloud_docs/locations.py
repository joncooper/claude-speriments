# Source Generated with Decompyle++
# File: locations.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Optional, Text
from dropbox.client.cloud_docs.constants import CloudDocsFileLocation
from dropbox.fileutils import is_path_trash
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_path import InvalidDropboxPathException

def get_path_location(file_path = None, sync_engine_wrapper = None):
    
    def is_path_in_home_ns(sync_engine = None, path = None):
        nucleus_wrapper = sync_engine
        local_path = nucleus_wrapper.file_system.make_path(path)
        
        try:
            server_path = nucleus_wrapper.lookup_local_path_properties(local_path).block().result().mr_server_path()
            return server_path.ns == nucleus_wrapper.account.home_ns_id
        except InvalidDropboxPathException:
            pass

        return False

# WARNING: Decompyle incomplete


def guess_external_path_location(file_path = None):
    if is_path_trash(file_path):
        return CloudDocsFileLocation.TRASH
    home_dir = None.path.expanduser('~')
    
    try:
        rel_path = os.path.relpath(file_path, home_dir)
    except ValueError:
        return 

    if rel_path.startswith('Downloads' + os.path.sep):
        return CloudDocsFileLocation.DOWNLOADS
    if None.startswith('AppData' + os.path.sep):
        return CloudDocsFileLocation.APP_DATA

