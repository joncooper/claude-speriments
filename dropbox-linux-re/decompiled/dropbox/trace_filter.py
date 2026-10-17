# Source Generated with Decompyle++
# File: trace_filter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import re
import traceback
from fnmatch import fnmatch
from typing import Set, Text

class TraceFilter(object):
    
    def __init__(self = None, trace_include = None):
        self._file_whitelist = {
            '<stdin>'}
        self._file_blacklist = set()
        self._globs = re.split('\\s*,\\s*', trace_include)()
        self._filtering_enabled = len(self._globs) > 0
        if self._filtering_enabled:
            print('[TRACE] filtering enabled for:\n\t' + '\n\t'.join(self._globs))
            return None
        return (lambda .0: pass# WARNING: Decompyle incomplete
)

    
    def stack_frame_matches_filters(self = None, call_depth = None):
        if not self._filtering_enabled:
            return True
        tb = traceback.extract_stack()
        index = len(tb) - 2 - call_depth
        if index < 0:
            return False
        stack_frame = None[index]
        file_name = stack_frame.filename
        if file_name in self._file_blacklist:
            return False
        if None in self._file_whitelist:
            return True
        for pattern in None._globs:
            if fnmatch(file_name, pattern):
                self._file_whitelist.add(file_name)
                return True
            self._file_blacklist.add(file_name)
            return False


