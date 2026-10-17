# Source Generated with Decompyle++
# File: keystore_linux.pyc (Python 3.11)

from __future__ import absolute_import
import os
from typing import Text
from lib.linuxffi.sys.api import statvfs
from keystore_posix import KeyStoreFileBacked
from dropbox.trace import TRACE

class KeyStoreLinux(KeyStoreFileBacked):
    
    def unique_id(self = None, path = None):
        inode = os.stat(path).st_ino
        stat = statvfs(path)
        TRACE('INFO: %r %r %r', path, inode, stat.f_fsid)
        return ('%d_%d' % (inode, stat.f_fsid)).encode('ascii')


