# Source Generated with Decompyle++
# File: memory_stub_folder_fs_mixin.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from file_system.constants import FILE_TYPE_DIRECTORY
from file_system.exceptions import create_not_a_directory_error
from infinite.stub_folder_fs_mixin import StubFolderFileSystemMixinInterface
from dropbox.infinite.exceptions import NotAStubFolderError
from dropbox.shared.stub_folder_details import StubFolderDetails
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError

class MemoryStubFolderFileSystemMixin(StubFolderFileSystemMixinInterface):
    
    def is_infinite_stub_folder(self = None, local_path = None):
        
        try:
            metadata = self._getmd(local_path)
        except FileNotFoundError:
            return False

        return getattr(metadata, 'stubfolder_details', None) is not None

    
    def set_stub_folder_by_path(self = None, local_path = None, stub_folder_details = None):
        metadata = self._getmd(local_path)
        if metadata.type != FILE_TYPE_DIRECTORY:
            raise create_not_a_directory_error(local_path)
        metadata.stubfolder_details = stub_folder_details.encode()

    
    def unset_stub_folder_by_path(self = None, local_path = None):
        metadata = self._getmd(local_path)
        if metadata.type != FILE_TYPE_DIRECTORY:
            raise create_not_a_directory_error(local_path)
        metadata.stubfolder_details = None

    
    def read_stub_folder_by_path(self = None, local_path = None):
        metadata = self._getmd(local_path)
        if not self.is_infinite_stub_folder(local_path):
            raise NotAStubFolderError
        return StubFolderDetails.decode(metadata.stubfolder_details)


