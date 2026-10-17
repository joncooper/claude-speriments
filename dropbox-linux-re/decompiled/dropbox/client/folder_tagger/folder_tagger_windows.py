# Source Generated with Decompyle++
# File: folder_tagger_windows.pyc (Python 3.11)

import contextlib
from typing import Any, Callable, Dict, List, Optional, Text, Union
from winffi.kernel32.api import FILE_ATTRIBUTE_HIDDEN, FILE_ATTRIBUTE_READONLY, FILE_ATTRIBUTE_SYSTEM, GetFileAttributesW, SetFileAttributesW
from build_number import is_frozen
from base_folder_tagger import BaseFolderTagger
from constants import FolderTag
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.folder_tagger.folder_icon_windows import FolderTagIcon
from dropbox.client.gandalf import Gandalf
from dropbox.client.util.win import FOLDER_INFOTIP
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_unicode
from dropbox.i18n import trans
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError
from dropbox.trace import TRACE
FileSystem = Any

class FolderTagger(BaseFolderTagger):
    pass
# WARNING: Decompyle incomplete

