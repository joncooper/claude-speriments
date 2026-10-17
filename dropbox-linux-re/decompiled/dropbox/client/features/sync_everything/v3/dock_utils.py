# Source Generated with Decompyle++
# File: dock_utils.pyc (Python 3.11)

import subprocess
from typing import Any, Dict, Optional, Text
from dropbox.platform import IS_MAC
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.trace import TRACE
if IS_MAC:
    from AppKit import NSDictionary, NSURL
    from Foundation import CFPreferencesAppSynchronize, CFPreferencesCopyAppValue, CFPreferencesSetAppValue
    from dropbox.mac.internal import autoreleasepool

class ReplaceDockEntryException(Exception):
    pass


class DockEntryHelper:
    DOCK_DOMAIN = 'com.apple.dock'
    DOCK_LAUNCHD_AGENT = 'com.apple.Dock.agent'
    DOCK_LAUNCHD_FILE = '/System/Library/LaunchAgents/com.apple.Dock.plist'
    
    def __init__(self = None):
        self._persistent_others = CFPreferencesCopyAppValue('persistent-others', self.DOCK_DOMAIN).mutableCopy()

    
    def _safe_get(self = None, obj = None, *keys):
        for key in keys:
            if isinstance(obj, NSDictionary) and key in obj:
                obj = obj.get(key)
                continue
            return None
            return obj

    
    def _find_matching_entry(self = None, search_path = None):
        search_ns_url = NSURL.fileURLWithPath_(search_path.to_unicode()).absoluteString()
        i = 0
    # WARNING: Decompyle incomplete

    
    def _save(self = None):
        subprocess.call([
            '/bin/launchctl',
            'unload',
            self.DOCK_LAUNCHD_FILE])
        CFPreferencesSetAppValue('persistent-others', self._persistent_others, self.DOCK_DOMAIN)
        CFPreferencesAppSynchronize(self.DOCK_DOMAIN)
        subprocess.call([
            '/bin/launchctl',
            'load',
            self.DOCK_LAUNCHD_FILE])
        subprocess.call([
            '/bin/launchctl',
            'start',
            self.DOCK_LAUNCHD_AGENT])

    
    def has_entry(self = None, search_path = None):
        autoreleasepool()
        None(None, None)
        return 
        with None:
            if not None, self._find_matching_entry(search_path) != -1:
                pass

    
    def replace(self = None, folder_id = None, search_path = None, replacement_path = ('folder_id', 'OSFolderID', 'search_path', 'LocalPath', 'replacement_path', 'LocalPath', 'return', 'bool')):
        pass
    # WARNING: Decompyle incomplete


