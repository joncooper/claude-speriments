# Source Generated with Decompyle++
# File: temp_volume_interface.pyc (Python 3.11)

from abc import ABC
from dropbox.foundation.futures import Future
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.types import Filesystem, TempVolumeInfo

class TempVolumeInterface(ABC):
    
    def create_temp_volume(self = None, file_system = None, size = None):
        pass

    
    def drop_temp_volume(self = None, mount_path = None):
        pass


