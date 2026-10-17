# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Dict, Text
from six import add_metaclass
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS

class UserFolderPathKeys(Enum):
    DOCUMENTS = 'DOCUMENTS'
    DESKTOP = 'DESKTOP'
    PICTURES = 'PICTURES'
    MUSIC = 'MUSIC'
    VIDEOS = 'VIDEOS'
    DOWNLOADS = 'DOWNLOADS'

UserFolderPaths = <NODE:12>()
