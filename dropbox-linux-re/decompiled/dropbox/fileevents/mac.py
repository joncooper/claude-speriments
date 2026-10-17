# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Optional, Text, Type
from common import BaseMetaDirectoryWatch, BaseMetaDirectoryWatchManager, FILEEVENT_REPORT_PREFIX, NoWorkingWatchError
from dbfsevents import MetaDirectoryWatch as DBFSEventMetaDirectoryWatch
from dir_fsevents import MetaDirectoryWatch as DirectoryEventMetaDirectoryWatch
from file_fsevents import MetaDirectoryWatch as FileEventMetaDirectoryWatch
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.mac.version import CATALINA, MAC_VERSION

def use_file_level_fsevents(gandalf = None):
    if MAC_VERSION >= CATALINA:
        return True
    if None and gandalf.get_variant('desktop-file-level-fsevents') == 'ACTIVE':
        return True


class MetaDirectoryWatchManager(BaseMetaDirectoryWatchManager):
    
    def __init__(self = None, gandalf = None):
        self.cur = None
        self.gandalf = gandalf

    
    def make_next_metawatch(self = None, reason = None):
        ret = None
    # WARNING: Decompyle incomplete


