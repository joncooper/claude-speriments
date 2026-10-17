# Source Generated with Decompyle++
# File: photolibrary_utils.pyc (Python 3.11)

import os
from typing import Optional, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
if IS_MAC:
    from Foundation import CFPreferencesCopyAppValue, CFURLCreateByResolvingBookmarkData
    from dropbox.mac.internal import autoreleasepool

def get_photolibrary_path():
    if not IS_MAC:
        return None
    
    try:
        photos_domain = os.path.join(os.path.expanduser('~'), 'Library/Containers/com.apple.Photos/Data/Library/Preferences/com.apple.Photos')
        autoreleasepool()
        bookmark_data = CFPreferencesCopyAppValue('IPXDefaultLibraryURLBookmark', photos_domain)
        (url, _, _) = CFURLCreateByResolvingBookmarkData(None, bookmark_data, 0, None, None, None, None)
        path = Text(url.fileSystemRepresentation(), 'utf-8')
        TRACE('[Sync Everything] found photolibrary at path %r', path)
        
        try:
            None(None, None)
            return 
            with None:
                if not None, path:
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            TRACE('[Sync Everything] hit exception parsing %r', e)
                            report_exception(severity = Severity.TRACE, component = DesktopComponent.SYNC_EVERYTHING)
                            None = None
                            del e
                            return None
                            e = None
                            del e





