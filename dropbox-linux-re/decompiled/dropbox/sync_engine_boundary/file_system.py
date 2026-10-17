# Source Generated with Decompyle++
# File: file_system.pyc (Python 3.11)

from dropbox.platform import IS_WINDOWS
from dropbox.sync_engine.file_system.abstract_file_system import AbstractFileSystem
from dropbox.sync_engine.file_system.memory import MemoryFS
from dropbox.sync_engine.file_system.mount import AbstractMountFS
if not IS_WINDOWS:
    from dropbox.sync_engine.file_system.posix import PosixFileSystem
    return None
