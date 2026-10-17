# Source Generated with Decompyle++
# File: directoryevent.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Optional, Text, Union
from dropbox.shared.local_path import LocalPath

class DirectoryEvent(object):
    __slots__ = [
        'path',
        'type',
        'cookie']
    TYPE_UNKNOWN = 0
    TYPE_ATTR_ONLY = 1
    TYPE_DROPPED_EVENTS = 2
    TYPE_WATCH_REMOVED = 3
    TYPE_WATCH_ERROR = 4
    TYPE_CREATE = 5
    TYPE_DELETE = 6
    TYPE_RENAME_TO = 7
    TYPE_RENAME_FROM = 8
    TYPE_RENAME = 9
    
    def __init__(self = None, path = None, t = None, cookie = (TYPE_UNKNOWN, None)):
        self.path = path
        self.type = t
        self.cookie = cookie

    TYPE_TO_STR = {
        TYPE_RENAME: 'rename',
        TYPE_RENAME_FROM: 'rename_from',
        TYPE_RENAME_TO: 'rename_to',
        TYPE_DELETE: 'delete',
        TYPE_CREATE: 'create',
        TYPE_WATCH_ERROR: 'watch_error',
        TYPE_WATCH_REMOVED: 'watch_removed',
        TYPE_DROPPED_EVENTS: 'dropped_events',
        TYPE_ATTR_ONLY: 'attr_only',
        TYPE_UNKNOWN: 'unknown' }
    
    def __repr__(self = None):
        cookie_str = ''
    # WARNING: Decompyle incomplete

    
    def __eq__(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __ne__(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __hash__(self = None):
        return hash((self.path, self.type, self.cookie))


