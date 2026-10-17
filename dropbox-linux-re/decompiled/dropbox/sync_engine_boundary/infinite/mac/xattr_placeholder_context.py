# Source Generated with Decompyle++
# File: xattr_placeholder_context.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Text
from dropbox.sync_engine_boundary.infinite.placeholder_context import PlaceholderContext

class XattrPlaceholderContext(PlaceholderContext):
    
    def __init__(self = None, st_dev = None, st_ino = None):
        self.st_dev = st_dev
        self.st_ino = st_ino

    
    def file_system_id(self = None):
        return '<%d, %d>' % (self.st_dev, self.st_ino)


