# Source Generated with Decompyle++
# File: stat_helper.pyc (Python 3.11)

from __future__ import absolute_import
import stat
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_BLOCK_DEVICE, FILE_TYPE_POSIX_CHARACTER_DEVICE, FILE_TYPE_POSIX_FIFO, FILE_TYPE_POSIX_SOCKET, FILE_TYPE_POSIX_SYMLINK, FILE_TYPE_REGULAR, FILE_TYPE_UNKNOWN

def stat_result_to_type(st):
    _mode = st.st_mode
    if stat.S_ISREG(_mode):
        pass
    elif stat.S_ISDIR(_mode):
        pass
    elif stat.S_ISBLK(_mode):
        pass
    elif stat.S_ISCHR(_mode):
        pass
    elif stat.S_ISLNK(_mode):
        pass
    elif stat.S_ISSOCK(_mode):
        pass
    elif stat.S_ISFIFO(_mode):
        pass
    
    _type = FILE_TYPE_UNKNOWN
    return _type

