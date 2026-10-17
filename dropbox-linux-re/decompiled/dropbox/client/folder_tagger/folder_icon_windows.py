# Source Generated with Decompyle++
# File: folder_icon_windows.pyc (Python 3.11)

import os.path as os
from typing import Dict, Text, Tuple
from build_number import BUILD_KEY, is_frozen
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.client.util.win import get_install_dir
from dropbox.win32.version import WIN10, WINDOWS_VERSION
_INSTALL_DIR = get_install_dir() if is_frozen() else ''
_EXECUTABLE_PATH = os.path.join(_INSTALL_DIR, '%s.exe' % BUILD_KEY)
_ICON_INDEX_BASE = 2000 if WINDOWS_VERSION.version_number() >= WIN10.version_number() else 1000

class FolderTagIcon:
    icon_tags: 'Dict[Text, Tuple[Text, int]]' = {
        FolderTag.ENCRYPTED_TEAM_FOLDER: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1606)),
        FolderTag.TEAM_MEMBER_FOLDER: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1604)),
        FolderTag.SHARED_VIEW_NAME_ONLY: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1603)),
        FolderTag.SHARED_READ_ONLY: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1602)),
        FolderTag.TEAM_FOLDER_READ_ONLY: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1605)),
        FolderTag.TEAM_FOLDER: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1601)),
        FolderTag.CAMERA_UPLOADS: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1501)),
        FolderTag.SANDBOX: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1401)),
        FolderTag.SHARED: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1301)),
        FolderTag.DROPBOX: (_EXECUTABLE_PATH, -(_ICON_INDEX_BASE + 1001)) }

