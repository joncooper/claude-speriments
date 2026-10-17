# Source Generated with Decompyle++
# File: shutdown_marker.pyc (Python 3.11)

import os
from typing import Text
from dropbox.client.constants import AppDataPaths
from dropbox.trace import TRACE

def _get_crash_marker_file():
    return os.path.join(AppDataPaths.dropbox_appdata_path, 'app_crashed.dbx')


def create_crash_marker():
    crash_marker = _get_crash_marker_file()
    
    try:
        open(crash_marker, 'w', encoding = 'utf-8')
        
        try:
            None(None, None)
            return None
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            e = None
                            TRACE('Exception occurred when writing crash marker: %r', e)
                            e = None
                            del e
                            return None
                            e = None
                            del e






def clear_crash_marker():
    crash_marker = _get_crash_marker_file()
    
    try:
        os.remove(crash_marker)
        return None
    except FileNotFoundError:
        return None
        except Exception:
            e = None
            TRACE('Exception occurred when clearing crash marker: %r', e)
            e = None
            del e
            return None
            e = None
            del e


