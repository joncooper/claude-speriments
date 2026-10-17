# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, List, Text
from six import iteritems
from dropbox.client.util.win import get_executable
from dropbox.proto.database.icons_pb2 import CAMERA_UPLOADS, DBXIcon, DEVICE_FOLDER_DESKTOP, DEVICE_FOLDER_DOCUMENTS, DEVICE_FOLDER_DOWNLOADS, DEVICE_FOLDER_GENERIC, DEVICE_FOLDER_MAC, DEVICE_FOLDER_MUSIC, DEVICE_FOLDER_PICTURES, DEVICE_FOLDER_VIDEOS, DEVICE_FOLDER_WIN, DROPBOX, ENCRYPTED_TEAM_FOLDER, FAMILY_SHARED_FOLDER, SANDBOX, SHARED, SHARED_READ_ONLY, SHARED_VIEW_NAME_ONLY, TEAM_FOLDER, TEAM_FOLDER_READ_ONLY, TEAM_MEMBER_FOLDER, VAULT
from dropbox.win32.version import WIN10, WIN11_VERSION_2109, WINDOWS_VERSION
MYPY = False
if MYPY:
    from dropbox.proto.database.icons_pb2 import DBXIconType

def generate_icon_paths():
    executable_path = get_executable() + ',-{}'
    imageres_path = '%SystemRoot%\\system32\\imageres.dll,-{}'
    icon_dict = { }
# WARNING: Decompyle incomplete

