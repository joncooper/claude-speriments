# Source Generated with Decompyle++
# File: xattr_placeholder_context.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Text
from dropbox.sync_engine_boundary.infinite.placeholder_context import PlaceholderContext

class XattrPlaceholderContext(PlaceholderContext):
    
    def __init__(self = None, fd = None, path = None):
        self.fd = fd
        self.writeable_fd = None
        self.path = path


