# Source Generated with Decompyle++
# File: hidden_symlink.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Any, Optional, Text
from dropbox.client.constants import DEFAULT_DROPBOX_FOLDER_NAME
from dropbox.client.util import create_hidden_symlink
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.fsutil import CreateHiddenSymlinkStatus
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError
from dropbox.trace import TRACE

def get_hidden_symlink(fs = None, folder = None, potential_symlink = None):
    if folder.basename == DEFAULT_DROPBOX_FOLDER_NAME:
        return None
# WARNING: Decompyle incomplete


def move_hidden_symlink(fs, symlink, new_folder):
    
    try:
        fs.remove_symbolic_link(symlink)
        ret = create_hidden_symlink(Text(symlink), Text(new_folder))
        if ret == CreateHiddenSymlinkStatus.SUCCESS:
            TRACE('Moved hidden symlink at %s to point to %s', Text(symlink), Text(new_folder))
            return None
        TRACE('Re-creating hidden symlink at %s failed with code: %d', Text(symlink), ret)
        return None
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)
        return None


